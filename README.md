
# Free HTTP Proxy List 🌍

[![Hourly Update](https://github.com/mertguvencli/http-proxy-list/actions/workflows/main.yml/badge.svg?branch=main)](https://github.com/mertguvencli/http-proxy-list/actions/workflows/main.yml)
![GitHub](https://img.shields.io/github/license/mertguvencli/http-proxy-list)
![GitHub last commit](https://img.shields.io/github/last-commit/mertguvencli/http-proxy-list)

It is a lightweight project that hourly scrapes lots of free-proxy sites, validates if it works, and serves a clean proxy list.


> Scraper found **3624** proxies at the latest update. Usable proxies are below.

## Usage

Click the file format that you want and copy the URL.


|File|Content|Count|
|----|-------|-----|
|[data.txt](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.txt)|`ip_address:port` combined (seperated new line)|200|
|[data.json](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.json)|`ip, port`|200|
|[data-with-geolocation.json](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data-with-geolocation.json)|`ip, port, geolocation`|200|

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
|[proxylist.geonode.com](https://proxylist.geonode.com/api/proxy-list?limit=300&page=1&sort_by=lastChecked&sort_type=desc&protocols=http,https)|0|🚫|
|[proxyscrape.com](https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all)|448|✅|
|[github.com/clarketm/proxy-list](https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt)|400|✅|
|[github.com/monosans/proxy-list](https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt)|91|✅|
|[github.com/TheSpeedX/PROXY-List](https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt)|2002|✅|


## Sample Proxies With Geolocation Info

|#|Ip|Port|Country|City|Internet Service Provider|
|-|--|----|-------|----|-------------------------|
|1|45.152.188.246|3128|United States|Ashburn|Sprint|
|2|12.231.44.251|3128|United States|Racine|AT&T Services, Inc.|
|3|45.152.188.246|3128|United States|Ashburn|Sprint|
|4|12.231.44.251|3128|United States|Racine|AT&T Services, Inc.|
|5|37.49.230.22|8187|Netherlands|Amsterdam|ABC Consultancy|
|6|157.100.12.138|999|Ecuador|Loja|Telconet S.A|
|7|173.82.188.82|9090|United States|Santa Clarita|Multacom Corporation|
|8|181.48.101.245|3128|Colombia|Bogotá|Telmex Colombia S.A.|
|9|170.178.214.108|59394|United States|Santa Clarita|Multacom Corporation|
|10|47.240.160.90|10001|Hong Kong|Central|Alibaba.com LLC|
|11|173.82.188.82|9090|United States|Santa Clarita|Multacom Corporation|
|12|170.178.214.108|59394|United States|Santa Clarita|Multacom Corporation|
|13|36.95.79.7|41890|Indonesia|Jakarta|PT. Telekomunikasi Indonesia|
|14|181.209.116.18|999|Argentina|Pico Truncado|ARSAT - Empresa Argentina de Soluciones Satelitales S.A|
|15|139.59.5.27|443|India|Bengaluru|DIGITALOCEAN|
|16|51.250.80.131|80|Russia|Moscow|Yandex.Cloud LLC|
|17|85.25.91.141|15333|Germany|Cologne|PlusServer GmbH|
|18|45.167.124.5|9992|Colombia|Guapi|Sepcom Comunicaciones SAS|
|19|162.215.22.120|59394|United States|Provo|Unified Layer|
|20|36.92.22.70|8080|Indonesia|Jakarta|PT. Telekomunikasi Indonesia|



## Contributing

Contributions are welcome, and they are greatly appreciated! Every
little bit helps, and credit will always be given.

