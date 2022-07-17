
# Free HTTP Proxy List 🌍

[![Hourly Update](https://github.com/mertguvencli/http-proxy-list/actions/workflows/main.yml/badge.svg?branch=main)](https://github.com/mertguvencli/http-proxy-list/actions/workflows/main.yml)
![GitHub](https://img.shields.io/github/license/mertguvencli/http-proxy-list)
![GitHub last commit](https://img.shields.io/github/last-commit/mertguvencli/http-proxy-list)

It is a lightweight project that hourly scrapes lots of free-proxy sites, validates if it works, and serves a clean proxy list.


> Scraper found **3158** proxies at the latest update. Usable proxies are below.

## Usage

Click the file format that you want and copy the URL.


|File|Content|Count|
|----|-------|-----|
|[data.txt](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.txt)|`ip_address:port` combined (seperated new line)|200|
|[data.json](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.json)|`ip, port`|200|
|[data-with-geolocation.json](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data-with-geolocation.json)|`ip, port, geolocation`|200|

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
|[proxyscrape.com](https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all)|189|✅|
|[github.com/clarketm/proxy-list](https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt)|400|✅|
|[github.com/monosans/proxy-list](https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt)|164|✅|
|[github.com/TheSpeedX/PROXY-List](https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt)|1822|✅|


## Sample Proxies With Geolocation Info

|#|Ip|Port|Country|City|Internet Service Provider|
|-|--|----|-------|----|-------------------------|
|1|5.161.105.105|80|United States|Ashburn|Hetzner Online GmbH|
|2|216.238.82.41|59394|Mexico|Mexico City|The Constant Company|
|3|5.161.105.105|80|United States|Ashburn|Hetzner Online GmbH|
|4|64.225.8.192|80|United States|Clifton|DigitalOcean, LLC|
|5|51.250.80.131|80|Russia|Moscow|Yandex.Cloud LLC|
|6|216.238.80.50|59394|Mexico|Mexico City|The Constant Company|
|7|178.32.148.251|8080|France|Gravelines|OVH SAS|
|8|157.100.12.138|999|Ecuador|Loja|Telconet S.A|
|9|8.219.97.248|80|Singapore|Singapore|Alibaba (US) Technology Co., Ltd.|
|10|209.97.152.208|8888|United States|Clifton|DigitalOcean, LLC|
|11|204.199.174.67|999|Peru|Arequipa|Level 3 Communications, Inc.|
|12|216.238.83.123|59394|Mexico|Mexico City|The Constant Company|
|13|80.252.5.34|7001|Poland|Warsaw|GWNET Autonomus System|
|14|138.68.238.19|31028|United States|Santa Clara|DigitalOcean, LLC|
|15|5.16.1.17|8080|Russia|St Petersburg|Enforta-MSK|
|16|195.211.219.146|5555|Russia|St Petersburg|OOO "Sestroretskoe Cable Television"|
|17|170.79.235.3|999|Chile|Santiago|TNA Solutions SpA|
|18|181.57.192.245|999|Colombia|Barrancabermeja|Telmex Colombia S.A.|
|19|1.10.182.161|8080|Thailand|Ban Kaeng|TOT Public Company Limited|
|20|161.38.217.6|8080|Australia|Brisbane|Gigafy|



## Contributing

Contributions are welcome, and they are greatly appreciated! Every
little bit helps, and credit will always be given.

