
# Free HTTP Proxy List 🌍

[![Hourly Update](https://github.com/mertguvencli/http-proxy-list/actions/workflows/main.yml/badge.svg?branch=main)](https://github.com/mertguvencli/http-proxy-list/actions/workflows/main.yml)
![GitHub](https://img.shields.io/github/license/mertguvencli/http-proxy-list)
![GitHub last commit](https://img.shields.io/github/last-commit/mertguvencli/http-proxy-list)

It is a lightweight project that hourly scrapes lots of free-proxy sites, validates if it works, and serves a clean proxy list.


> Scraper found **3591** proxies at the latest update. Usable proxies are below.

## Usage

Click the file format that you want and copy the URL.


|File|Content|Count|
|----|-------|-----|
|[data.txt](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.txt)|`ip_address:port` combined (seperated new line)|168|
|[data.json](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.json)|`ip, port`|168|
|[data-with-geolocation.json](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data-with-geolocation.json)|`ip, port, geolocation`|168|

## Sources

|Source|Found Proxies|Succeed|
|------|-------------|-------|
|[free-proxy-list.net](https://free-proxy-list.net)|300|✅|
|[us-proxy.org](https://www.us-proxy.org)|200|✅|
|[proxydb.net](http://proxydb.net)|15|✅|
|[free-proxy-list.com](https://free-proxy-list.com/?page=&port=&type%5B%5D=http&type%5B%5D=https&up_time=0&search=Search)|0|🚫|
|[proxy-list.download](https://www.proxy-list.download/HTTP)|26|✅|
|[vpnoverview.com](https://vpnoverview.com/privacy/anonymous-browsing/free-proxy-servers)|32|✅|
|[proxyscan.io](https://www.proxyscan.io)|0|🚫|
|[proxylist.geonode.com](https://proxylist.geonode.com/api/proxy-list?limit=300&page=1&sort_by=lastChecked&sort_type=desc&protocols=http,https)|300|✅|
|[proxyscrape.com](https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all)|314|✅|
|[github.com/clarketm/proxy-list](https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt)|400|✅|
|[github.com/monosans/proxy-list](https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt)|142|✅|
|[github.com/TheSpeedX/PROXY-List](https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt)|1862|✅|


## Sample Proxies With Geolocation Info

|#|Ip|Port|Country|City|Internet Service Provider|
|-|--|----|-------|----|-------------------------|
|1|147.75.68.201|80|United States|Sunnyvale|Packet Host, Inc.|
|2|3.128.120.252|80|United States|Dublin|Amazon.com, Inc.|
|3|147.75.68.201|80|United States|Sunnyvale|Packet Host, Inc.|
|4|45.167.125.209|9992|Colombia|Popayán|Sepcom Comunicaciones SAS|
|5|45.190.84.2|999|Venezuela|Caracas|TELECOM.CORPORATIVAS TELECORP, C.A|
|6|209.250.253.162|59394|Netherlands|Amsterdam|The Constant Company|
|7|190.97.226.236|999|Venezuela|Barinas|NetLink América C.A.|
|8|157.100.12.138|999|Ecuador|Quito|Telconet S.A|
|9|47.74.226.8|5001|Singapore|Singapore|Alibaba Cloud (Singapore) Private Limited|
|10|159.192.253.197|8080|Thailand|Samphanthawong|CAT-BB|
|11|139.255.25.85|3128|Indonesia|Jakarta|PT. LINKNET|
|12|81.12.106.158|8080|Iran|Tehran|Respina Networks & Beyond PJSC|
|13|181.129.14.166|999|Colombia|Medellín|EPM Telecomunicaciones S.A. E.S.P.|
|14|45.190.249.100|8080|Brazil|Passo Fundo|RK Telecom Provedor Internet LTDA|
|15|88.255.102.120|8080|Turkey|İskenderun|TurkTelekom|
|16|109.121.55.162|8888|Serbia|Belgrade|Orion telekom - DPI Sid|
|17|8.242.212.170|999|Colombia|Bogotá|CTL Colombia|
|18|200.25.254.193|54240|Colombia|Bogotá|Andinet ON Line|
|19|93.185.3.161|9812|Czechia|Dobratice|Ing. Roman Cvicek|
|20|128.201.213.253|8080|Brazil|Aracaju|VLZ TECNOLOGIAS EIRELI|



## Contributing

Contributions are welcome, and they are greatly appreciated! Every
little bit helps, and credit will always be given.

