
# Free HTTP Proxy List 🌍

[![Hourly Update](https://github.com/mertguvencli/http-proxy-list/actions/workflows/main.yml/badge.svg?branch=main)](https://github.com/mertguvencli/http-proxy-list/actions/workflows/main.yml)
![GitHub](https://img.shields.io/github/license/mertguvencli/http-proxy-list)
![GitHub last commit](https://img.shields.io/github/last-commit/mertguvencli/http-proxy-list)

It is a lightweight project that hourly scrapes lots of free-proxy sites, validates if it works, and serves a clean proxy list.


> Scraper found **3407** proxies at the latest update. Usable proxies are below.

## Usage

Click the file format that you want and copy the URL.


|File|Content|Count|
|----|-------|-----|
|[data.txt](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.txt)|`ip_address:port` combined (seperated new line)|141|
|[data.json](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.json)|`ip, port`|141|
|[data-with-geolocation.json](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data-with-geolocation.json)|`ip, port, geolocation`|141|

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
|[proxyscrape.com](https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all)|232|✅|
|[github.com/clarketm/proxy-list](https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt)|400|✅|
|[github.com/monosans/proxy-list](https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt)|124|✅|
|[github.com/TheSpeedX/PROXY-List](https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt)|1768|✅|


## Sample Proxies With Geolocation Info

|#|Ip|Port|Country|City|Internet Service Provider|
|-|--|----|-------|----|-------------------------|
|1|170.39.194.16|3128|United States|Ashburn|Rackdog, LLC|
|2|5.161.105.105|80|United States|Ashburn|Hetzner Online GmbH|
|3|20.47.108.204|8888|United States|Boydton|Microsoft Corporation|
|4|170.39.194.16|3128|United States|Ashburn|Rackdog, LLC|
|5|5.161.105.105|80|United States|Ashburn|Hetzner Online GmbH|
|6|51.250.80.131|80|Russia|Moscow|Yandex.Cloud LLC|
|7|198.59.191.234|8080|United States|Carlsbad|TDS TELECOM|
|8|20.47.108.204|8888|United States|Boydton|Microsoft Corporation|
|9|47.241.165.133|443|Singapore|Singapore|Alibaba.com LLC|
|10|5.161.105.105|80|United States|Ashburn|Hetzner Online GmbH|
|11|149.34.2.39|8080|Spain|Cassà de la Selva|Adamo Telecom Iberia S.A.|
|12|46.53.191.60|3128|Belarus|Borovlyany|FE "ALTERNATIVNAYA ZIFROVAYA SET" Minsk|
|13|202.21.110.82|8020|Mongolia|Ulan Bator|Mobinet LLC|
|14|51.250.80.131|80|Russia|Moscow|Yandex.Cloud LLC|
|15|8.219.97.248|80|Singapore|Singapore|Alibaba (US) Technology Co., Ltd.|
|16|187.190.0.205|999|Mexico|San Luis Potosí City|Total Play Telecomunicaciones SA De CV|
|17|45.70.15.2|8080|Ecuador|Alausi|Nedetel S.A.|
|18|59.124.224.205|3128|Taiwan|Taipei|Chunghwa Telecom Co., Ltd.|
|19|64.189.24.250|3129|United States|Chicago|WhiteSky Communications, LLC.|
|20|111.73.46.94|3128|China|Dunhou|Chinanet|



## Contributing

Contributions are welcome, and they are greatly appreciated! Every
little bit helps, and credit will always be given.

