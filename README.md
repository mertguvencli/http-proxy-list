
# Free HTTP Proxy List 🌍

[![Hourly Update](https://github.com/mertguvencli/http-proxy-list/actions/workflows/main.yml/badge.svg?branch=main)](https://github.com/mertguvencli/http-proxy-list/actions/workflows/main.yml)
![GitHub](https://img.shields.io/github/license/mertguvencli/http-proxy-list)
![GitHub last commit](https://img.shields.io/github/last-commit/mertguvencli/http-proxy-list)

It is a lightweight project that hourly scrapes lots of free-proxy sites, validates if it works, and serves a clean proxy list.


> Scraper found **3353** proxies at the latest update. Usable proxies are below.

## Usage

Click the file format that you want and copy the URL.


|File|Content|Count|
|----|-------|-----|
|[data.txt](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.txt)|`ip_address:port` combined (seperated new line)|117|
|[data.json](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.json)|`ip, port`|117|
|[data-with-geolocation.json](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data-with-geolocation.json)|`ip, port, geolocation`|117|

## Sources

|Source|Found Proxies|Succeed|
|------|-------------|-------|
|[free-proxy-list.net](https://free-proxy-list.net)|300|✅|
|[us-proxy.org](https://www.us-proxy.org)|200|✅|
|[proxydb.net](http://proxydb.net)|15|✅|
|[free-proxy-list.com](https://free-proxy-list.com/?page=&port=&type%5B%5D=http&type%5B%5D=https&up_time=0&search=Search)|10|✅|
|[proxy-list.download](https://www.proxy-list.download/HTTP)|26|✅|
|[vpnoverview.com](https://vpnoverview.com/privacy/anonymous-browsing/free-proxy-servers)|32|✅|
|[proxyscan.io](https://www.proxyscan.io)|78|✅|
|[proxylist.geonode.com](https://proxylist.geonode.com/api/proxy-list?limit=300&page=1&sort_by=lastChecked&sort_type=desc&protocols=http,https)|0|🚫|
|[proxyscrape.com](https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all)|311|✅|
|[github.com/clarketm/proxy-list](https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt)|400|✅|
|[github.com/monosans/proxy-list](https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt)|67|✅|
|[github.com/TheSpeedX/PROXY-List](https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt)|1914|✅|


## Sample Proxies With Geolocation Info

|#|Ip|Port|Country|City|Internet Service Provider|
|-|--|----|-------|----|-------------------------|
|1|45.42.177.51|3128|United States|Ashburn|PeaceWeb|
|2|149.19.224.38|3128|United States|Sterling|SPRINT|
|3|159.197.250.134|3128|United States|Mount Prospect|Sprint|
|4|45.42.177.51|3128|United States|Ashburn|PeaceWeb|
|5|159.197.250.134|3128|United States|Mount Prospect|Sprint|
|6|149.19.224.38|3128|United States|Sterling|SPRINT|
|7|128.201.119.250|999|Chile|Molina|COMERCIAL WASHINGTON ERNESTO OYARCE SAZO E.I.R.L. (SEÑALMAX)|
|8|103.142.200.58|8080|Indonesia|Ternate|THEKO|
|9|36.255.86.114|83|India|Mumbai|Gatik Business Solutions|
|10|189.193.224.222|999|Mexico|Papalotla|Mega Cable, S.A. de C.V.|
|11|103.248.93.5|8080|India|Delhi|Ani Network Pvt Ltd|
|12|45.42.177.51|3128|United States|Ashburn|PeaceWeb|
|13|20.47.108.204|8888|United States|Boydton|Microsoft Corporation|
|14|190.26.201.194|8080|Colombia|Bogotá|ETB - Colombia|
|15|157.100.12.138|999|Ecuador|Quito|Telconet S.A|
|16|176.9.162.107|443|Germany|Falkenstein|Hetzner Online GmbH|
|17|50.233.42.98|51696|United States|Evanston|Comcast Cable Communications, LLC|
|18|187.188.108.114|8080|Mexico|Coyoacán|Total Play Telecomunicaciones SA De CV|
|19|47.252.4.64|8888|United States|Charlottesville|Alibaba.com LLC|
|20|200.105.215.18|33630|Bolivia|La Paz|AXS Bolivia S. A.|



## Contributing

Contributions are welcome, and they are greatly appreciated! Every
little bit helps, and credit will always be given.

