
# Free HTTP Proxy List 🌍

[![Hourly Update](https://github.com/mertguvencli/http-proxy-list/actions/workflows/main.yml/badge.svg?branch=main)](https://github.com/mertguvencli/http-proxy-list/actions/workflows/main.yml)
![GitHub](https://img.shields.io/github/license/mertguvencli/http-proxy-list)
![GitHub last commit](https://img.shields.io/github/last-commit/mertguvencli/http-proxy-list)

It is a lightweight project that hourly scrapes lots of free-proxy sites, validates if it works, and serves a clean proxy list.


> Scraper found **3937** proxies at the latest update. Usable proxies are below.

## Usage

Click the file format that you want and copy the URL.


|File|Content|Count|
|----|-------|-----|
|[data.txt](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.txt)|`ip_address:port` combined (seperated new line)|315|
|[data.json](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.json)|`ip, port`|315|
|[data-with-geolocation.json](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data-with-geolocation.json)|`ip, port, geolocation`|315|

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
|[proxyscrape.com](https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all)|364|✅|
|[github.com/clarketm/proxy-list](https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt)|400|✅|
|[github.com/monosans/proxy-list](https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt)|197|✅|
|[github.com/TheSpeedX/PROXY-List](https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt)|1993|✅|


## Sample Proxies With Geolocation Info

|#|Ip|Port|Country|City|Internet Service Provider|
|-|--|----|-------|----|-------------------------|
|1|20.81.62.32|3128|United States|Boydton|Microsoft Corporation|
|2|45.131.251.234|3129|United States|Los Angeles|DediPath|
|3|20.81.62.32|3128|United States|Boydton|Microsoft Corporation|
|4|45.167.124.5|9992|Colombia|Guapi|Sepcom Comunicaciones SAS|
|5|85.14.243.31|3128|Germany|Meerbusch|myLoc managed IT AG|
|6|95.217.72.247|3128|Finland|Helsinki|Hetzner Online GmbH|
|7|45.131.251.234|3129|United States|Los Angeles|DediPath|
|8|157.100.12.138|999|Ecuador|Loja|Telconet S.A|
|9|206.189.23.38|8048|United Kingdom|London|DigitalOcean, LLC|
|10|165.22.211.212|3128|India|Bengaluru|DigitalOcean, LLC|
|11|173.212.224.134|3129|Germany|Nuremberg|Contabo GmbH|
|12|181.174.224.96|999|Peru|Lima|CHARACKWAVES CUSYPATA EXPORT/IMPORT S.A.C.|
|13|110.170.126.13|3128|Thailand|Din Daeng|True Internet Corporation CO. Ltd.|
|14|79.143.179.141|3128|Germany|Munich|Contabo GmbH|
|15|209.97.152.208|8888|United States|Clifton|DigitalOcean, LLC|
|16|181.176.161.39|999|Peru|Huaraz|VIETTEL PERÚ S.A.C.|
|17|152.32.218.99|8000|Singapore|Singapore|UCLOUD INFORMATION TECHNOLOGY (HK) LIMITED|
|18|194.233.69.90|443|Singapore|Singapore|Contabo Asia Private Limited|
|19|200.110.168.159|8080|Colombia|Trujillo|Media Commerce Partners S.A|
|20|66.94.97.238|443|United States|New York|Contabo Inc.|



## Contributing

Contributions are welcome, and they are greatly appreciated! Every
little bit helps, and credit will always be given.

