
# Free HTTP Proxy List 🌍

[![Hourly Update](https://github.com/mertguvencli/http-proxy-list/actions/workflows/main.yml/badge.svg?branch=main)](https://github.com/mertguvencli/http-proxy-list/actions/workflows/main.yml)
![GitHub](https://img.shields.io/github/license/mertguvencli/http-proxy-list)
![GitHub last commit](https://img.shields.io/github/last-commit/mertguvencli/http-proxy-list)

It is a lightweight project that hourly scrapes lots of free-proxy sites, validates if it works, and serves a clean proxy list.


> Scraper found **3700** proxies at the latest update. Usable proxies are below.

## Usage

Click the file format that you want and copy the URL.


|File|Content|Count|
|----|-------|-----|
|[data.txt](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.txt)|`ip_address:port` combined (seperated new line)|174|
|[data.json](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.json)|`ip, port`|174|
|[data-with-geolocation.json](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data-with-geolocation.json)|`ip, port, geolocation`|174|

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
|[proxylist.geonode.com](https://proxylist.geonode.com/api/proxy-list?limit=300&page=1&sort_by=lastChecked&sort_type=desc&protocols=http,https)|293|✅|
|[proxyscrape.com](https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all)|294|✅|
|[github.com/clarketm/proxy-list](https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt)|400|✅|
|[github.com/monosans/proxy-list](https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt)|145|✅|
|[github.com/TheSpeedX/PROXY-List](https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt)|1985|✅|


## Sample Proxies With Geolocation Info

|#|Ip|Port|Country|City|Internet Service Provider|
|-|--|----|-------|----|-------------------------|
|1|110.170.126.13|3128|Thailand|Din Daeng|True Internet Corporation CO. Ltd.|
|2|20.81.62.32|3128|United States|Boydton|Microsoft Corporation|
|3|52.221.138.117|80|Singapore|Singapore|Amazon.com, Inc.|
|4|45.167.124.5|9992|Colombia|Guapi|Sepcom Comunicaciones SAS|
|5|85.14.243.31|3128|Germany|Meerbusch|myLoc managed IT AG|
|6|45.174.87.18|999|Mexico|Ciudad Juárez|Computadoras y Servicios Especiales SA de CV|
|7|122.70.157.11|808|China|Beijing|China TieTong Telecommunications Corporation|
|8|121.101.133.61|8080|Indonesia|Klaten|TERABIT|
|9|110.170.126.13|3128|Thailand|Din Daeng|True Internet Corporation CO. Ltd.|
|10|76.81.164.246|8080|United States|Garden Grove|Spectrum|
|11|140.227.63.141|3180|Japan|Chiyoda|NTT PC Communications, Inc.|
|12|47.240.160.90|10001|Hong Kong|Central|Alibaba.com LLC|
|13|209.166.175.201|3128|United States|Pittsburgh|CONTINENTAL BROADBAND PENNSYLVANIA, INC.|
|14|46.0.203.186|8080|Russia|Samara|JSC "ER-Telecom Holding"|
|15|45.167.124.5|9992|Colombia|Guapi|Sepcom Comunicaciones SAS|
|16|85.14.243.31|3128|Germany|Meerbusch|myLoc managed IT AG|
|17|38.123.207.247|999|Mexico|Mexico City|Cogent Communications|
|18|209.182.235.252|3128|United States|Los Angeles|HIVELOCITY, Inc.|
|19|144.217.7.157|9300|Canada|Beauharnois|OVH SAS|
|20|157.100.12.138|999|Ecuador|Loja|Telconet S.A|



## Contributing

Contributions are welcome, and they are greatly appreciated! Every
little bit helps, and credit will always be given.

