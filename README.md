
# Free HTTP Proxy List 🌍

[![Hourly Update](https://github.com/mertguvencli/http-proxy-list/actions/workflows/main.yml/badge.svg?branch=main)](https://github.com/mertguvencli/http-proxy-list/actions/workflows/main.yml)
![GitHub](https://img.shields.io/github/license/mertguvencli/http-proxy-list)
![GitHub last commit](https://img.shields.io/github/last-commit/mertguvencli/http-proxy-list)

It is a lightweight project that hourly scrapes lots of free-proxy sites, validates if it works, and serves a clean proxy list.


> Scraper found **3109** proxies at the latest update. Usable proxies are below.

## Usage

Click the file format that you want and copy the URL.


|File|Content|Count|
|----|-------|-----|
|[data.txt](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.txt)|`ip_address:port` combined (seperated new line)|83|
|[data.json](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.json)|`ip, port`|83|
|[data-with-geolocation.json](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data-with-geolocation.json)|`ip, port, geolocation`|83|

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
|[proxylist.geonode.com](https://proxylist.geonode.com/api/proxy-list?limit=300&page=1&sort_by=lastChecked&sort_type=desc&protocols=http,https)|0|🚫|
|[proxyscrape.com](https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all)|160|✅|
|[github.com/clarketm/proxy-list](https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt)|400|✅|
|[github.com/monosans/proxy-list](https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt)|153|✅|
|[github.com/TheSpeedX/PROXY-List](https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt)|1813|✅|


## Sample Proxies With Geolocation Info

|#|Ip|Port|Country|City|Internet Service Provider|
|-|--|----|-------|----|-------------------------|
|1|78.46.123.202|80|Germany|Falkenstein|Hetzner Online GmbH|
|2|144.76.241.45|7890|Germany|Falkenstein|Hetzner Online GmbH|
|3|46.53.191.60|3128|Belarus|Borovlyany|FE "ALTERNATIVNAYA ZIFROVAYA SET" Minsk|
|4|152.70.53.167|3128|Netherlands|Amsterdam|Oracle Corporation|
|5|8.219.97.248|80|Singapore|Singapore|Alibaba (US) Technology Co., Ltd.|
|6|157.100.12.138|999|Ecuador|Loja|Telconet S.A|
|7|140.227.61.156|23456|Japan|Chiyoda|NTT PC Communications, Inc.|
|8|64.189.24.250|3129|United States|Chicago|WhiteSky Communications, LLC.|
|9|181.205.20.198|999|Colombia|Medellín|EPM Telecomunicaciones S.A. E.S.P.|
|10|8.219.97.248|80|Singapore|Singapore|Alibaba (US) Technology Co., Ltd.|
|11|181.205.20.194|999|Colombia|Medellín|EPM Telecomunicaciones S.A. E.S.P.|
|12|157.100.12.138|999|Ecuador|Loja|Telconet S.A|
|13|204.199.174.67|999|Peru|Arequipa|Level 3 Communications, Inc.|
|14|204.199.174.69|999|Peru|Arequipa|Level 3 Communications, Inc.|
|15|200.105.215.18|33630|Bolivia|La Paz|AXS Bolivia S. A.|
|16|38.123.207.246|999|Mexico|Mexico City|Cogent Communications|
|17|157.100.53.99|999|Ecuador|Machala|Nedetel S.A.|
|18|116.253.208.239|33080|China|Liuzhou|CHINATELECOM Guangxi Nanning IDC networkdescr: Nanning, Guangxi Province, P.R.|
|19|37.53.103.6|3128|Ukraine|Kyiv|UKRTELECOM|
|20|36.67.241.26|8080|Indonesia|Jakarta|PT. Telekomunikasi Indonesia|



## Contributing

Contributions are welcome, and they are greatly appreciated! Every
little bit helps, and credit will always be given.

