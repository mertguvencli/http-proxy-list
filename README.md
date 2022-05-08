
# Free HTTP Proxy List 🌍

[![Hourly Update](https://github.com/mertguvencli/http-proxy-list/actions/workflows/main.yml/badge.svg?branch=main)](https://github.com/mertguvencli/http-proxy-list/actions/workflows/main.yml)
![GitHub](https://img.shields.io/github/license/mertguvencli/http-proxy-list)
![GitHub last commit](https://img.shields.io/github/last-commit/mertguvencli/http-proxy-list)

It is a lightweight project that hourly scrapes lots of free-proxy sites, validates if it works, and serves a clean proxy list.


> Scraper found **3362** proxies at the latest update. Usable proxies are below.

## Usage

Click the file format that you want and copy the URL.


|File|Content|Count|
|----|-------|-----|
|[data.txt](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.txt)|`ip_address:port` combined (seperated new line)|189|
|[data.json](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.json)|`ip, port`|189|
|[data-with-geolocation.json](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data-with-geolocation.json)|`ip, port, geolocation`|189|

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
|[proxylist.geonode.com](https://proxylist.geonode.com/api/proxy-list?limit=300&page=1&sort_by=lastChecked&sort_type=desc&protocols=http,https)|0|🚫|
|[proxyscrape.com](https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all)|256|✅|
|[github.com/clarketm/proxy-list](https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt)|400|✅|
|[github.com/monosans/proxy-list](https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt)|242|✅|
|[github.com/TheSpeedX/PROXY-List](https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt)|1881|✅|


## Sample Proxies With Geolocation Info

|#|Ip|Port|Country|City|Internet Service Provider|
|-|--|----|-------|----|-------------------------|
|1|174.138.116.12|80|United States|Clifton|DigitalOcean, LLC|
|2|128.199.94.96|3128|Singapore|Singapore|DigitalOcean, LLC|
|3|174.138.116.12|80|United States|Clifton|DigitalOcean, LLC|
|4|149.248.5.225|59394|United States|Los Angeles|The Constant Company|
|5|45.77.86.30|59394|United States|Los Angeles|The Constant Company|
|6|143.198.40.108|3128|Canada|Toronto|DigitalOcean, LLC|
|7|183.89.97.135|18080|Thailand|Bangkok|Triple T Broadband Public Company Limited|
|8|200.105.215.18|33630|Bolivia|La Paz|AXS Bolivia S. A.|
|9|161.35.126.221|3128|United States|North Bergen|DigitalOcean, LLC|
|10|40.70.172.110|80|United States|Boydton|Microsoft Corporation|
|11|66.94.97.238|443|United States|New York|Contabo Inc.|
|12|45.189.253.1|999|Mexico|San Sabastian Tierra Blanca|Tracered SA De CV|
|13|190.26.201.194|8080|Colombia|Bogotá|ETB - Colombia|
|14|68.183.128.165|3128|United States|North Bergen|DigitalOcean, LLC|
|15|111.202.50.231|3128|China|Xicheng District|China Unicom Beijing Province Network|
|16|206.189.143.224|3128|India|Bengaluru|DigitalOcean, LLC|
|17|40.70.172.110|80|United States|Boydton|Microsoft Corporation|
|18|90.83.14.99|8080|France|Poitiers|Orange S.A.|
|19|111.202.50.231|3128|China|Xicheng District|China Unicom Beijing Province Network|
|20|189.112.10.242|3128|Brazil|São Paulo|ALGAR TELECOM S/A|



## Contributing

Contributions are welcome, and they are greatly appreciated! Every
little bit helps, and credit will always be given.

