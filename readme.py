from sources import SOURCES
import json


README = """
# Free HTTP Proxy List 🌍

[![Hourly Update](https://github.com/mertguvencli/http-proxy-list/actions/workflows/main.yml/badge.svg?branch=main)](https://github.com/mertguvencli/http-proxy-list/actions/workflows/main.yml)

It is a lightweight project that hourly scrapes lots of free-proxy sites, validates if it works, and serves a clean proxy list.

## Usage

Click the file that you want and copy the URL.

|File|Content|
|----|-------|
|[data.txt](/proxy-list/data.txt)|`ip_address:port` combined (seperated new line)|
|[data.json](/proxy-list/data.json)|`ip, port`|
|[data-with-geolocation.json](/proxy-list/data-with-geolocation.json)|`ip, port, geolocation`|

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


def update_readme():
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
            if i == 10:
                break

        for x in formatted:
            PROXY_LIST_MD += template.format(**x)

    README = README.replace('{{SOURCES}}', SOURCES_MD)
    README = README.replace('{{PROXY_LIST}}', PROXY_LIST_MD)

    with open('README.md', 'w') as f:
        f.write(README)
