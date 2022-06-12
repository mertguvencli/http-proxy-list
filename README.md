
# Free HTTP Proxy List 🌍

[![Hourly Update](https://github.com/mertguvencli/http-proxy-list/actions/workflows/main.yml/badge.svg?branch=main)](https://github.com/mertguvencli/http-proxy-list/actions/workflows/main.yml)
![GitHub](https://img.shields.io/github/license/mertguvencli/http-proxy-list)
![GitHub last commit](https://img.shields.io/github/last-commit/mertguvencli/http-proxy-list)

It is a lightweight project that hourly scrapes lots of free-proxy sites, validates if it works, and serves a clean proxy list.


> Scraper found **3465** proxies at the latest update. Usable proxies are below.

## Usage

Click the file format that you want and copy the URL.


|File|Content|Count|
|----|-------|-----|
|[data.txt](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.txt)|`ip_address:port` combined (seperated new line)|222|
|[data.json](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.json)|`ip, port`|222|
|[data-with-geolocation.json](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data-with-geolocation.json)|`ip, port, geolocation`|222|

## Sources

|Source|Found Proxies|Succeed|
|------|-------------|-------|
|[free-proxy-list.net](https://free-proxy-list.net)|300|✅|
|[us-proxy.org](https://www.us-proxy.org)|200|✅|
|[proxydb.net](http://proxydb.net)|15|✅|
|[free-proxy-list.com](https://free-proxy-list.com/?page=&port=&type%5B%5D=http&type%5B%5D=https&up_time=0&search=Search)|10|✅|
|[proxy-list.download](https://www.proxy-list.download/HTTP)|26|✅|
|[vpnoverview.com](https://vpnoverview.com/privacy/anonymous-browsing/free-proxy-servers)|32|✅|
|[proxyscan.io](https://www.proxyscan.io)|59|✅|
|[proxylist.geonode.com](https://proxylist.geonode.com/api/proxy-list?limit=300&page=1&sort_by=lastChecked&sort_type=desc&protocols=http,https)|0|🚫|
|[proxyscrape.com](https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all)|436|✅|
|[github.com/clarketm/proxy-list](https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt)|400|✅|
|[github.com/monosans/proxy-list](https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt)|141|✅|
|[github.com/TheSpeedX/PROXY-List](https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt)|1846|✅|


## Sample Proxies With Geolocation Info

|#|Ip|Port|Country|City|Internet Service Provider|
|-|--|----|-------|----|-------------------------|
|1|45.42.177.51|3128|United States|Ashburn|PeaceWeb|
|2|149.19.224.38|3128|United States|Sterling|SPRINT|
|3|159.197.250.134|3128|United States|Mount Prospect|Sprint|
|4|20.47.108.204|8888|United States|Boydton|Microsoft Corporation|
|5|159.197.250.134|3128|United States|Mount Prospect|Sprint|
|6|45.42.177.51|3128|United States|Ashburn|PeaceWeb|
|7|149.19.224.38|3128|United States|Sterling|SPRINT|
|8|157.100.12.138|999|Ecuador|Quito|Telconet S.A|
|9|183.111.25.253|8080|South Korea|Seongnam-si|Korea Telecom|
|10|189.79.62.116|8080|Brazil|São Paulo|Vivo|
|11|191.242.178.96|3128|Brazil|Lauro de Freitas|Conect Telecom|
|12|122.155.165.191|3128|Thailand|Ratchathewi|CAT Telecom Public Company Limited|
|13|152.231.25.194|60080|Colombia|Garzon|TV AZTECA SUCURSAL COLOMBIA|
|14|125.25.32.165|8080|Thailand|Khwaeng Thung Song Hong|TOT Public Company Limited|
|15|194.233.69.41|443|Singapore|Singapore|Contabo Asia Private Limited|
|16|194.233.69.38|443|Singapore|Singapore|Contabo Asia Private Limited|
|17|103.240.161.98|9812|India|Patan|GTPLJAYSANTOSHIMANETWORKPVTLTD|
|18|181.143.235.100|12345|Colombia|Santiago de Cali|EPM Telecomunicaciones S.A. E.S.P.|
|19|110.170.126.13|3128|Thailand|Din Daeng|True Internet Corporation CO. Ltd.|
|20|201.28.102.234|8080|Brazil|Itu|Vivo|



## Contributing

Contributions are welcome, and they are greatly appreciated! Every
little bit helps, and credit will always be given.

