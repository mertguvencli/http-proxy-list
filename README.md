
# Free HTTP Proxy List 🌍

[![Hourly Update](https://github.com/mertguvencli/http-proxy-list/actions/workflows/main.yml/badge.svg?branch=main)](https://github.com/mertguvencli/http-proxy-list/actions/workflows/main.yml)
![GitHub](https://img.shields.io/github/license/mertguvencli/http-proxy-list)
![GitHub last commit](https://img.shields.io/github/last-commit/mertguvencli/http-proxy-list)

It is a lightweight project that hourly scrapes lots of free-proxy sites, validates if it works, and serves a clean proxy list.


> Scraper found **3900** proxies at the latest update. Usable proxies are below.

## Usage

Click the file format that you want and copy the URL.


|File|Content|Count|
|----|-------|-----|
|[data.txt](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.txt)|`ip_address:port` combined (seperated new line)|113|
|[data.json](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.json)|`ip, port`|113|
|[data-with-geolocation.json](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data-with-geolocation.json)|`ip, port, geolocation`|113|

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
|[proxyscrape.com](https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all)|395|✅|
|[github.com/clarketm/proxy-list](https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt)|400|✅|
|[github.com/monosans/proxy-list](https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt)|265|✅|
|[github.com/TheSpeedX/PROXY-List](https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt)|1883|✅|


## Sample Proxies With Geolocation Info

|#|Ip|Port|Country|City|Internet Service Provider|
|-|--|----|-------|----|-------------------------|
|1|45.152.188.246|3128|United States|Ashburn|Sprint|
|2|35.234.248.49|3128|Canada|Montreal|Google LLC|
|3|45.152.188.246|3128|United States|Ashburn|Sprint|
|4|198.41.67.18|8080|United States|Lafayette|Cox Communications Inc.|
|5|8.219.97.248|80|Singapore|Singapore|Alibaba (US) Technology Co., Ltd.|
|6|206.54.182.179|3128|Netherlands|Amsterdam|Webzilla B.V.|
|7|195.154.70.151|3128|France|Paris|Online S.A.S.|
|8|206.54.182.179|3128|Netherlands|Amsterdam|Webzilla B.V.|
|9|180.183.118.166|8080|Thailand|Bangkok|Triple T Broadband Public Company Limited|
|10|177.141.99.50|8080|Brazil|São Paulo|Claro S.A.|
|11|84.54.191.22|8080|Bulgaria|Burgas|ComNet Bulgaria Ltd.|
|12|84.54.191.22|8080|Bulgaria|Burgas|ComNet Bulgaria Ltd.|
|13|190.107.224.150|3128|Chile|Santiago|WOM S.A.|
|14|199.58.128.75|8080|United States|Kingsville|Foremost Telecommunications|
|15|210.115.46.228|3128|South Korea|Chuncheon|Kangwon National University|
|16|116.253.208.239|33080|China|Lilancun|CHINATELECOM Guangxi Nanning IDC networkdescr: Nanning, Guangxi Province, P.R.|
|17|185.76.9.87|3128|Sweden|Stockholm|DataCamp Limited|
|18|66.94.116.111|3128|United States|New York|Contabo Inc.|
|19|187.190.0.205|999|Mexico|San Luis Potosí City|Total Play Telecomunicaciones SA De CV|
|20|178.32.148.251|8080|France|Gravelines|OVH SAS|



## Contributing

Contributions are welcome, and they are greatly appreciated! Every
little bit helps, and credit will always be given.

