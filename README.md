
# Free HTTP Proxy List 🌍

[![Hourly Update](https://github.com/mertguvencli/http-proxy-list/actions/workflows/main.yml/badge.svg?branch=main)](https://github.com/mertguvencli/http-proxy-list/actions/workflows/main.yml)
![GitHub](https://img.shields.io/github/license/mertguvencli/http-proxy-list)
![GitHub last commit](https://img.shields.io/github/last-commit/mertguvencli/http-proxy-list)

It is a lightweight project that hourly scrapes lots of free-proxy sites, validates if it works, and serves a clean proxy list.


> Scraper found **3434** proxies at the latest update. Usable proxies are below.

## Usage

Click the file format that you want and copy the URL.


|File|Content|Count|
|----|-------|-----|
|[data.txt](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.txt)|`ip_address:port` combined (seperated new line)|101|
|[data.json](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.json)|`ip, port`|101|
|[data-with-geolocation.json](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data-with-geolocation.json)|`ip, port, geolocation`|101|

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
|[proxyscrape.com](https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all)|253|✅|
|[github.com/clarketm/proxy-list](https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt)|400|✅|
|[github.com/monosans/proxy-list](https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt)|53|✅|
|[github.com/TheSpeedX/PROXY-List](https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt)|1845|✅|


## Sample Proxies With Geolocation Info

|#|Ip|Port|Country|City|Internet Service Provider|
|-|--|----|-------|----|-------------------------|
|1|66.196.238.179|3128|United States|Tomball|Logix|
|2|157.100.12.138|999|Ecuador|Quito|Telconet S.A|
|3|190.97.226.236|999|Venezuela|Barinas|NetLink América C.A.|
|4|176.9.162.107|443|Germany|Falkenstein|Hetzner Online GmbH|
|5|182.160.108.188|8090|Bangladesh|Dhaka|Aamra Networks Limited|
|6|200.105.215.18|33630|Bolivia|La Paz|AXS Bolivia S. A.|
|7|20.47.108.204|8888|United States|Boydton|Microsoft Corporation|
|8|177.37.16.104|8080|Brazil|Sao Sebastiao|R3 TELECOM|
|9|133.242.237.138|3128|Japan|Chiyoda|SAKURA Internet Inc.|
|10|190.217.101.79|999|Colombia|San Vicente del Caguan|Level 3 Colombia S.A|
|11|124.158.152.138|8081|Indonesia|Jakarta|PT iForte Global Internet|
|12|201.174.239.18|8080|Mexico|General Escobedo|Transtelco Inc|
|13|190.26.201.194|8080|Colombia|Bogotá|ETB - Colombia|
|14|103.70.79.2|8080|Indonesia|Jombor|Diskominfo Kabupaten Sukoharjo|
|15|157.100.12.138|999|Ecuador|Quito|Telconet S.A|
|16|176.9.162.107|443|Germany|Falkenstein|Hetzner Online GmbH|
|17|159.65.133.175|31280|Singapore|Singapore|DigitalOcean, LLC|
|18|94.23.241.200|3128|France|Roubaix|OVH SAS|
|19|103.214.9.13|3128|Vietnam|Hanoi|MEGACORE|
|20|74.82.50.155|3128|Japan|Shinagawa|Hurricane Electric|



## Contributing

Contributions are welcome, and they are greatly appreciated! Every
little bit helps, and credit will always be given.

