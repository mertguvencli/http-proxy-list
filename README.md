
# Free HTTP Proxy List 🌍

[![Hourly Update](https://github.com/mertguvencli/http-proxy-list/actions/workflows/main.yml/badge.svg?branch=main)](https://github.com/mertguvencli/http-proxy-list/actions/workflows/main.yml)
![GitHub](https://img.shields.io/github/license/mertguvencli/http-proxy-list)
![GitHub last commit](https://img.shields.io/github/last-commit/mertguvencli/http-proxy-list)

It is a lightweight project that hourly scrapes lots of free-proxy sites, validates if it works, and serves a clean proxy list.


> Scraper found **3446** proxies at the latest update. Usable proxies are below.

## Usage

Click the file format that you want and copy the URL.


|File|Content|Count|
|----|-------|-----|
|[data.txt](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.txt)|`ip_address:port` combined (seperated new line)|101|
|[data.json](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.json)|`ip, port`|101|
|[data-with-geolocation.json](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data-with-geolocation.json)|`ip, port, geolocation`|101|

## Sources

|Source|Found Proxies|Succeed|
|------|-------------|-------|
|[free-proxy-list.net](https://free-proxy-list.net)|300|✅|
|[us-proxy.org](https://www.us-proxy.org)|200|✅|
|[proxydb.net](http://proxydb.net)|15|✅|
|[free-proxy-list.com](https://free-proxy-list.com/?page=&port=&type%5B%5D=http&type%5B%5D=https&up_time=0&search=Search)|10|✅|
|[proxy-list.download](https://www.proxy-list.download/HTTP)|26|✅|
|[vpnoverview.com](https://vpnoverview.com/privacy/anonymous-browsing/free-proxy-servers)|32|✅|
|[proxyscan.io](https://www.proxyscan.io)|86|✅|
|[proxylist.geonode.com](https://proxylist.geonode.com/api/proxy-list?limit=300&page=1&sort_by=lastChecked&sort_type=desc&protocols=http,https)|0|🚫|
|[proxyscrape.com](https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all)|307|✅|
|[github.com/clarketm/proxy-list](https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt)|400|✅|
|[github.com/monosans/proxy-list](https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt)|143|✅|
|[github.com/TheSpeedX/PROXY-List](https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt)|1927|✅|


## Sample Proxies With Geolocation Info

|#|Ip|Port|Country|City|Internet Service Provider|
|-|--|----|-------|----|-------------------------|
|1|34.82.235.224|3128|United States|The Dalles|Google LLC|
|2|216.176.32.79|3128|United Kingdom|Slough|Rackdog, LLC|
|3|85.25.119.98|5566|France|Strasbourg|BSB-SERVICE|
|4|188.138.11.48|5566|France|Strasbourg|Host Europe GmbH|
|5|194.233.69.41|443|Singapore|Singapore|Contabo Asia Private Limited|
|6|85.25.133.28|5566|France|Strasbourg|Host Europe GmbH|
|7|65.51.178.92|3128|United States|Weehawken|Cablevision Systems Corp.|
|8|190.26.201.194|8080|Colombia|Bogotá|ETB - Colombia|
|9|190.26.201.194|8080|Colombia|Bogotá|ETB - Colombia|
|10|158.255.215.50|9090|France|Paris|Edis France|
|11|66.94.120.161|443|United States|Seattle|Contabo Inc.|
|12|149.154.157.17|5678|Italy|Milan|EDIS|
|13|85.25.208.198|5566|France|Strasbourg|Host Europe GmbH|
|14|45.190.248.25|8080|Brazil|Passo Fundo|RK Telecom Provedor Internet LTDA|
|15|194.233.69.38|443|Singapore|Singapore|Contabo Asia Private Limited|
|16|170.155.5.235|8080|Argentina|Castelar|Gobernacion de la Provincia de Buenos Aires|
|17|216.176.32.79|3128|United Kingdom|Slough|Rackdog, LLC|
|18|181.129.14.163|999|Colombia|Medellín|EPM Telecomunicaciones S.A. E.S.P.|
|19|103.164.99.58|8181|Indonesia|Jakarta|SOLUSINET|
|20|95.66.142.11|8080|Russia|Vladimir|Limited Liability Company "Infocentre"|



## Contributing

Contributions are welcome, and they are greatly appreciated! Every
little bit helps, and credit will always be given.

