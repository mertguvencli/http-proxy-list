
# Free HTTP Proxy List 🌍

[![Hourly Update](https://github.com/mertguvencli/http-proxy-list/actions/workflows/main.yml/badge.svg?branch=main)](https://github.com/mertguvencli/http-proxy-list/actions/workflows/main.yml)
![GitHub](https://img.shields.io/github/license/mertguvencli/http-proxy-list)
![GitHub last commit](https://img.shields.io/github/last-commit/mertguvencli/http-proxy-list)

It is a lightweight project that hourly scrapes lots of free-proxy sites, validates if it works, and serves a clean proxy list.


> Scraper found **3551** proxies at the latest update. Usable proxies are below.

## Usage

Click the file format that you want and copy the URL.


|File|Content|Count|
|----|-------|-----|
|[data.txt](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.txt)|`ip_address:port` combined (seperated new line)|114|
|[data.json](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.json)|`ip, port`|114|
|[data-with-geolocation.json](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data-with-geolocation.json)|`ip, port, geolocation`|114|

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
|[proxyscrape.com](https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all)|233|✅|
|[github.com/clarketm/proxy-list](https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt)|400|✅|
|[github.com/monosans/proxy-list](https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt)|191|✅|
|[github.com/TheSpeedX/PROXY-List](https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt)|1844|✅|


## Sample Proxies With Geolocation Info

|#|Ip|Port|Country|City|Internet Service Provider|
|-|--|----|-------|----|-------------------------|
|1|20.47.108.204|8888|United States|Boydton|Microsoft Corporation|
|2|20.81.62.32|3128|United States|Boydton|Microsoft Corporation|
|3|8.219.97.248|80|Singapore|Singapore|Alibaba (US) Technology Co., Ltd.|
|4|20.81.62.32|3128|United States|Boydton|Microsoft Corporation|
|5|157.100.12.138|999|Ecuador|Loja|Telconet S.A|
|6|103.151.221.41|3125|Indonesia|Jakarta|PT Parsaoran Global Datatrans|
|7|138.122.147.122|8080|Mexico|Huichapan|Operbes, S.A. de C.V.|
|8|176.99.2.43|1081|Russia|Moscow|"Domain names registrar REG.RU", Ltd|
|9|181.48.91.91|999|Colombia|Bogotá|Telmex Colombia S.A.|
|10|80.91.117.246|8089|Albania|Tirana|Abissnet Datacenter|
|11|103.175.237.9|3127|Indonesia|Malang|PT Marva Global Telekomunikasi|
|12|147.139.138.14|3128|Indonesia|Jakarta|Alibaba.com LLC|
|13|190.214.27.46|8080|Ecuador|Guayaquil|Corporacion Nacional De Telecomunicaciones - CNT EP|
|14|185.15.172.212|3128|Russia|Moscow|SafeData LLC|
|15|20.47.108.204|8888|United States|Boydton|Microsoft Corporation|
|16|20.81.62.32|3128|United States|Boydton|Microsoft Corporation|
|17|89.208.219.121|8080|Netherlands|Amsterdam|My.com B.V.|
|18|103.252.1.137|3128|Vietnam|Hanoi|CMCMIENBAC|
|19|85.14.243.31|3128|Germany|Kamp-Lintfort|myLoc managed IT AG|
|20|152.0.133.177|8080|Dominican Republic|Bayahibe|Compañía Dominicana de Teléfonos S. A.|



## Contributing

Contributions are welcome, and they are greatly appreciated! Every
little bit helps, and credit will always be given.

