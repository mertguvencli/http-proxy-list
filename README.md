
# Free HTTP Proxy List 🌍

[![Hourly Update](https://github.com/mertguvencli/http-proxy-list/actions/workflows/main.yml/badge.svg?branch=main)](https://github.com/mertguvencli/http-proxy-list/actions/workflows/main.yml)
![GitHub](https://img.shields.io/github/license/mertguvencli/http-proxy-list)
![GitHub last commit](https://img.shields.io/github/last-commit/mertguvencli/http-proxy-list)

It is a lightweight project that hourly scrapes lots of free-proxy sites, validates if it works, and serves a clean proxy list.


> Scraper found **3800** proxies at the latest update. Usable proxies are below.

## Usage

Click the file format that you want and copy the URL.


|File|Content|Count|
|----|-------|-----|
|[data.txt](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.txt)|`ip_address:port` combined (seperated new line)|135|
|[data.json](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.json)|`ip, port`|135|
|[data-with-geolocation.json](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data-with-geolocation.json)|`ip, port, geolocation`|135|

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
|[proxyscrape.com](https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all)|303|✅|
|[github.com/clarketm/proxy-list](https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt)|400|✅|
|[github.com/monosans/proxy-list](https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt)|193|✅|
|[github.com/TheSpeedX/PROXY-List](https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt)|1921|✅|


## Sample Proxies With Geolocation Info

|#|Ip|Port|Country|City|Internet Service Provider|
|-|--|----|-------|----|-------------------------|
|1|157.245.222.183|80|United States|Clifton|DigitalOcean, LLC|
|2|157.245.222.183|80|United States|Clifton|DigitalOcean, LLC|
|3|67.212.83.55|1080|Canada|Saint-Hyacinthe|eStruxture Data Centers Inc.|
|4|67.212.83.53|1080|Canada|Saint-Hyacinthe|eStruxture Data Centers Inc.|
|5|67.212.83.54|1080|Canada|Saint-Hyacinthe|eStruxture Data Centers Inc.|
|6|192.254.104.201|999|Puerto Rico|Humacao|OSNET Wireless|
|7|80.32.216.24|3128|Spain|Madrid|RIMA (Red IP Multi Acceso)|
|8|103.152.100.183|8080|Pakistan|Lahore|KK Networks (Pvt) Ltd.|
|9|144.202.116.156|59394|United States|Los Angeles|The Constant Company|
|10|5.167.141.239|3128|Russia|Tula|CJSC "ER-Telecom Holding" Tula branch|
|11|46.99.183.154|1234|Albania|Tirana|IPKO Telecommunications LLC|
|12|201.174.239.18|8080|Mexico|Ciudad Juárez|Transtelco Inc|
|13|190.26.201.194|8080|Colombia|Bogotá|ETB - Colombia|
|14|190.26.201.194|8080|Colombia|Bogotá|ETB - Colombia|
|15|103.161.164.103|8181|Indonesia|Ciamis|PT Galuh Multidata Solution|
|16|165.16.60.1|8080|Libya|Tripoli|Aljeel Aljadeed For Technology|
|17|186.67.230.45|3128|Chile|Santiago|Entel Chile S.A.|
|18|103.85.119.148|9812|India|Greater Noida|S A Internet Solution Pvt Ltd|
|19|101.43.95.215|7777|China|Haidian|Shenzhen Tencent Computer Systems Company Limited|
|20|182.253.65.40|8085|Indonesia|Jakarta|BIZNET|



## Contributing

Contributions are welcome, and they are greatly appreciated! Every
little bit helps, and credit will always be given.

