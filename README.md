
# Free HTTP Proxy List 🌍

[![Hourly Update](https://github.com/mertguvencli/http-proxy-list/actions/workflows/main.yml/badge.svg?branch=main)](https://github.com/mertguvencli/http-proxy-list/actions/workflows/main.yml)
![GitHub](https://img.shields.io/github/license/mertguvencli/http-proxy-list)
![GitHub last commit](https://img.shields.io/github/last-commit/mertguvencli/http-proxy-list)

It is a lightweight project that hourly scrapes lots of free-proxy sites, validates if it works, and serves a clean proxy list.


> Scraper found **3970** proxies at the latest update. Usable proxies are below.

## Usage

Click the file format that you want and copy the URL.


|File|Content|Count|
|----|-------|-----|
|[data.txt](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.txt)|`ip_address:port` combined (seperated new line)|218|
|[data.json](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.json)|`ip, port`|218|
|[data-with-geolocation.json](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data-with-geolocation.json)|`ip, port, geolocation`|218|

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
|[proxylist.geonode.com](https://proxylist.geonode.com/api/proxy-list?limit=300&page=1&sort_by=lastChecked&sort_type=desc&protocols=http,https)|300|✅|
|[proxyscrape.com](https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all)|351|✅|
|[github.com/clarketm/proxy-list](https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt)|400|✅|
|[github.com/monosans/proxy-list](https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt)|254|✅|
|[github.com/TheSpeedX/PROXY-List](https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt)|2025|✅|


## Sample Proxies With Geolocation Info

|#|Ip|Port|Country|City|Internet Service Provider|
|-|--|----|-------|----|-------------------------|
|1|136.243.37.84|9090|Germany|Falkenstein|Hetzner Online GmbH|
|2|95.165.164.51|8080|Russia|Moscow|Moscow Local Telephone Network (OAO MGTS)|
|3|47.91.24.231|80|Japan|Tokyo|Alibaba.com LLC|
|4|47.91.25.174|80|Japan|Tokyo|Alibaba.com LLC|
|5|209.190.32.28|3128|United States|Columbus|eNET Inc|
|6|47.91.25.94|80|Japan|Tokyo|Alibaba.com LLC|
|7|121.254.195.12|8080|South Korea|Yongsan-dong|LG DACOM Corporation|
|8|51.161.51.194|9090|Colombia|Bogotá|OVH Hosting|
|9|177.55.207.38|8080|Brazil|Campos dos Goytacazes|Sumicity Telecomunicacoes S.A.|
|10|131.72.69.150|40033|Brazil|Capela|TOP NET SERVIÔOS LTDA|
|11|51.161.51.196|9090|Colombia|Bogotá|OVH Hosting|
|12|46.4.35.210|9099|Germany|Falkenstein|Hetzner Online GmbH|
|13|5.167.141.239|3128|Russia|Tula|CJSC "ER-Telecom Holding" Tula branch|
|14|209.190.32.28|3128|United States|Columbus|eNET Inc|
|15|47.245.53.132|80|Japan|Tokyo|Alibaba.com LLC|
|16|158.255.215.50|16993|France|Paris|Edis France|
|17|202.57.2.19|8080|Indonesia|South Tangerang|Primanet - ISP|
|18|121.156.109.108|8080|South Korea|Seongnam-si|Korea Telecom|
|19|176.56.107.198|47855|Spain|Elche|Aire Networks|
|20|181.224.204.22|22800|Dominican Republic|Santiago de los Caballeros|BW TELECOM|



## Contributing

Contributions are welcome, and they are greatly appreciated! Every
little bit helps, and credit will always be given.

