
# Free HTTP Proxy List 🌍

[![Hourly Update](https://github.com/mertguvencli/http-proxy-list/actions/workflows/main.yml/badge.svg?branch=main)](https://github.com/mertguvencli/http-proxy-list/actions/workflows/main.yml)
![GitHub](https://img.shields.io/github/license/mertguvencli/http-proxy-list)
![GitHub last commit](https://img.shields.io/github/last-commit/mertguvencli/http-proxy-list)

It is a lightweight project that hourly scrapes lots of free-proxy sites, validates if it works, and serves a clean proxy list.


> Scraper found **3746** proxies at the latest update. Usable proxies are below.

## Usage

Click the file format that you want and copy the URL.


|File|Content|Count|
|----|-------|-----|
|[data.txt](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.txt)|`ip_address:port` combined (seperated new line)|187|
|[data.json](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.json)|`ip, port`|187|
|[data-with-geolocation.json](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data-with-geolocation.json)|`ip, port, geolocation`|187|

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
|[proxyscrape.com](https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all)|445|✅|
|[github.com/clarketm/proxy-list](https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt)|400|✅|
|[github.com/monosans/proxy-list](https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt)|225|✅|
|[github.com/TheSpeedX/PROXY-List](https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt)|1993|✅|


## Sample Proxies With Geolocation Info

|#|Ip|Port|Country|City|Internet Service Provider|
|-|--|----|-------|----|-------------------------|
|1|20.47.108.204|8888|United States|Boydton|Microsoft Corporation|
|2|216.176.32.79|3128|United Kingdom|Slough|Rackdog, LLC|
|3|167.172.239.13|3128|United States|Clifton|DigitalOcean, LLC|
|4|194.233.69.90|443|Singapore|Singapore|Contabo Asia Private Limited|
|5|41.164.68.194|8080|South Africa|Cape Town|Liquid Telecommunications Operations Limited|
|6|182.253.70.88|8080|Indonesia|Surabaya|BIZNET|
|7|164.90.252.243|8080|United States|North Bergen|DigitalOcean, LLC|
|8|190.26.201.194|8080|Colombia|Bogotá|ETB - Colombia|
|9|103.241.227.107|6666|India|Ahmedabad|GTPL SMC Network PVT LTD|
|10|216.176.32.79|3128|United Kingdom|Slough|Rackdog, LLC|
|11|179.1.88.27|999|Colombia|Anapoima|Internexa S.a. E.S.P|
|12|12.218.209.130|53281|United States|San Carlos|AT&T Services, Inc.|
|13|182.253.158.243|8080|Indonesia|Bandung|BIZNET|
|14|200.60.60.60|999|Peru|Lima|Telefonica del Peru S.A.A.|
|15|173.197.167.242|8080|United States|Ontario|Spectrum|
|16|45.88.42.75|8080|Singapore|Singapore|M247 Ltd|
|17|62.3.30.25|8080|Georgia|K'alak'i T'bilisi|Enbinet Ltd.|
|18|13.127.170.8|3128|India|Mumbai|Amazon Technologies Inc.|
|19|5.16.0.174|8080|Russia|St Petersburg|Enforta-MSK|
|20|84.205.17.234|8080|Poland|Szczecinek|Gawex Media Sp.zoo|



## Contributing

Contributions are welcome, and they are greatly appreciated! Every
little bit helps, and credit will always be given.

