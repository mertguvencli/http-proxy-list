
# Free HTTP Proxy List 🌍

[![Hourly Update](https://github.com/mertguvencli/http-proxy-list/actions/workflows/main.yml/badge.svg?branch=main)](https://github.com/mertguvencli/http-proxy-list/actions/workflows/main.yml)
![GitHub](https://img.shields.io/github/license/mertguvencli/http-proxy-list)
![GitHub last commit](https://img.shields.io/github/last-commit/mertguvencli/http-proxy-list)

It is a lightweight project that hourly scrapes lots of free-proxy sites, validates if it works, and serves a clean proxy list.


> Scraper found **3766** proxies at the latest update. Usable proxies are below.

## Usage

Click the file format that you want and copy the URL.


|File|Content|Count|
|----|-------|-----|
|[data.txt](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.txt)|`ip_address:port` combined (seperated new line)|161|
|[data.json](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.json)|`ip, port`|161|
|[data-with-geolocation.json](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data-with-geolocation.json)|`ip, port, geolocation`|161|

## Sources

|Source|Found Proxies|Succeed|
|------|-------------|-------|
|[free-proxy-list.net](https://free-proxy-list.net)|300|✅|
|[us-proxy.org](https://www.us-proxy.org)|200|✅|
|[proxydb.net](http://proxydb.net)|15|✅|
|[free-proxy-list.com](https://free-proxy-list.com/?page=&port=&type%5B%5D=http&type%5B%5D=https&up_time=0&search=Search)|0|🚫|
|[proxy-list.download](https://www.proxy-list.download/HTTP)|26|✅|
|[vpnoverview.com](https://vpnoverview.com/privacy/anonymous-browsing/free-proxy-servers)|32|✅|
|[proxyscan.io](https://www.proxyscan.io)|89|✅|
|[proxylist.geonode.com](https://proxylist.geonode.com/api/proxy-list?limit=300&page=1&sort_by=lastChecked&sort_type=desc&protocols=http,https)|300|✅|
|[proxyscrape.com](https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all)|299|✅|
|[github.com/clarketm/proxy-list](https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt)|400|✅|
|[github.com/monosans/proxy-list](https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt)|174|✅|
|[github.com/TheSpeedX/PROXY-List](https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt)|1931|✅|


## Sample Proxies With Geolocation Info

|#|Ip|Port|Country|City|Internet Service Provider|
|-|--|----|-------|----|-------------------------|
|1|136.243.37.84|9090|Germany|Falkenstein|Hetzner Online GmbH|
|2|3.128.120.252|80|United States|Dublin|Amazon.com, Inc.|
|3|121.254.195.12|8080|South Korea|Yongsan-dong|LG DACOM Corporation|
|4|117.20.216.218|8080|South Korea|Gumi|HYUNDAI COMMUNICATIONS & NETWORK|
|5|47.91.25.174|80|Japan|Tokyo|Alibaba.com LLC|
|6|47.245.58.113|80|Japan|Tokyo|Alibaba.com LLC|
|7|201.77.108.130|999|Mexico|Jose Mariano Jimenez|Nidix Networks S.a. De C.V.|
|8|47.245.56.201|80|Japan|Tokyo|Alibaba.com LLC|
|9|190.6.54.5|8080|Venezuela|Caracas|Net Uno|
|10|203.150.128.194|8080|Thailand|Chiang Mai|Internet Thailand Company Ltd|
|11|200.114.84.76|8080|Argentina|Lomas de Zamora|Citarella S.A.|
|12|200.106.187.252|999|Argentina|Carlos Spegazzini|Fullnet Solutions S.A.S.|
|13|47.91.25.94|80|Japan|Tokyo|Alibaba.com LLC|
|14|36.95.156.125|6969|Indonesia|Jakarta|PT. Telekomunikasi Indonesia|
|15|168.227.56.79|8080|Brazil|Votuporanga|RF connect provedor de acesso ltda-me|
|16|103.164.56.114|8080|Indonesia|Bekasi|PT Natha Buana Indonesia|
|17|116.197.134.98|8080|Indonesia|Ulujami|FIBERNET|
|18|103.124.104.139|3128|United States|Los Angeles|DediPath|
|19|159.65.133.175|31280|Singapore|Singapore|DigitalOcean, LLC|
|20|177.141.99.50|8080|Brazil|São Paulo|Claro S.A.|



## Contributing

Contributions are welcome, and they are greatly appreciated! Every
little bit helps, and credit will always be given.

