
# Free HTTP Proxy List 🌍

[![Hourly Update](https://github.com/mertguvencli/http-proxy-list/actions/workflows/main.yml/badge.svg?branch=main)](https://github.com/mertguvencli/http-proxy-list/actions/workflows/main.yml)
![GitHub](https://img.shields.io/github/license/mertguvencli/http-proxy-list)
![GitHub last commit](https://img.shields.io/github/last-commit/mertguvencli/http-proxy-list)

It is a lightweight project that hourly scrapes lots of free-proxy sites, validates if it works, and serves a clean proxy list.


> Scraper found **3234** proxies at the latest update. Usable proxies are below.

## Usage

Click the file format that you want and copy the URL.


|File|Content|Count|
|----|-------|-----|
|[data.txt](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.txt)|`ip_address:port` combined (seperated new line)|64|
|[data.json](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.json)|`ip, port`|64|
|[data-with-geolocation.json](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data-with-geolocation.json)|`ip, port, geolocation`|64|

## Sources

|Source|Found Proxies|Succeed|
|------|-------------|-------|
|[free-proxy-list.net](https://free-proxy-list.net)|300|✅|
|[us-proxy.org](https://www.us-proxy.org)|200|✅|
|[proxydb.net](http://proxydb.net)|15|✅|
|[free-proxy-list.com](https://free-proxy-list.com/?page=&port=&type%5B%5D=http&type%5B%5D=https&up_time=0&search=Search)|0|🚫|
|[proxy-list.download](https://www.proxy-list.download/HTTP)|26|✅|
|[vpnoverview.com](https://vpnoverview.com/privacy/anonymous-browsing/free-proxy-servers)|32|✅|
|[proxyscan.io](https://www.proxyscan.io)|37|✅|
|[proxylist.geonode.com](https://proxylist.geonode.com/api/proxy-list?limit=300&page=1&sort_by=lastChecked&sort_type=desc&protocols=http,https)|0|🚫|
|[proxyscrape.com](https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all)|286|✅|
|[github.com/clarketm/proxy-list](https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt)|400|✅|
|[github.com/monosans/proxy-list](https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt)|76|✅|
|[github.com/TheSpeedX/PROXY-List](https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt)|1862|✅|


## Sample Proxies With Geolocation Info

|#|Ip|Port|Country|City|Internet Service Provider|
|-|--|----|-------|----|-------------------------|
|1|20.47.108.204|8888|United States|Boydton|Microsoft Corporation|
|2|51.79.50.46|9300|Canada|Beauharnois|OVH SAS|
|3|201.174.239.18|8080|Mexico|Ciudad Juárez|Transtelco Inc|
|4|162.150.62.95|443|United States|Kincaid|Comcast Cable Communications, LLC|
|5|45.189.253.177|999|Mexico|Tetela|Tracered SA De CV|
|6|201.222.45.65|999|Chile|La Pintana|GRUPO ULLOA SpA|
|7|162.150.62.96|443|United States|Kincaid|Comcast Cable Communications, LLC|
|8|118.99.104.136|8080|Indonesia|Bojongsalaman|Biznet Networks|
|9|201.158.47.66|8080|Brazil|Sorocaba|AS|
|10|114.4.104.254|3128|Indonesia|Jakarta|PT. INDOSAT Tbk|
|11|103.151.246.14|10001|Indonesia|Mamuju|MANAKARRANET|
|12|121.156.109.108|8080|South Korea|Seongnam-si|Korea Telecom|
|13|104.37.102.181|8181|United States|Attica|ALTIUS Broadband, LLC|
|14|89.250.152.76|8080|Russia|Tyumen|JSC "ER-Telecom Holding"|
|15|162.150.62.96|443|United States|Kincaid|Comcast Cable Communications, LLC|
|16|47.252.4.64|8888|United States|Charlottesville|Alibaba.com LLC|
|17|162.150.62.93|443|United States|Kincaid|Comcast Cable Communications, LLC|
|18|190.26.217.98|999|Colombia|Montelíbano|ETB - Colombia|
|19|157.100.53.102|999|Ecuador|Machala|Nedetel S.A.|
|20|157.90.205.166|8080|Germany|Falkenstein|Hetzner Online GmbH|



## Contributing

Contributions are welcome, and they are greatly appreciated! Every
little bit helps, and credit will always be given.

