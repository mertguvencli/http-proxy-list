
# Free HTTP Proxy List 🌍

[![Hourly Update](https://github.com/mertguvencli/http-proxy-list/actions/workflows/main.yml/badge.svg?branch=main)](https://github.com/mertguvencli/http-proxy-list/actions/workflows/main.yml)
![GitHub](https://img.shields.io/github/license/mertguvencli/http-proxy-list)
![GitHub last commit](https://img.shields.io/github/last-commit/mertguvencli/http-proxy-list)

It is a lightweight project that hourly scrapes lots of free-proxy sites, validates if it works, and serves a clean proxy list.


> Scraper found **4182** proxies at the latest update. Usable proxies are below.

## Usage

Click the file format that you want and copy the URL.


|File|Content|Count|
|----|-------|-----|
|[data.txt](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.txt)|`ip_address:port` combined (seperated new line)|255|
|[data.json](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.json)|`ip, port`|255|
|[data-with-geolocation.json](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data-with-geolocation.json)|`ip, port, geolocation`|255|

## Sources

|Source|Found Proxies|Succeed|
|------|-------------|-------|
|[free-proxy-list.net](https://free-proxy-list.net)|300|✅|
|[us-proxy.org](https://www.us-proxy.org)|200|✅|
|[proxydb.net](http://proxydb.net)|15|✅|
|[free-proxy-list.com](https://free-proxy-list.com/?page=&port=&type%5B%5D=http&type%5B%5D=https&up_time=0&search=Search)|0|🚫|
|[proxy-list.download](https://www.proxy-list.download/HTTP)|26|✅|
|[vpnoverview.com](https://vpnoverview.com/privacy/anonymous-browsing/free-proxy-servers)|32|✅|
|[proxyscan.io](https://www.proxyscan.io)|100|✅|
|[proxylist.geonode.com](https://proxylist.geonode.com/api/proxy-list?limit=300&page=1&sort_by=lastChecked&sort_type=desc&protocols=http,https)|300|✅|
|[proxyscrape.com](https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all)|383|✅|
|[github.com/clarketm/proxy-list](https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt)|400|✅|
|[github.com/monosans/proxy-list](https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt)|369|✅|
|[github.com/TheSpeedX/PROXY-List](https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt)|2057|✅|


## Sample Proxies With Geolocation Info

|#|Ip|Port|Country|City|Internet Service Provider|
|-|--|----|-------|----|-------------------------|
|1|20.47.108.204|8888|United States|Boydton|Microsoft Corporation|
|2|86.57.157.233|3128|Belarus|Minsk|Republican Unitary Telecommunication Enterprise Beltelecom|
|3|186.67.230.45|3128|Chile|Santiago|Entel Chile S.A.|
|4|66.42.125.237|59394|United States|Elk Grove Village|The Constant Company|
|5|80.69.77.115|8007|Netherlands|Amsterdam|TransIP B.V. Amsterdam network|
|6|201.182.85.242|999|Ecuador|Nueva Loja|Expertservi S.A.|
|7|81.23.151.27|8080|Russia|Kazan’|Rostelecom networks|
|8|186.118.170.44|999|Colombia|Bogotá|Colombia Telecomunicaciones S.a. ESP|
|9|31.129.228.147|8081|Ukraine|Nogaisk|Unetco Ltd.|
|10|180.191.22.200|8080|Philippines|San Jose del Monte|Globe Telecom|
|11|103.143.196.50|8080|Indonesia|Karanganyar Wetankali|JERNIHNETWORK|
|12|200.125.223.142|9812|Ecuador|Guayaquil|Corporacion Nacional De Telecomunicaciones - CNT EP|
|13|181.224.207.21|999|Dominican Republic|Santiago de los Caballeros|BW TELECOM|
|14|187.45.106.164|3128|Brazil|Maravilha|Mhnet Telecom|
|15|194.233.69.90|443|Singapore|Singapore|Contabo Asia Private Limited|
|16|121.156.109.108|8080|South Korea|Seongnam-si|Korea Telecom|
|17|103.138.14.122|8080|Indonesia|Binjai|Adidaya Infocom Lestari|
|18|180.210.184.226|8080|Bangladesh|Dhaka|Premium Connectivity Limited|
|19|190.61.84.166|9812|Costa Rica|San José|Ufinet Costa Rica|
|20|36.93.2.50|8080|Indonesia|Jakarta|Telekomunikasi Indonesia|



## Contributing

Contributions are welcome, and they are greatly appreciated! Every
little bit helps, and credit will always be given.

