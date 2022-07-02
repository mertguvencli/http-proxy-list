
# Free HTTP Proxy List 🌍

[![Hourly Update](https://github.com/mertguvencli/http-proxy-list/actions/workflows/main.yml/badge.svg?branch=main)](https://github.com/mertguvencli/http-proxy-list/actions/workflows/main.yml)
![GitHub](https://img.shields.io/github/license/mertguvencli/http-proxy-list)
![GitHub last commit](https://img.shields.io/github/last-commit/mertguvencli/http-proxy-list)

It is a lightweight project that hourly scrapes lots of free-proxy sites, validates if it works, and serves a clean proxy list.


> Scraper found **3393** proxies at the latest update. Usable proxies are below.

## Usage

Click the file format that you want and copy the URL.


|File|Content|Count|
|----|-------|-----|
|[data.txt](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.txt)|`ip_address:port` combined (seperated new line)|148|
|[data.json](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.json)|`ip, port`|148|
|[data-with-geolocation.json](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data-with-geolocation.json)|`ip, port, geolocation`|148|

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
|[proxyscrape.com](https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all)|228|✅|
|[github.com/clarketm/proxy-list](https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt)|400|✅|
|[github.com/monosans/proxy-list](https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt)|66|✅|
|[github.com/TheSpeedX/PROXY-List](https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt)|2016|✅|


## Sample Proxies With Geolocation Info

|#|Ip|Port|Country|City|Internet Service Provider|
|-|--|----|-------|----|-------------------------|
|1|45.152.188.246|3128|United States|Ashburn|Sprint|
|2|5.161.105.105|80|United States|Ashburn|Hetzner Online GmbH|
|3|20.47.108.204|8888|United States|Boydton|Microsoft Corporation|
|4|5.161.105.105|80|United States|Ashburn|Hetzner Online GmbH|
|5|45.152.188.246|3128|United States|Ashburn|Sprint|
|6|157.100.12.138|999|Ecuador|Loja|Telconet S.A|
|7|200.110.173.118|8080|Colombia|Santiago de Cali|Media Commerce Partners S.A|
|8|173.82.188.82|9090|United States|Santa Clarita|Multacom Corporation|
|9|47.240.160.90|10001|Hong Kong|Central|Alibaba.com LLC|
|10|51.250.80.131|80|Russia|Moscow|Yandex.Cloud LLC|
|11|200.24.157.121|999|Ecuador|Azogues|Nedetel S.A.|
|12|38.108.119.176|59394|United States|New York|Cogent Communications|
|13|202.180.20.11|55443|Indonesia|Bandung|PT. HIPERNET INDODATA|
|14|170.245.56.195|999|Honduras|San Pedro Sula|Asociacion De Servicio De Internet S. De RL.|
|15|190.187.201.26|8080|Peru|Lima|Americatel Peru S.A.|
|16|193.138.178.6|8282|Russia|Chelyabinsk|New Communication Technologies|
|17|12.231.44.251|3128|United States|Racine|AT&T Services, Inc.|
|18|49.0.39.186|8080|Bangladesh|Dhaka|Always On Network Bangladesh Ltd.|
|19|190.113.43.66|999|Dominican Republic|Santo Domingo Este|MR Networking, SRL|
|20|45.167.124.5|9992|Colombia|Guapi|Sepcom Comunicaciones SAS|



## Contributing

Contributions are welcome, and they are greatly appreciated! Every
little bit helps, and credit will always be given.

