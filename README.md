
# Free HTTP Proxy List 🌍

[![Hourly Update](https://github.com/mertguvencli/http-proxy-list/actions/workflows/main.yml/badge.svg?branch=main)](https://github.com/mertguvencli/http-proxy-list/actions/workflows/main.yml)
![GitHub](https://img.shields.io/github/license/mertguvencli/http-proxy-list)
![GitHub last commit](https://img.shields.io/github/last-commit/mertguvencli/http-proxy-list)

It is a lightweight project that hourly scrapes lots of free-proxy sites, validates if it works, and serves a clean proxy list.


> Scraper found **3413** proxies at the latest update. Usable proxies are below.

## Usage

Click the file format that you want and copy the URL.


|File|Content|Count|
|----|-------|-----|
|[data.txt](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.txt)|`ip_address:port` combined (seperated new line)|105|
|[data.json](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.json)|`ip, port`|105|
|[data-with-geolocation.json](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data-with-geolocation.json)|`ip, port, geolocation`|105|

## Sources

|Source|Found Proxies|Succeed|
|------|-------------|-------|
|[free-proxy-list.net](https://free-proxy-list.net)|300|✅|
|[us-proxy.org](https://www.us-proxy.org)|200|✅|
|[proxydb.net](http://proxydb.net)|15|✅|
|[free-proxy-list.com](https://free-proxy-list.com/?page=&port=&type%5B%5D=http&type%5B%5D=https&up_time=0&search=Search)|0|🚫|
|[proxy-list.download](https://www.proxy-list.download/HTTP)|26|✅|
|[vpnoverview.com](https://vpnoverview.com/privacy/anonymous-browsing/free-proxy-servers)|32|✅|
|[proxyscan.io](https://www.proxyscan.io)|95|✅|
|[proxylist.geonode.com](https://proxylist.geonode.com/api/proxy-list?limit=300&page=1&sort_by=lastChecked&sort_type=desc&protocols=http,https)|0|🚫|
|[proxyscrape.com](https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all)|332|✅|
|[github.com/clarketm/proxy-list](https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt)|400|✅|
|[github.com/monosans/proxy-list](https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt)|177|✅|
|[github.com/TheSpeedX/PROXY-List](https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt)|1836|✅|


## Sample Proxies With Geolocation Info

|#|Ip|Port|Country|City|Internet Service Provider|
|-|--|----|-------|----|-------------------------|
|1|20.47.108.204|8888|United States|Boydton|Microsoft Corporation|
|2|178.209.51.218|7829|Switzerland|Zurich|Nine Internet Solutions AG|
|3|147.75.68.201|80|United States|Sunnyvale|Packet Host, Inc.|
|4|5.189.184.6|80|Germany|Nuremberg|Contabo GmbH|
|5|162.150.62.96|443|United States|Kincaid|Comcast Cable Communications, LLC|
|6|47.241.165.133|443|Singapore|Singapore|Alibaba.com LLC|
|7|66.94.120.161|443|United States|Seattle|Contabo Inc.|
|8|157.100.12.138|999|Ecuador|Quito|Telconet S.A|
|9|45.190.84.2|999|Venezuela|Caracas|TELECOM.CORPORATIVAS TELECORP, C.A|
|10|162.150.62.96|443|United States|Kincaid|Comcast Cable Communications, LLC|
|11|114.4.209.114|8080|Indonesia|Jakarta|PT. INDOSAT Tbk|
|12|110.80.172.180|16790|China|Fuzhou|Chinanet|
|13|45.167.125.209|9992|Colombia|Popayán|Sepcom Comunicaciones SAS|
|14|66.94.97.238|443|United States|New York|Contabo Inc.|
|15|181.225.68.27|999|Colombia|Villavicencio|Media Commerce Partners S.A|
|16|85.25.91.141|15333|Germany|Cologne|PlusServer GmbH|
|17|190.109.168.217|8080|Colombia|Medellín|Edatel S.a. E.S.P|
|18|103.214.9.13|3128|Vietnam|Hanoi|MEGACORE|
|19|18.218.45.35|3128|United States|Dublin|Amazon.com, Inc.|
|20|201.222.45.64|999|Chile|La Pintana|GRUPO ULLOA SpA|



## Contributing

Contributions are welcome, and they are greatly appreciated! Every
little bit helps, and credit will always be given.

