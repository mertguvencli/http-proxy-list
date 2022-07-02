
# Free HTTP Proxy List 🌍

[![Hourly Update](https://github.com/mertguvencli/http-proxy-list/actions/workflows/main.yml/badge.svg?branch=main)](https://github.com/mertguvencli/http-proxy-list/actions/workflows/main.yml)
![GitHub](https://img.shields.io/github/license/mertguvencli/http-proxy-list)
![GitHub last commit](https://img.shields.io/github/last-commit/mertguvencli/http-proxy-list)

It is a lightweight project that hourly scrapes lots of free-proxy sites, validates if it works, and serves a clean proxy list.


> Scraper found **3906** proxies at the latest update. Usable proxies are below.

## Usage

Click the file format that you want and copy the URL.


|File|Content|Count|
|----|-------|-----|
|[data.txt](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.txt)|`ip_address:port` combined (seperated new line)|222|
|[data.json](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.json)|`ip, port`|222|
|[data-with-geolocation.json](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data-with-geolocation.json)|`ip, port, geolocation`|222|

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
|[proxylist.geonode.com](https://proxylist.geonode.com/api/proxy-list?limit=300&page=1&sort_by=lastChecked&sort_type=desc&protocols=http,https)|152|✅|
|[proxyscrape.com](https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all)|412|✅|
|[github.com/clarketm/proxy-list](https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt)|400|✅|
|[github.com/monosans/proxy-list](https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt)|142|✅|
|[github.com/TheSpeedX/PROXY-List](https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt)|2117|✅|


## Sample Proxies With Geolocation Info

|#|Ip|Port|Country|City|Internet Service Provider|
|-|--|----|-------|----|-------------------------|
|1|138.68.238.19|31028|United States|Santa Clara|DigitalOcean, LLC|
|2|12.231.44.251|3128|United States|Racine|AT&T Services, Inc.|
|3|45.152.188.246|3128|United States|Ashburn|Sprint|
|4|200.110.173.118|8080|Colombia|Santiago de Cali|Media Commerce Partners S.A|
|5|12.231.44.251|3128|United States|Racine|AT&T Services, Inc.|
|6|20.47.108.204|8888|United States|Boydton|Microsoft Corporation|
|7|45.152.188.246|3128|United States|Ashburn|Sprint|
|8|45.167.124.5|9992|Colombia|Guapi|Sepcom Comunicaciones SAS|
|9|110.170.126.13|3128|Thailand|Din Daeng|True Internet Corporation CO. Ltd.|
|10|203.150.113.112|8080|Thailand|Watthana|Internet Thailand Company Ltd.|
|11|201.49.84.17|92|Brazil|Sao Jose do Rio Preto|Ensite Brasil Telecomunicações Ltda - ME|
|12|138.68.238.19|31028|United States|Santa Clara|DigitalOcean, LLC|
|13|47.240.160.90|10001|Hong Kong|Central|Alibaba.com LLC|
|14|20.81.62.32|3128|United States|Boydton|Microsoft Corporation|
|15|162.215.22.173|59394|United States|Provo|Unified Layer|
|16|20.81.62.32|3128|United States|Boydton|Microsoft Corporation|
|17|154.13.5.41|59394|United States|San Jose|Zhihua Lu trading as HostHub|
|18|88.135.210.179|8080|Ukraine|Ivano-Frankivsk|Uteam LTD|
|19|45.177.108.165|999|Colombia|Bogotá|TV AZTECA SUCURSAL COLOMBIA|
|20|173.82.188.82|9090|United States|Santa Clarita|Multacom Corporation|



## Contributing

Contributions are welcome, and they are greatly appreciated! Every
little bit helps, and credit will always be given.

