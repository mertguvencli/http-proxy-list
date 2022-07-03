
# Free HTTP Proxy List 🌍

[![Hourly Update](https://github.com/mertguvencli/http-proxy-list/actions/workflows/main.yml/badge.svg?branch=main)](https://github.com/mertguvencli/http-proxy-list/actions/workflows/main.yml)
![GitHub](https://img.shields.io/github/license/mertguvencli/http-proxy-list)
![GitHub last commit](https://img.shields.io/github/last-commit/mertguvencli/http-proxy-list)

It is a lightweight project that hourly scrapes lots of free-proxy sites, validates if it works, and serves a clean proxy list.


> Scraper found **3376** proxies at the latest update. Usable proxies are below.

## Usage

Click the file format that you want and copy the URL.


|File|Content|Count|
|----|-------|-----|
|[data.txt](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.txt)|`ip_address:port` combined (seperated new line)|110|
|[data.json](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.json)|`ip, port`|110|
|[data-with-geolocation.json](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data-with-geolocation.json)|`ip, port, geolocation`|110|

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
|[proxyscrape.com](https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all)|216|✅|
|[github.com/clarketm/proxy-list](https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt)|400|✅|
|[github.com/monosans/proxy-list](https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt)|89|✅|
|[github.com/TheSpeedX/PROXY-List](https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt)|1988|✅|


## Sample Proxies With Geolocation Info

|#|Ip|Port|Country|City|Internet Service Provider|
|-|--|----|-------|----|-------------------------|
|1|12.231.44.251|3128|United States|Racine|AT&T Services, Inc.|
|2|45.152.188.246|3128|United States|Ashburn|Sprint|
|3|12.231.44.251|3128|United States|Racine|AT&T Services, Inc.|
|4|45.152.188.246|3128|United States|Ashburn|Sprint|
|5|51.250.80.131|80|Russia|Moscow|Yandex.Cloud LLC|
|6|47.240.160.90|10001|Hong Kong|Central|Alibaba.com LLC|
|7|20.47.108.204|8888|United States|Boydton|Microsoft Corporation|
|8|38.108.119.176|59394|United States|New York|Cogent Communications|
|9|45.152.188.246|3128|United States|Ashburn|Sprint|
|10|179.49.117.226|999|Honduras|Yore|Asociacion De Servicio De Internet S. De RL.|
|11|51.250.80.131|80|Russia|Moscow|Yandex.Cloud LLC|
|12|173.212.245.135|3128|Germany|Nuremberg|Contabo GmbH|
|13|43.154.161.208|59394|Hong Kong|Hong Kong|Shenzhen Tencent Computer Systems Company Limited|
|14|116.253.208.239|33080|China|Guangxi|CHINATELECOM Guangxi Nanning IDC networkdescr: Nanning, Guangxi Province, P.R.|
|15|140.227.69.105|3180|Japan|Chiyoda|NTT PC Communications, Inc.|
|16|61.7.138.24|8080|Thailand|Samphanthawong|CAT-BB|
|17|111.225.153.32|8089|China|Gaocheng|Chinanet|
|18|45.167.124.5|9992|Colombia|Guapi|Sepcom Comunicaciones SAS|
|19|62.75.206.151|3128|France|Strasbourg|PlusServer GmbH|
|20|34.136.99.66|3128|United States|Council Bluffs|Google LLC|



## Contributing

Contributions are welcome, and they are greatly appreciated! Every
little bit helps, and credit will always be given.

