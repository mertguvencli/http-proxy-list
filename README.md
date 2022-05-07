
# Free HTTP Proxy List 🌍

[![Hourly Update](https://github.com/mertguvencli/http-proxy-list/actions/workflows/main.yml/badge.svg?branch=main)](https://github.com/mertguvencli/http-proxy-list/actions/workflows/main.yml)
![GitHub](https://img.shields.io/github/license/mertguvencli/http-proxy-list)
![GitHub last commit](https://img.shields.io/github/last-commit/mertguvencli/http-proxy-list)

It is a lightweight project that hourly scrapes lots of free-proxy sites, validates if it works, and serves a clean proxy list.


> Scraper found **3574** proxies at the latest update. Usable proxies are below.

## Usage

Click the file format that you want and copy the URL.


|File|Content|Count|
|----|-------|-----|
|[data.txt](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.txt)|`ip_address:port` combined (seperated new line)|204|
|[data.json](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.json)|`ip, port`|204|
|[data-with-geolocation.json](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data-with-geolocation.json)|`ip, port, geolocation`|204|

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
|[proxylist.geonode.com](https://proxylist.geonode.com/api/proxy-list?limit=300&page=1&sort_by=lastChecked&sort_type=desc&protocols=http,https)|0|🚫|
|[proxyscrape.com](https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all)|384|✅|
|[github.com/clarketm/proxy-list](https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt)|400|✅|
|[github.com/monosans/proxy-list](https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt)|180|✅|
|[github.com/TheSpeedX/PROXY-List](https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt)|1927|✅|


## Sample Proxies With Geolocation Info

|#|Ip|Port|Country|City|Internet Service Provider|
|-|--|----|-------|----|-------------------------|
|1|149.129.103.159|8213|Hong Kong|Central|Alibaba.com Singapore E-Commerce Private Limited|
|2|77.50.104.110|3128|Russia|Moscow|StarLink Telecom Network|
|3|190.26.201.194|8080|Colombia|Bogotá|ETB - Colombia|
|4|190.214.27.46|8080|Ecuador|Guayaquil|Corporacion Nacional De Telecomunicaciones - CNT EP|
|5|186.67.230.45|3128|Chile|Santiago|Entel Chile S.A.|
|6|186.233.186.60|8080|United States|Chicago|Maxihost LTDA|
|7|158.140.170.183|8085|Indonesia|Semarang|MYREPUBLIC|
|8|36.92.106.13|9812|Indonesia|Semarang|Telekomunikasi Indonesia|
|9|122.155.165.191|3128|Thailand|Ratchathewi|CAT Telecom Public Company Limited|
|10|186.67.230.45|3128|Chile|Santiago|Entel Chile S.A.|
|11|45.190.249.100|8080|Brazil|Passo Fundo|RK Telecom Provedor Internet LTDA|
|12|103.154.120.107|8080|Indonesia|Jakarta|MORATELINDONAP|
|13|186.96.30.153|999|Mexico|Puerto Vallarta|Total Play Telecomunicaciones SA De CV|
|14|186.67.230.45|3128|Chile|Santiago|Entel Chile S.A.|
|15|45.231.170.137|999|Mexico|Playa del Carmen|GigNet, S.A. de C.V.|
|16|154.159.246.66|8080|Kenya|Nairobi|Airtel KE Mobile & Fixed Internet|
|17|177.124.184.52|8080|Brazil|Ji Parana|R. Jose da Silva e Cia Ltda - OndaÁgil|
|18|152.231.25.58|8080|Colombia|El Paujil|Colombiatel Telecomunicaciones|
|19|89.22.17.62|61616|Russia|Moscow|Fortex Cjsc|
|20|103.154.120.107|8080|Indonesia|Jakarta|MORATELINDONAP|



## Contributing

Contributions are welcome, and they are greatly appreciated! Every
little bit helps, and credit will always be given.

