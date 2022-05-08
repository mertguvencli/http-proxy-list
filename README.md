
# Free HTTP Proxy List 🌍

[![Hourly Update](https://github.com/mertguvencli/http-proxy-list/actions/workflows/main.yml/badge.svg?branch=main)](https://github.com/mertguvencli/http-proxy-list/actions/workflows/main.yml)
![GitHub](https://img.shields.io/github/license/mertguvencli/http-proxy-list)
![GitHub last commit](https://img.shields.io/github/last-commit/mertguvencli/http-proxy-list)

It is a lightweight project that hourly scrapes lots of free-proxy sites, validates if it works, and serves a clean proxy list.


> Scraper found **3403** proxies at the latest update. Usable proxies are below.

## Usage

Click the file format that you want and copy the URL.


|File|Content|Count|
|----|-------|-----|
|[data.txt](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.txt)|`ip_address:port` combined (seperated new line)|134|
|[data.json](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.json)|`ip, port`|134|
|[data-with-geolocation.json](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data-with-geolocation.json)|`ip, port, geolocation`|134|

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
|[proxylist.geonode.com](https://proxylist.geonode.com/api/proxy-list?limit=300&page=1&sort_by=lastChecked&sort_type=desc&protocols=http,https)|0|🚫|
|[proxyscrape.com](https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all)|279|✅|
|[github.com/clarketm/proxy-list](https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt)|400|✅|
|[github.com/monosans/proxy-list](https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt)|205|✅|
|[github.com/TheSpeedX/PROXY-List](https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt)|1836|✅|


## Sample Proxies With Geolocation Info

|#|Ip|Port|Country|City|Internet Service Provider|
|-|--|----|-------|----|-------------------------|
|1|174.138.116.12|80|United States|Clifton|DigitalOcean, LLC|
|2|179.118.199.171|9812|Brazil|Campinas|Vivo|
|3|45.77.86.30|59394|United States|Los Angeles|The Constant Company|
|4|146.120.174.149|8989|Ukraine|Ivanykivka|Gargat Igor Vasilevich|
|5|189.157.126.4|999|Mexico|Ciudad Valles|Uninet S.A. de C.V|
|6|189.112.10.242|3128|Brazil|São Paulo|ALGAR TELECOM S/A|
|7|103.180.119.62|8080|Indonesia|Gedangan|PT Persada Data Multimedia|
|8|200.155.142.98|8080|Brazil|São Paulo|Telium TelecomunicaÔÔes Ltda|
|9|149.248.5.225|59394|United States|Los Angeles|The Constant Company|
|10|91.81.127.186|9812|Italy|Palermo|VODAFONE|
|11|194.233.73.106|443|Singapore|Singapore|Contabo Asia Private Limited|
|12|40.70.172.110|80|United States|Boydton|Microsoft Corporation|
|13|190.26.201.194|8080|Colombia|Bogotá|ETB - Colombia|
|14|190.26.201.194|8080|Colombia|Bogotá|ETB - Colombia|
|15|31.161.38.233|8090|Netherlands|Wateringen|KPN B.V|
|16|46.182.87.226|8080|Ukraine|Kyiv|Gigatrans' peering network|
|17|103.106.193.117|7532|India|Delhi|Elyzium Consulting|
|18|195.39.233.18|8080|Ukraine|Kharkiv|Active Operations LLC|
|19|103.156.249.31|1080|Indonesia|Malang|Trans Media Telekomunikasi|
|20|1.179.148.9|55636|Thailand|Sankhaburi|TOT Public Company Limited|



## Contributing

Contributions are welcome, and they are greatly appreciated! Every
little bit helps, and credit will always be given.

