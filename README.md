
# Free HTTP Proxy List 🌍

[![Hourly Update](https://github.com/mertguvencli/http-proxy-list/actions/workflows/main.yml/badge.svg?branch=main)](https://github.com/mertguvencli/http-proxy-list/actions/workflows/main.yml)
![GitHub](https://img.shields.io/github/license/mertguvencli/http-proxy-list)
![GitHub last commit](https://img.shields.io/github/last-commit/mertguvencli/http-proxy-list)

It is a lightweight project that hourly scrapes lots of free-proxy sites, validates if it works, and serves a clean proxy list.


> Scraper found **3432** proxies at the latest update. Usable proxies are below.

## Usage

Click the file format that you want and copy the URL.


|File|Content|Count|
|----|-------|-----|
|[data.txt](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.txt)|`ip_address:port` combined (seperated new line)|106|
|[data.json](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.json)|`ip, port`|106|
|[data-with-geolocation.json](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data-with-geolocation.json)|`ip, port, geolocation`|106|

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
|[proxyscrape.com](https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all)|247|✅|
|[github.com/clarketm/proxy-list](https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt)|400|✅|
|[github.com/monosans/proxy-list](https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt)|86|✅|
|[github.com/TheSpeedX/PROXY-List](https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt)|2016|✅|


## Sample Proxies With Geolocation Info

|#|Ip|Port|Country|City|Internet Service Provider|
|-|--|----|-------|----|-------------------------|
|1|20.47.108.204|8888|United States|Boydton|Microsoft Corporation|
|2|45.167.124.5|9992|Colombia|Guapi|Sepcom Comunicaciones SAS|
|3|216.37.138.177|3128|United States|Pittsburgh|Frontier Communications of America|
|4|157.100.12.138|999|Ecuador|Loja|Telconet S.A|
|5|173.82.188.82|9090|United States|Santa Clarita|Multacom Corporation|
|6|216.37.138.177|3128|United States|Pittsburgh|Frontier Communications of America|
|7|51.250.80.131|80|Russia|Moscow|Yandex.Cloud LLC|
|8|200.110.173.118|8080|Colombia|Santiago de Cali|Media Commerce Partners S.A|
|9|12.231.44.251|3128|United States|Racine|AT&T Services, Inc.|
|10|190.26.201.194|8080|Colombia|Bogotá|ETB - Colombia|
|11|190.2.210.116|999|Colombia|Santander de Quilichao|TV AZTECA SUCURSAL COLOMBIA|
|12|13.125.247.113|3128|South Korea|Seoul|Amazon Technologies Inc.|
|13|157.100.12.138|999|Ecuador|Loja|Telconet S.A|
|14|47.240.160.90|10001|Hong Kong|Central|Alibaba.com LLC|
|15|45.167.124.5|9992|Colombia|Guapi|Sepcom Comunicaciones SAS|
|16|12.31.246.5|8080|United States|Saint Helena|AT&T Services, Inc.|
|17|62.75.206.151|3128|France|Strasbourg|PlusServer GmbH|
|18|125.209.88.46|8080|Pakistan|Karachi|Multinet 125-88/24|
|19|80.244.226.92|8080|Russia|Moscow|Enforta-MSK|
|20|111.225.153.173|8089|China|Gaocheng|Chinanet|



## Contributing

Contributions are welcome, and they are greatly appreciated! Every
little bit helps, and credit will always be given.

