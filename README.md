
# Free HTTP Proxy List 🌍

[![Hourly Update](https://github.com/mertguvencli/http-proxy-list/actions/workflows/main.yml/badge.svg?branch=main)](https://github.com/mertguvencli/http-proxy-list/actions/workflows/main.yml)
![GitHub](https://img.shields.io/github/license/mertguvencli/http-proxy-list)
![GitHub last commit](https://img.shields.io/github/last-commit/mertguvencli/http-proxy-list)

It is a lightweight project that hourly scrapes lots of free-proxy sites, validates if it works, and serves a clean proxy list.


> Scraper found **4167** proxies at the latest update. Usable proxies are below.

## Usage

Click the file format that you want and copy the URL.


|File|Content|Count|
|----|-------|-----|
|[data.txt](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.txt)|`ip_address:port` combined (seperated new line)|245|
|[data.json](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.json)|`ip, port`|245|
|[data-with-geolocation.json](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data-with-geolocation.json)|`ip, port, geolocation`|245|

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
|[proxyscrape.com](https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all)|393|✅|
|[github.com/clarketm/proxy-list](https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt)|400|✅|
|[github.com/monosans/proxy-list](https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt)|413|✅|
|[github.com/TheSpeedX/PROXY-List](https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt)|2078|✅|


## Sample Proxies With Geolocation Info

|#|Ip|Port|Country|City|Internet Service Provider|
|-|--|----|-------|----|-------------------------|
|1|170.155.5.235|8080|Argentina|Castelar|Gobernacion de la Provincia de Buenos Aires|
|2|45.80.149.39|23456|Netherlands|Amsterdam|Hostgw SRL|
|3|103.73.194.2|80|Hong Kong|Wanchai|TouchPal HK Co., Limited|
|4|117.20.216.218|8080|South Korea|Gumi|HYUNDAI COMMUNICATIONS & NETWORK|
|5|85.25.196.218|5566|France|Strasbourg|Host Europe GmbH|
|6|66.94.97.238|443|United States|New York|Contabo Inc.|
|7|200.25.254.193|54240|Colombia|Bogotá|Andinet ON Line|
|8|134.209.148.107|8081|India|Bengaluru|DigitalOcean, LLC|
|9|188.138.11.48|5566|France|Strasbourg|Host Europe GmbH|
|10|62.75.219.49|5566|France|Strasbourg|BSB-SERVICE|
|11|103.175.236.102|8080|Indonesia|Malang|PT Marva Global Telekomunikasi|
|12|216.176.187.99|8886|United States|Bonney Lake|Wowrack.com|
|13|45.173.6.98|999|Colombia|Zipaquirá|Columbus Networks Colombia|
|14|172.96.169.33|9955|Puerto Rico|Guaynabo|Fuse Telecom LLC|
|15|66.94.97.238|443|United States|New York|Contabo Inc.|
|16|5.189.184.6|80|Germany|Nuremberg|Contabo GmbH|
|17|188.138.106.133|5566|France|Strasbourg|Host Europe GmbH|
|18|190.26.201.194|8080|Colombia|Castilla La Nueva|ETB - Colombia|
|19|85.25.111.162|5566|Germany|Cologne|PlusServer GmbH|
|20|190.26.201.194|8080|Colombia|Castilla La Nueva|ETB - Colombia|



## Contributing

Contributions are welcome, and they are greatly appreciated! Every
little bit helps, and credit will always be given.

