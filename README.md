
# Free HTTP Proxy List 🌍

[![Hourly Update](https://github.com/mertguvencli/http-proxy-list/actions/workflows/main.yml/badge.svg?branch=main)](https://github.com/mertguvencli/http-proxy-list/actions/workflows/main.yml)
![GitHub](https://img.shields.io/github/license/mertguvencli/http-proxy-list)
![GitHub last commit](https://img.shields.io/github/last-commit/mertguvencli/http-proxy-list)

It is a lightweight project that hourly scrapes lots of free-proxy sites, validates if it works, and serves a clean proxy list.


> Scraper found **4469** proxies at the latest update. Usable proxies are below.

## Usage

Click the file format that you want and copy the URL.


|File|Content|Count|
|----|-------|-----|
|[data.txt](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.txt)|`ip_address:port` combined (seperated new line)|429|
|[data.json](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.json)|`ip, port`|429|
|[data-with-geolocation.json](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data-with-geolocation.json)|`ip, port, geolocation`|429|

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
|[proxylist.geonode.com](https://proxylist.geonode.com/api/proxy-list?limit=300&page=1&sort_by=lastChecked&sort_type=desc&protocols=http,https)|300|✅|
|[proxyscrape.com](https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all)|609|✅|
|[github.com/clarketm/proxy-list](https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt)|400|✅|
|[github.com/monosans/proxy-list](https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt)|282|✅|
|[github.com/TheSpeedX/PROXY-List](https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt)|2195|✅|


## Sample Proxies With Geolocation Info

|#|Ip|Port|Country|City|Internet Service Provider|
|-|--|----|-------|----|-------------------------|
|1|20.47.108.204|8888|United States|Boydton|Microsoft Corporation|
|2|34.200.251.21|3128|United States|Ashburn|Amazon.com, Inc.|
|3|66.196.238.181|3128|United States|Houston|Logix|
|4|167.114.185.69|3128|Canada|Montreal|OVH SAS|
|5|35.240.63.166|3128|Belgium|Brussels|Google LLC|
|6|20.47.108.204|8888|United States|Boydton|Microsoft Corporation|
|7|34.200.251.21|3128|United States|Ashburn|Amazon.com, Inc.|
|8|181.225.54.38|999|Venezuela|Caracas|IFX Networks Venezuela C.A.|
|9|18.130.180.120|3128|United Kingdom|London|Amazon Technologies Inc.|
|10|207.180.199.65|3128|Germany|Nuremberg|Contabo GmbH|
|11|179.96.28.58|80|Brazil|Alexania|G8 NETWORKS LTDA|
|12|18.179.15.55|3128|Japan|Tokyo|Amazon Technologies Inc.|
|13|157.100.12.138|999|Ecuador|Quito|Telconet S.A|
|14|207.180.204.105|3128|Germany|Nuremberg|Contabo GmbH|
|15|207.180.217.107|3128|Germany|Nuremberg|Contabo GmbH|
|16|177.141.99.50|8080|Brazil|São Paulo|Claro S.A.|
|17|47.240.160.90|10001|Hong Kong|Central|Alibaba.com LLC|
|18|107.172.73.179|7890|United States|Buffalo|ColoCrossing|
|19|176.102.66.197|8888|Czechia|Letohrad|SecurityNet.cz s.r.o.|
|20|115.96.208.124|8080|India|Mumbai|Hathway IP over Cable Internet Access|



## Contributing

Contributions are welcome, and they are greatly appreciated! Every
little bit helps, and credit will always be given.

