
# Free HTTP Proxy List 🌍

[![Hourly Update](https://github.com/mertguvencli/http-proxy-list/actions/workflows/main.yml/badge.svg?branch=main)](https://github.com/mertguvencli/http-proxy-list/actions/workflows/main.yml)
![GitHub](https://img.shields.io/github/license/mertguvencli/http-proxy-list)
![GitHub last commit](https://img.shields.io/github/last-commit/mertguvencli/http-proxy-list)

It is a lightweight project that hourly scrapes lots of free-proxy sites, validates if it works, and serves a clean proxy list.


> Scraper found **3678** proxies at the latest update. Usable proxies are below.

## Usage

Click the file format that you want and copy the URL.


|File|Content|Count|
|----|-------|-----|
|[data.txt](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.txt)|`ip_address:port` combined (seperated new line)|210|
|[data.json](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.json)|`ip, port`|210|
|[data-with-geolocation.json](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data-with-geolocation.json)|`ip, port, geolocation`|210|

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
|[proxyscrape.com](https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all)|338|✅|
|[github.com/clarketm/proxy-list](https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt)|400|✅|
|[github.com/monosans/proxy-list](https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt)|146|✅|
|[github.com/TheSpeedX/PROXY-List](https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt)|1911|✅|


## Sample Proxies With Geolocation Info

|#|Ip|Port|Country|City|Internet Service Provider|
|-|--|----|-------|----|-------------------------|
|1|52.45.107.168|80|United States|Ashburn|Amazon.com, Inc.|
|2|65.108.136.229|9090|Finland|Helsinki|Hetzner Online GmbH|
|3|52.45.107.168|80|United States|Ashburn|Amazon.com, Inc.|
|4|144.217.75.65|8800|Canada|Beauharnois|OVH SAS|
|5|189.164.89.55|3128|Mexico|Amozoc de Mota|Uninet S.A. de C.V|
|6|176.57.188.32|443|Germany|Düsseldorf|Contabo GmbH|
|7|190.85.34.140|999|Colombia|Barranquilla|Telmex Colombia S.A.|
|8|180.180.23.49|8080|Thailand|U Thong|TOT Public Company Limited|
|9|68.183.235.131|8080|Singapore|Singapore|DigitalOcean, LLC|
|10|47.241.165.133|443|Singapore|Singapore|Alibaba.com LLC|
|11|194.233.73.106|443|Singapore|Singapore|Contabo Asia Private Limited|
|12|66.196.238.180|3128|United States|Tomball|Logix|
|13|201.174.239.18|8080|Mexico|Ciudad Juárez|Transtelco Inc|
|14|190.26.201.194|8080|Colombia|Bogotá|ETB - Colombia|
|15|45.167.125.209|9992|Colombia|Popayán|Sepcom Comunicaciones SAS|
|16|66.196.238.180|3128|United States|Tomball|Logix|
|17|91.150.189.122|30389|Poland|Rzeszów|Skyware Sp. z o.o.|
|18|18.218.45.35|3128|United States|Dublin|Amazon.com, Inc.|
|19|168.194.90.50|999|Mexico|Tijuana|Konecta de Mexico, S. de R.L. de C.V.|
|20|45.190.84.2|999|Venezuela|Caracas|TELECOM.CORPORATIVAS TELECORP, C.A|



## Contributing

Contributions are welcome, and they are greatly appreciated! Every
little bit helps, and credit will always be given.

