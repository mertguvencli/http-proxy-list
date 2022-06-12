
# Free HTTP Proxy List 🌍

[![Hourly Update](https://github.com/mertguvencli/http-proxy-list/actions/workflows/main.yml/badge.svg?branch=main)](https://github.com/mertguvencli/http-proxy-list/actions/workflows/main.yml)
![GitHub](https://img.shields.io/github/license/mertguvencli/http-proxy-list)
![GitHub last commit](https://img.shields.io/github/last-commit/mertguvencli/http-proxy-list)

It is a lightweight project that hourly scrapes lots of free-proxy sites, validates if it works, and serves a clean proxy list.


> Scraper found **3400** proxies at the latest update. Usable proxies are below.

## Usage

Click the file format that you want and copy the URL.


|File|Content|Count|
|----|-------|-----|
|[data.txt](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.txt)|`ip_address:port` combined (seperated new line)|61|
|[data.json](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.json)|`ip, port`|61|
|[data-with-geolocation.json](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data-with-geolocation.json)|`ip, port, geolocation`|61|

## Sources

|Source|Found Proxies|Succeed|
|------|-------------|-------|
|[free-proxy-list.net](https://free-proxy-list.net)|300|✅|
|[us-proxy.org](https://www.us-proxy.org)|200|✅|
|[proxydb.net](http://proxydb.net)|15|✅|
|[free-proxy-list.com](https://free-proxy-list.com/?page=&port=&type%5B%5D=http&type%5B%5D=https&up_time=0&search=Search)|10|✅|
|[proxy-list.download](https://www.proxy-list.download/HTTP)|26|✅|
|[vpnoverview.com](https://vpnoverview.com/privacy/anonymous-browsing/free-proxy-servers)|32|✅|
|[proxyscan.io](https://www.proxyscan.io)|63|✅|
|[proxylist.geonode.com](https://proxylist.geonode.com/api/proxy-list?limit=300&page=1&sort_by=lastChecked&sort_type=desc&protocols=http,https)|300|✅|
|[proxyscrape.com](https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all)|165|✅|
|[github.com/clarketm/proxy-list](https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt)|400|✅|
|[github.com/monosans/proxy-list](https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt)|56|✅|
|[github.com/TheSpeedX/PROXY-List](https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt)|1833|✅|


## Sample Proxies With Geolocation Info

|#|Ip|Port|Country|City|Internet Service Provider|
|-|--|----|-------|----|-------------------------|
|1|159.197.250.134|3128|United States|Mount Prospect|Sprint|
|2|20.47.108.204|8888|United States|Boydton|Microsoft Corporation|
|3|159.197.250.134|3128|United States|Mount Prospect|Sprint|
|4|20.47.108.204|8888|United States|Boydton|Microsoft Corporation|
|5|157.100.12.138|999|Ecuador|Quito|Telconet S.A|
|6|178.238.236.233|3128|Germany|Munich|Contabo GmbH|
|7|110.170.126.13|3128|Thailand|Din Daeng|True Internet Corporation CO. Ltd.|
|8|182.52.83.197|8080|Thailand|Satun|TOT Public Company Limited|
|9|191.242.178.96|3128|Brazil|Lauro de Freitas|Conect Telecom|
|10|159.197.250.134|3128|United States|Mount Prospect|Sprint|
|11|201.174.239.18|8080|Mexico|General Escobedo|Transtelco Inc|
|12|45.167.124.5|9992|Colombia|Guapi|Sepcom Comunicaciones SAS|
|13|45.229.205.28|55555|Argentina|Dock Sud|Visio RED SRL|
|14|47.252.4.64|8888|United States|Charlottesville|Alibaba.com LLC|
|15|123.56.13.137|80|China|Beijing|Hangzhou Alibaba Advertising Co|
|16|106.249.44.10|3128|South Korea|Anyang-si|LG DACOM Corporation|
|17|157.100.12.138|999|Ecuador|Quito|Telconet S.A|
|18|179.70.107.119|8080|Brazil|Salvador|Telemar Norte Leste S.A.|
|19|47.89.185.178|8888|United States|Charlottesville|Alibaba.com LLC|
|20|88.255.64.88|1981|Turkey|Gaziantep|Turk Telekomunikasyon Anonim Sirketi|



## Contributing

Contributions are welcome, and they are greatly appreciated! Every
little bit helps, and credit will always be given.

