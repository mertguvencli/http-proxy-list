
# Free HTTP Proxy List 🌍

[![Hourly Update](https://github.com/mertguvencli/http-proxy-list/actions/workflows/main.yml/badge.svg?branch=main)](https://github.com/mertguvencli/http-proxy-list/actions/workflows/main.yml)
![GitHub](https://img.shields.io/github/license/mertguvencli/http-proxy-list)
![GitHub last commit](https://img.shields.io/github/last-commit/mertguvencli/http-proxy-list)

It is a lightweight project that hourly scrapes lots of free-proxy sites, validates if it works, and serves a clean proxy list.


> Scraper found **3894** proxies at the latest update. Usable proxies are below.

## Usage

Click the file format that you want and copy the URL.


|File|Content|Count|
|----|-------|-----|
|[data.txt](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.txt)|`ip_address:port` combined (seperated new line)|256|
|[data.json](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.json)|`ip, port`|256|
|[data-with-geolocation.json](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data-with-geolocation.json)|`ip, port, geolocation`|256|

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
|[proxyscrape.com](https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all)|298|✅|
|[github.com/clarketm/proxy-list](https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt)|400|✅|
|[github.com/monosans/proxy-list](https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt)|309|✅|
|[github.com/TheSpeedX/PROXY-List](https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt)|2004|✅|


## Sample Proxies With Geolocation Info

|#|Ip|Port|Country|City|Internet Service Provider|
|-|--|----|-------|----|-------------------------|
|1|170.39.194.16|3128|United States|Ashburn|Rackdog, LLC|
|2|5.161.105.105|80|United States|Ashburn|Hetzner Online GmbH|
|3|170.39.194.16|3128|United States|Ashburn|Rackdog, LLC|
|4|5.161.105.105|80|United States|Ashburn|Hetzner Online GmbH|
|5|64.189.24.250|3129|United States|Chicago|WhiteSky Communications, LLC.|
|6|216.238.68.96|59394|Mexico|Mexico City|The Constant Company|
|7|165.227.205.246|8081|United States|North Bergen|DigitalOcean, LLC|
|8|200.125.171.57|999|Dominican Republic|Santiago de los Caballeros|WIRELESS MULTI SERVICE VARGAS CABRERA, S. R. L|
|9|102.38.17.121|8080|Libya|Tripoli|GHA|
|10|36.67.241.26|8080|Indonesia|Jakarta|PT. Telekomunikasi Indonesia|
|11|8.219.97.248|80|Singapore|Singapore|Alibaba (US) Technology Co., Ltd.|
|12|190.95.156.166|999|Ecuador|Quito|Telconet S.A|
|13|216.238.70.136|59394|Mexico|Mexico City|The Constant Company|
|14|173.197.167.242|8080|United States|Ontario|Spectrum|
|15|138.68.238.19|31028|United States|Santa Clara|DigitalOcean, LLC|
|16|167.71.190.253|80|United States|Clifton|DigitalOcean, LLC|
|17|170.39.194.16|3128|United States|Ashburn|Rackdog, LLC|
|18|200.105.215.18|33630|Bolivia|La Paz|AXS Bolivia S. A.|
|19|95.217.72.247|3127|Finland|Helsinki|Hetzner Online GmbH|
|20|46.53.191.60|3128|Belarus|Borovlyany|FE "ALTERNATIVNAYA ZIFROVAYA SET" Minsk|



## Contributing

Contributions are welcome, and they are greatly appreciated! Every
little bit helps, and credit will always be given.

