
# Free HTTP Proxy List 🌍

[![Hourly Update](https://github.com/mertguvencli/http-proxy-list/actions/workflows/main.yml/badge.svg?branch=main)](https://github.com/mertguvencli/http-proxy-list/actions/workflows/main.yml)
![GitHub](https://img.shields.io/github/license/mertguvencli/http-proxy-list)
![GitHub last commit](https://img.shields.io/github/last-commit/mertguvencli/http-proxy-list)

It is a lightweight project that hourly scrapes lots of free-proxy sites, validates if it works, and serves a clean proxy list.


> Scraper found **3324** proxies at the latest update. Usable proxies are below.

## Usage

Click the file format that you want and copy the URL.


|File|Content|Count|
|----|-------|-----|
|[data.txt](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.txt)|`ip_address:port` combined (seperated new line)|119|
|[data.json](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.json)|`ip, port`|119|
|[data-with-geolocation.json](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data-with-geolocation.json)|`ip, port, geolocation`|119|

## Sources

|Source|Found Proxies|Succeed|
|------|-------------|-------|
|[free-proxy-list.net](https://free-proxy-list.net)|300|✅|
|[us-proxy.org](https://www.us-proxy.org)|200|✅|
|[proxydb.net](http://proxydb.net)|15|✅|
|[free-proxy-list.com](https://free-proxy-list.com/?page=&port=&type%5B%5D=http&type%5B%5D=https&up_time=0&search=Search)|10|✅|
|[proxy-list.download](https://www.proxy-list.download/HTTP)|26|✅|
|[vpnoverview.com](https://vpnoverview.com/privacy/anonymous-browsing/free-proxy-servers)|32|✅|
|[proxyscan.io](https://www.proxyscan.io)|99|✅|
|[proxylist.geonode.com](https://proxylist.geonode.com/api/proxy-list?limit=300&page=1&sort_by=lastChecked&sort_type=desc&protocols=http,https)|0|🚫|
|[proxyscrape.com](https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all)|250|✅|
|[github.com/clarketm/proxy-list](https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt)|400|✅|
|[github.com/monosans/proxy-list](https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt)|156|✅|
|[github.com/TheSpeedX/PROXY-List](https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt)|1836|✅|


## Sample Proxies With Geolocation Info

|#|Ip|Port|Country|City|Internet Service Provider|
|-|--|----|-------|----|-------------------------|
|1|5.161.105.105|80|United States|Ashburn|Hetzner Online GmbH|
|2|35.230.142.201|8080|United Kingdom|London|Google LLC|
|3|20.47.108.204|8888|United States|Boydton|Microsoft Corporation|
|4|5.161.105.105|80|United States|Ashburn|Hetzner Online GmbH|
|5|51.250.80.131|80|Russia|Moscow|Yandex.Cloud LLC|
|6|144.202.61.154|8888|United States|Elk Grove Village|The Constant Company|
|7|172.105.53.88|3128|India|Mumbai|Linode, LLC|
|8|103.154.230.118|5678|Indonesia|Sukorejo|DIGITNET|
|9|185.88.158.34|3128|Russia|St Petersburg|LLC Country Online|
|10|187.188.147.170|999|Mexico|San Luis Potosí City|Total Play Telecomunicaciones SA De CV|
|11|157.100.12.138|999|Ecuador|Loja|Telconet S.A|
|12|204.199.174.67|999|Peru|Arequipa|Level 3 Communications, Inc.|
|13|204.199.174.69|999|Peru|Arequipa|Level 3 Communications, Inc.|
|14|147.139.138.14|3128|Indonesia|Jakarta|Alibaba.com LLC|
|15|173.212.245.135|3128|Germany|Nuremberg|Contabo GmbH|
|16|144.202.61.154|8888|United States|Elk Grove Village|The Constant Company|
|17|46.53.191.60|3128|Belarus|Borovlyany|FE "ALTERNATIVNAYA ZIFROVAYA SET" Minsk|
|18|102.68.128.219|8080|Libya|Tripoli|Aljeel Aljadeed For Technology|
|19|200.29.108.225|8080|Colombia|Santiago de Cali|Empresas Municipales De Cali E.i.c.e. E.S.P.|
|20|38.130.249.137|999|United States|Dallas|Cogent Communications|



## Contributing

Contributions are welcome, and they are greatly appreciated! Every
little bit helps, and credit will always be given.

