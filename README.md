
# Free HTTP Proxy List 🌍

[![Hourly Update](https://github.com/mertguvencli/http-proxy-list/actions/workflows/main.yml/badge.svg?branch=main)](https://github.com/mertguvencli/http-proxy-list/actions/workflows/main.yml)
![GitHub](https://img.shields.io/github/license/mertguvencli/http-proxy-list)
![GitHub last commit](https://img.shields.io/github/last-commit/mertguvencli/http-proxy-list)

It is a lightweight project that hourly scrapes lots of free-proxy sites, validates if it works, and serves a clean proxy list.


> Scraper found **3728** proxies at the latest update. Usable proxies are below.

## Usage

Click the file format that you want and copy the URL.


|File|Content|Count|
|----|-------|-----|
|[data.txt](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.txt)|`ip_address:port` combined (seperated new line)|278|
|[data.json](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.json)|`ip, port`|278|
|[data-with-geolocation.json](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data-with-geolocation.json)|`ip, port, geolocation`|278|

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
|[proxyscrape.com](https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all)|429|✅|
|[github.com/clarketm/proxy-list](https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt)|400|✅|
|[github.com/monosans/proxy-list](https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt)|155|✅|
|[github.com/TheSpeedX/PROXY-List](https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt)|1861|✅|


## Sample Proxies With Geolocation Info

|#|Ip|Port|Country|City|Internet Service Provider|
|-|--|----|-------|----|-------------------------|
|1|3.128.120.252|80|United States|Dublin|Amazon.com, Inc.|
|2|43.130.47.100|8081|United States|Santa Clara|Shenzhen Tencent Computer Systems Company Limited|
|3|54.93.165.96|39593|Germany|Frankfurt am Main|Amazon Technologies Inc.|
|4|18.196.224.91|36776|Germany|Frankfurt am Main|Amazon Technologies Inc.|
|5|35.157.249.83|39593|Germany|Frankfurt am Main|Amazon Technologies Inc.|
|6|3.128.120.252|80|United States|Dublin|Amazon.com, Inc.|
|7|47.74.24.169|80|Japan|Tokyo|Alibaba.com LLC|
|8|45.167.125.209|9992|Colombia|Popayán|Sepcom Comunicaciones SAS|
|9|89.238.178.55|10605|Spain|Madrid|M247 Ltd|
|10|45.77.136.46|59394|Netherlands|Amsterdam|Choopa|
|11|157.100.12.138|999|Ecuador|Quito|Telconet S.A|
|12|107.191.48.64|59069|United States|Elk Grove Village|Choopa|
|13|201.77.108.225|999|Mexico|Jose Mariano Jimenez|Nidix Networks S.a. De C.V.|
|14|61.72.81.14|8080|South Korea|Seodaemun-gu|Korea Telecom|
|15|107.191.48.64|59069|United States|Elk Grove Village|Choopa|
|16|103.50.5.236|9812|India|Faridabad|Elxire IT Solution|
|17|12.31.246.5|8080|United States|Saint Helena|AT&T Services, Inc.|
|18|47.56.69.11|8000|Hong Kong|Central|Alibaba (US) Technology Co., Ltd.|
|19|213.136.101.37|3128|Ivory Coast|Abidjan|ORANGE COTE D'IVOIRE|
|20|186.195.252.34|53281|Brazil|Rio das Pedras|Reinaldo Teodora Dutra Informatica ME|



## Contributing

Contributions are welcome, and they are greatly appreciated! Every
little bit helps, and credit will always be given.

