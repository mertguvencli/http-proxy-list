
# Free HTTP Proxy List 🌍

[![Hourly Update](https://github.com/mertguvencli/http-proxy-list/actions/workflows/main.yml/badge.svg?branch=main)](https://github.com/mertguvencli/http-proxy-list/actions/workflows/main.yml)
![GitHub](https://img.shields.io/github/license/mertguvencli/http-proxy-list)
![GitHub last commit](https://img.shields.io/github/last-commit/mertguvencli/http-proxy-list)

It is a lightweight project that hourly scrapes lots of free-proxy sites, validates if it works, and serves a clean proxy list.


> Scraper found **3572** proxies at the latest update. Usable proxies are below.

## Usage

Click the file format that you want and copy the URL.


|File|Content|Count|
|----|-------|-----|
|[data.txt](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.txt)|`ip_address:port` combined (seperated new line)|195|
|[data.json](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.json)|`ip, port`|195|
|[data-with-geolocation.json](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data-with-geolocation.json)|`ip, port, geolocation`|195|

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
|[proxyscrape.com](https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all)|233|✅|
|[github.com/clarketm/proxy-list](https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt)|400|✅|
|[github.com/monosans/proxy-list](https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt)|173|✅|
|[github.com/TheSpeedX/PROXY-List](https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt)|1883|✅|


## Sample Proxies With Geolocation Info

|#|Ip|Port|Country|City|Internet Service Provider|
|-|--|----|-------|----|-------------------------|
|1|178.32.148.251|8080|France|Gravelines|OVH SAS|
|2|8.219.97.248|80|Singapore|Singapore|Alibaba (US) Technology Co., Ltd.|
|3|138.68.238.19|31028|United States|Santa Clara|DigitalOcean, LLC|
|4|216.238.69.103|59394|Mexico|Mexico City|The Constant Company|
|5|206.189.195.74|8080|United States|North Bergen|DigitalOcean, LLC|
|6|136.243.124.244|3128|Germany|Nuremberg|Hetzner Online GmbH|
|7|47.240.40.84|8228|Hong Kong|Central|Alibaba.com LLC|
|8|113.53.60.220|8080|Thailand|Chanthaburi|TOT Public Company Limited|
|9|200.91.223.124|8080|Colombia|Barranquilla|IFX Corporation|
|10|174.138.116.12|80|United States|Clifton|DigitalOcean, LLC|
|11|206.189.195.74|8080|United States|North Bergen|DigitalOcean, LLC|
|12|91.233.111.49|1080|Ukraine|Kyiv|Helpteh L-side|
|13|64.225.8.192|80|United States|Clifton|DigitalOcean, LLC|
|14|50.246.120.125|8080|United States|Washington|Comcast Cable Communications, LLC|
|15|185.15.172.212|3128|Russia|Moscow|SafeData LLC|
|16|193.142.218.12|3128|Ukraine|Kyiv|OJSC "Bank "Kievska Rus"|
|17|200.146.77.133|80|Brazil|Curitiba|Vivo|
|18|46.53.191.60|3128|Belarus|Borovlyany|FE "ALTERNATIVNAYA ZIFROVAYA SET" Minsk|
|19|92.205.21.186|3128|France|Strasbourg|GD MASS Network|
|20|197.251.233.122|8080|Ghana|Accra|Vodafone Ghana AS International Transit|



## Contributing

Contributions are welcome, and they are greatly appreciated! Every
little bit helps, and credit will always be given.

