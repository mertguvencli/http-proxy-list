
# Free HTTP Proxy List 🌍

[![Hourly Update](https://github.com/mertguvencli/http-proxy-list/actions/workflows/main.yml/badge.svg?branch=main)](https://github.com/mertguvencli/http-proxy-list/actions/workflows/main.yml)
![GitHub](https://img.shields.io/github/license/mertguvencli/http-proxy-list)
![GitHub last commit](https://img.shields.io/github/last-commit/mertguvencli/http-proxy-list)

It is a lightweight project that hourly scrapes lots of free-proxy sites, validates if it works, and serves a clean proxy list.


> Scraper found **4205** proxies at the latest update. Usable proxies are below.

## Usage

Click the file format that you want and copy the URL.


|File|Content|Count|
|----|-------|-----|
|[data.txt](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.txt)|`ip_address:port` combined (seperated new line)|303|
|[data.json](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.json)|`ip, port`|303|
|[data-with-geolocation.json](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data-with-geolocation.json)|`ip, port, geolocation`|303|

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
|[proxylist.geonode.com](https://proxylist.geonode.com/api/proxy-list?limit=300&page=1&sort_by=lastChecked&sort_type=desc&protocols=http,https)|270|✅|
|[proxyscrape.com](https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all)|495|✅|
|[github.com/clarketm/proxy-list](https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt)|400|✅|
|[github.com/monosans/proxy-list](https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt)|379|✅|
|[github.com/TheSpeedX/PROXY-List](https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt)|2078|✅|


## Sample Proxies With Geolocation Info

|#|Ip|Port|Country|City|Internet Service Provider|
|-|--|----|-------|----|-------------------------|
|1|77.50.114.205|3128|Russia|Moscow|StarLink Telecom Network|
|2|103.73.194.2|80|Hong Kong|Wanchai|TouchPal HK Co., Limited|
|3|181.64.11.193|3128|Peru|Rioja|Telefonica del Peru|
|4|170.155.5.235|8080|Argentina|Castelar|Gobernacion de la Provincia de Buenos Aires|
|5|190.26.201.194|8080|Colombia|Castilla La Nueva|ETB - Colombia|
|6|103.145.142.54|80|Indonesia|Tamiajeng|PT. Indonesia Comnets Plus|
|7|5.189.229.42|1081|Russia|St Petersburg|OOO "Network of data-centers "Selectel"|
|8|194.233.86.75|1234|Singapore|Singapore|Contabo Asia Private Limited|
|9|85.25.196.218|5566|France|Strasbourg|Host Europe GmbH|
|10|85.25.117.68|5566|France|Strasbourg|BSB-SERVICE|
|11|188.138.90.226|5566|France|Strasbourg|Host Europe GmbH|
|12|188.138.106.158|5566|France|Strasbourg|Host Europe GmbH|
|13|105.243.252.21|8080|South Africa|Johannesburg|Vodacom UMTS Pretoria Silverton North Gauteng INTERNET APN|
|14|171.6.76.91|8080|Thailand|Bang Lamung|Triple T Broadband Public Company Limited|
|15|85.25.150.32|5566|France|Strasbourg|Host Europe GmbH|
|16|181.129.245.124|999|Colombia|Santiago de Cali|EPM Telecomunicaciones S.A. E.S.P.|
|17|188.138.89.29|5566|France|Strasbourg|Host Europe GmbH|
|18|202.180.20.11|55443|Indonesia|Bandung|PT. HIPERNET INDODATA|
|19|85.25.99.106|5566|France|Strasbourg|PLUSSERVER|
|20|62.138.7.104|5566|France|Strasbourg|Host Europe Group|



## Contributing

Contributions are welcome, and they are greatly appreciated! Every
little bit helps, and credit will always be given.

