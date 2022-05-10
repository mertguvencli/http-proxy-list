
# Free HTTP Proxy List 🌍

[![Hourly Update](https://github.com/mertguvencli/http-proxy-list/actions/workflows/main.yml/badge.svg?branch=main)](https://github.com/mertguvencli/http-proxy-list/actions/workflows/main.yml)
![GitHub](https://img.shields.io/github/license/mertguvencli/http-proxy-list)
![GitHub last commit](https://img.shields.io/github/last-commit/mertguvencli/http-proxy-list)

It is a lightweight project that hourly scrapes lots of free-proxy sites, validates if it works, and serves a clean proxy list.


> Scraper found **3605** proxies at the latest update. Usable proxies are below.

## Usage

Click the file format that you want and copy the URL.


|File|Content|Count|
|----|-------|-----|
|[data.txt](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.txt)|`ip_address:port` combined (seperated new line)|93|
|[data.json](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.json)|`ip, port`|93|
|[data-with-geolocation.json](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data-with-geolocation.json)|`ip, port, geolocation`|93|

## Sources

|Source|Found Proxies|Succeed|
|------|-------------|-------|
|[free-proxy-list.net](https://free-proxy-list.net)|300|✅|
|[us-proxy.org](https://www.us-proxy.org)|200|✅|
|[proxydb.net](http://proxydb.net)|15|✅|
|[free-proxy-list.com](https://free-proxy-list.com/?page=&port=&type%5B%5D=http&type%5B%5D=https&up_time=0&search=Search)|10|✅|
|[proxy-list.download](https://www.proxy-list.download/HTTP)|0|🚫|
|[vpnoverview.com](https://vpnoverview.com/privacy/anonymous-browsing/free-proxy-servers)|32|✅|
|[proxyscan.io](https://www.proxyscan.io)|100|✅|
|[proxylist.geonode.com](https://proxylist.geonode.com/api/proxy-list?limit=300&page=1&sort_by=lastChecked&sort_type=desc&protocols=http,https)|300|✅|
|[proxyscrape.com](https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all)|236|✅|
|[github.com/clarketm/proxy-list](https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt)|400|✅|
|[github.com/monosans/proxy-list](https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt)|193|✅|
|[github.com/TheSpeedX/PROXY-List](https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt)|1819|✅|


## Sample Proxies With Geolocation Info

|#|Ip|Port|Country|City|Internet Service Provider|
|-|--|----|-------|----|-------------------------|
|1|85.214.124.194|5001|Germany|Berlin|Strato AG|
|2|200.105.215.18|33630|Bolivia|La Paz|AXS Bolivia S. A.|
|3|200.125.171.200|9991|Dominican Republic|Santiago de los Caballeros|WIRELESS MULTI SERVICE VARGAS CABRERA, S. R. L|
|4|109.167.134.253|30710|Russia|St Petersburg|JSC "ER-Telecom Holding"|
|5|176.88.168.155|8080|Turkey|Istanbul|Superonline Iletisim Hizmetleri A.S.|
|6|45.250.65.3|9812|India|Faridabad|Abc|
|7|128.199.240.219|3128|Singapore|Singapore|DigitalOcean, LLC|
|8|198.52.241.4|999|Puerto Rico|Corozal|OSNET Wireless|
|9|200.54.194.10|53281|Chile|Providencia|CTC. CORP S.A. (TELEFONICA EMPRESAS)|
|10|50.193.36.173|8080|United States|Lathrop|Comcast Cable Communications|
|11|103.159.90.22|84|India|Karimpur|Pegasuswave Private Limited|
|12|186.67.230.45|3128|Chile|Santiago|Entel Chile S.A.|
|13|212.52.180.43|8080|Hungary|Budaors|INTEGRITY Informatics Ltd.|
|14|200.25.254.193|54240|Colombia|Bogotá|Andinet ON Line|
|15|91.142.172.7|41890|Ukraine|Kyiv|Sitel Ltd|
|16|217.79.181.49|3128|Germany|Düsseldorf|myLoc managed IT AG|
|17|164.68.117.160|3128|Germany|Nuremberg|Contabo GmbH|
|18|195.191.182.108|8080|Russia|St Petersburg|MediaNet Ltd.|
|19|200.26.190.74|999|Dominican Republic|Santiago de los Caballeros|TELERY NETWORKS, S.R.L|
|20|5.53.16.185|18080|Russia|Surgut|Metroset Ltd|



## Contributing

Contributions are welcome, and they are greatly appreciated! Every
little bit helps, and credit will always be given.

