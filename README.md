
# Free HTTP Proxy List 🌍

[![Hourly Update](https://github.com/mertguvencli/http-proxy-list/actions/workflows/main.yml/badge.svg?branch=main)](https://github.com/mertguvencli/http-proxy-list/actions/workflows/main.yml)
![GitHub](https://img.shields.io/github/license/mertguvencli/http-proxy-list)
![GitHub last commit](https://img.shields.io/github/last-commit/mertguvencli/http-proxy-list)

It is a lightweight project that hourly scrapes lots of free-proxy sites, validates if it works, and serves a clean proxy list.


> Scraper found **3650** proxies at the latest update. Usable proxies are below.

## Usage

Click the file format that you want and copy the URL.


|File|Content|Count|
|----|-------|-----|
|[data.txt](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.txt)|`ip_address:port` combined (seperated new line)|131|
|[data.json](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.json)|`ip, port`|131|
|[data-with-geolocation.json](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data-with-geolocation.json)|`ip, port, geolocation`|131|

## Sources

|Source|Found Proxies|Succeed|
|------|-------------|-------|
|[free-proxy-list.net](https://free-proxy-list.net)|300|✅|
|[us-proxy.org](https://www.us-proxy.org)|200|✅|
|[proxydb.net](http://proxydb.net)|15|✅|
|[free-proxy-list.com](https://free-proxy-list.com/?page=&port=&type%5B%5D=http&type%5B%5D=https&up_time=0&search=Search)|10|✅|
|[proxy-list.download](https://www.proxy-list.download/HTTP)|26|✅|
|[vpnoverview.com](https://vpnoverview.com/privacy/anonymous-browsing/free-proxy-servers)|32|✅|
|[proxyscan.io](https://www.proxyscan.io)|82|✅|
|[proxylist.geonode.com](https://proxylist.geonode.com/api/proxy-list?limit=300&page=1&sort_by=lastChecked&sort_type=desc&protocols=http,https)|285|✅|
|[proxyscrape.com](https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all)|339|✅|
|[github.com/clarketm/proxy-list](https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt)|400|✅|
|[github.com/monosans/proxy-list](https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt)|119|✅|
|[github.com/TheSpeedX/PROXY-List](https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt)|1842|✅|


## Sample Proxies With Geolocation Info

|#|Ip|Port|Country|City|Internet Service Provider|
|-|--|----|-------|----|-------------------------|
|1|64.225.8.192|80|United States|Clifton|DigitalOcean, LLC|
|2|201.174.239.18|8080|Mexico|General Escobedo|Transtelco Inc|
|3|110.78.138.59|8080|Thailand|Samphanthawong|CAT-BB|
|4|12.31.246.5|8080|United States|Saint Helena|AT&T Services, Inc.|
|5|110.170.126.13|3128|Thailand|Din Daeng|True Internet Corporation CO. Ltd.|
|6|50.250.56.129|46456|United States|Lawrence|Comcast Cable Communications, LLC|
|7|66.94.120.161|443|United States|Seattle|Contabo Inc.|
|8|103.47.175.161|83|India|Ghaziabad|Precious netcom pvt ltd|
|9|47.89.185.178|8888|United States|Charlottesville|Alibaba.com LLC|
|10|47.241.165.133|443|Singapore|Singapore|Alibaba.com LLC|
|11|47.89.185.178|8888|United States|Charlottesville|Alibaba.com LLC|
|12|95.217.72.253|3128|Finland|Helsinki|Hetzner Online GmbH|
|13|103.19.130.50|8080|Bangladesh|Dhaka|InfoLink|
|14|50.250.56.129|46456|United States|Lawrence|Comcast Cable Communications, LLC|
|15|103.73.102.174|60080|Pakistan|Lahore|KK Networks (Pvt) Ltd|
|16|122.155.165.191|3128|Thailand|Ratchathewi|CAT Telecom Public Company Limited|
|17|94.23.241.200|3128|France|Roubaix|OVH SAS|
|18|123.163.55.123|3128|China|Zhoukou|Chinanet|
|19|36.67.52.35|8080|Indonesia|Carenang|PT. Telekomunikasi Indonesia|
|20|157.100.12.138|999|Ecuador|Quito|Telconet S.A|



## Contributing

Contributions are welcome, and they are greatly appreciated! Every
little bit helps, and credit will always be given.

