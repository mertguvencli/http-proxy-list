
# Free HTTP Proxy List 🌍

[![Hourly Update](https://github.com/mertguvencli/http-proxy-list/actions/workflows/main.yml/badge.svg?branch=main)](https://github.com/mertguvencli/http-proxy-list/actions/workflows/main.yml)
![GitHub](https://img.shields.io/github/license/mertguvencli/http-proxy-list)
![GitHub last commit](https://img.shields.io/github/last-commit/mertguvencli/http-proxy-list)

It is a lightweight project that hourly scrapes lots of free-proxy sites, validates if it works, and serves a clean proxy list.


> Scraper found **4099** proxies at the latest update. Usable proxies are below.

## Usage

Click the file format that you want and copy the URL.


|File|Content|Count|
|----|-------|-----|
|[data.txt](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.txt)|`ip_address:port` combined (seperated new line)|206|
|[data.json](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.json)|`ip, port`|206|
|[data-with-geolocation.json](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data-with-geolocation.json)|`ip, port, geolocation`|206|

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
|[proxyscrape.com](https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all)|316|✅|
|[github.com/clarketm/proxy-list](https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt)|400|✅|
|[github.com/monosans/proxy-list](https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt)|218|✅|
|[github.com/TheSpeedX/PROXY-List](https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt)|2182|✅|


## Sample Proxies With Geolocation Info

|#|Ip|Port|Country|City|Internet Service Provider|
|-|--|----|-------|----|-------------------------|
|1|170.39.118.187|3128|United States|Ashburn|Rackdog, LLC|
|2|34.145.226.144|8080|United States|Washington|Google LLC|
|3|35.170.197.3|8888|United States|Ashburn|Amazon.com, Inc.|
|4|170.39.118.187|3128|United States|Ashburn|Rackdog, LLC|
|5|35.170.197.3|8888|United States|Ashburn|Amazon.com, Inc.|
|6|34.145.226.144|8080|United States|Washington|Google LLC|
|7|45.167.124.5|9992|Colombia|Guapi|Sepcom Comunicaciones SAS|
|8|65.21.206.151|3128|Finland|Helsinki|Hetzner Online GmbH|
|9|5.189.140.161|3128|Germany|Nuremberg|Contabo GmbH|
|10|157.100.12.138|999|Ecuador|Quito|Telconet S.A|
|11|177.141.99.50|8080|Brazil|São Paulo|Claro S.A.|
|12|183.111.25.253|8080|South Korea|Seongnam-si|Korea Telecom|
|13|165.154.233.46|8080|Philippines|Manila|Scloud Pte Ltd|
|14|190.94.199.14|999|Venezuela|Caracas|IFX Networks Venezuela C.A.|
|15|89.107.197.165|3128|Russia|Tula|LLC TK Altair|
|16|170.233.240.3|3180|Brazil|Sao Goncalo|Navenet Informatica Ltda|
|17|110.170.126.13|3128|Thailand|Din Daeng|True Internet Corporation CO. Ltd.|
|18|117.1.134.89|6666|Vietnam|Hanoi|Viettel Corporation|
|19|45.189.254.2|999|Mexico|Alvarado|Tracered SA De CV|
|20|152.32.218.99|8000|Singapore|Singapore|UCLOUD INFORMATION TECHNOLOGY (HK) LIMITED|



## Contributing

Contributions are welcome, and they are greatly appreciated! Every
little bit helps, and credit will always be given.

