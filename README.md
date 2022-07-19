
# Free HTTP Proxy List 🌍

[![Hourly Update](https://github.com/mertguvencli/http-proxy-list/actions/workflows/main.yml/badge.svg?branch=main)](https://github.com/mertguvencli/http-proxy-list/actions/workflows/main.yml)
![GitHub](https://img.shields.io/github/license/mertguvencli/http-proxy-list)
![GitHub last commit](https://img.shields.io/github/last-commit/mertguvencli/http-proxy-list)

It is a lightweight project that hourly scrapes lots of free-proxy sites, validates if it works, and serves a clean proxy list.


> Scraper found **3484** proxies at the latest update. Usable proxies are below.

## Usage

Click the file format that you want and copy the URL.


|File|Content|Count|
|----|-------|-----|
|[data.txt](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.txt)|`ip_address:port` combined (seperated new line)|185|
|[data.json](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.json)|`ip, port`|185|
|[data-with-geolocation.json](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data-with-geolocation.json)|`ip, port, geolocation`|185|

## Sources

|Source|Found Proxies|Succeed|
|------|-------------|-------|
|[free-proxy-list.net](https://free-proxy-list.net)|300|✅|
|[us-proxy.org](https://www.us-proxy.org)|200|✅|
|[proxydb.net](http://proxydb.net)|15|✅|
|[free-proxy-list.com](https://free-proxy-list.com/?page=&port=&type%5B%5D=http&type%5B%5D=https&up_time=0&search=Search)|10|✅|
|[proxy-list.download](https://www.proxy-list.download/HTTP)|26|✅|
|[vpnoverview.com](https://vpnoverview.com/privacy/anonymous-browsing/free-proxy-servers)|32|✅|
|[proxyscan.io](https://www.proxyscan.io)|79|✅|
|[proxylist.geonode.com](https://proxylist.geonode.com/api/proxy-list?limit=300&page=1&sort_by=lastChecked&sort_type=desc&protocols=http,https)|0|🚫|
|[proxyscrape.com](https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all)|322|✅|
|[github.com/clarketm/proxy-list](https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt)|400|✅|
|[github.com/monosans/proxy-list](https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt)|176|✅|
|[github.com/TheSpeedX/PROXY-List](https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt)|1924|✅|


## Sample Proxies With Geolocation Info

|#|Ip|Port|Country|City|Internet Service Provider|
|-|--|----|-------|----|-------------------------|
|1|20.47.108.204|8888|United States|Boydton|Microsoft Corporation|
|2|5.161.105.105|80|United States|Ashburn|Hetzner Online GmbH|
|3|20.47.108.204|8888|United States|Boydton|Microsoft Corporation|
|4|5.161.105.105|80|United States|Ashburn|Hetzner Online GmbH|
|5|157.100.12.138|999|Ecuador|Loja|Telconet S.A|
|6|8.219.97.248|80|Singapore|Singapore|Alibaba (US) Technology Co., Ltd.|
|7|136.243.124.244|3128|Germany|Nuremberg|Hetzner Online GmbH|
|8|78.38.11.131|8080|Iran|Urmia|Adsl Project Azargharbi Data|
|9|103.143.196.50|8080|Indonesia|Sukoharjo|JERNIHNETWORK|
|10|103.154.230.58|8080|Indonesia|Sukorejo|DIGITNET|
|11|181.74.81.195|999|Chile|Limache|Telmex Servicios Empresariales S.A.|
|12|62.3.30.26|8080|Georgia|Tbilisi|Enbinet Ltd.|
|13|190.95.156.166|999|Ecuador|Guayaquil|Telconet S.A|
|14|45.182.22.54|999|Honduras|San Pedro Sula|Multicable De Honduras|
|15|190.26.201.194|8080|Colombia|Bogotá|ETB - Colombia|
|16|5.161.105.105|80|United States|Ashburn|Hetzner Online GmbH|
|17|103.14.130.39|8080|Bangladesh|Madaripur|Radiant telecommunications|
|18|8.219.97.248|80|Singapore|Singapore|Alibaba (US) Technology Co., Ltd.|
|19|51.250.80.131|80|Russia|Moscow|Yandex.Cloud LLC|
|20|14.141.209.11|8080|India|Chennai|Tata Communications Limited|



## Contributing

Contributions are welcome, and they are greatly appreciated! Every
little bit helps, and credit will always be given.

