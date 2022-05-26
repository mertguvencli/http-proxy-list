
# Free HTTP Proxy List 🌍

[![Hourly Update](https://github.com/mertguvencli/http-proxy-list/actions/workflows/main.yml/badge.svg?branch=main)](https://github.com/mertguvencli/http-proxy-list/actions/workflows/main.yml)
![GitHub](https://img.shields.io/github/license/mertguvencli/http-proxy-list)
![GitHub last commit](https://img.shields.io/github/last-commit/mertguvencli/http-proxy-list)

It is a lightweight project that hourly scrapes lots of free-proxy sites, validates if it works, and serves a clean proxy list.


> Scraper found **3479** proxies at the latest update. Usable proxies are below.

## Usage

Click the file format that you want and copy the URL.


|File|Content|Count|
|----|-------|-----|
|[data.txt](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.txt)|`ip_address:port` combined (seperated new line)|63|
|[data.json](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.json)|`ip, port`|63|
|[data-with-geolocation.json](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data-with-geolocation.json)|`ip, port, geolocation`|63|

## Sources

|Source|Found Proxies|Succeed|
|------|-------------|-------|
|[free-proxy-list.net](https://free-proxy-list.net)|300|✅|
|[us-proxy.org](https://www.us-proxy.org)|200|✅|
|[proxydb.net](http://proxydb.net)|15|✅|
|[free-proxy-list.com](https://free-proxy-list.com/?page=&port=&type%5B%5D=http&type%5B%5D=https&up_time=0&search=Search)|0|🚫|
|[proxy-list.download](https://www.proxy-list.download/HTTP)|26|✅|
|[vpnoverview.com](https://vpnoverview.com/privacy/anonymous-browsing/free-proxy-servers)|32|✅|
|[proxyscan.io](https://www.proxyscan.io)|84|✅|
|[proxylist.geonode.com](https://proxylist.geonode.com/api/proxy-list?limit=300&page=1&sort_by=lastChecked&sort_type=desc&protocols=http,https)|229|✅|
|[proxyscrape.com](https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all)|225|✅|
|[github.com/clarketm/proxy-list](https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt)|400|✅|
|[github.com/monosans/proxy-list](https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt)|149|✅|
|[github.com/TheSpeedX/PROXY-List](https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt)|1819|✅|


## Sample Proxies With Geolocation Info

|#|Ip|Port|Country|City|Internet Service Provider|
|-|--|----|-------|----|-------------------------|
|1|43.129.187.73|2888|Hong Kong|Hong Kong|Shenzhen Tencent Computer Systems Company Limited|
|2|118.99.124.161|8080|Indonesia|Mampang Prapatan|BIZNET|
|3|45.167.126.129|9992|Colombia|Guapi|Sepcom Comunicaciones SAS|
|4|157.245.222.183|80|United States|Clifton|DigitalOcean, LLC|
|5|47.74.226.8|5001|Singapore|Singapore|Alibaba Cloud (Singapore) Private Limited|
|6|181.176.221.151|9812|Peru|San Francisco De Borja|VIETTEL PERÚ S.A.C.|
|7|41.60.237.5|8080|Kenya|Nairobi|Maintainer Liquid Telecommunications Operations Limited|
|8|122.155.165.191|3128|Thailand|Ratchathewi|CAT Telecom Public Company Limited|
|9|181.129.14.165|999|Colombia|Medellín|EPM Telecomunicaciones S.A. E.S.P.|
|10|179.189.125.222|8080|Brazil|Parnaiba|IP CARRIER BRASIL|
|11|36.66.124.193|3128|Indonesia|Lubang Buaya|PT. Telekomunikasi Indonesia|
|12|36.94.98.146|8080|Indonesia|Jakarta|PT. Telekomunikasi Indonesia|
|13|212.114.31.231|8080|France|Marseille|Jaguar Network SAS|
|14|180.180.171.123|8080|Thailand|Nakhon Pathom|TOT Public Company Limited|
|15|64.225.8.192|80|United States|Clifton|DigitalOcean, LLC|
|16|123.163.55.123|3128|China|Zhoukou|Chinanet|
|17|212.108.144.67|8080|Cyprus|Kyrenia|Lifecell Digital LTD|
|18|201.174.239.18|8080|Mexico|General Escobedo|Transtelco Inc|
|19|89.208.35.81|3128|Russia|Moscow|DINET-HOSTING|
|20|194.114.128.149|61213|Russia|Sochi|OOO "Matritsa"|



## Contributing

Contributions are welcome, and they are greatly appreciated! Every
little bit helps, and credit will always be given.

