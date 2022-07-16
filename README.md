
# Free HTTP Proxy List 🌍

[![Hourly Update](https://github.com/mertguvencli/http-proxy-list/actions/workflows/main.yml/badge.svg?branch=main)](https://github.com/mertguvencli/http-proxy-list/actions/workflows/main.yml)
![GitHub](https://img.shields.io/github/license/mertguvencli/http-proxy-list)
![GitHub last commit](https://img.shields.io/github/last-commit/mertguvencli/http-proxy-list)

It is a lightweight project that hourly scrapes lots of free-proxy sites, validates if it works, and serves a clean proxy list.


> Scraper found **3715** proxies at the latest update. Usable proxies are below.

## Usage

Click the file format that you want and copy the URL.


|File|Content|Count|
|----|-------|-----|
|[data.txt](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.txt)|`ip_address:port` combined (seperated new line)|194|
|[data.json](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.json)|`ip, port`|194|
|[data-with-geolocation.json](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data-with-geolocation.json)|`ip, port, geolocation`|194|

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
|[proxyscrape.com](https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all)|368|✅|
|[github.com/clarketm/proxy-list](https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt)|400|✅|
|[github.com/monosans/proxy-list](https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt)|221|✅|
|[github.com/TheSpeedX/PROXY-List](https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt)|1843|✅|


## Sample Proxies With Geolocation Info

|#|Ip|Port|Country|City|Internet Service Provider|
|-|--|----|-------|----|-------------------------|
|1|5.161.105.105|80|United States|Ashburn|Hetzner Online GmbH|
|2|170.39.194.16|3128|United States|Ashburn|Rackdog, LLC|
|3|198.41.67.18|8080|United States|Lafayette|Cox Communications Inc.|
|4|170.39.194.16|3128|United States|Ashburn|Rackdog, LLC|
|5|5.161.105.105|80|United States|Ashburn|Hetzner Online GmbH|
|6|198.41.67.18|8080|United States|Lafayette|Cox Communications Inc.|
|7|20.81.62.32|3128|United States|Boydton|Microsoft Corporation|
|8|8.219.97.248|80|Singapore|Singapore|Alibaba (US) Technology Co., Ltd.|
|9|20.81.62.32|3128|United States|Boydton|Microsoft Corporation|
|10|104.37.102.181|8181|United States|Veedersburg|ALTIUS Broadband, LLC|
|11|157.100.12.138|999|Ecuador|Loja|Telconet S.A|
|12|85.14.243.31|3128|Germany|Kamp-Lintfort|myLoc managed IT AG|
|13|163.47.11.211|12358|Singapore|Singapore|DigitalOcean|
|14|103.252.1.137|3128|Vietnam|Hanoi|CMCMIENBAC|
|15|216.238.83.123|59394|Mexico|Mexico City|The Constant Company|
|16|216.238.80.50|59394|Mexico|Mexico City|The Constant Company|
|17|216.238.81.217|59394|Mexico|Mexico City|The Constant Company|
|18|181.205.20.195|999|Colombia|Medellín|EPM Telecomunicaciones S.A. E.S.P.|
|19|206.189.195.74|8080|United States|North Bergen|DigitalOcean, LLC|
|20|218.185.234.194|8080|Australia|Melbourne|World Without Wires Pty Ltd|



## Contributing

Contributions are welcome, and they are greatly appreciated! Every
little bit helps, and credit will always be given.

