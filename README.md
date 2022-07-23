
# Free HTTP Proxy List 🌍

[![Hourly Update](https://github.com/mertguvencli/http-proxy-list/actions/workflows/main.yml/badge.svg?branch=main)](https://github.com/mertguvencli/http-proxy-list/actions/workflows/main.yml)
![GitHub](https://img.shields.io/github/license/mertguvencli/http-proxy-list)
![GitHub last commit](https://img.shields.io/github/last-commit/mertguvencli/http-proxy-list)

It is a lightweight project that hourly scrapes lots of free-proxy sites, validates if it works, and serves a clean proxy list.


> Scraper found **3885** proxies at the latest update. Usable proxies are below.

## Usage

Click the file format that you want and copy the URL.


|File|Content|Count|
|----|-------|-----|
|[data.txt](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.txt)|`ip_address:port` combined (seperated new line)|255|
|[data.json](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.json)|`ip, port`|255|
|[data-with-geolocation.json](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data-with-geolocation.json)|`ip, port, geolocation`|255|

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
|[proxyscrape.com](https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all)|408|✅|
|[github.com/clarketm/proxy-list](https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt)|400|✅|
|[github.com/monosans/proxy-list](https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt)|268|✅|
|[github.com/TheSpeedX/PROXY-List](https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt)|1826|✅|


## Sample Proxies With Geolocation Info

|#|Ip|Port|Country|City|Internet Service Provider|
|-|--|----|-------|----|-------------------------|
|1|66.196.238.181|3128|United States|Cypress|Logix|
|2|5.161.105.105|80|United States|Ashburn|Hetzner Online GmbH|
|3|5.161.105.105|80|United States|Ashburn|Hetzner Online GmbH|
|4|13.125.238.23|3128|South Korea|Seoul|Amazon Technologies Inc.|
|5|200.111.182.6|443|Chile|Santiago|Entel Chile S.A.|
|6|8.219.97.248|80|Singapore|Singapore|Alibaba (US) Technology Co., Ltd.|
|7|180.183.8.91|8080|Thailand|Bangkok|Triple T Broadband Public Company Limited|
|8|103.143.209.242|8090|Vietnam|Hanoi|Branch of N Support Joint Stock Company|
|9|136.243.124.244|3128|Germany|Nuremberg|Hetzner Online GmbH|
|10|20.81.62.32|3128|United States|Boydton|Microsoft Corporation|
|11|20.81.62.32|3128|United States|Boydton|Microsoft Corporation|
|12|1.32.49.253|8080|Malaysia|Masai|Telekom Malaysia Berhad|
|13|197.211.35.195|8080|Nigeria|Lagos|Globacom Limited|
|14|43.249.224.170|83|India|Hyderabad|Equinox Consulting PVT LTD|
|15|5.161.105.105|80|United States|Ashburn|Hetzner Online GmbH|
|16|121.156.109.108|8080|South Korea|Seongnam-si|Korea Telecom|
|17|121.156.109.108|8080|South Korea|Seongnam-si|Korea Telecom|
|18|103.252.45.162|2019|India|New Delhi|MegaHostZone|
|19|209.166.175.201|8080|United States|Pittsburgh|CONTINENTAL BROADBAND PENNSYLVANIA, INC.|
|20|200.105.215.18|33630|Bolivia|La Paz|AXS Bolivia S. A.|



## Contributing

Contributions are welcome, and they are greatly appreciated! Every
little bit helps, and credit will always be given.

