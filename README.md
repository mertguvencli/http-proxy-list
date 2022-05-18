
# Free HTTP Proxy List 🌍

[![Hourly Update](https://github.com/mertguvencli/http-proxy-list/actions/workflows/main.yml/badge.svg?branch=main)](https://github.com/mertguvencli/http-proxy-list/actions/workflows/main.yml)
![GitHub](https://img.shields.io/github/license/mertguvencli/http-proxy-list)
![GitHub last commit](https://img.shields.io/github/last-commit/mertguvencli/http-proxy-list)

It is a lightweight project that hourly scrapes lots of free-proxy sites, validates if it works, and serves a clean proxy list.


> Scraper found **3672** proxies at the latest update. Usable proxies are below.

## Usage

Click the file format that you want and copy the URL.


|File|Content|Count|
|----|-------|-----|
|[data.txt](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.txt)|`ip_address:port` combined (seperated new line)|180|
|[data.json](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.json)|`ip, port`|180|
|[data-with-geolocation.json](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data-with-geolocation.json)|`ip, port, geolocation`|180|

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
|[proxyscrape.com](https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all)|201|✅|
|[github.com/clarketm/proxy-list](https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt)|400|✅|
|[github.com/monosans/proxy-list](https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt)|181|✅|
|[github.com/TheSpeedX/PROXY-List](https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt)|1907|✅|


## Sample Proxies With Geolocation Info

|#|Ip|Port|Country|City|Internet Service Provider|
|-|--|----|-------|----|-------------------------|
|1|149.19.224.15|3128|United States|Sterling|SPRINT|
|2|162.150.62.96|443|United States|Kincaid|Comcast Cable Communications, LLC|
|3|162.150.62.95|443|United States|Kincaid|Comcast Cable Communications, LLC|
|4|138.197.69.179|8080|United States|Clifton|DigitalOcean, LLC|
|5|149.19.224.15|3128|United States|Sterling|SPRINT|
|6|148.251.66.8|3128|Germany|Falkenstein|Hetzner Online GmbH|
|7|162.150.62.95|443|United States|Kincaid|Comcast Cable Communications, LLC|
|8|185.16.60.14|3128|Germany|Karlsruhe|netcup GmbH|
|9|162.150.62.96|443|United States|Kincaid|Comcast Cable Communications, LLC|
|10|3.128.120.252|80|United States|Dublin|Amazon.com, Inc.|
|11|168.8.209.253|80|United States|Roswell|Board of Regents of the University System of Georgia|
|12|157.245.222.183|80|United States|Clifton|DigitalOcean, LLC|
|13|129.226.43.3|3218|India|Mumbai|Tencent Cloud Computing (Beijing) Co|
|14|194.5.25.34|443|Singapore|Singapore|Mod Mission Critical LLC|
|15|186.67.230.45|3128|Chile|Santiago|Entel Chile S.A.|
|16|157.230.34.219|3128|Singapore|Singapore|DigitalOcean, LLC|
|17|121.254.195.12|8080|South Korea|Yongsan-dong|LG DACOM Corporation|
|18|194.233.73.109|443|Singapore|Singapore|Contabo Asia Private Limited|
|19|129.226.42.57|3218|India|Mumbai|Tencent Cloud Computing (Beijing) Co|
|20|129.226.42.46|3218|India|Mumbai|Tencent Cloud Computing (Beijing) Co|



## Contributing

Contributions are welcome, and they are greatly appreciated! Every
little bit helps, and credit will always be given.

