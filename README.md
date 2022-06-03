
# Free HTTP Proxy List 🌍

[![Hourly Update](https://github.com/mertguvencli/http-proxy-list/actions/workflows/main.yml/badge.svg?branch=main)](https://github.com/mertguvencli/http-proxy-list/actions/workflows/main.yml)
![GitHub](https://img.shields.io/github/license/mertguvencli/http-proxy-list)
![GitHub last commit](https://img.shields.io/github/last-commit/mertguvencli/http-proxy-list)

It is a lightweight project that hourly scrapes lots of free-proxy sites, validates if it works, and serves a clean proxy list.


> Scraper found **3850** proxies at the latest update. Usable proxies are below.

## Usage

Click the file format that you want and copy the URL.


|File|Content|Count|
|----|-------|-----|
|[data.txt](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.txt)|`ip_address:port` combined (seperated new line)|259|
|[data.json](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.json)|`ip, port`|259|
|[data-with-geolocation.json](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data-with-geolocation.json)|`ip, port, geolocation`|259|

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
|[proxyscrape.com](https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all)|430|✅|
|[github.com/clarketm/proxy-list](https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt)|400|✅|
|[github.com/monosans/proxy-list](https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt)|198|✅|
|[github.com/TheSpeedX/PROXY-List](https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt)|1939|✅|


## Sample Proxies With Geolocation Info

|#|Ip|Port|Country|City|Internet Service Provider|
|-|--|----|-------|----|-------------------------|
|1|3.128.120.252|80|United States|Dublin|Amazon.com, Inc.|
|2|52.45.107.168|80|United States|Ashburn|Amazon.com, Inc.|
|3|54.193.249.144|8080|United States|San Jose|Amazon.com, Inc.|
|4|20.47.108.204|8888|United States|Boydton|Microsoft Corporation|
|5|5.196.124.204|80|France|Bordeaux|OVH SAS|
|6|209.80.129.2|3129|United States|Medford|HopOne Internet Corporation|
|7|3.128.120.252|80|United States|Dublin|Amazon.com, Inc.|
|8|173.82.188.82|9090|United States|Santa Clarita|Multacom Corporation|
|9|129.226.182.140|8888|Hong Kong|Central|Tencent Cloud Computing (Beijing) Co|
|10|189.203.212.101|9812|Mexico|Yauhquemehcan|Total Play Telecomunicaciones SA De CV|
|11|173.82.188.82|9090|United States|Santa Clarita|Multacom Corporation|
|12|43.156.70.173|8001|Singapore|Singapore|Shenzhen Tencent Computer Systems Company Limited|
|13|209.80.129.2|3129|United States|Medford|HopOne Internet Corporation|
|14|190.61.61.70|8080|Colombia|Buriticá|Ufinet Panama S.A.|
|15|54.193.249.144|8080|United States|San Jose|Amazon.com, Inc.|
|16|182.52.83.116|8080|Thailand|Bangkok|TOT Public Company Limited|
|17|115.96.208.124|8080|India|Kalyan|Hathway IP over Cable Internet Access|
|18|49.48.111.238|8080|Thailand|Ban Kho|Triple T Broadband Public Company Limited|
|19|103.102.14.150|3125|Indonesia|Gombong|GLOBALMEDIANET|
|20|85.25.91.141|15333|Germany|Cologne|PlusServer GmbH|



## Contributing

Contributions are welcome, and they are greatly appreciated! Every
little bit helps, and credit will always be given.

