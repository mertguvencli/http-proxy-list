
# Free HTTP Proxy List 🌍

[![Hourly Update](https://github.com/mertguvencli/http-proxy-list/actions/workflows/main.yml/badge.svg?branch=main)](https://github.com/mertguvencli/http-proxy-list/actions/workflows/main.yml)
![GitHub](https://img.shields.io/github/license/mertguvencli/http-proxy-list)
![GitHub last commit](https://img.shields.io/github/last-commit/mertguvencli/http-proxy-list)

It is a lightweight project that hourly scrapes lots of free-proxy sites, validates if it works, and serves a clean proxy list.


> Scraper found **3857** proxies at the latest update. Usable proxies are below.

## Usage

Click the file format that you want and copy the URL.


|File|Content|Count|
|----|-------|-----|
|[data.txt](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.txt)|`ip_address:port` combined (seperated new line)|293|
|[data.json](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.json)|`ip, port`|293|
|[data-with-geolocation.json](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data-with-geolocation.json)|`ip, port, geolocation`|293|

## Sources

|Source|Found Proxies|Succeed|
|------|-------------|-------|
|[free-proxy-list.net](https://free-proxy-list.net)|300|✅|
|[us-proxy.org](https://www.us-proxy.org)|200|✅|
|[proxydb.net](http://proxydb.net)|15|✅|
|[free-proxy-list.com](https://free-proxy-list.com/?page=&port=&type%5B%5D=http&type%5B%5D=https&up_time=0&search=Search)|10|✅|
|[proxy-list.download](https://www.proxy-list.download/HTTP)|26|✅|
|[vpnoverview.com](https://vpnoverview.com/privacy/anonymous-browsing/free-proxy-servers)|32|✅|
|[proxyscan.io](https://www.proxyscan.io)|0|🚫|
|[proxylist.geonode.com](https://proxylist.geonode.com/api/proxy-list?limit=300&page=1&sort_by=lastChecked&sort_type=desc&protocols=http,https)|300|✅|
|[proxyscrape.com](https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all)|432|✅|
|[github.com/clarketm/proxy-list](https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt)|400|✅|
|[github.com/monosans/proxy-list](https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt)|179|✅|
|[github.com/TheSpeedX/PROXY-List](https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt)|1963|✅|


## Sample Proxies With Geolocation Info

|#|Ip|Port|Country|City|Internet Service Provider|
|-|--|----|-------|----|-------------------------|
|1|45.152.188.246|3128|United States|Ashburn|Sprint|
|2|157.185.179.70|59394|United States|Los Angeles|Quantil Networks Inc|
|3|12.231.44.251|3128|United States|Racine|AT&T Services, Inc.|
|4|216.238.74.45|59394|Mexico|Mexico City|The Constant Company|
|5|216.238.76.66|59394|Mexico|Mexico City|The Constant Company|
|6|45.152.188.246|3128|United States|Ashburn|Sprint|
|7|157.185.179.70|59394|United States|Los Angeles|Quantil Networks Inc|
|8|12.231.44.251|3128|United States|Racine|AT&T Services, Inc.|
|9|8.219.97.248|80|Singapore|Singapore|Alibaba (US) Technology Co., Ltd.|
|10|8.210.66.212|3128|Hong Kong|Hong Kong|Alibaba.com LLC|
|11|5.161.105.105|80|United States|Ashburn|Hetzner Online GmbH|
|12|64.189.24.250|3129|United States|Chicago|WhiteSky Communications, LLC.|
|13|198.41.67.18|8080|United States|Lafayette|Cox Communications Inc.|
|14|148.163.85.162|2019|United States|Phoenix|Input Output Flood LLC|
|15|150.230.114.193|80|United Kingdom|London|Oracle Corporation|
|16|209.166.175.201|8080|United States|Pittsburgh|CONTINENTAL BROADBAND PENNSYLVANIA, INC.|
|17|182.90.224.115|3128|China|Beihai|China Unicom Guangxi Province Network|
|18|85.25.91.141|15333|Germany|Cologne|PlusServer GmbH|
|19|105.112.191.250|3128|Nigeria|Lagos|Airtel Networks Limited|
|20|85.14.243.31|3128|Germany|Meerbusch|myLoc managed IT AG|



## Contributing

Contributions are welcome, and they are greatly appreciated! Every
little bit helps, and credit will always be given.

