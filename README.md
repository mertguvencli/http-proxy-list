
# Free HTTP Proxy List 🌍

[![Hourly Update](https://github.com/mertguvencli/http-proxy-list/actions/workflows/main.yml/badge.svg?branch=main)](https://github.com/mertguvencli/http-proxy-list/actions/workflows/main.yml)
![GitHub](https://img.shields.io/github/license/mertguvencli/http-proxy-list)
![GitHub last commit](https://img.shields.io/github/last-commit/mertguvencli/http-proxy-list)

It is a lightweight project that hourly scrapes lots of free-proxy sites, validates if it works, and serves a clean proxy list.


> Scraper found **3599** proxies at the latest update. Usable proxies are below.

## Usage

Click the file format that you want and copy the URL.


|File|Content|Count|
|----|-------|-----|
|[data.txt](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.txt)|`ip_address:port` combined (seperated new line)|221|
|[data.json](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.json)|`ip, port`|221|
|[data-with-geolocation.json](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data-with-geolocation.json)|`ip, port, geolocation`|221|

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
|[proxyscrape.com](https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all)|318|✅|
|[github.com/clarketm/proxy-list](https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt)|400|✅|
|[github.com/monosans/proxy-list](https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt)|224|✅|
|[github.com/TheSpeedX/PROXY-List](https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt)|1774|✅|


## Sample Proxies With Geolocation Info

|#|Ip|Port|Country|City|Internet Service Provider|
|-|--|----|-------|----|-------------------------|
|1|20.47.108.204|8888|United States|Boydton|Microsoft Corporation|
|2|209.97.152.208|8888|United States|Clifton|DigitalOcean, LLC|
|3|20.47.108.204|8888|United States|Boydton|Microsoft Corporation|
|4|64.189.24.250|3129|United States|Chicago|WhiteSky Communications, LLC.|
|5|51.250.80.131|80|Russia|Moscow|Yandex.Cloud LLC|
|6|207.204.241.126|8118|United States|San Francisco|Strong Technology|
|7|138.68.238.19|31028|United States|Santa Clara|DigitalOcean, LLC|
|8|64.189.24.250|3129|United States|Chicago|WhiteSky Communications, LLC.|
|9|47.89.185.178|8888|United States|Charlottesville|Alibaba.com LLC|
|10|209.97.152.208|8888|United States|Clifton|DigitalOcean, LLC|
|11|157.100.12.138|999|Ecuador|Loja|Telconet S.A|
|12|8.219.97.248|80|Singapore|Singapore|Alibaba (US) Technology Co., Ltd.|
|13|216.238.82.41|59394|Mexico|Mexico City|The Constant Company|
|14|47.89.185.178|8888|United States|Charlottesville|Alibaba.com LLC|
|15|163.47.11.211|12358|Singapore|Singapore|DigitalOcean|
|16|103.252.1.137|3128|Vietnam|Hanoi|CMCMIENBAC|
|17|45.182.190.186|999|Colombia|Bogotá|TV AZTECA SUCURSAL COLOMBIA|
|18|216.238.73.171|59394|Mexico|Mexico City|The Constant Company|
|19|103.145.253.237|3128|Vietnam|Hanoi|Enterprise Sortware Company Limited|
|20|102.68.128.216|8080|Libya|Tripoli|Aljeel Aljadeed For Technology|



## Contributing

Contributions are welcome, and they are greatly appreciated! Every
little bit helps, and credit will always be given.

