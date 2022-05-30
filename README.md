
# Free HTTP Proxy List 🌍

[![Hourly Update](https://github.com/mertguvencli/http-proxy-list/actions/workflows/main.yml/badge.svg?branch=main)](https://github.com/mertguvencli/http-proxy-list/actions/workflows/main.yml)
![GitHub](https://img.shields.io/github/license/mertguvencli/http-proxy-list)
![GitHub last commit](https://img.shields.io/github/last-commit/mertguvencli/http-proxy-list)

It is a lightweight project that hourly scrapes lots of free-proxy sites, validates if it works, and serves a clean proxy list.


> Scraper found **3940** proxies at the latest update. Usable proxies are below.

## Usage

Click the file format that you want and copy the URL.


|File|Content|Count|
|----|-------|-----|
|[data.txt](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.txt)|`ip_address:port` combined (seperated new line)|192|
|[data.json](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.json)|`ip, port`|192|
|[data-with-geolocation.json](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data-with-geolocation.json)|`ip, port, geolocation`|192|

## Sources

|Source|Found Proxies|Succeed|
|------|-------------|-------|
|[free-proxy-list.net](https://free-proxy-list.net)|300|✅|
|[us-proxy.org](https://www.us-proxy.org)|200|✅|
|[proxydb.net](http://proxydb.net)|15|✅|
|[free-proxy-list.com](https://free-proxy-list.com/?page=&port=&type%5B%5D=http&type%5B%5D=https&up_time=0&search=Search)|0|🚫|
|[proxy-list.download](https://www.proxy-list.download/HTTP)|26|✅|
|[vpnoverview.com](https://vpnoverview.com/privacy/anonymous-browsing/free-proxy-servers)|32|✅|
|[proxyscan.io](https://www.proxyscan.io)|100|✅|
|[proxylist.geonode.com](https://proxylist.geonode.com/api/proxy-list?limit=300&page=1&sort_by=lastChecked&sort_type=desc&protocols=http,https)|300|✅|
|[proxyscrape.com](https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all)|408|✅|
|[github.com/clarketm/proxy-list](https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt)|400|✅|
|[github.com/monosans/proxy-list](https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt)|254|✅|
|[github.com/TheSpeedX/PROXY-List](https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt)|1905|✅|


## Sample Proxies With Geolocation Info

|#|Ip|Port|Country|City|Internet Service Provider|
|-|--|----|-------|----|-------------------------|
|1|18.206.33.119|8888|United States|Ashburn|Amazon.com, Inc.|
|2|177.141.99.50|8080|Brazil|São Paulo|Claro S.A.|
|3|59.10.223.99|8080|South Korea|Seoul|Korea Telecom|
|4|66.94.120.161|443|United States|Seattle|Contabo Inc.|
|5|181.143.235.94|999|Colombia|Santiago de Cali|EPM Telecomunicaciones S.A. E.S.P.|
|6|85.195.104.71|80|Germany|Frankfurt am Main|Host Europe GmbH|
|7|66.94.120.161|443|United States|Seattle|Contabo Inc.|
|8|194.233.69.41|443|Singapore|Singapore|Contabo Asia Private Limited|
|9|194.143.251.17|41258|Hungary|Kalmanhaza|INVITEL Zrt.|
|10|201.91.82.155|3128|Brazil|São Paulo|Vivo|
|11|183.88.232.207|8080|Thailand|Bangkok|Triple T Broadband Public Company Limited|
|12|147.75.68.201|80|United States|Sunnyvale|Packet Host, Inc.|
|13|181.129.43.3|8080|Colombia|Medellín|EPM Telecomunicaciones S.A. E.S.P.|
|14|190.26.201.194|8080|Colombia|Bogotá|ETB - Colombia|
|15|45.167.125.209|9992|Colombia|Popayán|Sepcom Comunicaciones SAS|
|16|203.189.137.180|9812|Cambodia|Phnom Penh|ONLINE|
|17|103.105.228.134|8080|India|Mumbai|Mnk Infoway Private Limited|
|18|121.156.109.108|8080|South Korea|Seongnam-si|Korea Telecom|
|19|123.163.55.123|3128|China|Zhoukou|Chinanet|
|20|109.72.6.70|8080|Czechia|Drasov|Nej.cz s.r.o.|



## Contributing

Contributions are welcome, and they are greatly appreciated! Every
little bit helps, and credit will always be given.

