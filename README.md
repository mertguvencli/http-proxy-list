
# Free HTTP Proxy List 🌍

[![Hourly Update](https://github.com/mertguvencli/http-proxy-list/actions/workflows/main.yml/badge.svg?branch=main)](https://github.com/mertguvencli/http-proxy-list/actions/workflows/main.yml)
![GitHub](https://img.shields.io/github/license/mertguvencli/http-proxy-list)
![GitHub last commit](https://img.shields.io/github/last-commit/mertguvencli/http-proxy-list)

It is a lightweight project that hourly scrapes lots of free-proxy sites, validates if it works, and serves a clean proxy list.


> Scraper found **3851** proxies at the latest update. Usable proxies are below.

## Usage

Click the file format that you want and copy the URL.


|File|Content|Count|
|----|-------|-----|
|[data.txt](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.txt)|`ip_address:port` combined (seperated new line)|171|
|[data.json](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.json)|`ip, port`|171|
|[data-with-geolocation.json](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data-with-geolocation.json)|`ip, port, geolocation`|171|

## Sources

|Source|Found Proxies|Succeed|
|------|-------------|-------|
|[free-proxy-list.net](https://free-proxy-list.net)|300|✅|
|[us-proxy.org](https://www.us-proxy.org)|200|✅|
|[proxydb.net](http://proxydb.net)|15|✅|
|[free-proxy-list.com](https://free-proxy-list.com/?page=&port=&type%5B%5D=http&type%5B%5D=https&up_time=0&search=Search)|0|🚫|
|[proxy-list.download](https://www.proxy-list.download/HTTP)|26|✅|
|[vpnoverview.com](https://vpnoverview.com/privacy/anonymous-browsing/free-proxy-servers)|32|✅|
|[proxyscan.io](https://www.proxyscan.io)|90|✅|
|[proxylist.geonode.com](https://proxylist.geonode.com/api/proxy-list?limit=300&page=1&sort_by=lastChecked&sort_type=desc&protocols=http,https)|300|✅|
|[proxyscrape.com](https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all)|376|✅|
|[github.com/clarketm/proxy-list](https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt)|400|✅|
|[github.com/monosans/proxy-list](https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt)|182|✅|
|[github.com/TheSpeedX/PROXY-List](https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt)|1930|✅|


## Sample Proxies With Geolocation Info

|#|Ip|Port|Country|City|Internet Service Provider|
|-|--|----|-------|----|-------------------------|
|1|3.128.120.252|80|United States|Dublin|Amazon.com, Inc.|
|2|132.145.59.254|3128|United Kingdom|London|Oracle Corporation|
|3|138.197.69.179|8080|United States|Clifton|DigitalOcean, LLC|
|4|161.49.215.57|8080|Philippines|Bulacan|Converge Information and Communications Technology Solutions|
|5|159.192.249.211|8080|Thailand|Bangkok|CAT-BB|
|6|175.100.64.127|9812|Cambodia|Phnom Penh|VIETTEL (CAMBODIA) PTE., LTD|
|7|101.109.176.153|8080|Thailand|Kanchanaburi|TOT Public Company Limited|
|8|103.138.14.43|8080|Indonesia|Medan|Adidaya Infocom Lestari|
|9|125.25.33.64|8080|Thailand|Chiang Mai|TOT Public Company Limited|
|10|159.65.69.186|9300|United States|Santa Clara|DigitalOcean, LLC|
|11|85.195.104.71|80|Germany|Frankfurt am Main|Host Europe GmbH|
|12|58.147.186.226|8080|Indonesia|Sambas|PT. Transhybrid Communication|
|13|152.70.61.93|3128|Netherlands|Amsterdam|Oracle Corporation|
|14|20.47.108.204|8888|United States|Boydton|Microsoft Corporation|
|15|183.88.172.222|8080|Thailand|Ban Khoi Tai|Triple T Broadband Public Company Limited|
|16|47.252.4.64|8888|United States|Charlottesville|Alibaba.com LLC|
|17|167.114.96.27|9300|Canada|Montreal|OVH SAS|
|18|34.136.99.66|3128|United States|Council Bluffs|Google LLC|
|19|58.27.255.98|8080|Pakistan|Karachi|Wateen Telecom Limited|
|20|103.214.9.13|3128|Vietnam|Hanoi|MEGACORE|



## Contributing

Contributions are welcome, and they are greatly appreciated! Every
little bit helps, and credit will always be given.

