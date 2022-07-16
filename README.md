
# Free HTTP Proxy List 🌍

[![Hourly Update](https://github.com/mertguvencli/http-proxy-list/actions/workflows/main.yml/badge.svg?branch=main)](https://github.com/mertguvencli/http-proxy-list/actions/workflows/main.yml)
![GitHub](https://img.shields.io/github/license/mertguvencli/http-proxy-list)
![GitHub last commit](https://img.shields.io/github/last-commit/mertguvencli/http-proxy-list)

It is a lightweight project that hourly scrapes lots of free-proxy sites, validates if it works, and serves a clean proxy list.


> Scraper found **3603** proxies at the latest update. Usable proxies are below.

## Usage

Click the file format that you want and copy the URL.


|File|Content|Count|
|----|-------|-----|
|[data.txt](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.txt)|`ip_address:port` combined (seperated new line)|218|
|[data.json](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.json)|`ip, port`|218|
|[data-with-geolocation.json](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data-with-geolocation.json)|`ip, port, geolocation`|218|

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
|[proxyscrape.com](https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all)|260|✅|
|[github.com/clarketm/proxy-list](https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt)|400|✅|
|[github.com/monosans/proxy-list](https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt)|200|✅|
|[github.com/TheSpeedX/PROXY-List](https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt)|1860|✅|


## Sample Proxies With Geolocation Info

|#|Ip|Port|Country|City|Internet Service Provider|
|-|--|----|-------|----|-------------------------|
|1|170.39.194.16|3128|United States|Ashburn|Rackdog, LLC|
|2|20.47.108.204|8888|United States|Boydton|Microsoft Corporation|
|3|198.41.67.18|8080|United States|Lafayette|Cox Communications Inc.|
|4|170.39.194.16|3128|United States|Ashburn|Rackdog, LLC|
|5|198.41.67.18|8080|United States|Lafayette|Cox Communications Inc.|
|6|78.46.123.202|80|Germany|Falkenstein|Hetzner Online GmbH|
|7|102.68.129.30|8080|Libya|Tripoli|LTT Autonomous System|
|8|216.238.80.71|59394|Mexico|Mexico City|The Constant Company|
|9|216.238.80.50|59394|Mexico|Mexico City|The Constant Company|
|10|138.68.238.19|31028|United States|Santa Clara|DigitalOcean, LLC|
|11|198.41.67.18|8080|United States|Lafayette|Cox Communications Inc.|
|12|5.161.105.105|80|United States|Ashburn|Hetzner Online GmbH|
|13|216.238.83.123|59394|Mexico|Mexico City|The Constant Company|
|14|149.34.2.39|8080|Spain|Cassà de la Selva|Adamo Telecom Iberia S.A.|
|15|95.217.72.247|3127|Finland|Helsinki|Hetzner Online GmbH|
|16|95.217.72.247|3127|Finland|Helsinki|Hetzner Online GmbH|
|17|209.166.175.201|8080|United States|Pittsburgh|CONTINENTAL BROADBAND PENNSYLVANIA, INC.|
|18|179.49.113.230|999|Honduras|Pinalejo|Asociacion De Servicio De Internet S. De RL.|
|19|167.71.199.228|8080|Singapore|Singapore|DigitalOcean, LLC|
|20|140.227.58.238|3180|Japan|Chiyoda|NTT PC Communications, Inc.|



## Contributing

Contributions are welcome, and they are greatly appreciated! Every
little bit helps, and credit will always be given.

