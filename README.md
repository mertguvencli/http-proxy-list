
# Free HTTP Proxy List 🌍

[![Hourly Update](https://github.com/mertguvencli/http-proxy-list/actions/workflows/main.yml/badge.svg?branch=main)](https://github.com/mertguvencli/http-proxy-list/actions/workflows/main.yml)
![GitHub](https://img.shields.io/github/license/mertguvencli/http-proxy-list)
![GitHub last commit](https://img.shields.io/github/last-commit/mertguvencli/http-proxy-list)

It is a lightweight project that hourly scrapes lots of free-proxy sites, validates if it works, and serves a clean proxy list.


> Scraper found **3649** proxies at the latest update. Usable proxies are below.

## Usage

Click the file format that you want and copy the URL.


|File|Content|Count|
|----|-------|-----|
|[data.txt](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.txt)|`ip_address:port` combined (seperated new line)|136|
|[data.json](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.json)|`ip, port`|136|
|[data-with-geolocation.json](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data-with-geolocation.json)|`ip, port, geolocation`|136|

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
|[proxyscrape.com](https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all)|317|✅|
|[github.com/clarketm/proxy-list](https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt)|400|✅|
|[github.com/monosans/proxy-list](https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt)|89|✅|
|[github.com/TheSpeedX/PROXY-List](https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt)|1891|✅|


## Sample Proxies With Geolocation Info

|#|Ip|Port|Country|City|Internet Service Provider|
|-|--|----|-------|----|-------------------------|
|1|45.152.188.246|3128|United States|Ashburn|Sprint|
|2|173.82.188.82|9090|United States|Santa Clarita|Multacom Corporation|
|3|52.155.227.108|3128|Ireland|Dublin|Microsoft Corporation|
|4|20.47.108.204|8888|United States|Boydton|Microsoft Corporation|
|5|45.152.188.246|3128|United States|Ashburn|Sprint|
|6|51.250.80.131|80|Russia|Moscow|Yandex.Cloud LLC|
|7|200.105.215.18|33630|Bolivia|La Paz|AXS Bolivia S. A.|
|8|45.32.105.89|3128|Singapore|Singapore|The Constant Company|
|9|59.124.224.205|3128|Taiwan|Bade District|Chunghwa Telecom Co., Ltd.|
|10|173.82.188.82|9090|United States|Santa Clarita|Multacom Corporation|
|11|157.100.12.138|999|Ecuador|Loja|Telconet S.A|
|12|47.240.160.90|10001|Hong Kong|Central|Alibaba.com LLC|
|13|185.221.134.234|3129|United States|Los Angeles|DediPath|
|14|116.253.208.239|33080|China|Guangxi|CHINATELECOM Guangxi Nanning IDC networkdescr: Nanning, Guangxi Province, P.R.|
|15|38.123.207.247|999|Mexico|Mexico City|Cogent Communications|
|16|186.97.182.3|999|Colombia|Medellín|Colombia Móvil|
|17|186.248.89.6|5005|Brazil|Belo Horizonte|Cemig Telecomunicações SA|
|18|59.124.224.205|3128|Taiwan|Bade District|Chunghwa Telecom Co., Ltd.|
|19|20.47.108.204|8888|United States|Boydton|Microsoft Corporation|
|20|201.220.102.146|8080|Chile|Valdivia|Telefonica del Sur S.A.|



## Contributing

Contributions are welcome, and they are greatly appreciated! Every
little bit helps, and credit will always be given.

