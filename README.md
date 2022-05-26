
# Free HTTP Proxy List 🌍

[![Hourly Update](https://github.com/mertguvencli/http-proxy-list/actions/workflows/main.yml/badge.svg?branch=main)](https://github.com/mertguvencli/http-proxy-list/actions/workflows/main.yml)
![GitHub](https://img.shields.io/github/license/mertguvencli/http-proxy-list)
![GitHub last commit](https://img.shields.io/github/last-commit/mertguvencli/http-proxy-list)

It is a lightweight project that hourly scrapes lots of free-proxy sites, validates if it works, and serves a clean proxy list.


> Scraper found **3519** proxies at the latest update. Usable proxies are below.

## Usage

Click the file format that you want and copy the URL.


|File|Content|Count|
|----|-------|-----|
|[data.txt](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.txt)|`ip_address:port` combined (seperated new line)|102|
|[data.json](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.json)|`ip, port`|102|
|[data-with-geolocation.json](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data-with-geolocation.json)|`ip, port, geolocation`|102|

## Sources

|Source|Found Proxies|Succeed|
|------|-------------|-------|
|[free-proxy-list.net](https://free-proxy-list.net)|300|✅|
|[us-proxy.org](https://www.us-proxy.org)|200|✅|
|[proxydb.net](http://proxydb.net)|15|✅|
|[free-proxy-list.com](https://free-proxy-list.com/?page=&port=&type%5B%5D=http&type%5B%5D=https&up_time=0&search=Search)|0|🚫|
|[proxy-list.download](https://www.proxy-list.download/HTTP)|26|✅|
|[vpnoverview.com](https://vpnoverview.com/privacy/anonymous-browsing/free-proxy-servers)|32|✅|
|[proxyscan.io](https://www.proxyscan.io)|0|🚫|
|[proxylist.geonode.com](https://proxylist.geonode.com/api/proxy-list?limit=300&page=1&sort_by=lastChecked&sort_type=desc&protocols=http,https)|229|✅|
|[proxyscrape.com](https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all)|268|✅|
|[github.com/clarketm/proxy-list](https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt)|400|✅|
|[github.com/monosans/proxy-list](https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt)|155|✅|
|[github.com/TheSpeedX/PROXY-List](https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt)|1894|✅|


## Sample Proxies With Geolocation Info

|#|Ip|Port|Country|City|Internet Service Provider|
|-|--|----|-------|----|-------------------------|
|1|3.128.120.252|80|United States|Dublin|Amazon.com, Inc.|
|2|136.243.37.84|9090|Germany|Falkenstein|Hetzner Online GmbH|
|3|45.230.47.17|999|Venezuela|Valencia|Gandalf Comunicaciones C.A.|
|4|118.99.124.161|8080|Indonesia|Mampang Prapatan|BIZNET|
|5|41.60.239.201|8080|Kenya|Nairobi|Maintainer Liquid Telecommunications Operations Limited|
|6|45.189.113.15|999|Ecuador|Milagro|Anibal Humberto Enriquez Moncayo(Comunicate)|
|7|20.47.108.204|8888|United States|Boydton|Microsoft Corporation|
|8|157.245.222.183|80|United States|Clifton|DigitalOcean, LLC|
|9|201.174.239.18|8080|Mexico|General Escobedo|Transtelco Inc|
|10|190.26.201.194|8080|Colombia|Bogotá|ETB - Colombia|
|11|177.141.99.50|8080|Brazil|São Paulo|Claro S.A.|
|12|212.108.144.67|8080|Cyprus|Kyrenia|Lifecell Digital LTD|
|13|101.128.67.46|8181|Indonesia|Denpasar|CBN|
|14|80.241.215.128|5566|Germany|Nuremberg|Contabo GmbH|
|15|195.39.233.18|8080|Ukraine|Kharkiv|Active Operations LLC|
|16|136.243.37.84|9090|Germany|Falkenstein|Hetzner Online GmbH|
|17|84.204.40.155|8080|Russia|St Petersburg|PJSC MegaFon|
|18|36.37.160.242|8080|Cambodia|Phnom Penh|VIETTEL (CAMBODIA) PTE.|
|19|114.4.104.254|3128|Indonesia|Jakarta|PT. INDOSAT Tbk|
|20|188.133.188.20|8080|Russia|Moscow|JSC "ER-Telecom Holding"|



## Contributing

Contributions are welcome, and they are greatly appreciated! Every
little bit helps, and credit will always be given.

