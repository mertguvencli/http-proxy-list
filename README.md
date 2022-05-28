
# Free HTTP Proxy List 🌍

[![Hourly Update](https://github.com/mertguvencli/http-proxy-list/actions/workflows/main.yml/badge.svg?branch=main)](https://github.com/mertguvencli/http-proxy-list/actions/workflows/main.yml)
![GitHub](https://img.shields.io/github/license/mertguvencli/http-proxy-list)
![GitHub last commit](https://img.shields.io/github/last-commit/mertguvencli/http-proxy-list)

It is a lightweight project that hourly scrapes lots of free-proxy sites, validates if it works, and serves a clean proxy list.


> Scraper found **3280** proxies at the latest update. Usable proxies are below.

## Usage

Click the file format that you want and copy the URL.


|File|Content|Count|
|----|-------|-----|
|[data.txt](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.txt)|`ip_address:port` combined (seperated new line)|85|
|[data.json](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.json)|`ip, port`|85|
|[data-with-geolocation.json](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data-with-geolocation.json)|`ip, port, geolocation`|85|

## Sources

|Source|Found Proxies|Succeed|
|------|-------------|-------|
|[free-proxy-list.net](https://free-proxy-list.net)|300|✅|
|[us-proxy.org](https://www.us-proxy.org)|200|✅|
|[proxydb.net](http://proxydb.net)|15|✅|
|[free-proxy-list.com](https://free-proxy-list.com/?page=&port=&type%5B%5D=http&type%5B%5D=https&up_time=0&search=Search)|0|🚫|
|[proxy-list.download](https://www.proxy-list.download/HTTP)|26|✅|
|[vpnoverview.com](https://vpnoverview.com/privacy/anonymous-browsing/free-proxy-servers)|32|✅|
|[proxyscan.io](https://www.proxyscan.io)|47|✅|
|[proxylist.geonode.com](https://proxylist.geonode.com/api/proxy-list?limit=300&page=1&sort_by=lastChecked&sort_type=desc&protocols=http,https)|0|🚫|
|[proxyscrape.com](https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all)|359|✅|
|[github.com/clarketm/proxy-list](https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt)|400|✅|
|[github.com/monosans/proxy-list](https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt)|55|✅|
|[github.com/TheSpeedX/PROXY-List](https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt)|1846|✅|


## Sample Proxies With Geolocation Info

|#|Ip|Port|Country|City|Internet Service Provider|
|-|--|----|-------|----|-------------------------|
|1|45.167.125.209|9992|Colombia|Popayán|Sepcom Comunicaciones SAS|
|2|45.190.84.2|999|Venezuela|Caracas|TELECOM.CORPORATIVAS TELECORP, C.A|
|3|190.97.226.236|999|Venezuela|Barinas|NetLink América C.A.|
|4|157.100.12.138|999|Ecuador|Quito|Telconet S.A|
|5|181.129.14.166|999|Colombia|Medellín|EPM Telecomunicaciones S.A. E.S.P.|
|6|177.66.100.101|10009|Brazil|Tres Ranchos|WN TELECOM LTDA - ME|
|7|125.162.73.115|8080|Indonesia|Suka Ramai|PT. TELKOM INDONESIA|
|8|190.71.80.91|8080|Colombia|Santiago de Cali|EPM Telecomunicaciones S.A. E.S.P|
|9|200.106.184.13|999|Argentina|Canning|Fullnet Solutions S.A.S.|
|10|178.184.12.60|8080|Russia|Irkutsk|OJSC "Sibirtelecom"|
|11|116.48.124.172|8888|Hong Kong|Shatin|Hong Kong Telecommunications (HKT) Limited Mass Internet|
|12|159.192.253.63|8080|Thailand|Bangkok|CAT-BB|
|13|45.190.84.2|999|Venezuela|Caracas|TELECOM.CORPORATIVAS TELECORP, C.A|
|14|94.253.71.79|53281|Russia|Elektrogorsk|Flex ISP|
|15|201.140.208.146|3128|Brazil|Janauba|Norte Line Telecomunicacoes Ltda.|
|16|187.44.167.78|60786|Brazil|Salvador|ITS TELECOMUNICACOES LTDA|
|17|162.150.62.96|443|United States|Kincaid|Comcast Cable Communications, LLC|
|18|162.150.62.95|443|United States|Kincaid|Comcast Cable Communications, LLC|
|19|200.125.171.57|999|Dominican Republic|Santiago de los Caballeros|WIRELESS MULTI SERVICE VARGAS CABRERA, S. R. L|
|20|20.47.108.204|8888|United States|Boydton|Microsoft Corporation|



## Contributing

Contributions are welcome, and they are greatly appreciated! Every
little bit helps, and credit will always be given.

