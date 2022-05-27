
# Free HTTP Proxy List 🌍

[![Hourly Update](https://github.com/mertguvencli/http-proxy-list/actions/workflows/main.yml/badge.svg?branch=main)](https://github.com/mertguvencli/http-proxy-list/actions/workflows/main.yml)
![GitHub](https://img.shields.io/github/license/mertguvencli/http-proxy-list)
![GitHub last commit](https://img.shields.io/github/last-commit/mertguvencli/http-proxy-list)

It is a lightweight project that hourly scrapes lots of free-proxy sites, validates if it works, and serves a clean proxy list.


> Scraper found **3499** proxies at the latest update. Usable proxies are below.

## Usage

Click the file format that you want and copy the URL.


|File|Content|Count|
|----|-------|-----|
|[data.txt](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.txt)|`ip_address:port` combined (seperated new line)|80|
|[data.json](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.json)|`ip, port`|80|
|[data-with-geolocation.json](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data-with-geolocation.json)|`ip, port, geolocation`|80|

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
|[proxylist.geonode.com](https://proxylist.geonode.com/api/proxy-list?limit=300&page=1&sort_by=lastChecked&sort_type=desc&protocols=http,https)|282|✅|
|[proxyscrape.com](https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all)|208|✅|
|[github.com/clarketm/proxy-list](https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt)|400|✅|
|[github.com/monosans/proxy-list](https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt)|125|✅|
|[github.com/TheSpeedX/PROXY-List](https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt)|1911|✅|


## Sample Proxies With Geolocation Info

|#|Ip|Port|Country|City|Internet Service Provider|
|-|--|----|-------|----|-------------------------|
|1|20.47.108.204|8888|United States|Boydton|Microsoft Corporation|
|2|126.109.104.128|3128|Japan|Fukuoka|Softbank BB Corp.|
|3|95.216.249.203|83|Finland|Helsinki|Hetzner Online GmbH|
|4|118.99.122.124|3128|Indonesia|Bandung|BIZNET|
|5|201.174.239.18|8080|Mexico|Ciudad Juárez|Transtelco Inc|
|6|191.5.163.149|9812|Brazil|Bela Vista do Paraiso|1toc Informatica Ltda|
|7|181.129.14.165|999|Colombia|Medellín|EPM Telecomunicaciones S.A. E.S.P.|
|8|170.245.132.38|999|Paraguay|Caraguatay|MACHADO BAEZ, NERY JAVIER|
|9|41.242.116.235|50000|Mayotte|Mamoudzou|STOI-block1|
|10|181.129.2.90|8081|Colombia|Caldas|EPM Telecomunicaciones S.A. E.S.P.|
|11|103.93.237.81|8080|Indonesia|Cibubur|PT Artha Media Lintas Nusa|
|12|193.34.21.4|55277|Ukraine|Kryvyi Rih|TRK Cable TV LLC|
|13|8.242.212.170|999|Colombia|Bogotá|CTL Colombia|
|14|181.196.241.198|9100|Ecuador|Guayaquil|Corporacion Nacional De Telecomunicaciones - CNT EP|
|15|91.242.213.247|8080|Russia|Murom|NAVIGATOR-MUROM|
|16|181.188.206.42|999|Ecuador|Cuenca|Otecel S.A.|
|17|63.151.67.7|8080|United States|Hayden|Visionary Communications, Inc.|
|18|143.208.59.2|999|Guatemala|Guatemala City|Comunicaciones Metropolitanas Cablecolor|
|19|83.174.218.83|8080|Russia|Ufa|BASHTEL|
|20|185.158.175.6|8080|Iran|Kahrīzak|Ertebatat Sabet Parsian Co. PJS|



## Contributing

Contributions are welcome, and they are greatly appreciated! Every
little bit helps, and credit will always be given.

