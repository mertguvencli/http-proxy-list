
# Free HTTP Proxy List 🌍

[![Hourly Update](https://github.com/mertguvencli/http-proxy-list/actions/workflows/main.yml/badge.svg?branch=main)](https://github.com/mertguvencli/http-proxy-list/actions/workflows/main.yml)
![GitHub](https://img.shields.io/github/license/mertguvencli/http-proxy-list)
![GitHub last commit](https://img.shields.io/github/last-commit/mertguvencli/http-proxy-list)

It is a lightweight project that hourly scrapes lots of free-proxy sites, validates if it works, and serves a clean proxy list.


> Scraper found **3628** proxies at the latest update. Usable proxies are below.

## Usage

Click the file format that you want and copy the URL.


|File|Content|Count|
|----|-------|-----|
|[data.txt](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.txt)|`ip_address:port` combined (seperated new line)|159|
|[data.json](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.json)|`ip, port`|159|
|[data-with-geolocation.json](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data-with-geolocation.json)|`ip, port, geolocation`|159|

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
|[proxylist.geonode.com](https://proxylist.geonode.com/api/proxy-list?limit=300&page=1&sort_by=lastChecked&sort_type=desc&protocols=http,https)|152|✅|
|[proxyscrape.com](https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all)|228|✅|
|[github.com/clarketm/proxy-list](https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt)|400|✅|
|[github.com/monosans/proxy-list](https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt)|136|✅|
|[github.com/TheSpeedX/PROXY-List](https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt)|2029|✅|


## Sample Proxies With Geolocation Info

|#|Ip|Port|Country|City|Internet Service Provider|
|-|--|----|-------|----|-------------------------|
|1|20.47.108.204|8888|United States|Boydton|Microsoft Corporation|
|2|167.71.250.200|8118|United States|Clifton|DigitalOcean, LLC|
|3|51.81.16.50|21987|United States|Warrenton|OVH US LLC|
|4|12.231.44.251|3128|United States|Racine|AT&T Services, Inc.|
|5|51.81.16.50|21987|United States|Warrenton|OVH US LLC|
|6|12.231.44.251|3128|United States|Racine|AT&T Services, Inc.|
|7|38.108.119.176|59394|United States|New York|Cogent Communications|
|8|200.110.173.118|8080|Colombia|Santiago de Cali|Media Commerce Partners S.A|
|9|110.78.143.208|80|Thailand|Ban Kha|CAT-BB|
|10|175.111.129.154|8080|India|Jaipur|Spiderlink Networks Pvt Ltd|
|11|154.13.5.41|59394|United States|San Jose|Zhihua Lu trading as HostHub|
|12|154.13.5.41|59394|United States|San Jose|Zhihua Lu trading as HostHub|
|13|13.125.247.113|3128|South Korea|Seoul|Amazon Technologies Inc.|
|14|47.240.160.90|10001|Hong Kong|Central|Alibaba.com LLC|
|15|105.112.191.250|3128|Nigeria|Lagos|Airtel Networks Limited|
|16|111.73.46.94|3128|China|Dunhou|Chinanet|
|17|104.239.136.210|3128|United States|Dallas|Rackspace Hosting|
|18|47.89.185.178|8888|United States|Charlottesville|Alibaba.com LLC|
|19|85.14.243.31|3128|Germany|Meerbusch|myLoc managed IT AG|
|20|59.124.224.205|3128|Taiwan|Bade District|Chunghwa Telecom Co., Ltd.|



## Contributing

Contributions are welcome, and they are greatly appreciated! Every
little bit helps, and credit will always be given.

