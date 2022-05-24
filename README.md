
# Free HTTP Proxy List 🌍

[![Hourly Update](https://github.com/mertguvencli/http-proxy-list/actions/workflows/main.yml/badge.svg?branch=main)](https://github.com/mertguvencli/http-proxy-list/actions/workflows/main.yml)
![GitHub](https://img.shields.io/github/license/mertguvencli/http-proxy-list)
![GitHub last commit](https://img.shields.io/github/last-commit/mertguvencli/http-proxy-list)

It is a lightweight project that hourly scrapes lots of free-proxy sites, validates if it works, and serves a clean proxy list.


> Scraper found **4178** proxies at the latest update. Usable proxies are below.

## Usage

Click the file format that you want and copy the URL.


|File|Content|Count|
|----|-------|-----|
|[data.txt](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.txt)|`ip_address:port` combined (seperated new line)|377|
|[data.json](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.json)|`ip, port`|377|
|[data-with-geolocation.json](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data-with-geolocation.json)|`ip, port, geolocation`|377|

## Sources

|Source|Found Proxies|Succeed|
|------|-------------|-------|
|[free-proxy-list.net](https://free-proxy-list.net)|300|✅|
|[us-proxy.org](https://www.us-proxy.org)|200|✅|
|[proxydb.net](http://proxydb.net)|15|✅|
|[free-proxy-list.com](https://free-proxy-list.com/?page=&port=&type%5B%5D=http&type%5B%5D=https&up_time=0&search=Search)|0|🚫|
|[proxy-list.download](https://www.proxy-list.download/HTTP)|26|✅|
|[vpnoverview.com](https://vpnoverview.com/privacy/anonymous-browsing/free-proxy-servers)|32|✅|
|[proxyscan.io](https://www.proxyscan.io)|89|✅|
|[proxylist.geonode.com](https://proxylist.geonode.com/api/proxy-list?limit=300&page=1&sort_by=lastChecked&sort_type=desc&protocols=http,https)|300|✅|
|[proxyscrape.com](https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all)|517|✅|
|[github.com/clarketm/proxy-list](https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt)|400|✅|
|[github.com/monosans/proxy-list](https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt)|329|✅|
|[github.com/TheSpeedX/PROXY-List](https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt)|1970|✅|


## Sample Proxies With Geolocation Info

|#|Ip|Port|Country|City|Internet Service Provider|
|-|--|----|-------|----|-------------------------|
|1|51.161.51.194|9090|Colombia|Bogotá|OVH Hosting|
|2|47.91.25.174|80|Japan|Tokyo|Alibaba.com LLC|
|3|59.124.224.205|3128|Taiwan|Bade District|Chunghwa Telecom Co., Ltd.|
|4|121.254.195.12|8080|South Korea|Yongsan-dong|LG DACOM Corporation|
|5|195.189.123.213|3128|Russia|Moscow|Iptp LTD|
|6|47.91.25.94|80|Japan|Tokyo|Alibaba.com LLC|
|7|51.161.51.196|9090|Colombia|Bogotá|OVH Hosting|
|8|209.80.129.2|3128|United States|Medford|HopOne Internet Corporation|
|9|47.245.53.132|80|Japan|Tokyo|Alibaba.com LLC|
|10|194.233.69.38|443|Singapore|Singapore|Contabo Asia Private Limited|
|11|66.94.120.161|443|United States|Seattle|Contabo Inc.|
|12|194.233.69.41|443|Singapore|Singapore|Contabo Asia Private Limited|
|13|176.57.188.32|443|Germany|Düsseldorf|Contabo GmbH|
|14|51.161.51.195|9090|Colombia|Bogotá|OVH Hosting|
|15|103.147.77.66|3125|Indonesia|Madiun|TRIDATA|
|16|194.233.73.108|443|Singapore|Singapore|Contabo Asia Private Limited|
|17|87.103.175.250|9812|Russia|Irkutsk|PJSC Rostelecom|
|18|14.161.31.192|53281|Vietnam|Ho Chi Minh City|VNPT|
|19|181.48.15.227|9991|Colombia|Santiago de Cali|Telmex Colombia S.A.|
|20|178.169.139.180|8080|Bulgaria|Byala|Bulsatcom EAD|



## Contributing

Contributions are welcome, and they are greatly appreciated! Every
little bit helps, and credit will always be given.

