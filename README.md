
# Free HTTP Proxy List 🌍

[![Hourly Update](https://github.com/mertguvencli/http-proxy-list/actions/workflows/main.yml/badge.svg?branch=main)](https://github.com/mertguvencli/http-proxy-list/actions/workflows/main.yml)
![GitHub](https://img.shields.io/github/license/mertguvencli/http-proxy-list)
![GitHub last commit](https://img.shields.io/github/last-commit/mertguvencli/http-proxy-list)

It is a lightweight project that hourly scrapes lots of free-proxy sites, validates if it works, and serves a clean proxy list.


> Scraper found **4004** proxies at the latest update. Usable proxies are below.

## Usage

Click the file format that you want and copy the URL.


|File|Content|Count|
|----|-------|-----|
|[data.txt](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.txt)|`ip_address:port` combined (seperated new line)|344|
|[data.json](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.json)|`ip, port`|344|
|[data-with-geolocation.json](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data-with-geolocation.json)|`ip, port, geolocation`|344|

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
|[proxyscrape.com](https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all)|453|✅|
|[github.com/clarketm/proxy-list](https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt)|400|✅|
|[github.com/monosans/proxy-list](https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt)|216|✅|
|[github.com/TheSpeedX/PROXY-List](https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt)|2052|✅|


## Sample Proxies With Geolocation Info

|#|Ip|Port|Country|City|Internet Service Provider|
|-|--|----|-------|----|-------------------------|
|1|20.47.108.204|8888|United States|Boydton|Microsoft Corporation|
|2|104.131.109.98|3128|United States|Clifton|DigitalOcean, LLC|
|3|20.47.108.204|8888|United States|Boydton|Microsoft Corporation|
|4|81.4.102.223|8081|Netherlands|Amsterdam|WeservIT|
|5|206.189.23.38|8048|United Kingdom|London|DigitalOcean, LLC|
|6|81.4.102.233|8081|Netherlands|Amsterdam|WeservIT|
|7|181.205.20.194|999|Colombia|Medellín|EPM Telecomunicaciones S.A. E.S.P.|
|8|195.154.67.61|3128|France|Paris|Online S.A.S.|
|9|45.167.124.5|9992|Colombia|Guapi|Sepcom Comunicaciones SAS|
|10|104.131.109.98|3128|United States|Clifton|DigitalOcean, LLC|
|11|95.217.72.247|3128|Finland|Helsinki|Hetzner Online GmbH|
|12|189.164.118.26|3128|Mexico|Coronango|Uninet S.A. de C.V|
|13|174.138.116.12|80|United States|Clifton|DigitalOcean, LLC|
|14|45.131.251.234|3129|United States|Los Angeles|DediPath|
|15|35.228.49.185|3128|Finland|Lappeenranta|Google LLC|
|16|207.180.217.107|3128|Germany|Nuremberg|Contabo GmbH|
|17|157.100.12.138|999|Ecuador|Quito|Telconet S.A|
|18|47.240.160.90|10001|Hong Kong|Central|Alibaba.com LLC|
|19|37.233.102.184|3128|Poland|Warsaw|Techstorage sp. z o.o.|
|20|167.235.63.238|3128|Germany|Falkenstein|Hetzner Online GmbH|



## Contributing

Contributions are welcome, and they are greatly appreciated! Every
little bit helps, and credit will always be given.

