
# Free HTTP Proxy List 🌍

[![Hourly Update](https://github.com/mertguvencli/http-proxy-list/actions/workflows/main.yml/badge.svg?branch=main)](https://github.com/mertguvencli/http-proxy-list/actions/workflows/main.yml)
![GitHub](https://img.shields.io/github/license/mertguvencli/http-proxy-list)
![GitHub last commit](https://img.shields.io/github/last-commit/mertguvencli/http-proxy-list)

It is a lightweight project that hourly scrapes lots of free-proxy sites, validates if it works, and serves a clean proxy list.


> Scraper found **4049** proxies at the latest update. Usable proxies are below.

## Usage

Click the file format that you want and copy the URL.


|File|Content|Count|
|----|-------|-----|
|[data.txt](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.txt)|`ip_address:port` combined (seperated new line)|304|
|[data.json](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.json)|`ip, port`|304|
|[data-with-geolocation.json](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data-with-geolocation.json)|`ip, port, geolocation`|304|

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
|[proxyscrape.com](https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all)|487|✅|
|[github.com/clarketm/proxy-list](https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt)|400|✅|
|[github.com/monosans/proxy-list](https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt)|263|✅|
|[github.com/TheSpeedX/PROXY-List](https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt)|2016|✅|


## Sample Proxies With Geolocation Info

|#|Ip|Port|Country|City|Internet Service Provider|
|-|--|----|-------|----|-------------------------|
|1|65.51.178.93|3128|United States|Weehawken|Cablevision Systems Corp.|
|2|20.47.108.204|8888|United States|Boydton|Microsoft Corporation|
|3|20.47.108.204|8888|United States|Boydton|Microsoft Corporation|
|4|85.25.242.142|5566|France|Strasbourg|Host Europe GmbH|
|5|14.139.184.130|3128|India|Manantoddy|National Knowledge Network|
|6|117.20.216.218|8080|South Korea|Gumi|HYUNDAI COMMUNICATIONS & NETWORK|
|7|194.233.69.90|443|Singapore|Singapore|Contabo Asia Private Limited|
|8|157.245.222.183|80|United States|Clifton|DigitalOcean, LLC|
|9|85.25.226.242|5566|France|Strasbourg|Host Europe GmbH|
|10|103.145.142.54|80|Indonesia|Tamiajeng|PT. Indonesia Comnets Plus|
|11|85.198.142.186|8081|Ukraine|Dnipro|Apex NCC|
|12|91.217.42.3|8080|Russia|Chelyabinsk|Uralskie Kabelnye Seti Ltd. Verkhny Ufaley|
|13|85.25.139.22|5566|France|Strasbourg|Host Europe GmbH|
|14|222.127.90.179|8080|Philippines|Makati City|INNOVE|
|15|103.47.67.154|8080|India|Delhi|Zapbytes Technologies Pvt. Ltd|
|16|85.25.208.212|5566|France|Strasbourg|Host Europe GmbH|
|17|103.156.17.63|8181|Indonesia|Indramayu|RSTNET|
|18|196.251.12.129|8080|South Africa|Cape Town|HERO TELECOMS (PTY) LTD|
|19|119.235.17.105|55443|Indonesia|Jakarta|PT Inet Global Indo|
|20|45.65.132.149|8080|Brazil|Carlos Chagas|Aspeednet Telecom ME|



## Contributing

Contributions are welcome, and they are greatly appreciated! Every
little bit helps, and credit will always be given.

