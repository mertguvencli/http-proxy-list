
# Free HTTP Proxy List 🌍

[![Hourly Update](https://github.com/mertguvencli/http-proxy-list/actions/workflows/main.yml/badge.svg?branch=main)](https://github.com/mertguvencli/http-proxy-list/actions/workflows/main.yml)
![GitHub](https://img.shields.io/github/license/mertguvencli/http-proxy-list)
![GitHub last commit](https://img.shields.io/github/last-commit/mertguvencli/http-proxy-list)

It is a lightweight project that hourly scrapes lots of free-proxy sites, validates if it works, and serves a clean proxy list.


> Scraper found **3907** proxies at the latest update. Usable proxies are below.

## Usage

Click the file format that you want and copy the URL.


|File|Content|Count|
|----|-------|-----|
|[data.txt](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.txt)|`ip_address:port` combined (seperated new line)|307|
|[data.json](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.json)|`ip, port`|307|
|[data-with-geolocation.json](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data-with-geolocation.json)|`ip, port, geolocation`|307|

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
|[proxyscrape.com](https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all)|417|✅|
|[github.com/clarketm/proxy-list](https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt)|400|✅|
|[github.com/monosans/proxy-list](https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt)|206|✅|
|[github.com/TheSpeedX/PROXY-List](https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt)|2001|✅|


## Sample Proxies With Geolocation Info

|#|Ip|Port|Country|City|Internet Service Provider|
|-|--|----|-------|----|-------------------------|
|1|3.128.120.252|80|United States|Dublin|Amazon.com, Inc.|
|2|173.82.188.82|9090|United States|Santa Clarita|Multacom Corporation|
|3|3.128.120.252|80|United States|Dublin|Amazon.com, Inc.|
|4|147.75.68.201|80|United States|Sunnyvale|Equinix Services|
|5|3.126.242.11|3128|Germany|Frankfurt am Main|Amazon Technologies Inc.|
|6|45.167.125.209|9992|Colombia|Popayán|Sepcom Comunicaciones SAS|
|7|43.130.47.100|8081|United States|Santa Clara|Shenzhen Tencent Computer Systems Company Limited|
|8|147.75.68.201|80|United States|Sunnyvale|Equinix Services|
|9|5.189.184.6|80|Germany|Nuremberg|Contabo GmbH|
|10|2.187.229.7|8080|Iran|Urmia|Iran Telecommunication Company PJS|
|11|47.74.226.8|5001|Singapore|Singapore|Alibaba Cloud (Singapore) Private Limited|
|12|75.119.130.35|3128|Germany|Düsseldorf|Contabo GmbH|
|13|54.193.249.144|8080|United States|San Jose|Amazon.com, Inc.|
|14|54.193.249.144|8080|United States|San Jose|Amazon.com, Inc.|
|15|194.233.73.105|443|Singapore|Singapore|Contabo Asia Private Limited|
|16|61.72.81.14|8080|South Korea|Seodaemun-gu|Korea Telecom|
|17|194.233.73.109|443|Singapore|Singapore|Contabo Asia Private Limited|
|18|62.183.81.38|8080|Russia|Kenzhe|Kabardian-Balkar Telecommunications Company|
|19|45.181.122.74|999|Chile|Santiago|Interpit Telecomunicaciones Ltda|
|20|45.55.57.204|443|United States|Clifton|DigitalOcean, LLC|



## Contributing

Contributions are welcome, and they are greatly appreciated! Every
little bit helps, and credit will always be given.

