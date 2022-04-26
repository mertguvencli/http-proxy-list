
# Free HTTP Proxy List 🌍

[![Hourly Update](https://github.com/mertguvencli/http-proxy-list/actions/workflows/main.yml/badge.svg?branch=main)](https://github.com/mertguvencli/http-proxy-list/actions/workflows/main.yml)
![GitHub](https://img.shields.io/github/license/mertguvencli/http-proxy-list)
![GitHub last commit](https://img.shields.io/github/last-commit/mertguvencli/http-proxy-list)

It is a lightweight project that hourly scrapes lots of free-proxy sites, validates if it works, and serves a clean proxy list.


> Scraper found **3686** proxies at the latest update. Usable proxies are below.

## Usage

Click the file format that you want and copy the URL.


|File|Content|Count|
|----|-------|-----|
|[data.txt](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.txt)|`ip_address:port` combined (seperated new line)|206|
|[data.json](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.json)|`ip, port`|206|
|[data-with-geolocation.json](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data-with-geolocation.json)|`ip, port, geolocation`|206|

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
|[proxyscrape.com](https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all)|295|✅|
|[github.com/clarketm/proxy-list](https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt)|400|✅|
|[github.com/monosans/proxy-list](https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt)|126|✅|
|[github.com/TheSpeedX/PROXY-List](https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt)|1982|✅|


## Sample Proxies With Geolocation Info

|#|Ip|Port|Country|City|Internet Service Provider|
|-|--|----|-------|----|-------------------------|
|1|103.73.194.2|80|Hong Kong|Wanchai|TouchPal HK Co., Limited|
|2|170.155.5.235|8080|Argentina|Castelar|Gobernacion de la Provincia de Buenos Aires|
|3|191.97.6.214|999|Colombia|Quibdó|TV AZTECA SUCURSAL COLOMBIA|
|4|5.189.184.6|80|Germany|Nuremberg|Contabo GmbH|
|5|85.25.117.134|5566|France|Strasbourg|BSB-SERVICE|
|6|62.138.8.42|5566|France|Strasbourg|Host Europe GmbH|
|7|85.25.199.122|5566|France|Strasbourg|Host Europe GmbH|
|8|179.1.129.134|999|Colombia|Neiva|Internexa S.a. E.S.P|
|9|194.233.86.75|1234|Singapore|Singapore|Contabo Asia Private Limited|
|10|190.26.201.194|8080|Colombia|Castilla La Nueva|ETB - Colombia|
|11|190.26.201.194|8080|Colombia|Castilla La Nueva|ETB - Colombia|
|12|158.255.215.50|11857|France|Paris|Edis France|
|13|158.255.215.50|11857|France|Paris|Edis France|
|14|62.138.7.104|5566|France|Strasbourg|Host Europe Group|
|15|49.48.116.93|8080|Thailand|Chum Phae|Triple T Broadband Public Company Limited|
|16|128.90.172.181|33080|Ukraine|Kyiv|Powerhouse Management, Inc.|
|17|41.60.237.83|8080|Kenya|Nairobi|Maintainer Liquid Telecommunications Operations Limited|
|18|122.155.165.191|3128|Thailand|Ratchathewi|CAT Telecom Public Company Limited|
|19|79.135.219.223|8080|Ukraine|Odessa|ICN Ltd.|
|20|132.145.195.93|3128|United States|Ashburn|Oracle Corporation|



## Contributing

Contributions are welcome, and they are greatly appreciated! Every
little bit helps, and credit will always be given.

