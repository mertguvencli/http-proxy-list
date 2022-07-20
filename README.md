
# Free HTTP Proxy List 🌍

[![Hourly Update](https://github.com/mertguvencli/http-proxy-list/actions/workflows/main.yml/badge.svg?branch=main)](https://github.com/mertguvencli/http-proxy-list/actions/workflows/main.yml)
![GitHub](https://img.shields.io/github/license/mertguvencli/http-proxy-list)
![GitHub last commit](https://img.shields.io/github/last-commit/mertguvencli/http-proxy-list)

It is a lightweight project that hourly scrapes lots of free-proxy sites, validates if it works, and serves a clean proxy list.


> Scraper found **3485** proxies at the latest update. Usable proxies are below.

## Usage

Click the file format that you want and copy the URL.


|File|Content|Count|
|----|-------|-----|
|[data.txt](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.txt)|`ip_address:port` combined (seperated new line)|168|
|[data.json](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.json)|`ip, port`|168|
|[data-with-geolocation.json](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data-with-geolocation.json)|`ip, port, geolocation`|168|

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
|[proxyscrape.com](https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all)|346|✅|
|[github.com/clarketm/proxy-list](https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt)|400|✅|
|[github.com/monosans/proxy-list](https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt)|206|✅|
|[github.com/TheSpeedX/PROXY-List](https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt)|1850|✅|


## Sample Proxies With Geolocation Info

|#|Ip|Port|Country|City|Internet Service Provider|
|-|--|----|-------|----|-------------------------|
|1|35.230.142.201|8080|United Kingdom|London|Google LLC|
|2|20.47.108.204|8888|United States|Boydton|Microsoft Corporation|
|3|193.123.104.244|3128|Brazil|Vinhedo|Oracle Corporation|
|4|51.250.80.131|80|Russia|Moscow|Yandex.Cloud LLC|
|5|8.219.97.248|80|Singapore|Singapore|Alibaba (US) Technology Co., Ltd.|
|6|186.251.64.10|8085|Brazil|Trindade|PW INFORMATICA E TECNOLOGIA LTDA|
|7|95.0.90.243|8080|Turkey|Istanbul|Turk Telekomunikasyon Anonim Sirketi|
|8|190.112.39.2|8080|Argentina|Piguee|Loop Coronel Suarez S.A.|
|9|200.105.215.18|33630|Bolivia|La Paz|AXS Bolivia S. A.|
|10|36.95.73.141|80|Indonesia|Pegangsaan Dua|PT. Telekomunikasi Indonesia|
|11|187.188.147.170|999|Mexico|San Luis Potosí City|Total Play Telecomunicaciones SA De CV|
|12|45.33.51.77|3128|United States|Fremont|Linode, LLC|
|13|14.226.30.36|8080|Vietnam|Hai Duong|VNPT|
|14|54.149.196.242|3128|United States|Portland|Amazon.com, Inc.|
|15|79.143.179.141|3128|Germany|Munich|Contabo GmbH|
|16|51.250.80.131|80|Russia|Moscow|Yandex.Cloud LLC|
|17|105.112.191.250|3128|Nigeria|Lagos|Airtel Networks Limited|
|18|51.75.5.209|32648|France|Gravelines|OVH SAS|
|19|37.186.242.183|8080|Italy|Milan|Fastweb Networks|
|20|143.0.234.206|9090|Brazil|Piracicaba|Snell Telecomunica??es Ltda. ME|



## Contributing

Contributions are welcome, and they are greatly appreciated! Every
little bit helps, and credit will always be given.

