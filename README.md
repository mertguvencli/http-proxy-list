
# Free HTTP Proxy List 🌍

[![Hourly Update](https://github.com/mertguvencli/http-proxy-list/actions/workflows/main.yml/badge.svg?branch=main)](https://github.com/mertguvencli/http-proxy-list/actions/workflows/main.yml)
![GitHub](https://img.shields.io/github/license/mertguvencli/http-proxy-list)
![GitHub last commit](https://img.shields.io/github/last-commit/mertguvencli/http-proxy-list)

It is a lightweight project that hourly scrapes lots of free-proxy sites, validates if it works, and serves a clean proxy list.


> Scraper found **3636** proxies at the latest update. Usable proxies are below.

## Usage

Click the file format that you want and copy the URL.


|File|Content|Count|
|----|-------|-----|
|[data.txt](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.txt)|`ip_address:port` combined (seperated new line)|135|
|[data.json](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.json)|`ip, port`|135|
|[data-with-geolocation.json](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data-with-geolocation.json)|`ip, port, geolocation`|135|

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
|[proxyscrape.com](https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all)|310|✅|
|[github.com/clarketm/proxy-list](https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt)|400|✅|
|[github.com/monosans/proxy-list](https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt)|149|✅|
|[github.com/TheSpeedX/PROXY-List](https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt)|1894|✅|


## Sample Proxies With Geolocation Info

|#|Ip|Port|Country|City|Internet Service Provider|
|-|--|----|-------|----|-------------------------|
|1|20.47.108.204|8888|United States|Boydton|Microsoft Corporation|
|2|121.254.195.12|8080|South Korea|Yongsan-dong|LG DACOM Corporation|
|3|51.161.51.195|9090|Colombia|Bogotá|OVH Hosting|
|4|176.29.189.195|8080|Jordan|Amman|Zain Jordan|
|5|188.156.240.240|8118|Hungary|Tiszasziget|Magyar Telekom plc.|
|6|139.0.4.34|8080|Indonesia|Cipulir|PT. First Media, Tbk|
|7|85.25.91.141|15333|Germany|Cologne|PlusServer GmbH|
|8|51.161.51.195|9090|Colombia|Bogotá|OVH Hosting|
|9|103.122.60.5|8080|India|Visakhapatnam|Vizag Broadband Communications Pvt Ltd|
|10|112.78.32.62|3127|Indonesia|Yogyakarta|PT Media Sarana Data|
|11|186.97.172.178|60080|Colombia|Medellín|Colombia Móvil|
|12|51.81.32.81|8888|United States|Reston|OVH SAS|
|13|121.254.195.12|8080|South Korea|Yongsan-dong|LG DACOM Corporation|
|14|91.250.83.200|3128|France|Strasbourg|Host Europe GmbH|
|15|78.36.198.158|80|Russia|Kaliningrad|PJSC Rostelecom|
|16|91.250.83.200|3128|France|Strasbourg|Host Europe GmbH|
|17|122.155.165.191|3128|Thailand|Ratchathewi|CAT Telecom Public Company Limited|
|18|165.0.50.110|8080|South Africa|Cape Town|RSAWEB (PTY) LTD|
|19|180.183.244.166|8080|Thailand|Bang Bon|Triple T Broadband Public Company Limited|
|20|190.107.224.150|3128|Chile|Santiago|WOM S.A.|



## Contributing

Contributions are welcome, and they are greatly appreciated! Every
little bit helps, and credit will always be given.

