
# Free HTTP Proxy List 🌍

[![Hourly Update](https://github.com/mertguvencli/http-proxy-list/actions/workflows/main.yml/badge.svg?branch=main)](https://github.com/mertguvencli/http-proxy-list/actions/workflows/main.yml)
![GitHub](https://img.shields.io/github/license/mertguvencli/http-proxy-list)
![GitHub last commit](https://img.shields.io/github/last-commit/mertguvencli/http-proxy-list)

It is a lightweight project that hourly scrapes lots of free-proxy sites, validates if it works, and serves a clean proxy list.


> Scraper found **3730** proxies at the latest update. Usable proxies are below.

## Usage

Click the file format that you want and copy the URL.


|File|Content|Count|
|----|-------|-----|
|[data.txt](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.txt)|`ip_address:port` combined (seperated new line)|132|
|[data.json](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.json)|`ip, port`|132|
|[data-with-geolocation.json](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data-with-geolocation.json)|`ip, port, geolocation`|132|

## Sources

|Source|Found Proxies|Succeed|
|------|-------------|-------|
|[free-proxy-list.net](https://free-proxy-list.net)|300|✅|
|[us-proxy.org](https://www.us-proxy.org)|200|✅|
|[proxydb.net](http://proxydb.net)|15|✅|
|[free-proxy-list.com](https://free-proxy-list.com/?page=&port=&type%5B%5D=http&type%5B%5D=https&up_time=0&search=Search)|0|🚫|
|[proxy-list.download](https://www.proxy-list.download/HTTP)|26|✅|
|[vpnoverview.com](https://vpnoverview.com/privacy/anonymous-browsing/free-proxy-servers)|32|✅|
|[proxyscan.io](https://www.proxyscan.io)|67|✅|
|[proxylist.geonode.com](https://proxylist.geonode.com/api/proxy-list?limit=300&page=1&sort_by=lastChecked&sort_type=desc&protocols=http,https)|282|✅|
|[proxyscrape.com](https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all)|271|✅|
|[github.com/clarketm/proxy-list](https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt)|400|✅|
|[github.com/monosans/proxy-list](https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt)|179|✅|
|[github.com/TheSpeedX/PROXY-List](https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt)|1958|✅|


## Sample Proxies With Geolocation Info

|#|Ip|Port|Country|City|Internet Service Provider|
|-|--|----|-------|----|-------------------------|
|1|20.47.108.204|8888|United States|Boydton|Microsoft Corporation|
|2|47.252.4.64|8888|United States|Charlottesville|Alibaba.com LLC|
|3|136.243.37.84|9090|Germany|Falkenstein|Hetzner Online GmbH|
|4|47.252.4.64|8888|United States|Charlottesville|Alibaba.com LLC|
|5|128.199.214.87|3128|Singapore|Singapore|Partner Communications Ltd.|
|6|200.111.182.6|443|Chile|Las Condes|Entel Chile S.A.|
|7|95.216.249.203|83|Finland|Helsinki|Hetzner Online GmbH|
|8|89.223.8.10|3128|Russia|St Petersburg|United Networks Ltd.|
|9|181.196.241.198|9100|Ecuador|Guayaquil|Corporacion Nacional De Telecomunicaciones - CNT EP|
|10|183.89.115.248|8080|Thailand|Bang Lamung|Triple T Broadband Public Company Limited|
|11|177.5.161.145|80|Brazil|Penha|Brasil Telecom Comunicacao Multimidia S.A|
|12|189.63.232.244|3128|Brazil|Ribeirão Preto|Claro S.A.|
|13|81.18.51.184|8888|Serbia|Kragujevac|Orion Telekom users in Uzice|
|14|103.124.86.1|8080|India|Ranchi|Streamonn Internet Services Private Limited|
|15|103.174.115.253|80|Indonesia|Cicurug|PT Cloud Hosting Indonesia|
|16|201.174.239.18|8080|Mexico|General Escobedo|Transtelco Inc|
|17|181.114.192.1|3128|Argentina|Santa Rosa|Aguas Del Colorado Sapem|
|18|200.25.254.193|54240|Colombia|Bogotá|Andinet ON Line|
|19|103.204.119.186|8080|India|Kolhapur|Akhuratha Communications Pvt. ltd|
|20|103.78.170.13|83|India|Pune|Sanjeevan Networks Services Pvt Ltd|



## Contributing

Contributions are welcome, and they are greatly appreciated! Every
little bit helps, and credit will always be given.

