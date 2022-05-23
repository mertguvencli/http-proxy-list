
# Free HTTP Proxy List 🌍

[![Hourly Update](https://github.com/mertguvencli/http-proxy-list/actions/workflows/main.yml/badge.svg?branch=main)](https://github.com/mertguvencli/http-proxy-list/actions/workflows/main.yml)
![GitHub](https://img.shields.io/github/license/mertguvencli/http-proxy-list)
![GitHub last commit](https://img.shields.io/github/last-commit/mertguvencli/http-proxy-list)

It is a lightweight project that hourly scrapes lots of free-proxy sites, validates if it works, and serves a clean proxy list.


> Scraper found **3801** proxies at the latest update. Usable proxies are below.

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
|[free-proxy-list.com](https://free-proxy-list.com/?page=&port=&type%5B%5D=http&type%5B%5D=https&up_time=0&search=Search)|10|✅|
|[proxy-list.download](https://www.proxy-list.download/HTTP)|26|✅|
|[vpnoverview.com](https://vpnoverview.com/privacy/anonymous-browsing/free-proxy-servers)|32|✅|
|[proxyscan.io](https://www.proxyscan.io)|0|🚫|
|[proxylist.geonode.com](https://proxylist.geonode.com/api/proxy-list?limit=300&page=1&sort_by=lastChecked&sort_type=desc&protocols=http,https)|290|✅|
|[proxyscrape.com](https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all)|369|✅|
|[github.com/clarketm/proxy-list](https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt)|400|✅|
|[github.com/monosans/proxy-list](https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt)|229|✅|
|[github.com/TheSpeedX/PROXY-List](https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt)|1930|✅|


## Sample Proxies With Geolocation Info

|#|Ip|Port|Country|City|Internet Service Provider|
|-|--|----|-------|----|-------------------------|
|1|20.47.108.204|8888|United States|Boydton|Microsoft Corporation|
|2|3.128.120.252|80|United States|Dublin|Amazon.com, Inc.|
|3|121.254.195.12|8080|South Korea|Yongsan-dong|LG DACOM Corporation|
|4|47.91.25.174|80|Japan|Tokyo|Alibaba.com LLC|
|5|86.57.157.233|3128|Belarus|Minsk|Republican Unitary Telecommunication Enterprise Beltelecom|
|6|81.4.102.233|8081|Netherlands|Amsterdam|WeservIT|
|7|102.130.79.1|3128|South Africa|Johannesburg|Adnexus Celerity Networks (Proprietary) Limited|
|8|188.136.144.85|8080|Iran|Isfahan|Ariana Gostar Spadana|
|9|128.199.214.87|3128|Singapore|Singapore|Partner Communications Ltd.|
|10|194.233.73.108|443|Singapore|Singapore|Contabo Asia Private Limited|
|11|182.52.51.10|61124|Thailand|Kanchanaburi|TOT Public Company Limited|
|12|47.91.25.174|80|Japan|Tokyo|Alibaba.com LLC|
|13|158.255.215.50|16993|France|Paris|Edis France|
|14|121.156.109.108|8080|South Korea|Seongnam-si|Korea Telecom|
|15|148.251.66.8|3128|Germany|Falkenstein|Hetzner Online GmbH|
|16|51.79.124.80|3128|Canada|Beauharnois|OVH SAS|
|17|181.224.207.21|999|Dominican Republic|Santiago de los Caballeros|BW TELECOM|
|18|138.121.113.182|999|Argentina|Formosa|Refsa Telecomunicaciones|
|19|41.216.178.151|8080|Indonesia|Jakarta|CV Atha Media Prima|
|20|43.250.127.98|9001|Mongolia|Ulan Bator|Wicom Networks|



## Contributing

Contributions are welcome, and they are greatly appreciated! Every
little bit helps, and credit will always be given.

