
# Free HTTP Proxy List 🌍

[![Hourly Update](https://github.com/mertguvencli/http-proxy-list/actions/workflows/main.yml/badge.svg?branch=main)](https://github.com/mertguvencli/http-proxy-list/actions/workflows/main.yml)
![GitHub](https://img.shields.io/github/license/mertguvencli/http-proxy-list)
![GitHub last commit](https://img.shields.io/github/last-commit/mertguvencli/http-proxy-list)

It is a lightweight project that hourly scrapes lots of free-proxy sites, validates if it works, and serves a clean proxy list.


> Scraper found **3588** proxies at the latest update. Usable proxies are below.

## Usage

Click the file format that you want and copy the URL.


|File|Content|Count|
|----|-------|-----|
|[data.txt](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.txt)|`ip_address:port` combined (seperated new line)|200|
|[data.json](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.json)|`ip, port`|200|
|[data-with-geolocation.json](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data-with-geolocation.json)|`ip, port, geolocation`|200|

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
|[proxyscrape.com](https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all)|379|✅|
|[github.com/clarketm/proxy-list](https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt)|400|✅|
|[github.com/monosans/proxy-list](https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt)|234|✅|
|[github.com/TheSpeedX/PROXY-List](https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt)|1892|✅|


## Sample Proxies With Geolocation Info

|#|Ip|Port|Country|City|Internet Service Provider|
|-|--|----|-------|----|-------------------------|
|1|3.128.120.252|80|United States|Dublin|Amazon.com, Inc.|
|2|67.212.83.55|1080|Canada|Saint-Hyacinthe|eStruxture Data Centers Inc.|
|3|121.254.195.12|8080|South Korea|Yongsan-dong|LG DACOM Corporation|
|4|3.128.120.252|80|United States|Dublin|Amazon.com, Inc.|
|5|176.29.189.195|8080|Jordan|Amman|Zain Jordan|
|6|136.243.37.84|9090|Germany|Falkenstein|Hetzner Online GmbH|
|7|47.91.25.174|80|Japan|Tokyo|Alibaba.com LLC|
|8|67.212.83.54|1080|Canada|Saint-Hyacinthe|eStruxture Data Centers Inc.|
|9|67.212.83.53|1080|Canada|Saint-Hyacinthe|eStruxture Data Centers Inc.|
|10|186.67.230.45|3128|Chile|Santiago|Entel Chile S.A.|
|11|193.34.21.4|55277|Ukraine|Kryvyi Rih|TRK Cable TV LLC|
|12|175.144.202.18|3128|Malaysia|Marabu|Tmnet, Telekom Malaysia Bhd.|
|13|51.79.121.94|3128|Canada|Beauharnois|OVH SAS|
|14|66.94.120.161|443|United States|Seattle|Contabo Inc.|
|15|51.79.124.80|3128|Canada|Beauharnois|OVH SAS|
|16|85.117.239.22|3128|Turkey|Bahçelievler|Taner Temel|
|17|20.47.108.204|8888|United States|Boydton|Microsoft Corporation|
|18|31.171.154.199|8118|Albania|Tirana|Keminet Ltd|
|19|31.171.152.68|8118|Albania|Tirana|Keminet SHPK|
|20|51.81.32.81|8888|United States|Reston|OVH SAS|



## Contributing

Contributions are welcome, and they are greatly appreciated! Every
little bit helps, and credit will always be given.

