import time
import ssl
import json
import logging
import concurrent.futures
import requests
import pandas as pd
from fake_useragent import UserAgent
import itertools
from sources import SOURCES

logging.basicConfig(
    format='%(asctime)s %(name)s - %(levelname)s - %(message)s',
    level=logging.DEBUG
)
# ssl._create_default_https_context = ssl._create_unverified_context
user_agent = UserAgent()
HEADERS = {'User-Agent': user_agent.random}
MAX_WORKER = 300
AVAILABLE_PROXIES = []
USABLE_PROXIES = []


class ProxyItem:
    def __init__(self, ip: str, port: int):
        self.ip = ip
        self.port = port
        self.proxy = {
            'http': f'http://{self.ip}:{self.port}',
            'https': f'http://{self.ip}:{self.port}'
        }
        self.is_valid = self.check()
        print(self.__dict__)

    def check(self) -> bool:
        global USABLE_PROXIES
        try:
            start_time = time.time()
            requests.get(
                url='https://ipecho.net/plain',
                proxies=self.proxy,
                timeout=5
            )
            USABLE_PROXIES.append({'ip': self.ip, 'port': self.port})
            return True
        except: # noqa
            return False


class Scraper:
    def __init__(self, config: dict) -> None:
        self.config = config
        self.url: str = self.config.get('url')
        self.method: str = self.config.get('method')
        self.parser: dict = self.config.get('parser', {})
        self.parser_type: str = list(self.parser.keys())[0]
        self.parser_config: dict = list(self.parser.values())[0]
        self.request_timeout = 10
        self.is_succeed = False
        logging.debug(f'Source: {self.config.get("id")} has started.')

    def crawl(self) -> requests.Response:
        return requests.request(
            method=self.method,
            url=self.url,
            headers=HEADERS,
            timeout=self.request_timeout
        )

    def parse(self) -> list:
        proxies = []
        try:
            response = self.crawl()
            if self.parser_type == "pandas":
                df = pd.read_html(response.content)[self.parser_config.get('table_index', 0)]
                for x in range(0, len(df)):
                    if not self.parser_config.get('combined', None):
                        ip = str(df.loc[df.index[x], self.parser_config.get('ip')]).strip()
                        port = int(df.loc[df.index[x], self.parser_config.get('port')])
                        proxies.append({'ip': ip, 'port': port})
                    else:
                        combined: str = df.loc[df.index[x], self.parser_config.get('combined')]
                        if len(combined.split(':')) == 2:
                            ip = combined.split(':')[0].strip()
                            port = int(combined.split(':')[1])
                            proxies.append({'ip': ip, 'port': port})
            
            if self.parser_type == "json":
                data = response.json()[self.parser_config.get('data')]
                for x in data:
                    proxies.append({
                        'ip': str(x[self.parser_config.get('ip', '')]).strip(),
                        'port': int(x[self.parser_config.get('port', '')])
                    })

            if self.parser_type == "txt":
                data = str(response.content, encoding='utf-8')
                for x in data.split('\n'):
                    if len(x.split(':')) == 2:
                        proxies.append({
                            'ip': x.split(':')[0].strip(),
                            'port': int(x.split(':')[1].strip())
                        })
        except Exception as e:  # noqa
            self.is_succeed = False
            logging.error(f'Source: {self.config.get("id")}', exc_info=True)

        return proxies

    def run(self) -> bool:
        global AVAILABLE_PROXIES
        proxies = self.parse()
        if len(proxies) > 0:
            AVAILABLE_PROXIES = itertools.chain(AVAILABLE_PROXIES, proxies)

        return self.is_succeed


def main():
    global MAX_WORKER

    for item in SOURCES:
        scraper = Scraper(item)
        scraper.run()

    list_of_proxies = list(AVAILABLE_PROXIES)
    with concurrent.futures.ThreadPoolExecutor(max_workers=MAX_WORKER) as executor:
        worker_to_queue = {
            executor.submit(ProxyItem, x['ip'], x['port']): x for x in list_of_proxies
        }
        for worker in concurrent.futures.as_completed(worker_to_queue):
            worker_to_queue[worker]

    with open("proxy-list.json", "w") as f:
        json.dump(USABLE_PROXIES, f, indent=4)

    logging.info(f'{len(list_of_proxies)} proxies are crawled.')
    logging.info(f'{len(USABLE_PROXIES)} proxies are usable.')


if __name__ == '__main__':
    main()
