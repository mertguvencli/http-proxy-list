
# Free HTTP Proxy List 🌍

[![Hourly Update](https://github.com/mertguvencli/http-proxy-list/actions/workflows/main.yml/badge.svg?branch=main)](https://github.com/mertguvencli/http-proxy-list/actions/workflows/main.yml)
![GitHub](https://img.shields.io/github/license/mertguvencli/http-proxy-list)
![GitHub last commit](https://img.shields.io/github/last-commit/mertguvencli/http-proxy-list)

It is a lightweight project that hourly scrapes lots of free-proxy sites, validates if it works, and serves a clean proxy list.


> Scraper found **4120** proxies at the latest update. Usable proxies are below.

## Usage

Click the file format that you want and copy the URL.


|File|Content|Count|
|----|-------|-----|
|[data.txt](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.txt)|`ip_address:port` combined (seperated new line)|257|
|[data.json](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.json)|`ip, port`|257|
|[data-with-geolocation.json](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data-with-geolocation.json)|`ip, port, geolocation`|257|

## Sources

|Source|Found Proxies|Succeed|
|------|-------------|-------|
|[free-proxy-list.net](https://free-proxy-list.net)|300|✅|
|[us-proxy.org](https://www.us-proxy.org)|200|✅|
|[proxydb.net](http://proxydb.net)|15|✅|
|[free-proxy-list.com](https://free-proxy-list.com/?page=&port=&type%5B%5D=http&type%5B%5D=https&up_time=0&search=Search)|0|🚫|
|[proxy-list.download](https://www.proxy-list.download/HTTP)|26|✅|
|[vpnoverview.com](https://vpnoverview.com/privacy/anonymous-browsing/free-proxy-servers)|32|✅|
|[proxyscan.io](https://www.proxyscan.io)|100|✅|
|[proxylist.geonode.com](https://proxylist.geonode.com/api/proxy-list?limit=300&page=1&sort_by=lastChecked&sort_type=desc&protocols=http,https)|300|✅|
|[proxyscrape.com](https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all)|425|✅|
|[github.com/clarketm/proxy-list](https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt)|400|✅|
|[github.com/monosans/proxy-list](https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt)|290|✅|
|[github.com/TheSpeedX/PROXY-List](https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt)|2032|✅|


## Sample Proxies With Geolocation Info

|#|Ip|Port|Country|City|Internet Service Provider|
|-|--|----|-------|----|-------------------------|
|1|3.128.120.252|80|United States|Dublin|Amazon.com, Inc.|
|2|128.199.214.87|3128|Singapore|Singapore|Partner Communications Ltd.|
|3|115.96.208.124|8080|India|Kalyan|Hathway IP over Cable Internet Access|
|4|183.88.172.222|8080|Thailand|Ban Khoi Tai|Triple T Broadband Public Company Limited|
|5|113.53.60.221|8080|Thailand|Chanthaburi|TOT Public Company Limited|
|6|190.107.31.102|999|Colombia|Puerto Tejada|Media Commerce Partners S.A|
|7|170.81.35.26|36681|Costa Rica|San José|Navegalo S.A.|
|8|45.5.68.59|999|Peru|Lima|Wi-net Telecom S.A.C.|
|9|146.196.123.211|9812|India|Srinagar|CNS Infotel Services Pvt. Ltd.|
|10|190.26.201.194|8080|Colombia|Bogotá|ETB - Colombia|
|11|152.231.25.58|8080|Colombia|El Paujil|TV AZTECA SUCURSAL COLOMBIA|
|12|176.56.107.210|32161|Spain|Elche|Aire Networks|
|13|193.138.146.67|3128|Ukraine|Kharkiv|Triolan|
|14|45.229.33.29|999|Dominican Republic|Santo Domingo Este|Gold Data C.A.|
|15|205.201.49.132|53281|United States|Dexter|BPS Networks|
|16|82.114.118.142|1256|Russia|St Petersburg|ArtCommunications Ltd.|
|17|182.253.247.179|8080|Indonesia|Jakarta|BIZNET|
|18|162.150.62.93|443|United States|Kincaid|Comcast Cable Communications, LLC|
|19|212.12.69.43|8080|Russia|Moscow|Telecommunication Center Ostankino|
|20|47.74.226.8|5001|Singapore|Singapore|Alibaba Cloud (Singapore) Private Limited|



## Contributing

Contributions are welcome, and they are greatly appreciated! Every
little bit helps, and credit will always be given.

