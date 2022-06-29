
# Free HTTP Proxy List 🌍

[![Hourly Update](https://github.com/mertguvencli/http-proxy-list/actions/workflows/main.yml/badge.svg?branch=main)](https://github.com/mertguvencli/http-proxy-list/actions/workflows/main.yml)
![GitHub](https://img.shields.io/github/license/mertguvencli/http-proxy-list)
![GitHub last commit](https://img.shields.io/github/last-commit/mertguvencli/http-proxy-list)

It is a lightweight project that hourly scrapes lots of free-proxy sites, validates if it works, and serves a clean proxy list.


> Scraper found **3880** proxies at the latest update. Usable proxies are below.

## Usage

Click the file format that you want and copy the URL.


|File|Content|Count|
|----|-------|-----|
|[data.txt](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.txt)|`ip_address:port` combined (seperated new line)|234|
|[data.json](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.json)|`ip, port`|234|
|[data-with-geolocation.json](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data-with-geolocation.json)|`ip, port, geolocation`|234|

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
|[proxyscrape.com](https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all)|359|✅|
|[github.com/clarketm/proxy-list](https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt)|400|✅|
|[github.com/monosans/proxy-list](https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt)|158|✅|
|[github.com/TheSpeedX/PROXY-List](https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt)|2080|✅|


## Sample Proxies With Geolocation Info

|#|Ip|Port|Country|City|Internet Service Provider|
|-|--|----|-------|----|-------------------------|
|1|35.234.248.49|3128|Canada|Montreal|Google LLC|
|2|209.182.235.252|3128|United States|Los Angeles|HIVELOCITY, Inc.|
|3|47.240.160.90|10001|Hong Kong|Central|Alibaba.com LLC|
|4|45.167.124.5|9992|Colombia|Guapi|Sepcom Comunicaciones SAS|
|5|85.14.243.31|3128|Germany|Meerbusch|myLoc managed IT AG|
|6|110.170.126.13|3128|Thailand|Din Daeng|True Internet Corporation CO. Ltd.|
|7|119.17.232.29|8080|Vietnam|Hanoi|Netnam Corporation|
|8|209.182.235.252|3128|United States|Los Angeles|HIVELOCITY, Inc.|
|9|93.63.78.7|3128|Italy|Milan|Fastweb SpA|
|10|157.100.12.138|999|Ecuador|Loja|Telconet S.A|
|11|68.183.235.131|8080|Singapore|Singapore|DigitalOcean, LLC|
|12|173.212.229.53|3128|Germany|Nuremberg|Contabo GmbH|
|13|20.81.62.32|3128|United States|Boydton|Microsoft Corporation|
|14|185.221.134.234|3129|United States|Los Angeles|DediPath|
|15|51.250.80.131|80|Russia|Moscow|Yandex.Cloud LLC|
|16|207.180.236.72|3128|Germany|Nuremberg|Contabo GmbH|
|17|66.94.120.161|443|United States|Seattle|Contabo Inc.|
|18|181.129.2.90|8081|Colombia|Caldas|EPM Telecomunicaciones S.A. E.S.P.|
|19|184.82.15.83|8080|Thailand|Bangkok|AIS-Fibre|
|20|88.208.34.131|18081|Netherlands|Amsterdam|DataWeb Global Group B.V.|



## Contributing

Contributions are welcome, and they are greatly appreciated! Every
little bit helps, and credit will always be given.

