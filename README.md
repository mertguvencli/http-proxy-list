
# Free HTTP Proxy List 🌍

[![Hourly Update](https://github.com/mertguvencli/http-proxy-list/actions/workflows/main.yml/badge.svg?branch=main)](https://github.com/mertguvencli/http-proxy-list/actions/workflows/main.yml)
![GitHub](https://img.shields.io/github/license/mertguvencli/http-proxy-list)
![GitHub last commit](https://img.shields.io/github/last-commit/mertguvencli/http-proxy-list)

It is a lightweight project that hourly scrapes lots of free-proxy sites, validates if it works, and serves a clean proxy list.


> Scraper found **3372** proxies at the latest update. Usable proxies are below.

## Usage

Click the file format that you want and copy the URL.


|File|Content|Count|
|----|-------|-----|
|[data.txt](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.txt)|`ip_address:port` combined (seperated new line)|97|
|[data.json](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.json)|`ip, port`|97|
|[data-with-geolocation.json](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data-with-geolocation.json)|`ip, port, geolocation`|97|

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
|[proxyscrape.com](https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all)|261|✅|
|[github.com/clarketm/proxy-list](https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt)|400|✅|
|[github.com/monosans/proxy-list](https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt)|143|✅|
|[github.com/TheSpeedX/PROXY-List](https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt)|1885|✅|


## Sample Proxies With Geolocation Info

|#|Ip|Port|Country|City|Internet Service Provider|
|-|--|----|-------|----|-------------------------|
|1|20.47.108.204|8888|United States|Boydton|Microsoft Corporation|
|2|34.82.235.224|3128|United States|The Dalles|Google LLC|
|3|103.73.194.2|80|Hong Kong|Wanchai|TouchPal HK Co., Limited|
|4|186.67.230.45|3128|Chile|Santiago|Entel Chile S.A.|
|5|188.138.106.143|5566|France|Strasbourg|Host Europe GmbH|
|6|85.25.4.28|5566|France|Strasbourg|Host Europe GmbH|
|7|85.25.100.47|5566|France|Strasbourg|Host Europe GmbH|
|8|190.26.201.194|8080|Colombia|Bogotá|ETB - Colombia|
|9|62.75.219.49|5566|France|Strasbourg|BSB-SERVICE|
|10|170.155.5.235|8080|Argentina|Castelar|Gobernacion de la Provincia de Buenos Aires|
|11|103.100.208.56|59394|Hong Kong|Kwai Chung|Yisu Cloud LTD|
|12|62.75.229.165|5566|France|Strasbourg|Host Europe GmbH|
|13|188.138.106.93|5566|France|Strasbourg|Host Europe GmbH|
|14|188.138.106.133|5566|France|Strasbourg|Host Europe GmbH|
|15|188.138.106.143|5566|France|Strasbourg|Host Europe GmbH|
|16|85.25.133.28|5566|France|Strasbourg|Host Europe GmbH|
|17|181.196.241.198|9100|Ecuador|Guayaquil|Corporacion Nacional De Telecomunicaciones - CNT EP|
|18|80.90.141.167|8888|Czechia|Boretice|Oxid - III|
|19|191.102.104.225|999|Colombia|Gama|TV AZTECA SUCURSAL COLOMBIA|
|20|5.16.0.174|8080|Russia|St Petersburg|Enforta-MSK|



## Contributing

Contributions are welcome, and they are greatly appreciated! Every
little bit helps, and credit will always be given.

