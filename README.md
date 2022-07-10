
# Free HTTP Proxy List 🌍

[![Hourly Update](https://github.com/mertguvencli/http-proxy-list/actions/workflows/main.yml/badge.svg?branch=main)](https://github.com/mertguvencli/http-proxy-list/actions/workflows/main.yml)
![GitHub](https://img.shields.io/github/license/mertguvencli/http-proxy-list)
![GitHub last commit](https://img.shields.io/github/last-commit/mertguvencli/http-proxy-list)

It is a lightweight project that hourly scrapes lots of free-proxy sites, validates if it works, and serves a clean proxy list.


> Scraper found **3963** proxies at the latest update. Usable proxies are below.

## Usage

Click the file format that you want and copy the URL.


|File|Content|Count|
|----|-------|-----|
|[data.txt](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.txt)|`ip_address:port` combined (seperated new line)|365|
|[data.json](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.json)|`ip, port`|365|
|[data-with-geolocation.json](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data-with-geolocation.json)|`ip, port, geolocation`|365|

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
|[proxyscrape.com](https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all)|397|✅|
|[github.com/clarketm/proxy-list](https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt)|400|✅|
|[github.com/monosans/proxy-list](https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt)|289|✅|
|[github.com/TheSpeedX/PROXY-List](https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt)|1920|✅|


## Sample Proxies With Geolocation Info

|#|Ip|Port|Country|City|Internet Service Provider|
|-|--|----|-------|----|-------------------------|
|1|45.152.188.246|3128|United States|Ashburn|Sprint|
|2|20.81.62.32|3128|United States|Boydton|Microsoft Corporation|
|3|45.152.188.246|3128|United States|Ashburn|Sprint|
|4|64.189.24.250|3129|United States|Chicago|WhiteSky Communications, LLC.|
|5|178.32.148.251|8080|France|Gravelines|OVH SAS|
|6|162.214.193.59|3128|United States|Provo|Unified Layer|
|7|66.196.238.178|3128|United States|Cypress|Logix|
|8|20.81.62.32|3128|United States|Boydton|Microsoft Corporation|
|9|51.250.80.131|80|Russia|Moscow|Yandex.Cloud LLC|
|10|185.76.9.87|3128|Sweden|Stockholm|DataCamp Limited|
|11|64.189.24.250|3129|United States|Chicago|WhiteSky Communications, LLC.|
|12|185.76.9.123|3128|Sweden|Stockholm|DataCamp Limited|
|13|157.100.12.138|999|Ecuador|Loja|Telconet S.A|
|14|179.51.162.8|9812|Peru|Íllimo|Telecable Central Network Sociedad Anonima Cerrada|
|15|185.157.161.85|8118|Sweden|Stockholm|OVPN|
|16|66.94.116.111|3128|United States|New York|Contabo Inc.|
|17|163.47.11.211|12358|Singapore|Singapore|DigitalOcean|
|18|181.10.117.254|999|Argentina|La Cocha|Telecom Argentina S.A.|
|19|157.185.163.54|59394|United States|Monrovia|Quantil Networks Inc|
|20|103.252.1.137|3128|Vietnam|Hanoi|CMCMIENBAC|



## Contributing

Contributions are welcome, and they are greatly appreciated! Every
little bit helps, and credit will always be given.

