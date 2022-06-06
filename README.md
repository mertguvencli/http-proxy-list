
# Free HTTP Proxy List 🌍

[![Hourly Update](https://github.com/mertguvencli/http-proxy-list/actions/workflows/main.yml/badge.svg?branch=main)](https://github.com/mertguvencli/http-proxy-list/actions/workflows/main.yml)
![GitHub](https://img.shields.io/github/license/mertguvencli/http-proxy-list)
![GitHub last commit](https://img.shields.io/github/last-commit/mertguvencli/http-proxy-list)

It is a lightweight project that hourly scrapes lots of free-proxy sites, validates if it works, and serves a clean proxy list.


> Scraper found **3347** proxies at the latest update. Usable proxies are below.

## Usage

Click the file format that you want and copy the URL.


|File|Content|Count|
|----|-------|-----|
|[data.txt](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.txt)|`ip_address:port` combined (seperated new line)|155|
|[data.json](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.json)|`ip, port`|155|
|[data-with-geolocation.json](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data-with-geolocation.json)|`ip, port, geolocation`|155|

## Sources

|Source|Found Proxies|Succeed|
|------|-------------|-------|
|[free-proxy-list.net](https://free-proxy-list.net)|300|✅|
|[us-proxy.org](https://www.us-proxy.org)|200|✅|
|[proxydb.net](http://proxydb.net)|15|✅|
|[free-proxy-list.com](https://free-proxy-list.com/?page=&port=&type%5B%5D=http&type%5B%5D=https&up_time=0&search=Search)|10|✅|
|[proxy-list.download](https://www.proxy-list.download/HTTP)|26|✅|
|[vpnoverview.com](https://vpnoverview.com/privacy/anonymous-browsing/free-proxy-servers)|32|✅|
|[proxyscan.io](https://www.proxyscan.io)|71|✅|
|[proxylist.geonode.com](https://proxylist.geonode.com/api/proxy-list?limit=300&page=1&sort_by=lastChecked&sort_type=desc&protocols=http,https)|0|🚫|
|[proxyscrape.com](https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all)|316|✅|
|[github.com/clarketm/proxy-list](https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt)|400|✅|
|[github.com/monosans/proxy-list](https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt)|123|✅|
|[github.com/TheSpeedX/PROXY-List](https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt)|1854|✅|


## Sample Proxies With Geolocation Info

|#|Ip|Port|Country|City|Internet Service Provider|
|-|--|----|-------|----|-------------------------|
|1|20.47.108.204|8888|United States|Boydton|Microsoft Corporation|
|2|45.167.125.209|9992|Colombia|Popayán|Sepcom Comunicaciones SAS|
|3|190.97.226.236|999|Venezuela|Barinas|NetLink América C.A.|
|4|157.100.12.138|999|Ecuador|Quito|Telconet S.A|
|5|18.196.224.91|39593|Germany|Frankfurt am Main|Amazon Technologies Inc.|
|6|46.188.53.7|8008|Russia|Moscow|2COM|
|7|114.4.104.254|3128|Indonesia|Jakarta|PT. INDOSAT Tbk|
|8|192.241.205.151|3129|United States|San Francisco|DigitalOcean, LLC|
|9|191.241.184.61|40033|Brazil|Nossa Senhora da Gloria|NetGloria Telecom|
|10|158.140.181.148|8081|Indonesia|Bogor|MYREPUBLIC|
|11|203.150.113.10|8080|Thailand|Bangkok|Internet Thailand Company Ltd.|
|12|187.1.57.206|20183|Brazil|Belo Horizonte|Companhia Itabirana TelecomunicaÔÔes Ltda|
|13|36.76.85.238|8080|Indonesia|Medan|PT. TELKOM INDONESIA|
|14|194.233.69.90|443|Singapore|Singapore|Contabo Asia Private Limited|
|15|201.158.47.66|8080|Brazil|Sorocaba|AS|
|16|201.174.239.18|8080|Mexico|Ciudad Juárez|Transtelco Inc|
|17|45.167.125.209|9992|Colombia|Popayán|Sepcom Comunicaciones SAS|
|18|179.43.101.150|999|Argentina|Belen de Escobar|Advantun SRL|
|19|121.156.109.108|8080|South Korea|Seongnam-si|Korea Telecom|
|20|176.36.20.67|61935|Ukraine|Kyiv|Lanet Network|



## Contributing

Contributions are welcome, and they are greatly appreciated! Every
little bit helps, and credit will always be given.

