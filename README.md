
# Free HTTP Proxy List 🌍

[![Hourly Update](https://github.com/mertguvencli/http-proxy-list/actions/workflows/main.yml/badge.svg?branch=main)](https://github.com/mertguvencli/http-proxy-list/actions/workflows/main.yml)
![GitHub](https://img.shields.io/github/license/mertguvencli/http-proxy-list)
![GitHub last commit](https://img.shields.io/github/last-commit/mertguvencli/http-proxy-list)

It is a lightweight project that hourly scrapes lots of free-proxy sites, validates if it works, and serves a clean proxy list.


> Scraper found **3722** proxies at the latest update. Usable proxies are below.

## Usage

Click the file format that you want and copy the URL.


|File|Content|Count|
|----|-------|-----|
|[data.txt](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.txt)|`ip_address:port` combined (seperated new line)|207|
|[data.json](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.json)|`ip, port`|207|
|[data-with-geolocation.json](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data-with-geolocation.json)|`ip, port, geolocation`|207|

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
|[proxyscrape.com](https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all)|361|✅|
|[github.com/clarketm/proxy-list](https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt)|400|✅|
|[github.com/monosans/proxy-list](https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt)|151|✅|
|[github.com/TheSpeedX/PROXY-List](https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt)|1927|✅|


## Sample Proxies With Geolocation Info

|#|Ip|Port|Country|City|Internet Service Provider|
|-|--|----|-------|----|-------------------------|
|1|20.47.108.204|8888|United States|Boydton|Microsoft Corporation|
|2|43.130.47.100|8081|United States|Santa Clara|Shenzhen Tencent Computer Systems Company Limited|
|3|173.82.188.82|9090|United States|Santa Clarita|Multacom Corporation|
|4|154.49.216.33|3128|France|Vélizy-Villacoublay|Cogent Communications|
|5|20.47.108.204|8888|United States|Boydton|Microsoft Corporation|
|6|43.130.47.100|8081|United States|Santa Clara|Shenzhen Tencent Computer Systems Company Limited|
|7|154.49.216.33|3128|France|Vélizy-Villacoublay|Cogent Communications|
|8|138.197.146.58|31028|Canada|Toronto|DigitalOcean, LLC|
|9|173.82.188.82|9090|United States|Santa Clarita|Multacom Corporation|
|10|187.95.112.36|6666|Brazil|Campo Largo|COPEL Telecomunicações S.A|
|11|103.145.142.54|9812|Indonesia|Tamiajeng|PT. Indonesia Comnets Plus|
|12|102.68.128.214|8080|Libya|Tripoli|Aljeel Aljadeed For Technology|
|13|103.151.140.165|8080|Indonesia|Jakarta|PT Indotechno Digital Komputasi|
|14|148.255.91.237|8080|Dominican Republic|Santiago de los Caballeros|Compañía Dominicana de Teléfonos S. A.|
|15|3.128.120.252|80|United States|Dublin|Amazon.com, Inc.|
|16|179.93.65.233|8080|Brazil|São Paulo|Vivo|
|17|203.189.142.168|53281|Cambodia|Phnom Penh|ONLINE|
|18|190.26.201.194|8080|Colombia|Bogotá|ETB - Colombia|
|19|157.100.12.138|999|Ecuador|Quito|Telconet S.A|
|20|103.122.253.98|9812|Bangladesh|Gazipur|Falcon Link|



## Contributing

Contributions are welcome, and they are greatly appreciated! Every
little bit helps, and credit will always be given.

