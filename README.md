
# Free HTTP Proxy List 🌍

[![Hourly Update](https://github.com/mertguvencli/http-proxy-list/actions/workflows/main.yml/badge.svg?branch=main)](https://github.com/mertguvencli/http-proxy-list/actions/workflows/main.yml)
![GitHub](https://img.shields.io/github/license/mertguvencli/http-proxy-list)
![GitHub last commit](https://img.shields.io/github/last-commit/mertguvencli/http-proxy-list)

It is a lightweight project that hourly scrapes lots of free-proxy sites, validates if it works, and serves a clean proxy list.


> Scraper found **3901** proxies at the latest update. Usable proxies are below.

## Usage

Click the file format that you want and copy the URL.


|File|Content|Count|
|----|-------|-----|
|[data.txt](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.txt)|`ip_address:port` combined (seperated new line)|129|
|[data.json](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.json)|`ip, port`|129|
|[data-with-geolocation.json](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data-with-geolocation.json)|`ip, port, geolocation`|129|

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
|[proxyscrape.com](https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all)|307|✅|
|[github.com/clarketm/proxy-list](https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt)|400|✅|
|[github.com/monosans/proxy-list](https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt)|194|✅|
|[github.com/TheSpeedX/PROXY-List](https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt)|2117|✅|


## Sample Proxies With Geolocation Info

|#|Ip|Port|Country|City|Internet Service Provider|
|-|--|----|-------|----|-------------------------|
|1|34.145.226.144|8080|United States|Washington|Google LLC|
|2|143.198.242.86|8048|United Kingdom|London|DigitalOcean, LLC|
|3|34.145.226.144|8080|United States|Washington|Google LLC|
|4|192.241.170.242|3128|United States|New York|DigitalOcean, LLC|
|5|47.240.160.90|10001|Hong Kong|Central|Alibaba.com LLC|
|6|182.52.83.161|8080|Thailand|Satun|TOT Public Company Limited|
|7|192.241.170.242|3128|United States|New York|DigitalOcean, LLC|
|8|88.255.94.2|8080|Turkey|İskenderun|Turk Telekomunikasyon Anonim Sirketi|
|9|66.94.120.161|443|United States|Seattle|Contabo Inc.|
|10|36.81.236.48|8080|Indonesia|Baregbeg Dua|PT. Telekomunikasi Indonesia|
|11|107.172.73.179|7890|United States|Buffalo|ColoCrossing|
|12|134.122.58.174|80|Netherlands|Amsterdam|DigitalOcean, LLC|
|13|186.5.5.125|8080|Ecuador|Guayaquil|Telconet S.A|
|14|85.105.139.53|8090|Turkey|Cankaya|TurkTelecom|
|15|34.145.226.144|8080|United States|Washington|Google LLC|
|16|143.198.242.86|8048|United Kingdom|London|DigitalOcean, LLC|
|17|67.212.83.55|1080|Canada|Saint-Hyacinthe|eStruxture Data Centers Inc.|
|18|190.214.52.226|53281|Ecuador|Guayaquil|Corporacion Nacional De Telecomunicaciones - CNT EP|
|19|191.55.57.35|8080|Brazil|Uberlândia|ALGAR TELECOM S/A|
|20|14.155.113.135|9000|China|Shenzhen|Chinanet|



## Contributing

Contributions are welcome, and they are greatly appreciated! Every
little bit helps, and credit will always be given.

