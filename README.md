
# Free HTTP Proxy List 🌍

[![Hourly Update](https://github.com/mertguvencli/http-proxy-list/actions/workflows/main.yml/badge.svg?branch=main)](https://github.com/mertguvencli/http-proxy-list/actions/workflows/main.yml)
![GitHub](https://img.shields.io/github/license/mertguvencli/http-proxy-list)
![GitHub last commit](https://img.shields.io/github/last-commit/mertguvencli/http-proxy-list)

It is a lightweight project that hourly scrapes lots of free-proxy sites, validates if it works, and serves a clean proxy list.


> Scraper found **3897** proxies at the latest update. Usable proxies are below.

## Usage

Click the file format that you want and copy the URL.


|File|Content|Count|
|----|-------|-----|
|[data.txt](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.txt)|`ip_address:port` combined (seperated new line)|241|
|[data.json](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.json)|`ip, port`|241|
|[data-with-geolocation.json](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data-with-geolocation.json)|`ip, port, geolocation`|241|

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
|[proxylist.geonode.com](https://proxylist.geonode.com/api/proxy-list?limit=300&page=1&sort_by=lastChecked&sort_type=desc&protocols=http,https)|0|🚫|
|[proxyscrape.com](https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all)|574|✅|
|[github.com/clarketm/proxy-list](https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt)|400|✅|
|[github.com/monosans/proxy-list](https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt)|410|✅|
|[github.com/TheSpeedX/PROXY-List](https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt)|1930|✅|


## Sample Proxies With Geolocation Info

|#|Ip|Port|Country|City|Internet Service Provider|
|-|--|----|-------|----|-------------------------|
|1|20.47.108.204|8888|United States|Boydton|Microsoft Corporation|
|2|216.176.32.79|3128|United Kingdom|Slough|Rackdog, LLC|
|3|199.195.254.168|8118|United States|New York|FranTech Solutions|
|4|20.47.108.204|8888|United States|Boydton|Microsoft Corporation|
|5|65.51.178.93|3128|United States|Weehawken|Cablevision Systems Corp.|
|6|186.67.230.45|3128|Chile|Santiago|Entel Chile S.A.|
|7|109.194.101.128|3128|Russia|Surok|CJSC "ER-Telecom Holding" Yoshkar-Ola branch|
|8|85.25.133.28|5566|France|Strasbourg|Host Europe GmbH|
|9|85.25.117.171|5566|France|Strasbourg|BSB-SERVICE|
|10|143.248.55.62|8118|South Korea|Daejeon|Korea Advanced Institute of Science and Technology|
|11|200.116.198.222|9812|Colombia|Manizales|EPM Telecomunicaciones S.A. E.S.P|
|12|167.172.6.161|443|Singapore|Singapore|DigitalOcean, LLC|
|13|103.162.152.5|8085|Indonesia|Dusun Tua|AKSIRIAU|
|14|103.178.43.2|8181|Indonesia|Jakarta|PT Jaring Solusi Persada|
|15|186.233.186.60|8080|United States|Chicago|Maxihost LTDA|
|16|190.26.201.194|8080|Colombia|Bogotá|ETB - Colombia|
|17|14.177.242.64|8080|Vietnam|Hanoi|VNPT|
|18|118.70.109.148|55443|Vietnam|Hanoi|FPT Telecom Company|
|19|85.15.152.39|3128|Russia|Tyumen|Rostelecom networks|
|20|178.159.40.19|8080|Russia|Moscow|Linenet Ltd.|



## Contributing

Contributions are welcome, and they are greatly appreciated! Every
little bit helps, and credit will always be given.

