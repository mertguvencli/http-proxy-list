
# Free HTTP Proxy List 🌍

[![Hourly Update](https://github.com/mertguvencli/http-proxy-list/actions/workflows/main.yml/badge.svg?branch=main)](https://github.com/mertguvencli/http-proxy-list/actions/workflows/main.yml)
![GitHub](https://img.shields.io/github/license/mertguvencli/http-proxy-list)
![GitHub last commit](https://img.shields.io/github/last-commit/mertguvencli/http-proxy-list)

It is a lightweight project that hourly scrapes lots of free-proxy sites, validates if it works, and serves a clean proxy list.


> Scraper found **3645** proxies at the latest update. Usable proxies are below.

## Usage

Click the file format that you want and copy the URL.


|File|Content|Count|
|----|-------|-----|
|[data.txt](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.txt)|`ip_address:port` combined (seperated new line)|197|
|[data.json](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.json)|`ip, port`|197|
|[data-with-geolocation.json](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data-with-geolocation.json)|`ip, port, geolocation`|197|

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
|[proxyscrape.com](https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all)|336|✅|
|[github.com/clarketm/proxy-list](https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt)|400|✅|
|[github.com/monosans/proxy-list](https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt)|280|✅|
|[github.com/TheSpeedX/PROXY-List](https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt)|1946|✅|


## Sample Proxies With Geolocation Info

|#|Ip|Port|Country|City|Internet Service Provider|
|-|--|----|-------|----|-------------------------|
|1|8.219.97.248|80|Singapore|Singapore|Alibaba (US) Technology Co., Ltd.|
|2|118.99.73.152|8080|Indonesia|Jakarta|BIZNET|
|3|45.4.253.135|999|Argentina|Puerto Iguazú|Fernando German Fischer (FIBERNET TELECOM)|
|4|5.161.105.105|80|United States|Ashburn|Hetzner Online GmbH|
|5|20.47.108.204|8888|United States|Boydton|Microsoft Corporation|
|6|51.250.80.131|80|Russia|Moscow|Yandex.Cloud LLC|
|7|79.143.179.141|3128|Germany|Munich|Contabo GmbH|
|8|8.219.97.248|80|Singapore|Singapore|Alibaba (US) Technology Co., Ltd.|
|9|5.161.105.105|80|United States|Ashburn|Hetzner Online GmbH|
|10|8.219.97.248|80|Singapore|Singapore|Alibaba (US) Technology Co., Ltd.|
|11|103.252.1.137|3128|Vietnam|Hanoi|CMCMIENBAC|
|12|200.146.77.133|80|Brazil|Curitiba|Vivo|
|13|157.100.12.138|999|Ecuador|Loja|Telconet S.A|
|14|5.61.44.89|3128|Germany|Frankfurt am Main|LeaseWeb DE|
|15|181.205.20.197|999|Colombia|Medellín|EPM Telecomunicaciones S.A. E.S.P.|
|16|201.218.158.79|999|Peru|Lima|M & B Soluciones Peru S.A.C.|
|17|194.169.167.5|8080|Serbia|Belgrade|Kadri Haxhiaj trading as "B.I."|
|18|216.238.77.41|59394|Mexico|Mexico City|The Constant Company|
|19|121.156.109.108|8080|South Korea|Seongnam-si|Korea Telecom|
|20|143.137.147.218|999|Peru|Santiago de Surco|Wigo S.A.|



## Contributing

Contributions are welcome, and they are greatly appreciated! Every
little bit helps, and credit will always be given.

