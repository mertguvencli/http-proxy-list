
# Free HTTP Proxy List 🌍

[![Hourly Update](https://github.com/mertguvencli/http-proxy-list/actions/workflows/main.yml/badge.svg?branch=main)](https://github.com/mertguvencli/http-proxy-list/actions/workflows/main.yml)
![GitHub](https://img.shields.io/github/license/mertguvencli/http-proxy-list)
![GitHub last commit](https://img.shields.io/github/last-commit/mertguvencli/http-proxy-list)

It is a lightweight project that hourly scrapes lots of free-proxy sites, validates if it works, and serves a clean proxy list.


> Scraper found **4014** proxies at the latest update. Usable proxies are below.

## Usage

Click the file format that you want and copy the URL.


|File|Content|Count|
|----|-------|-----|
|[data.txt](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.txt)|`ip_address:port` combined (seperated new line)|323|
|[data.json](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.json)|`ip, port`|323|
|[data-with-geolocation.json](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data-with-geolocation.json)|`ip, port, geolocation`|323|

## Sources

|Source|Found Proxies|Succeed|
|------|-------------|-------|
|[free-proxy-list.net](https://free-proxy-list.net)|300|✅|
|[us-proxy.org](https://www.us-proxy.org)|200|✅|
|[proxydb.net](http://proxydb.net)|15|✅|
|[free-proxy-list.com](https://free-proxy-list.com/?page=&port=&type%5B%5D=http&type%5B%5D=https&up_time=0&search=Search)|10|✅|
|[proxy-list.download](https://www.proxy-list.download/HTTP)|0|🚫|
|[vpnoverview.com](https://vpnoverview.com/privacy/anonymous-browsing/free-proxy-servers)|32|✅|
|[proxyscan.io](https://www.proxyscan.io)|100|✅|
|[proxylist.geonode.com](https://proxylist.geonode.com/api/proxy-list?limit=300&page=1&sort_by=lastChecked&sort_type=desc&protocols=http,https)|300|✅|
|[proxyscrape.com](https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all)|429|✅|
|[github.com/clarketm/proxy-list](https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt)|400|✅|
|[github.com/monosans/proxy-list](https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt)|343|✅|
|[github.com/TheSpeedX/PROXY-List](https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt)|1885|✅|


## Sample Proxies With Geolocation Info

|#|Ip|Port|Country|City|Internet Service Provider|
|-|--|----|-------|----|-------------------------|
|1|45.152.188.246|3128|United States|Ashburn|Sprint|
|2|20.81.62.32|3128|United States|Boydton|Microsoft Corporation|
|3|174.138.116.12|80|United States|Clifton|DigitalOcean, LLC|
|4|45.152.188.246|3128|United States|Ashburn|Sprint|
|5|178.32.148.251|8080|France|Gravelines|OVH SAS|
|6|198.41.67.18|8080|United States|Lafayette|Cox Communications Inc.|
|7|20.81.62.32|3128|United States|Boydton|Microsoft Corporation|
|8|157.185.163.54|59394|United States|Monrovia|Quantil Networks Inc|
|9|157.185.163.54|59394|United States|Monrovia|Quantil Networks Inc|
|10|51.250.80.131|80|Russia|Moscow|Yandex.Cloud LLC|
|11|110.170.126.13|3128|Thailand|Din Daeng|True Internet Corporation CO. Ltd.|
|12|103.141.108.122|9812|Indonesia|Blitar|Data Buana Nusantara|
|13|49.48.104.177|80|Thailand|Ban Kho|Triple T Broadband Public Company Limited|
|14|37.1.12.133|53281|Russia|Moscow|Rial Com JSC|
|15|85.195.104.71|80|Germany|Frankfurt am Main|Host Europe GmbH|
|16|200.105.215.18|33630|Bolivia|La Paz|AXS Bolivia S. A.|
|17|8.219.97.248|80|Singapore|Singapore|Alibaba (US) Technology Co., Ltd.|
|18|81.163.49.32|55443|Russia|Makhachkala|SUBNET05|
|19|206.189.195.74|8080|United States|North Bergen|DigitalOcean, LLC|
|20|176.192.70.58|8001|Russia|Andreyevka|Net By Net Holding LLC|



## Contributing

Contributions are welcome, and they are greatly appreciated! Every
little bit helps, and credit will always be given.

