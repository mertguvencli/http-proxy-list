
# Free HTTP Proxy List 🌍

[![Hourly Update](https://github.com/mertguvencli/http-proxy-list/actions/workflows/main.yml/badge.svg?branch=main)](https://github.com/mertguvencli/http-proxy-list/actions/workflows/main.yml)
![GitHub](https://img.shields.io/github/license/mertguvencli/http-proxy-list)
![GitHub last commit](https://img.shields.io/github/last-commit/mertguvencli/http-proxy-list)

It is a lightweight project that hourly scrapes lots of free-proxy sites, validates if it works, and serves a clean proxy list.


> Scraper found **4474** proxies at the latest update. Usable proxies are below.

## Usage

Click the file format that you want and copy the URL.


|File|Content|Count|
|----|-------|-----|
|[data.txt](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.txt)|`ip_address:port` combined (seperated new line)|413|
|[data.json](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.json)|`ip, port`|413|
|[data-with-geolocation.json](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data-with-geolocation.json)|`ip, port, geolocation`|413|

## Sources

|Source|Found Proxies|Succeed|
|------|-------------|-------|
|[free-proxy-list.net](https://free-proxy-list.net)|300|✅|
|[us-proxy.org](https://www.us-proxy.org)|200|✅|
|[proxydb.net](http://proxydb.net)|15|✅|
|[free-proxy-list.com](https://free-proxy-list.com/?page=&port=&type%5B%5D=http&type%5B%5D=https&up_time=0&search=Search)|10|✅|
|[proxy-list.download](https://www.proxy-list.download/HTTP)|26|✅|
|[vpnoverview.com](https://vpnoverview.com/privacy/anonymous-browsing/free-proxy-servers)|32|✅|
|[proxyscan.io](https://www.proxyscan.io)|80|✅|
|[proxylist.geonode.com](https://proxylist.geonode.com/api/proxy-list?limit=300&page=1&sort_by=lastChecked&sort_type=desc&protocols=http,https)|300|✅|
|[proxyscrape.com](https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all)|579|✅|
|[github.com/clarketm/proxy-list](https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt)|400|✅|
|[github.com/monosans/proxy-list](https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt)|395|✅|
|[github.com/TheSpeedX/PROXY-List](https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt)|2137|✅|


## Sample Proxies With Geolocation Info

|#|Ip|Port|Country|City|Internet Service Provider|
|-|--|----|-------|----|-------------------------|
|1|66.196.238.181|3128|United States|Houston|Logix|
|2|66.196.238.181|3128|United States|Houston|Logix|
|3|35.240.63.166|3128|Belgium|Brussels|Google LLC|
|4|47.240.160.90|10001|Hong Kong|Central|Alibaba.com LLC|
|5|206.189.23.38|8048|United Kingdom|London|DigitalOcean, LLC|
|6|115.96.208.124|8080|India|Mumbai|Hathway IP over Cable Internet Access|
|7|140.227.66.63|3180|Japan|Chiyoda|NTT PC Communications, Inc.|
|8|195.201.115.230|8118|Germany|Gunzenhausen|Hetzner Online GmbH|
|9|44.204.247.143|3128|United States|Ashburn|Amazon.com|
|10|18.188.193.74|3128|United States|Dublin|Amazon.com, Inc.|
|11|80.252.5.34|7001|Poland|Warsaw|GWNET Autonomus System|
|12|185.82.98.22|8091|Lebanon|Tripoli|Protected|
|13|181.129.138.114|30838|Colombia|Manizales|EPM Telecomunicaciones S.A. E.S.P.|
|14|194.233.73.109|443|Singapore|Singapore|Contabo Asia Private Limited|
|15|92.118.92.107|8181|Russia|Krasnodar|TSK LLC|
|16|175.100.64.127|9812|Cambodia|Phnom Penh|VIETTEL (CAMBODIA) PTE., LTD|
|17|195.43.168.10|3128|Italy|Fusignano|Irideos S.P.A.|
|18|14.207.82.229|8080|Thailand|Bangkok|Triple T Broadband Public Company Limited|
|19|110.170.126.13|3128|Thailand|Din Daeng|True Internet Corporation CO. Ltd.|
|20|89.107.197.165|3128|Russia|Tula|LLC TK Altair|



## Contributing

Contributions are welcome, and they are greatly appreciated! Every
little bit helps, and credit will always be given.

