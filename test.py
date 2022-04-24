import random
import requests
import pandas as pd
from sources import SOURCES


def test(save_response=False):
    config = SOURCES[0]
    HEADERS = {
        'User-Agent': f'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.{random.randint(0, 9999)} Safari/537.{random.randint(0, 99)}'  # noqa
    }

    url: str = config.get('url')
    method: str = config.get('method')
    parser: dict = config.get('parser', {})
    parser_type: str = list(parser.keys())[0]
    parser_config: dict = list(parser.values())[0]

    response = requests.request(
        method=method,
        url=url,
        headers=HEADERS,
        timeout=10
    )

    if save_response:
        with open('response.html', 'w', encoding='utf8') as f:
            f.write(str(response.content))

    if parser_type == "pandas":
        df = pd.read_html(response.content)[parser_config.get('table_index', 0)]
        for x in range(0, len(df)):
            if not parser_config.get('combined', None):
                ip = str(df.loc[df.index[x], parser_config.get('ip')]).strip()
                port = int(df.loc[df.index[x], parser_config.get('port')])
                print('STEP-1', {'ip': ip, 'port': port})
            else:
                combined: str = df.loc[df.index[x], parser_config.get('combined')]
                if len(combined.split(':')) == 2:
                    ip = combined.split(':')[0].strip()
                    port = int(combined.split(':')[1])
                    print('STEP-2', {'ip': ip, 'port': port})

    if parser_type == "json":
        data = response.json()[parser_config.get('data')]
        for x in data:
            print(
                'STEP-3',
                {
                    'ip': str(x[parser_config.get('ip', '')]).strip(),
                    'port': int(x[parser_config.get('port', '')])
                }
            )

    if parser_type == "txt":
        data = str(response.content, encoding='utf-8')
        for x in data.split('\n'):
            if len(x.split(':')) == 2:
                print(
                    'STEP-4',
                    {
                        'ip': x.split(':')[0].strip(),
                        'port': int(x.split(':')[1].strip())
                    }
                )
