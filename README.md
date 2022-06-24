
# Free HTTP Proxy List 🌍

[![Hourly Update](https://github.com/mertguvencli/http-proxy-list/actions/workflows/main.yml/badge.svg?branch=main)](https://github.com/mertguvencli/http-proxy-list/actions/workflows/main.yml)
![GitHub](https://img.shields.io/github/license/mertguvencli/http-proxy-list)
![GitHub last commit](https://img.shields.io/github/last-commit/mertguvencli/http-proxy-list)

It is a lightweight project that hourly scrapes lots of free-proxy sites, validates if it works, and serves a clean proxy list.


> Scraper found **3902** proxies at the latest update. Usable proxies are below.

## Usage

Click the file format that you want and copy the URL.


|File|Content|Count|
|----|-------|-----|
|[data.txt](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.txt)|`ip_address:port` combined (seperated new line)|239|
|[data.json](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.json)|`ip, port`|239|
|[data-with-geolocation.json](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data-with-geolocation.json)|`ip, port, geolocation`|239|

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
|[proxyscrape.com](https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all)|375|✅|
|[github.com/clarketm/proxy-list](https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt)|400|✅|
|[github.com/monosans/proxy-list](https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt)|193|✅|
|[github.com/TheSpeedX/PROXY-List](https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt)|2051|✅|


## Sample Proxies With Geolocation Info

|#|Ip|Port|Country|City|Internet Service Provider|
|-|--|----|-------|----|-------------------------|
|1|20.81.62.32|3128|United States|Boydton|Microsoft Corporation|
|2|209.97.152.208|8888|United States|Clifton|DigitalOcean, LLC|
|3|199.195.254.168|8118|United States|New York|FranTech Solutions|
|4|45.131.251.234|3129|United States|Los Angeles|DediPath|
|5|189.164.118.26|3128|Mexico|Coronango|Uninet S.A. de C.V|
|6|206.189.23.38|8048|United Kingdom|London|DigitalOcean, LLC|
|7|20.81.62.32|3128|United States|Boydton|Microsoft Corporation|
|8|47.240.160.90|10001|Hong Kong|Central|Alibaba.com LLC|
|9|144.76.241.45|7890|Germany|Falkenstein|Hetzner Online GmbH|
|10|183.89.41.134|8080|Thailand|Ban Khung Thong (1)|Triple T Broadband Public Company Limited|
|11|180.183.4.153|8080|Thailand|Si Racha|Triple T Broadband Public Company Limited|
|12|66.94.97.238|443|United States|New York|Contabo Inc.|
|13|216.176.187.99|8886|United States|Bellevue|Wowrack.com|
|14|209.97.152.208|8888|United States|Clifton|DigitalOcean, LLC|
|15|47.241.165.133|443|Singapore|Singapore|Alibaba.com LLC|
|16|168.119.170.87|33314|Germany|Nuremberg|Hetzner Online GmbH|
|17|110.170.126.13|3128|Thailand|Din Daeng|True Internet Corporation CO. Ltd.|
|18|113.161.152.157|3128|Vietnam|Ho Chi Minh City|VietNam Post and Telecom Corporation|
|19|85.25.91.141|15333|Germany|Cologne|PlusServer GmbH|
|20|80.191.162.2|514|Iran|Shahrestān-e Bandar-e Māhshahr|Area|



## Contributing

Contributions are welcome, and they are greatly appreciated! Every
little bit helps, and credit will always be given.

