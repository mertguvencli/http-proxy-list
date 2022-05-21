
# Free HTTP Proxy List 🌍

[![Hourly Update](https://github.com/mertguvencli/http-proxy-list/actions/workflows/main.yml/badge.svg?branch=main)](https://github.com/mertguvencli/http-proxy-list/actions/workflows/main.yml)
![GitHub](https://img.shields.io/github/license/mertguvencli/http-proxy-list)
![GitHub last commit](https://img.shields.io/github/last-commit/mertguvencli/http-proxy-list)

It is a lightweight project that hourly scrapes lots of free-proxy sites, validates if it works, and serves a clean proxy list.


> Scraper found **3742** proxies at the latest update. Usable proxies are below.

## Usage

Click the file format that you want and copy the URL.


|File|Content|Count|
|----|-------|-----|
|[data.txt](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.txt)|`ip_address:port` combined (seperated new line)|88|
|[data.json](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.json)|`ip, port`|88|
|[data-with-geolocation.json](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data-with-geolocation.json)|`ip, port, geolocation`|88|

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
|[proxylist.geonode.com](https://proxylist.geonode.com/api/proxy-list?limit=300&page=1&sort_by=lastChecked&sort_type=desc&protocols=http,https)|300|✅|
|[proxyscrape.com](https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all)|242|✅|
|[github.com/clarketm/proxy-list](https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt)|400|✅|
|[github.com/monosans/proxy-list](https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt)|179|✅|
|[github.com/TheSpeedX/PROXY-List](https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt)|1938|✅|


## Sample Proxies With Geolocation Info

|#|Ip|Port|Country|City|Internet Service Provider|
|-|--|----|-------|----|-------------------------|
|1|121.254.195.12|8080|South Korea|Yongsan-dong|LG DACOM Corporation|
|2|47.91.25.174|80|Japan|Tokyo|Alibaba.com LLC|
|3|47.241.165.133|443|Singapore|Singapore|Alibaba.com LLC|
|4|181.204.9.182|9812|Colombia|Cartagena|EPM Telecomunicaciones S.A. E.S.P.|
|5|66.94.120.161|443|United States|Seattle|Contabo Inc.|
|6|18.218.45.35|3128|United States|Dublin|Amazon.com, Inc.|
|7|176.120.213.206|41258|Russia|Makhachkala|SUBNET05|
|8|111.202.50.231|3128|China|Xicheng District|China Unicom Beijing Province Network|
|9|185.177.222.171|8089|Russia|Murom|Modus LLC|
|10|45.189.254.2|999|Mexico|Alvarado|Tracered SA De CV|
|11|182.90.224.115|3128|China|Beihai|China Unicom Guangxi Province Network|
|12|121.254.195.12|8080|South Korea|Yongsan-dong|LG DACOM Corporation|
|13|51.77.141.29|1081|France|Strasbourg|OVH SAS|
|14|54.39.102.233|3128|Canada|Beauharnois|OVH SAS|
|15|190.107.224.150|3128|Chile|Santiago|WOM S.A.|
|16|190.113.42.73|999|Dominican Republic|Santo Domingo Este|MR Networking, SRL|
|17|186.67.230.45|3128|Chile|Santiago|Entel Chile S.A.|
|18|182.90.224.115|3128|China|Beihai|China Unicom Guangxi Province Network|
|19|175.184.230.233|6565|Indonesia|Semarang|DATAUTAMANET|
|20|51.79.152.70|80|Singapore|Singapore|OVH SAS|



## Contributing

Contributions are welcome, and they are greatly appreciated! Every
little bit helps, and credit will always be given.

