
# Free HTTP Proxy List 🌍

[![Hourly Update](https://github.com/mertguvencli/http-proxy-list/actions/workflows/main.yml/badge.svg?branch=main)](https://github.com/mertguvencli/http-proxy-list/actions/workflows/main.yml)
![GitHub](https://img.shields.io/github/license/mertguvencli/http-proxy-list)
![GitHub last commit](https://img.shields.io/github/last-commit/mertguvencli/http-proxy-list)

It is a lightweight project that hourly scrapes lots of free-proxy sites, validates if it works, and serves a clean proxy list.


> Scraper found **3736** proxies at the latest update. Usable proxies are below.

## Usage

Click the file format that you want and copy the URL.


|File|Content|Count|
|----|-------|-----|
|[data.txt](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.txt)|`ip_address:port` combined (seperated new line)|220|
|[data.json](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.json)|`ip, port`|220|
|[data-with-geolocation.json](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data-with-geolocation.json)|`ip, port, geolocation`|220|

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
|[proxylist.geonode.com](https://proxylist.geonode.com/api/proxy-list?limit=300&page=1&sort_by=lastChecked&sort_type=desc&protocols=http,https)|300|✅|
|[proxyscrape.com](https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all)|354|✅|
|[github.com/clarketm/proxy-list](https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt)|400|✅|
|[github.com/monosans/proxy-list](https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt)|85|✅|
|[github.com/TheSpeedX/PROXY-List](https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt)|1914|✅|


## Sample Proxies With Geolocation Info

|#|Ip|Port|Country|City|Internet Service Provider|
|-|--|----|-------|----|-------------------------|
|1|198.41.67.18|8080|United States|Lafayette|Cox Communications Inc.|
|2|216.238.76.66|59394|Mexico|Mexico City|The Constant Company|
|3|20.47.108.204|8888|United States|Boydton|Microsoft Corporation|
|4|12.231.44.251|3128|United States|Racine|AT&T Services, Inc.|
|5|5.161.105.105|80|United States|Ashburn|Hetzner Online GmbH|
|6|216.238.74.45|59394|Mexico|Mexico City|The Constant Company|
|7|12.231.44.251|3128|United States|Racine|AT&T Services, Inc.|
|8|198.41.67.18|8080|United States|Lafayette|Cox Communications Inc.|
|9|157.185.179.70|59394|United States|Los Angeles|Quantil Networks Inc|
|10|5.161.105.105|80|United States|Ashburn|Hetzner Online GmbH|
|11|159.192.249.44|8080|Thailand|Bangkok|CAT-BB|
|12|51.250.80.131|80|Russia|Moscow|Yandex.Cloud LLC|
|13|8.210.66.212|3128|Hong Kong|Hong Kong|Alibaba.com LLC|
|14|88.132.95.93|53281|Hungary|Olaszliszka|PRTELECOM|
|15|12.231.44.251|3128|United States|Racine|AT&T Services, Inc.|
|16|121.156.109.108|8080|South Korea|Seongnam-si|Korea Telecom|
|17|51.250.80.131|80|Russia|Moscow|Yandex.Cloud LLC|
|18|45.182.140.201|999|Venezuela|Valencia|NETCOM PLUS, C.A|
|19|116.253.208.239|33080|China|Guangxi|CHINATELECOM Guangxi Nanning IDC networkdescr: Nanning, Guangxi Province, P.R.|
|20|157.230.34.219|3128|Singapore|Singapore|DigitalOcean, LLC|



## Contributing

Contributions are welcome, and they are greatly appreciated! Every
little bit helps, and credit will always be given.

