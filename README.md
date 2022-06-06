
# Free HTTP Proxy List 🌍

[![Hourly Update](https://github.com/mertguvencli/http-proxy-list/actions/workflows/main.yml/badge.svg?branch=main)](https://github.com/mertguvencli/http-proxy-list/actions/workflows/main.yml)
![GitHub](https://img.shields.io/github/license/mertguvencli/http-proxy-list)
![GitHub last commit](https://img.shields.io/github/last-commit/mertguvencli/http-proxy-list)

It is a lightweight project that hourly scrapes lots of free-proxy sites, validates if it works, and serves a clean proxy list.


> Scraper found **3130** proxies at the latest update. Usable proxies are below.

## Usage

Click the file format that you want and copy the URL.


|File|Content|Count|
|----|-------|-----|
|[data.txt](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.txt)|`ip_address:port` combined (seperated new line)|151|
|[data.json](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.json)|`ip, port`|151|
|[data-with-geolocation.json](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data-with-geolocation.json)|`ip, port, geolocation`|151|

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
|[proxylist.geonode.com](https://proxylist.geonode.com/api/proxy-list?limit=300&page=1&sort_by=lastChecked&sort_type=desc&protocols=http,https)|0|🚫|
|[proxyscrape.com](https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all)|204|✅|
|[github.com/clarketm/proxy-list](https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt)|400|✅|
|[github.com/monosans/proxy-list](https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt)|93|✅|
|[github.com/TheSpeedX/PROXY-List](https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt)|1850|✅|


## Sample Proxies With Geolocation Info

|#|Ip|Port|Country|City|Internet Service Provider|
|-|--|----|-------|----|-------------------------|
|1|20.47.108.204|8888|United States|Boydton|Microsoft Corporation|
|2|116.203.72.47|8118|Germany|Nuremberg|Hetzner Online GmbH|
|3|192.241.205.151|3129|United States|San Francisco|DigitalOcean, LLC|
|4|45.167.125.209|9992|Colombia|Popayán|Sepcom Comunicaciones SAS|
|5|190.97.226.236|999|Venezuela|Barinas|NetLink América C.A.|
|6|157.100.12.138|999|Ecuador|Quito|Telconet S.A|
|7|18.196.224.91|39593|Germany|Frankfurt am Main|Amazon Technologies Inc.|
|8|110.170.126.13|3128|Thailand|Din Daeng|True Internet Corporation CO. Ltd.|
|9|103.155.199.24|8181|Indonesia|Batununggal|PT Lintas Jaringan Nusantara|
|10|162.150.62.96|443|United States|Kincaid|Comcast Cable Communications, LLC|
|11|103.106.219.135|8080|Indonesia|Pasuruan|PT. ARTHA LINTAS DATA MANDIRI|
|12|85.117.56.151|8080|Georgia|Tbilisi|Caucasus Online Ltd.|
|13|31.173.10.58|3128|Russia|Balashikha|MegaFon|
|14|192.241.205.151|3129|United States|San Francisco|DigitalOcean, LLC|
|15|162.150.62.93|443|United States|Kincaid|Comcast Cable Communications, LLC|
|16|200.105.215.18|33630|Bolivia|La Paz|AXS Bolivia S. A.|
|17|45.167.125.209|9992|Colombia|Popayán|Sepcom Comunicaciones SAS|
|18|222.127.178.58|8080|Philippines|Makati City|Globe Telecom Inc.|
|19|91.151.89.32|1697|Turkey|Sisli|Talha Bogaz|
|20|183.98.167.131|9999|South Korea|Gangnam-gu|Korea Telecom|



## Contributing

Contributions are welcome, and they are greatly appreciated! Every
little bit helps, and credit will always be given.

