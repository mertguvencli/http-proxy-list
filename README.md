
# Free HTTP Proxy List 🌍

[![Hourly Update](https://github.com/mertguvencli/http-proxy-list/actions/workflows/main.yml/badge.svg?branch=main)](https://github.com/mertguvencli/http-proxy-list/actions/workflows/main.yml)
![GitHub](https://img.shields.io/github/license/mertguvencli/http-proxy-list)
![GitHub last commit](https://img.shields.io/github/last-commit/mertguvencli/http-proxy-list)

It is a lightweight project that hourly scrapes lots of free-proxy sites, validates if it works, and serves a clean proxy list.


> Scraper found **3911** proxies at the latest update. Usable proxies are below.

## Usage

Click the file format that you want and copy the URL.


|File|Content|Count|
|----|-------|-----|
|[data.txt](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.txt)|`ip_address:port` combined (seperated new line)|177|
|[data.json](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.json)|`ip, port`|177|
|[data-with-geolocation.json](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data-with-geolocation.json)|`ip, port, geolocation`|177|

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
|[proxyscrape.com](https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all)|371|✅|
|[github.com/clarketm/proxy-list](https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt)|400|✅|
|[github.com/monosans/proxy-list](https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt)|246|✅|
|[github.com/TheSpeedX/PROXY-List](https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt)|1911|✅|


## Sample Proxies With Geolocation Info

|#|Ip|Port|Country|City|Internet Service Provider|
|-|--|----|-------|----|-------------------------|
|1|20.47.108.204|8888|United States|Boydton|Microsoft Corporation|
|2|155.138.232.110|59394|United States|Atlanta|The Constant Company|
|3|20.47.108.204|8888|United States|Boydton|Microsoft Corporation|
|4|155.138.232.110|59394|United States|Atlanta|The Constant Company|
|5|167.71.207.46|8080|Singapore|Singapore|DigitalOcean, LLC|
|6|45.63.69.252|59394|United States|Elk Grove Village|The Constant Company|
|7|5.202.104.202|3128|Iran|Saveh|Pishgaman Toseeh Ertebatat Company (Private Joint Stock)|
|8|200.229.147.2|999|Honduras|Tegucigalpa|Ufinet Panama S.A.|
|9|103.144.79.186|8080|Indonesia|Jakarta|PT. Indonesia Comnets Plus|
|10|200.125.126.32|999|Argentina|Pilar|Telecentro S.A.|
|11|103.156.15.48|8080|Indonesia|Pinrang|PT Lintas Jaringan Nusantara|
|12|181.224.255.42|8080|Peru|Lima|Econocable Media SAC|
|13|167.114.96.27|9300|Canada|Montreal|OVH SAS|
|14|185.104.252.10|9090|Lebanon|Bdebba|B SMART|
|15|155.138.229.91|59394|United States|Atlanta|The Constant Company|
|16|155.138.229.91|59394|United States|Atlanta|The Constant Company|
|17|45.76.13.167|59394|United States|Piscataway|The Constant Company|
|18|190.26.201.194|8080|Colombia|Bogotá|ETB - Colombia|
|19|190.26.201.194|8080|Colombia|Bogotá|ETB - Colombia|
|20|168.195.137.34|8080|Brazil|Cabo de Santo Agostinho|R M SILVA DE PAULA INFORMATICA ME|



## Contributing

Contributions are welcome, and they are greatly appreciated! Every
little bit helps, and credit will always be given.

