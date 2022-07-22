
# Free HTTP Proxy List 🌍

[![Hourly Update](https://github.com/mertguvencli/http-proxy-list/actions/workflows/main.yml/badge.svg?branch=main)](https://github.com/mertguvencli/http-proxy-list/actions/workflows/main.yml)
![GitHub](https://img.shields.io/github/license/mertguvencli/http-proxy-list)
![GitHub last commit](https://img.shields.io/github/last-commit/mertguvencli/http-proxy-list)

It is a lightweight project that hourly scrapes lots of free-proxy sites, validates if it works, and serves a clean proxy list.


> Scraper found **3336** proxies at the latest update. Usable proxies are below.

## Usage

Click the file format that you want and copy the URL.


|File|Content|Count|
|----|-------|-----|
|[data.txt](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.txt)|`ip_address:port` combined (seperated new line)|126|
|[data.json](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.json)|`ip, port`|126|
|[data-with-geolocation.json](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data-with-geolocation.json)|`ip, port, geolocation`|126|

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
|[proxyscrape.com](https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all)|255|✅|
|[github.com/clarketm/proxy-list](https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt)|400|✅|
|[github.com/monosans/proxy-list](https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt)|152|✅|
|[github.com/TheSpeedX/PROXY-List](https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt)|1846|✅|


## Sample Proxies With Geolocation Info

|#|Ip|Port|Country|City|Internet Service Provider|
|-|--|----|-------|----|-------------------------|
|1|144.202.61.154|8888|United States|Elk Grove Village|The Constant Company|
|2|20.47.108.204|8888|United States|Boydton|Microsoft Corporation|
|3|144.202.61.154|8888|United States|Elk Grove Village|The Constant Company|
|4|157.100.12.138|999|Ecuador|Loja|Telconet S.A|
|5|51.250.80.131|80|Russia|Moscow|Yandex.Cloud LLC|
|6|8.219.97.248|80|Singapore|Singapore|Alibaba (US) Technology Co., Ltd.|
|7|116.58.239.10|80|Thailand|Ban Kha|CAT-BB|
|8|140.227.61.156|23456|Japan|Chiyoda|NTT PC Communications, Inc.|
|9|190.61.55.138|999|Colombia|Chapinero|Ufinet Panama S.A.|
|10|120.29.124.131|8080|Philippines|Tarlac City|ComClark Network & Technology Corp|
|11|47.89.185.178|8888|United States|Charlottesville|Alibaba.com LLC|
|12|157.100.12.138|999|Ecuador|Loja|Telconet S.A|
|13|8.219.97.248|80|Singapore|Singapore|Alibaba (US) Technology Co., Ltd.|
|14|85.14.243.31|3128|Germany|Kamp-Lintfort|myLoc managed IT AG|
|15|122.155.165.191|3128|Thailand|Ratchathewi|CAT Telecom Public Company Limited|
|16|209.166.175.201|3128|United States|Pittsburgh|CONTINENTAL BROADBAND PENNSYLVANIA, INC.|
|17|136.243.124.244|3128|Germany|Nuremberg|Hetzner Online GmbH|
|18|187.188.147.170|999|Mexico|San Luis Potosí City|Total Play Telecomunicaciones SA De CV|
|19|159.65.133.175|31280|Singapore|Singapore|DigitalOcean, LLC|
|20|8.219.97.248|80|Singapore|Singapore|Alibaba (US) Technology Co., Ltd.|



## Contributing

Contributions are welcome, and they are greatly appreciated! Every
little bit helps, and credit will always be given.

