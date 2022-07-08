
# Free HTTP Proxy List 🌍

[![Hourly Update](https://github.com/mertguvencli/http-proxy-list/actions/workflows/main.yml/badge.svg?branch=main)](https://github.com/mertguvencli/http-proxy-list/actions/workflows/main.yml)
![GitHub](https://img.shields.io/github/license/mertguvencli/http-proxy-list)
![GitHub last commit](https://img.shields.io/github/last-commit/mertguvencli/http-proxy-list)

It is a lightweight project that hourly scrapes lots of free-proxy sites, validates if it works, and serves a clean proxy list.


> Scraper found **3421** proxies at the latest update. Usable proxies are below.

## Usage

Click the file format that you want and copy the URL.


|File|Content|Count|
|----|-------|-----|
|[data.txt](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.txt)|`ip_address:port` combined (seperated new line)|127|
|[data.json](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.json)|`ip, port`|127|
|[data-with-geolocation.json](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data-with-geolocation.json)|`ip, port, geolocation`|127|

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
|[proxylist.geonode.com](https://proxylist.geonode.com/api/proxy-list?limit=300&page=1&sort_by=lastChecked&sort_type=desc&protocols=http,https)|181|✅|
|[proxyscrape.com](https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all)|300|✅|
|[github.com/clarketm/proxy-list](https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt)|400|✅|
|[github.com/monosans/proxy-list](https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt)|104|✅|
|[github.com/TheSpeedX/PROXY-List](https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt)|1853|✅|


## Sample Proxies With Geolocation Info

|#|Ip|Port|Country|City|Internet Service Provider|
|-|--|----|-------|----|-------------------------|
|1|45.152.188.246|3128|United States|Ashburn|Sprint|
|2|198.41.67.18|8080|United States|Lafayette|Cox Communications Inc.|
|3|198.41.67.18|8080|United States|Lafayette|Cox Communications Inc.|
|4|159.192.249.226|8080|Thailand|Bangkok|CAT-BB|
|5|206.189.195.74|8080|United States|North Bergen|DigitalOcean, LLC|
|6|198.41.67.18|8080|United States|Lafayette|Cox Communications Inc.|
|7|199.58.128.75|8080|United States|Kingsville|Foremost Telecommunications|
|8|119.42.86.79|8080|Thailand|Samphanthawong|CAT-BB|
|9|122.155.165.191|3128|Thailand|Ratchathewi|CAT Telecom Public Company Limited|
|10|94.181.48.171|1256|Russia|Moscow|Enforta-MSK|
|11|203.112.74.35|8080|Bangladesh|Dhaka|OptiMax Communication Ltd|
|12|199.58.128.75|8080|United States|Kingsville|Foremost Telecommunications|
|13|45.152.188.246|3128|United States|Ashburn|Sprint|
|14|20.47.108.204|8888|United States|Boydton|Microsoft Corporation|
|15|103.252.1.137|3128|Vietnam|Hanoi|CMCMIENBAC|
|16|116.253.208.239|33080|China|Lilancun|CHINATELECOM Guangxi Nanning IDC networkdescr: Nanning, Guangxi Province, P.R.|
|17|79.143.179.141|3128|Germany|Munich|Contabo GmbH|
|18|140.227.80.237|3180|Japan|Chiyoda|NTT PC Communications, Inc.|
|19|115.96.208.124|8080|India|Mumbai|Hathway IP over Cable Internet Access|
|20|185.15.172.212|3128|Russia|Moscow|SafeData LLC|



## Contributing

Contributions are welcome, and they are greatly appreciated! Every
little bit helps, and credit will always be given.

