
# Free HTTP Proxy List 🌍

[![Hourly Update](https://github.com/mertguvencli/http-proxy-list/actions/workflows/main.yml/badge.svg?branch=main)](https://github.com/mertguvencli/http-proxy-list/actions/workflows/main.yml)
![GitHub](https://img.shields.io/github/license/mertguvencli/http-proxy-list)
![GitHub last commit](https://img.shields.io/github/last-commit/mertguvencli/http-proxy-list)

It is a lightweight project that hourly scrapes lots of free-proxy sites, validates if it works, and serves a clean proxy list.


> Scraper found **3378** proxies at the latest update. Usable proxies are below.

## Usage

Click the file format that you want and copy the URL.


|File|Content|Count|
|----|-------|-----|
|[data.txt](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.txt)|`ip_address:port` combined (seperated new line)|119|
|[data.json](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.json)|`ip, port`|119|
|[data-with-geolocation.json](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data-with-geolocation.json)|`ip, port, geolocation`|119|

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
|[proxylist.geonode.com](https://proxylist.geonode.com/api/proxy-list?limit=300&page=1&sort_by=lastChecked&sort_type=desc&protocols=http,https)|0|🚫|
|[proxyscrape.com](https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all)|287|✅|
|[github.com/clarketm/proxy-list](https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt)|400|✅|
|[github.com/monosans/proxy-list](https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt)|123|✅|
|[github.com/TheSpeedX/PROXY-List](https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt)|1885|✅|


## Sample Proxies With Geolocation Info

|#|Ip|Port|Country|City|Internet Service Provider|
|-|--|----|-------|----|-------------------------|
|1|20.47.108.204|8888|United States|Boydton|Microsoft Corporation|
|2|173.82.201.21|8080|United States|Santa Clarita|Multacom Corporation|
|3|173.82.201.21|8080|United States|Santa Clarita|Multacom Corporation|
|4|85.25.91.141|15333|Germany|Cologne|PlusServer GmbH|
|5|153.126.179.216|8080|Japan|Osaka|SAKURA Internet Inc.|
|6|85.25.99.106|5566|France|Strasbourg|PLUSSERVER|
|7|188.138.106.158|5566|France|Strasbourg|Host Europe GmbH|
|8|172.104.102.178|7721|Japan|Tokyo|Linode, LLC|
|9|85.25.226.242|5566|France|Strasbourg|Host Europe GmbH|
|10|36.91.166.98|8080|Indonesia|Jakarta|PT Telekomunikasi Indonesia|
|11|190.26.201.194|8080|Colombia|Bogotá|ETB - Colombia|
|12|190.26.201.194|8080|Colombia|Bogotá|ETB - Colombia|
|13|182.253.158.243|8080|Indonesia|Bandung|BIZNET|
|14|188.138.106.158|5566|France|Strasbourg|Host Europe GmbH|
|15|102.130.79.254|3128|South Africa|Pretoria|Adnexus Celerity Networks (Proprietary) Limited|
|16|170.246.39.7|999|Argentina|Caleta Olivia|Carrasco Leonardo Javier|
|17|85.25.196.218|5566|France|Strasbourg|Host Europe GmbH|
|18|85.25.117.68|5566|France|Strasbourg|BSB-SERVICE|
|19|43.250.127.98|9001|Mongolia|Ulan Bator|Wicom Networks|
|20|95.216.12.141|22214|Finland|Helsinki|Hetzner Online GmbH|



## Contributing

Contributions are welcome, and they are greatly appreciated! Every
little bit helps, and credit will always be given.

