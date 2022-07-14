
# Free HTTP Proxy List 🌍

[![Hourly Update](https://github.com/mertguvencli/http-proxy-list/actions/workflows/main.yml/badge.svg?branch=main)](https://github.com/mertguvencli/http-proxy-list/actions/workflows/main.yml)
![GitHub](https://img.shields.io/github/license/mertguvencli/http-proxy-list)
![GitHub last commit](https://img.shields.io/github/last-commit/mertguvencli/http-proxy-list)

It is a lightweight project that hourly scrapes lots of free-proxy sites, validates if it works, and serves a clean proxy list.


> Scraper found **3378** proxies at the latest update. Usable proxies are below.

## Usage

Click the file format that you want and copy the URL.


|File|Content|Count|
|----|-------|-----|
|[data.txt](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.txt)|`ip_address:port` combined (seperated new line)|141|
|[data.json](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.json)|`ip, port`|141|
|[data-with-geolocation.json](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data-with-geolocation.json)|`ip, port, geolocation`|141|

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
|[proxyscrape.com](https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all)|288|✅|
|[github.com/clarketm/proxy-list](https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt)|400|✅|
|[github.com/monosans/proxy-list](https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt)|127|✅|
|[github.com/TheSpeedX/PROXY-List](https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt)|1880|✅|


## Sample Proxies With Geolocation Info

|#|Ip|Port|Country|City|Internet Service Provider|
|-|--|----|-------|----|-------------------------|
|1|20.47.108.204|8888|United States|Boydton|Microsoft Corporation|
|2|170.39.194.16|3128|United States|Ashburn|Rackdog, LLC|
|3|20.81.62.32|3128|United States|Boydton|Microsoft Corporation|
|4|170.39.194.16|3128|United States|Ashburn|Rackdog, LLC|
|5|178.32.148.251|8080|France|Gravelines|OVH SAS|
|6|157.100.12.138|999|Ecuador|Loja|Telconet S.A|
|7|167.235.63.238|3128|Germany|Falkenstein|Hetzner Online GmbH|
|8|216.238.81.217|59394|Mexico|Mexico City|The Constant Company|
|9|18.162.146.115|3128|Hong Kong|Hong Kong|Amazon Technologies Inc.|
|10|216.176.187.99|30013|United States|Los Angeles|Wowrack.com|
|11|181.191.141.14|999|Argentina|San Rafael|Jara Pedro Javier|
|12|206.189.195.74|8080|United States|North Bergen|DigitalOcean, LLC|
|13|84.54.191.22|8080|Bulgaria|Burgas|ComNet Bulgaria Ltd.|
|14|201.218.158.79|999|Peru|Lima|M & B Soluciones Peru S.A.C.|
|15|163.47.11.211|12358|Singapore|Singapore|DigitalOcean|
|16|64.189.24.250|3129|United States|Chicago|WhiteSky Communications, LLC.|
|17|116.253.208.239|33080|China|Lilancun|CHINATELECOM Guangxi Nanning IDC networkdescr: Nanning, Guangxi Province, P.R.|
|18|20.81.62.32|3128|United States|Boydton|Microsoft Corporation|
|19|51.250.80.131|80|Russia|Moscow|Yandex.Cloud LLC|
|20|8.219.97.248|80|Singapore|Singapore|Alibaba (US) Technology Co., Ltd.|



## Contributing

Contributions are welcome, and they are greatly appreciated! Every
little bit helps, and credit will always be given.

