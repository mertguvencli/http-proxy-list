
# Free HTTP Proxy List 🌍

[![Hourly Update](https://github.com/mertguvencli/http-proxy-list/actions/workflows/main.yml/badge.svg?branch=main)](https://github.com/mertguvencli/http-proxy-list/actions/workflows/main.yml)
![GitHub](https://img.shields.io/github/license/mertguvencli/http-proxy-list)
![GitHub last commit](https://img.shields.io/github/last-commit/mertguvencli/http-proxy-list)

It is a lightweight project that hourly scrapes lots of free-proxy sites, validates if it works, and serves a clean proxy list.


> Scraper found **3600** proxies at the latest update. Usable proxies are below.

## Usage

Click the file format that you want and copy the URL.


|File|Content|Count|
|----|-------|-----|
|[data.txt](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.txt)|`ip_address:port` combined (seperated new line)|145|
|[data.json](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.json)|`ip, port`|145|
|[data-with-geolocation.json](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data-with-geolocation.json)|`ip, port, geolocation`|145|

## Sources

|Source|Found Proxies|Succeed|
|------|-------------|-------|
|[free-proxy-list.net](https://free-proxy-list.net)|300|✅|
|[us-proxy.org](https://www.us-proxy.org)|200|✅|
|[proxydb.net](http://proxydb.net)|15|✅|
|[free-proxy-list.com](https://free-proxy-list.com/?page=&port=&type%5B%5D=http&type%5B%5D=https&up_time=0&search=Search)|10|✅|
|[proxy-list.download](https://www.proxy-list.download/HTTP)|26|✅|
|[vpnoverview.com](https://vpnoverview.com/privacy/anonymous-browsing/free-proxy-servers)|32|✅|
|[proxyscan.io](https://www.proxyscan.io)|100|✅|
|[proxylist.geonode.com](https://proxylist.geonode.com/api/proxy-list?limit=300&page=1&sort_by=lastChecked&sort_type=desc&protocols=http,https)|269|✅|
|[proxyscrape.com](https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all)|192|✅|
|[github.com/clarketm/proxy-list](https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt)|400|✅|
|[github.com/monosans/proxy-list](https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt)|77|✅|
|[github.com/TheSpeedX/PROXY-List](https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt)|1979|✅|


## Sample Proxies With Geolocation Info

|#|Ip|Port|Country|City|Internet Service Provider|
|-|--|----|-------|----|-------------------------|
|1|158.101.100.104|3128|United States|Ashburn|Oracle Corporation|
|2|45.152.188.246|3128|United States|Ashburn|Sprint|
|3|5.161.105.105|80|United States|Ashburn|Hetzner Online GmbH|
|4|140.238.87.185|3128|United Kingdom|London|Oracle Corporation|
|5|35.193.25.172|3128|United States|Council Bluffs|Google LLC|
|6|18.130.94.155|3128|United Kingdom|London|Amazon Technologies Inc.|
|7|18.130.172.110|3128|United Kingdom|London|Amazon Technologies Inc.|
|8|35.178.81.137|3128|United Kingdom|London|Amazon Technologies Inc.|
|9|59.124.224.205|3128|Taiwan|Bade District|Chunghwa Telecom Co., Ltd.|
|10|173.82.188.82|9090|United States|Santa Clarita|Multacom Corporation|
|11|173.82.188.82|9090|United States|Santa Clarita|Multacom Corporation|
|12|47.240.160.90|10001|Hong Kong|Central|Alibaba.com LLC|
|13|181.36.230.242|999|Dominican Republic|Santo Domingo Este|Altice Dominicana S.A.|
|14|159.223.135.219|8080|United States|North Bergen|DigitalOcean, LLC|
|15|138.68.149.26|3128|United Kingdom|London|DigitalOcean, LLC|
|16|78.46.123.202|80|Germany|Falkenstein|Hetzner Online GmbH|
|17|158.101.100.104|3128|United States|Ashburn|Oracle Corporation|
|18|45.152.188.246|3128|United States|Ashburn|Sprint|
|19|5.161.105.105|80|United States|Ashburn|Hetzner Online GmbH|
|20|35.193.25.172|3128|United States|Council Bluffs|Google LLC|



## Contributing

Contributions are welcome, and they are greatly appreciated! Every
little bit helps, and credit will always be given.

