
# Free HTTP Proxy List 🌍

[![Hourly Update](https://github.com/mertguvencli/http-proxy-list/actions/workflows/main.yml/badge.svg?branch=main)](https://github.com/mertguvencli/http-proxy-list/actions/workflows/main.yml)
![GitHub](https://img.shields.io/github/license/mertguvencli/http-proxy-list)
![GitHub last commit](https://img.shields.io/github/last-commit/mertguvencli/http-proxy-list)

It is a lightweight project that hourly scrapes lots of free-proxy sites, validates if it works, and serves a clean proxy list.


> Scraper found **3350** proxies at the latest update. Usable proxies are below.

## Usage

Click the file format that you want and copy the URL.


|File|Content|Count|
|----|-------|-----|
|[data.txt](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.txt)|`ip_address:port` combined (seperated new line)|104|
|[data.json](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.json)|`ip, port`|104|
|[data-with-geolocation.json](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data-with-geolocation.json)|`ip, port, geolocation`|104|

## Sources

|Source|Found Proxies|Succeed|
|------|-------------|-------|
|[free-proxy-list.net](https://free-proxy-list.net)|300|✅|
|[us-proxy.org](https://www.us-proxy.org)|200|✅|
|[proxydb.net](http://proxydb.net)|15|✅|
|[free-proxy-list.com](https://free-proxy-list.com/?page=&port=&type%5B%5D=http&type%5B%5D=https&up_time=0&search=Search)|10|✅|
|[proxy-list.download](https://www.proxy-list.download/HTTP)|26|✅|
|[vpnoverview.com](https://vpnoverview.com/privacy/anonymous-browsing/free-proxy-servers)|32|✅|
|[proxyscan.io](https://www.proxyscan.io)|94|✅|
|[proxylist.geonode.com](https://proxylist.geonode.com/api/proxy-list?limit=300&page=1&sort_by=lastChecked&sort_type=desc&protocols=http,https)|0|🚫|
|[proxyscrape.com](https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all)|259|✅|
|[github.com/clarketm/proxy-list](https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt)|400|✅|
|[github.com/monosans/proxy-list](https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt)|168|✅|
|[github.com/TheSpeedX/PROXY-List](https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt)|1846|✅|


## Sample Proxies With Geolocation Info

|#|Ip|Port|Country|City|Internet Service Provider|
|-|--|----|-------|----|-------------------------|
|1|158.101.98.114|3128|United States|Ashburn|Oracle Corporation|
|2|5.161.105.105|80|United States|Ashburn|Hetzner Online GmbH|
|3|20.47.108.204|8888|United States|Boydton|Microsoft Corporation|
|4|5.161.105.105|80|United States|Ashburn|Hetzner Online GmbH|
|5|158.101.98.114|3128|United States|Ashburn|Oracle Corporation|
|6|190.61.55.138|999|Colombia|Chapinero|Ufinet Panama S.A.|
|7|157.100.12.138|999|Ecuador|Loja|Telconet S.A|
|8|144.202.61.154|8888|United States|Elk Grove Village|The Constant Company|
|9|213.6.149.2|8080|Palestine|Gaza|Palestine Telecommunications Company|
|10|8.219.97.248|80|Singapore|Singapore|Alibaba (US) Technology Co., Ltd.|
|11|144.202.61.154|8888|United States|Elk Grove Village|The Constant Company|
|12|178.128.211.134|6868|Singapore|Singapore|DigitalOcean, LLC|
|13|119.110.71.161|63123|Indonesia|Bogor|Maxindo|
|14|123.56.13.137|80|China|Beijing|Hangzhou Alibaba Advertising Co|
|15|194.233.95.214|3128|Singapore|Singapore|Contabo Asia Private Limited|
|16|157.100.12.138|999|Ecuador|Loja|Telconet S.A|
|17|187.188.147.170|999|Mexico|San Luis Potosí City|Total Play Telecomunicaciones SA De CV|
|18|8.219.97.248|80|Singapore|Singapore|Alibaba (US) Technology Co., Ltd.|
|19|45.189.112.225|999|Ecuador|Milagro|Anibal Humberto Enriquez Moncayo(Comunicate)|
|20|173.212.224.134|3128|Germany|Nuremberg|Contabo GmbH|



## Contributing

Contributions are welcome, and they are greatly appreciated! Every
little bit helps, and credit will always be given.

