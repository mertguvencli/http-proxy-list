
# Free HTTP Proxy List 🌍

[![Hourly Update](https://github.com/mertguvencli/http-proxy-list/actions/workflows/main.yml/badge.svg?branch=main)](https://github.com/mertguvencli/http-proxy-list/actions/workflows/main.yml)
![GitHub](https://img.shields.io/github/license/mertguvencli/http-proxy-list)
![GitHub last commit](https://img.shields.io/github/last-commit/mertguvencli/http-proxy-list)

It is a lightweight project that hourly scrapes lots of free-proxy sites, validates if it works, and serves a clean proxy list.


> Scraper found **3876** proxies at the latest update. Usable proxies are below.

## Usage

Click the file format that you want and copy the URL.


|File|Content|Count|
|----|-------|-----|
|[data.txt](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.txt)|`ip_address:port` combined (seperated new line)|226|
|[data.json](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.json)|`ip, port`|226|
|[data-with-geolocation.json](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data-with-geolocation.json)|`ip, port, geolocation`|226|

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
|[proxylist.geonode.com](https://proxylist.geonode.com/api/proxy-list?limit=300&page=1&sort_by=lastChecked&sort_type=desc&protocols=http,https)|300|✅|
|[proxyscrape.com](https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all)|432|✅|
|[github.com/clarketm/proxy-list](https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt)|400|✅|
|[github.com/monosans/proxy-list](https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt)|230|✅|
|[github.com/TheSpeedX/PROXY-List](https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt)|1941|✅|


## Sample Proxies With Geolocation Info

|#|Ip|Port|Country|City|Internet Service Provider|
|-|--|----|-------|----|-------------------------|
|1|51.161.51.196|9090|Colombia|Bogotá|OVH Hosting|
|2|121.254.195.12|8080|South Korea|Yongsan-dong|LG DACOM Corporation|
|3|181.78.3.157|999|Colombia|Medellín|IFX Networks Argentina S.R.L|
|4|202.43.72.203|8080|Indonesia|Kuningan Barat|PT. INTERLINK TECHNOLOGY|
|5|47.245.59.11|80|Japan|Tokyo|Alibaba.com LLC|
|6|136.243.37.84|9090|Germany|Falkenstein|Hetzner Online GmbH|
|7|51.161.51.194|9090|Colombia|Bogotá|OVH Hosting|
|8|85.234.126.107|55555|Russia|Irkutsk|LLC "Regional company Svyaztranzit"|
|9|209.250.253.162|59394|Netherlands|Amsterdam|The Constant Company|
|10|47.91.25.174|80|Japan|Tokyo|Alibaba.com LLC|
|11|47.245.58.113|80|Japan|Tokyo|Alibaba.com LLC|
|12|110.74.195.65|55443|Cambodia|Phnom Penh|EZECOM limited|
|13|45.17.249.223|8080|United States|Rockwall|AT&T Services, Inc.|
|14|47.245.54.114|80|Japan|Tokyo|Alibaba.com LLC|
|15|158.255.215.50|16993|France|Paris|Edis France|
|16|121.254.195.12|8080|South Korea|Yongsan-dong|LG DACOM Corporation|
|17|47.91.24.231|80|Japan|Tokyo|Alibaba.com LLC|
|18|51.161.51.196|9090|Colombia|Bogotá|OVH Hosting|
|19|190.120.250.219|999|Venezuela|Valencia|CORPORACION FIBEX TELECOM, C.A.|
|20|178.79.135.30|3128|United Kingdom|London|Linode, LLC|



## Contributing

Contributions are welcome, and they are greatly appreciated! Every
little bit helps, and credit will always be given.

