
# Free HTTP Proxy List 🌍

[![Hourly Update](https://github.com/mertguvencli/http-proxy-list/actions/workflows/main.yml/badge.svg?branch=main)](https://github.com/mertguvencli/http-proxy-list/actions/workflows/main.yml)
![GitHub](https://img.shields.io/github/license/mertguvencli/http-proxy-list)
![GitHub last commit](https://img.shields.io/github/last-commit/mertguvencli/http-proxy-list)

It is a lightweight project that hourly scrapes lots of free-proxy sites, validates if it works, and serves a clean proxy list.


> Scraper found **3240** proxies at the latest update. Usable proxies are below.

## Usage

Click the file format that you want and copy the URL.


|File|Content|Count|
|----|-------|-----|
|[data.txt](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.txt)|`ip_address:port` combined (seperated new line)|123|
|[data.json](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.json)|`ip, port`|123|
|[data-with-geolocation.json](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data-with-geolocation.json)|`ip, port, geolocation`|123|

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
|[proxyscrape.com](https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all)|183|✅|
|[github.com/clarketm/proxy-list](https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt)|400|✅|
|[github.com/monosans/proxy-list](https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt)|138|✅|
|[github.com/TheSpeedX/PROXY-List](https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt)|1836|✅|


## Sample Proxies With Geolocation Info

|#|Ip|Port|Country|City|Internet Service Provider|
|-|--|----|-------|----|-------------------------|
|1|20.47.108.204|8888|United States|Boydton|Microsoft Corporation|
|2|8.219.97.248|80|Singapore|Singapore|Alibaba (US) Technology Co., Ltd.|
|3|144.202.61.154|8888|United States|Elk Grove Village|The Constant Company|
|4|192.163.206.200|3128|United States|Provo|Unified Layer|
|5|103.86.159.25|80|Indonesia|Jakarta|PT Cyberindo Aditama|
|6|144.202.61.154|8888|United States|Elk Grove Village|The Constant Company|
|7|50.231.95.3|8080|United States|Marietta|Comcast Cable Communications, LLC|
|8|190.121.140.233|999|Colombia|Bogotá|Media Commerce Partners S.A|
|9|80.252.5.34|7001|Poland|Warsaw|GWNET Autonomus System|
|10|200.24.157.119|999|Ecuador|Azogues|Nedetel S.A.|
|11|5.167.141.239|3128|Russia|Tula|CJSC "ER-Telecom Holding" Tula branch|
|12|8.219.97.248|80|Singapore|Singapore|Alibaba (US) Technology Co., Ltd.|
|13|192.163.206.200|3128|United States|Provo|Unified Layer|
|14|204.199.174.69|999|Peru|Arequipa|Level 3 Communications, Inc.|
|15|204.199.174.67|999|Peru|Arequipa|Level 3 Communications, Inc.|
|16|149.5.36.113|8080|Ireland|Enniscorthy|Carnsore Broadband Limited|
|17|1.71.132.64|30003|China|Taiyuan|Chinanet|
|18|38.130.249.129|999|United States|Dallas|Cogent Communications|
|19|132.255.210.119|999|El Salvador|Santa Rosa de Lima|Conective S.a. De C.V.|
|20|59.124.224.205|3128|Taiwan|Taipei|Chunghwa Telecom Co., Ltd.|



## Contributing

Contributions are welcome, and they are greatly appreciated! Every
little bit helps, and credit will always be given.

