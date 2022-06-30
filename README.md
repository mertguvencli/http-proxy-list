
# Free HTTP Proxy List 🌍

[![Hourly Update](https://github.com/mertguvencli/http-proxy-list/actions/workflows/main.yml/badge.svg?branch=main)](https://github.com/mertguvencli/http-proxy-list/actions/workflows/main.yml)
![GitHub](https://img.shields.io/github/license/mertguvencli/http-proxy-list)
![GitHub last commit](https://img.shields.io/github/last-commit/mertguvencli/http-proxy-list)

It is a lightweight project that hourly scrapes lots of free-proxy sites, validates if it works, and serves a clean proxy list.


> Scraper found **3640** proxies at the latest update. Usable proxies are below.

## Usage

Click the file format that you want and copy the URL.


|File|Content|Count|
|----|-------|-----|
|[data.txt](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.txt)|`ip_address:port` combined (seperated new line)|202|
|[data.json](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.json)|`ip, port`|202|
|[data-with-geolocation.json](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data-with-geolocation.json)|`ip, port, geolocation`|202|

## Sources

|Source|Found Proxies|Succeed|
|------|-------------|-------|
|[free-proxy-list.net](https://free-proxy-list.net)|300|✅|
|[us-proxy.org](https://www.us-proxy.org)|200|✅|
|[proxydb.net](http://proxydb.net)|15|✅|
|[free-proxy-list.com](https://free-proxy-list.com/?page=&port=&type%5B%5D=http&type%5B%5D=https&up_time=0&search=Search)|10|✅|
|[proxy-list.download](https://www.proxy-list.download/HTTP)|26|✅|
|[vpnoverview.com](https://vpnoverview.com/privacy/anonymous-browsing/free-proxy-servers)|32|✅|
|[proxyscan.io](https://www.proxyscan.io)|87|✅|
|[proxylist.geonode.com](https://proxylist.geonode.com/api/proxy-list?limit=300&page=1&sort_by=lastChecked&sort_type=desc&protocols=http,https)|229|✅|
|[proxyscrape.com](https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all)|311|✅|
|[github.com/clarketm/proxy-list](https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt)|400|✅|
|[github.com/monosans/proxy-list](https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt)|95|✅|
|[github.com/TheSpeedX/PROXY-List](https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt)|1935|✅|


## Sample Proxies With Geolocation Info

|#|Ip|Port|Country|City|Internet Service Provider|
|-|--|----|-------|----|-------------------------|
|1|20.47.108.204|8888|United States|Boydton|Microsoft Corporation|
|2|172.105.9.142|3128|Canada|Toronto|Linode, LLC|
|3|20.47.108.204|8888|United States|Boydton|Microsoft Corporation|
|4|45.167.124.5|9992|Colombia|Guapi|Sepcom Comunicaciones SAS|
|5|157.100.12.138|999|Ecuador|Loja|Telconet S.A|
|6|121.156.109.108|8080|South Korea|Seongnam-si|Korea Telecom|
|7|47.89.185.178|8888|United States|Charlottesville|Alibaba.com LLC|
|8|125.26.199.173|8080|Thailand|Khlung|TOT Public Company Limited|
|9|114.129.23.58|3128|Indonesia|Jakarta|PT Hipernet Indodata|
|10|47.88.104.22|8888|United States|San Mateo|Alibaba.com LLC|
|11|176.99.2.43|1081|Russia|Moscow|"Domain names registrar REG.RU", Ltd|
|12|131.161.44.146|8083|Brazil|Brasília|Teranet comunicacoes multimidia ltda|
|13|47.74.226.8|5001|Singapore|Singapore|Alibaba Cloud (Singapore) Private Limited|
|14|20.81.62.32|3128|United States|Boydton|Microsoft Corporation|
|15|47.240.160.90|10001|Hong Kong|Central|Alibaba.com LLC|
|16|185.221.134.234|3129|United States|Los Angeles|DediPath|
|17|20.81.62.32|3128|United States|Boydton|Microsoft Corporation|
|18|198.211.28.7|59394|United States|Santa Clarita|Multacom Corporation|
|19|200.110.168.159|8080|Colombia|Trujillo|Media Commerce Partners S.A|
|20|154.13.5.41|59394|United States|San Jose|Zhihua Lu trading as HostHub|



## Contributing

Contributions are welcome, and they are greatly appreciated! Every
little bit helps, and credit will always be given.

