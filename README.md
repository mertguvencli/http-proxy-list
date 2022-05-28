
# Free HTTP Proxy List 🌍

[![Hourly Update](https://github.com/mertguvencli/http-proxy-list/actions/workflows/main.yml/badge.svg?branch=main)](https://github.com/mertguvencli/http-proxy-list/actions/workflows/main.yml)
![GitHub](https://img.shields.io/github/license/mertguvencli/http-proxy-list)
![GitHub last commit](https://img.shields.io/github/last-commit/mertguvencli/http-proxy-list)

It is a lightweight project that hourly scrapes lots of free-proxy sites, validates if it works, and serves a clean proxy list.


> Scraper found **3487** proxies at the latest update. Usable proxies are below.

## Usage

Click the file format that you want and copy the URL.


|File|Content|Count|
|----|-------|-----|
|[data.txt](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.txt)|`ip_address:port` combined (seperated new line)|124|
|[data.json](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.json)|`ip, port`|124|
|[data-with-geolocation.json](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data-with-geolocation.json)|`ip, port, geolocation`|124|

## Sources

|Source|Found Proxies|Succeed|
|------|-------------|-------|
|[free-proxy-list.net](https://free-proxy-list.net)|300|✅|
|[us-proxy.org](https://www.us-proxy.org)|200|✅|
|[proxydb.net](http://proxydb.net)|15|✅|
|[free-proxy-list.com](https://free-proxy-list.com/?page=&port=&type%5B%5D=http&type%5B%5D=https&up_time=0&search=Search)|0|🚫|
|[proxy-list.download](https://www.proxy-list.download/HTTP)|26|✅|
|[vpnoverview.com](https://vpnoverview.com/privacy/anonymous-browsing/free-proxy-servers)|32|✅|
|[proxyscan.io](https://www.proxyscan.io)|0|🚫|
|[proxylist.geonode.com](https://proxylist.geonode.com/api/proxy-list?limit=300&page=1&sort_by=lastChecked&sort_type=desc&protocols=http,https)|246|✅|
|[proxyscrape.com](https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all)|252|✅|
|[github.com/clarketm/proxy-list](https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt)|400|✅|
|[github.com/monosans/proxy-list](https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt)|185|✅|
|[github.com/TheSpeedX/PROXY-List](https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt)|1831|✅|


## Sample Proxies With Geolocation Info

|#|Ip|Port|Country|City|Internet Service Provider|
|-|--|----|-------|----|-------------------------|
|1|20.47.108.204|8888|United States|Boydton|Microsoft Corporation|
|2|46.243.220.71|3128|Russia|Moscow|Hostkey B.V.|
|3|168.138.203.206|8080|Japan|Tokyo|Oracle Corporation|
|4|182.52.83.69|8080|Thailand|Bangkok|TOT Public Company Limited|
|5|173.165.102.210|8080|United States|Park Ridge|Comcast Cable Communications|
|6|80.91.125.119|8089|Albania|Tirana|Abissnet ISP|
|7|135.148.15.113|3175|United States|Fremont|OVH US LLC|
|8|183.89.190.241|8080|Thailand|Chiang Mai|Triple T Broadband Public Company Limited|
|9|14.207.17.220|8080|Thailand|Samut Prakan|Triple T Broadband Public Company Limited|
|10|47.241.165.133|443|Singapore|Singapore|Alibaba.com LLC|
|11|186.3.9.218|999|Ecuador|Loja|Telconet S.A|
|12|147.75.68.201|80|United States|Sunnyvale|Packet Host, Inc.|
|13|200.25.254.193|54240|Colombia|Bogotá|Andinet ON Line|
|14|75.106.98.189|8080|United States|New York|ViaSat, Inc.|
|15|181.176.161.39|999|Peru|Huaraz|VIETTEL PERÚ S.A.C.|
|16|75.106.98.189|8080|United States|New York|ViaSat, Inc.|
|17|96.9.87.113|8080|Cambodia|Phnom Penh|SIGROUPS|
|18|187.109.120.190|38653|Brazil|Juiz de Fora|Avelino e Rodrigues LTDA|
|19|114.4.104.254|3128|Indonesia|Jakarta|PT. INDOSAT Tbk|
|20|103.240.161.98|9812|India|Patan|GTPLJAYSANTOSHIMANETWORKPVTLTD|



## Contributing

Contributions are welcome, and they are greatly appreciated! Every
little bit helps, and credit will always be given.

