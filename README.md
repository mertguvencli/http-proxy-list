
# Free HTTP Proxy List 🌍

[![Hourly Update](https://github.com/mertguvencli/http-proxy-list/actions/workflows/main.yml/badge.svg?branch=main)](https://github.com/mertguvencli/http-proxy-list/actions/workflows/main.yml)
![GitHub](https://img.shields.io/github/license/mertguvencli/http-proxy-list)
![GitHub last commit](https://img.shields.io/github/last-commit/mertguvencli/http-proxy-list)

It is a lightweight project that hourly scrapes lots of free-proxy sites, validates if it works, and serves a clean proxy list.


> Scraper found **3836** proxies at the latest update. Usable proxies are below.

## Usage

Click the file format that you want and copy the URL.


|File|Content|Count|
|----|-------|-----|
|[data.txt](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.txt)|`ip_address:port` combined (seperated new line)|215|
|[data.json](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.json)|`ip, port`|215|
|[data-with-geolocation.json](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data-with-geolocation.json)|`ip, port, geolocation`|215|

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
|[proxyscrape.com](https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all)|364|✅|
|[github.com/clarketm/proxy-list](https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt)|400|✅|
|[github.com/monosans/proxy-list](https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt)|176|✅|
|[github.com/TheSpeedX/PROXY-List](https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt)|1913|✅|


## Sample Proxies With Geolocation Info

|#|Ip|Port|Country|City|Internet Service Provider|
|-|--|----|-------|----|-------------------------|
|1|34.145.226.144|8080|United States|Washington|Google LLC|
|2|5.161.62.31|3128|United States|Ashburn|Hetzner Online GmbH|
|3|104.200.18.76|3128|United States|Richardson|Linode, LLC|
|4|199.241.139.193|8001|United States|Los Angeles|HIVELOCITY, Inc.|
|5|104.200.18.76|3128|United States|Richardson|Linode, LLC|
|6|187.190.0.233|999|Mexico|San Luis Potosí City|Total Play Telecomunicaciones SA De CV|
|7|195.4.156.172|8080|Germany|Huellhorst|WORTMANN AG|
|8|34.145.226.144|8080|United States|Washington|Google LLC|
|9|45.167.125.42|999|Colombia|Popayán|Sepcom Comunicaciones SAS|
|10|5.161.62.31|3128|United States|Ashburn|Hetzner Online GmbH|
|11|160.16.72.10|3180|Japan|Tokyo|SAKURA Internet Inc.|
|12|45.225.106.107|999|Ecuador|Vinces|Nedetel S.A.|
|13|198.167.196.118|8118|Sweden|Stockholm|ab stract|
|14|151.80.129.26|3127|France|Roubaix|OVH SAS|
|15|200.69.93.166|999|Colombia|Pamplona|TV AZTECA SUCURSAL COLOMBIA|
|16|138.199.15.141|8080|France|Marseille|DataCamp Limited|
|17|172.94.111.29|8118|Germany|Frankfurt am Main|VOXILITY-DE|
|18|189.157.106.116|999|Mexico|Soledad de Graciano Sanchez|Uninet S.A. de C.V|
|19|159.223.37.189|83|Singapore|Singapore|DigitalOcean, LLC|
|20|191.55.57.35|8080|Brazil|Uberlândia|ALGAR TELECOM S/A|



## Contributing

Contributions are welcome, and they are greatly appreciated! Every
little bit helps, and credit will always be given.

