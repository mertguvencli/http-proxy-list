
# Free HTTP Proxy List 🌍

[![Hourly Update](https://github.com/mertguvencli/http-proxy-list/actions/workflows/main.yml/badge.svg?branch=main)](https://github.com/mertguvencli/http-proxy-list/actions/workflows/main.yml)
![GitHub](https://img.shields.io/github/license/mertguvencli/http-proxy-list)
![GitHub last commit](https://img.shields.io/github/last-commit/mertguvencli/http-proxy-list)

It is a lightweight project that hourly scrapes lots of free-proxy sites, validates if it works, and serves a clean proxy list.


> Scraper found **3625** proxies at the latest update. Usable proxies are below.

## Usage

Click the file format that you want and copy the URL.


|File|Content|Count|
|----|-------|-----|
|[data.txt](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.txt)|`ip_address:port` combined (seperated new line)|130|
|[data.json](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.json)|`ip, port`|130|
|[data-with-geolocation.json](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data-with-geolocation.json)|`ip, port, geolocation`|130|

## Sources

|Source|Found Proxies|Succeed|
|------|-------------|-------|
|[free-proxy-list.net](https://free-proxy-list.net)|300|✅|
|[us-proxy.org](https://www.us-proxy.org)|200|✅|
|[proxydb.net](http://proxydb.net)|15|✅|
|[free-proxy-list.com](https://free-proxy-list.com/?page=&port=&type%5B%5D=http&type%5B%5D=https&up_time=0&search=Search)|10|✅|
|[proxy-list.download](https://www.proxy-list.download/HTTP)|0|🚫|
|[vpnoverview.com](https://vpnoverview.com/privacy/anonymous-browsing/free-proxy-servers)|32|✅|
|[proxyscan.io](https://www.proxyscan.io)|0|🚫|
|[proxylist.geonode.com](https://proxylist.geonode.com/api/proxy-list?limit=300&page=1&sort_by=lastChecked&sort_type=desc&protocols=http,https)|300|✅|
|[proxyscrape.com](https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all)|297|✅|
|[github.com/clarketm/proxy-list](https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt)|400|✅|
|[github.com/monosans/proxy-list](https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt)|193|✅|
|[github.com/TheSpeedX/PROXY-List](https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt)|1878|✅|


## Sample Proxies With Geolocation Info

|#|Ip|Port|Country|City|Internet Service Provider|
|-|--|----|-------|----|-------------------------|
|1|159.65.198.235|443|Netherlands|Amsterdam|DigitalOcean, LLC|
|2|20.81.62.32|3128|United States|Boydton|Microsoft Corporation|
|3|20.47.108.204|8888|United States|Boydton|Microsoft Corporation|
|4|5.161.105.105|80|United States|Ashburn|Hetzner Online GmbH|
|5|174.138.116.12|80|United States|Clifton|DigitalOcean, LLC|
|6|5.161.105.105|80|United States|Ashburn|Hetzner Online GmbH|
|7|47.89.185.178|8888|United States|Charlottesville|Alibaba.com LLC|
|8|144.202.61.154|8888|United States|Elk Grove Village|The Constant Company|
|9|114.4.104.254|3128|Indonesia|Jakarta|PT. INDOSAT Tbk|
|10|105.112.191.250|3128|Nigeria|Lagos|Airtel Networks Limited|
|11|64.189.24.250|3129|United States|Chicago|WhiteSky Communications, LLC.|
|12|37.120.192.154|8080|Netherlands|Amsterdam|M247 Ltd|
|13|192.195.57.72|3128|Brazil|Maceió|AS|
|14|20.81.62.32|3128|United States|Boydton|Microsoft Corporation|
|15|20.81.62.32|3128|United States|Boydton|Microsoft Corporation|
|16|110.44.113.105|8080|Nepal|Kathmandu|Vianet Communications Pvt. Ltd|
|17|5.161.105.105|80|United States|Ashburn|Hetzner Online GmbH|
|18|187.190.0.205|999|Mexico|San Luis Potosí City|Total Play Telecomunicaciones SA De CV|
|19|46.53.191.60|3128|Belarus|Borovlyany|FE "ALTERNATIVNAYA ZIFROVAYA SET" Minsk|
|20|8.219.97.248|80|Singapore|Singapore|Alibaba (US) Technology Co., Ltd.|



## Contributing

Contributions are welcome, and they are greatly appreciated! Every
little bit helps, and credit will always be given.

