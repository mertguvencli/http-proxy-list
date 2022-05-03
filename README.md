
# Free HTTP Proxy List 🌍

[![Hourly Update](https://github.com/mertguvencli/http-proxy-list/actions/workflows/main.yml/badge.svg?branch=main)](https://github.com/mertguvencli/http-proxy-list/actions/workflows/main.yml)
![GitHub](https://img.shields.io/github/license/mertguvencli/http-proxy-list)
![GitHub last commit](https://img.shields.io/github/last-commit/mertguvencli/http-proxy-list)

It is a lightweight project that hourly scrapes lots of free-proxy sites, validates if it works, and serves a clean proxy list.


> Scraper found **3857** proxies at the latest update. Usable proxies are below.

## Usage

Click the file format that you want and copy the URL.


|File|Content|Count|
|----|-------|-----|
|[data.txt](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.txt)|`ip_address:port` combined (seperated new line)|172|
|[data.json](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.json)|`ip, port`|172|
|[data-with-geolocation.json](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data-with-geolocation.json)|`ip, port, geolocation`|172|

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
|[proxylist.geonode.com](https://proxylist.geonode.com/api/proxy-list?limit=300&page=1&sort_by=lastChecked&sort_type=desc&protocols=http,https)|300|✅|
|[proxyscrape.com](https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all)|417|✅|
|[github.com/clarketm/proxy-list](https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt)|400|✅|
|[github.com/monosans/proxy-list](https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt)|178|✅|
|[github.com/TheSpeedX/PROXY-List](https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt)|1879|✅|


## Sample Proxies With Geolocation Info

|#|Ip|Port|Country|City|Internet Service Provider|
|-|--|----|-------|----|-------------------------|
|1|20.47.108.204|8888|United States|Boydton|Microsoft Corporation|
|2|65.51.178.92|3128|United States|Weehawken|Cablevision Systems Corp.|
|3|216.176.32.79|3128|United Kingdom|Slough|Rackdog, LLC|
|4|20.47.108.204|8888|United States|Boydton|Microsoft Corporation|
|5|195.189.123.213|3128|Russia|Moscow|Iptp LTD|
|6|167.172.239.13|3128|United States|Clifton|DigitalOcean, LLC|
|7|47.56.69.11|8000|Hong Kong|Central|Alibaba (US) Technology Co., Ltd.|
|8|128.199.94.96|3128|Singapore|Singapore|DigitalOcean, LLC|
|9|146.196.110.246|8080|Indonesia|Surabaya|PT Maxindo Mitra Solusi|
|10|181.37.140.144|3128|Dominican Republic|Santo Domingo Este|Altice Dominicana S.A.|
|11|183.88.82.149|8080|Thailand|Bang Bon|Triple T Broadband Public Company Limited|
|12|167.114.96.27|9300|Canada|Montreal|OVH SAS|
|13|66.94.97.238|443|United States|New York|Contabo Inc.|
|14|140.227.61.156|23456|Japan|Chiyoda|NTT PC Communications, Inc.|
|15|122.102.43.50|8080|Indonesia|Jakarta|PT Hipernet Indodata|
|16|186.67.230.45|3128|Chile|Santiago|Entel Chile S.A.|
|17|5.131.243.11|8080|Russia|Moscow|Novotelecom Ltd|
|18|58.82.154.3|8080|Thailand|Watthana Nakhon|CUST-COPP-JASTEL|
|19|37.113.20.226|55443|Russia|Penza|CJSC "ER-Telecom Holding" Penza branch|
|20|36.92.111.49|9812|Indonesia|Jakarta|Telekomunikasi Indonesia|



## Contributing

Contributions are welcome, and they are greatly appreciated! Every
little bit helps, and credit will always be given.

