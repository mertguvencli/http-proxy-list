from sources import SOURCES
import json

README = """
# Free HTTP Proxy List 🌍

[![Hourly Update](https://github.com/mertguvencli/http-proxy-list/actions/workflows/main.yml/badge.svg?branch=main)](https://github.com/mertguvencli/http-proxy-list/actions/workflows/main.yml)
![GitHub](https://img.shields.io/github/license/mertguvencli/http-proxy-list)
![GitHub last commit](https://img.shields.io/github/last-commit/mertguvencli/http-proxy-list)

It is a lightweight project that hourly scrapes lots of free-proxy sites, validates if it works, and serves a clean proxy list.


> Scraper found **{NUMBER_OF_TOTAL_PROXIES}** proxies at the latest update. Usable proxies are below.

## Usage

Click the file format that you want and copy the URL.


|File|Content|Count|
|----|-------|-----|
|[data.txt]({GITHUB_RAW_URL}/proxy-list/data.txt)|`ip_address:port` combined (seperated new line)|{NUMBER_OF_USABLE_PROXIES}|
|[data.json]({GITHUB_RAW_URL}/proxy-list/data.json)|`ip, port`|{NUMBER_OF_USABLE_PROXIES}|
|[data-with-geolocation.json]({GITHUB_RAW_URL}/proxy-list/data-with-geolocation.json)|`ip, port, geolocation`|{NUMBER_OF_USABLE_GEO_PROXIES}|

## Sources

|Source|Found Proxies|Succeed|
|------|-------------|-------|
{SOURCES}

## Sample Proxies With Geolocation Info

|#|Ip|Port|Country|City|Internet Service Provider|
|-|--|----|-------|----|-------------------------|
{PROXY_LIST}


## Contributing

Contributions are welcome, and they are greatly appreciated! Every
little bit helps, and credit will always be given.

"""  # noqa

GITHUB_RAW_URL = 'https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main'  # noqa


def update_readme(metrics: dict):
    global README
    global GITHUB_RAW_URL

    SOURCES_MD = ''
    template = '|{}|{}|{}|\n'
    for x in metrics['sources']:
        source = f'[{x.get("id")}]({x.get("url")})'
        found_proxies = x['count']
        succeed = x['succeed']
        if succeed:
            succeed = '✅'
        else:
            succeed = '🚫'
        SOURCES_MD += template.format(source, found_proxies, succeed)


    PROXY_LIST_MD = ''
    template = '|{row_num}|{ip}|{port}|{country}|{city}|{isp}|\n'
    with open('proxy-list/data-with-geolocation.json', 'r') as f:
        geolocations = json.load(f)
        formatted = []
        for i, x in enumerate(geolocations, 1):
            tmp = dict((k, v) for k, v in dict(x["geolocation"]).items())
            tmp["ip"] = x["ip"]
            tmp["port"] = x["port"]
            tmp['row_num'] = i
            formatted.append(tmp)
            if i == 20:
                break

        for x in formatted:
            PROXY_LIST_MD += template.format(**x)

    data = {
        'SOURCES': SOURCES_MD,
        'PROXY_LIST': PROXY_LIST_MD,
        'GITHUB_RAW_URL': GITHUB_RAW_URL,
        'NUMBER_OF_TOTAL_PROXIES': str(metrics['counts']['found']),
        'NUMBER_OF_USABLE_PROXIES': str(metrics['counts']['usable']),
        'NUMBER_OF_USABLE_GEO_PROXIES': str(metrics['counts']['geolocation']),
    }

    with open('README.md', 'w') as f:
        f.write(README.format(**data))
