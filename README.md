
# Free HTTP Proxy List 🌍

[![Hourly Update](https://github.com/mertguvencli/http-proxy-list/actions/workflows/main.yml/badge.svg?branch=main)](https://github.com/mertguvencli/http-proxy-list/actions/workflows/main.yml)
![GitHub](https://img.shields.io/github/license/mertguvencli/http-proxy-list)
![GitHub last commit](https://img.shields.io/github/last-commit/mertguvencli/http-proxy-list)

It is a lightweight project that hourly scrapes lots of free-proxy sites, validates if it works, and serves a clean proxy list.


> Scraper found **3283** proxies at the latest update. Usable proxies are below.

## Usage

Click the file format that you want and copy the URL.


|File|Content|Count|
|----|-------|-----|
|[data.txt](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.txt)|`ip_address:port` combined (seperated new line)|89|
|[data.json](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.json)|`ip, port`|89|
|[data-with-geolocation.json](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data-with-geolocation.json)|`ip, port, geolocation`|89|

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
|[proxyscrape.com](https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all)|0|✅|
|[github.com/clarketm/proxy-list](https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt)|400|✅|
|[github.com/monosans/proxy-list](https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt)|125|✅|
|[github.com/TheSpeedX/PROXY-List](https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt)|1775|✅|


## Sample Proxies With Geolocation Info

|#|Ip|Port|Country|City|Internet Service Provider|
|-|--|----|-------|----|-------------------------|
|1|216.176.32.79|3128|United Kingdom|Slough|Rackdog, LLC|
|2|54.38.78.108|1337|United Kingdom|Purfleet|OVH SAS|
|3|66.94.97.238|443|United States|New York|Contabo Inc.|
|4|186.67.230.45|3128|Chile|Santiago|Entel Chile S.A.|
|5|153.92.221.54|3128|Cyprus|Larnaca|Hostinger International Limited|
|6|203.217.169.100|6969|Cambodia|Phnom Penh|S.I Group|
|7|216.176.187.99|8886|United States|Los Angeles|Wowrack.com|
|8|85.25.150.32|5566|France|Strasbourg|Host Europe GmbH|
|9|85.25.139.22|5566|France|Strasbourg|Host Europe GmbH|
|10|190.2.211.134|8080|Colombia|Popayán|TV AZTECA SUCURSAL COLOMBIA|
|11|181.129.2.90|8081|Colombia|Caldas|EPM Telecomunicaciones S.A. E.S.P.|
|12|190.26.201.194|8080|Colombia|Bogotá|ETB - Colombia|
|13|85.25.119.98|5566|France|Strasbourg|BSB-SERVICE|
|14|182.253.158.243|8080|Indonesia|Bandung|BIZNET|
|15|85.25.242.142|5566|France|Strasbourg|Host Europe GmbH|
|16|123.163.55.123|3128|China|Zhoukou|Chinanet|
|17|122.155.165.191|3128|Thailand|Ratchathewi|CAT Telecom Public Company Limited|
|18|140.246.87.238|3128|China|Jinan|Cloud Computing Corporation|
|19|186.96.30.153|999|Mexico|Puerto Vallarta|Total Play Telecomunicaciones SA De CV|
|20|200.25.254.193|54240|Colombia|Bogotá|Andinet ON Line|



## Contributing

Contributions are welcome, and they are greatly appreciated! Every
little bit helps, and credit will always be given.

