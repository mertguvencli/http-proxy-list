from sources import SOURCES
import json


README = """
# Free HTTP Proxy List 🌍

[![Hourly Update](https://github.com/mertguvencli/http-proxy-list/actions/workflows/main.yml/badge.svg?branch=main)](https://github.com/mertguvencli/http-proxy-list/actions/workflows/main.yml)

It is a lightweight project that hourly scrapes lots of free-proxy sites, validates if it works, and serves a clean proxy list.

> Scraper found **{{NUMBER_OF_TOTAL_PROXIES}}** proxies at the latest update. Usable proxies are below.

## Usage

Click the file format that you want and copy the URL.


|File|Content|Count|
|----|-------|-----|
|[data.txt](/proxy-list/data.txt)|`ip_address:port` combined (seperated new line)|{{NUMBER_OF_USABLE_PROXIES}}|
|[data.json](/proxy-list/data.json)|`ip, port`|{{NUMBER_OF_USABLE_PROXIES}}|
|[data-with-geolocation.json](/proxy-list/data-with-geolocation.json)|`ip, port, geolocation`|{{NUMBER_OF_USABLE_GEO_PROXIES}}|

## Sources

{{SOURCES}}

## Sample Proxies With Geolocation Info

|#|Ip|Port|Country|City|Internet Service Provider|
|-|--|----|-------|----|-------------------------|
{{PROXY_LIST}}


## Contributing

Contributions are welcome, and they are greatly appreciated! Every
little bit helps, and credit will always be given.

"""  # noqa


def update_readme(metrics: dict):
    global README

    SOURCES_MD = ''
    for config in SOURCES:
        SOURCES_MD += f'* [{config.get("id")}]({config.get("url")})\n'

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

    README = README.replace('{{SOURCES}}', SOURCES_MD)
    README = README.replace('{{PROXY_LIST}}', PROXY_LIST_MD)
    README = README.replace('{{NUMBER_OF_TOTAL_PROXIES}}', str(metrics['counts']['found']))
    README = README.replace('{{NUMBER_OF_USABLE_PROXIES}}', str(metrics['counts']['usable']))
    README = README.replace('{{NUMBER_OF_USABLE_GEO_PROXIES}}', str(metrics['counts']['geolocation']))

    with open('README.md', 'w') as f:
        f.write(README)
