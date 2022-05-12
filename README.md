
# Free HTTP Proxy List 🌍

[![Hourly Update](https://github.com/mertguvencli/http-proxy-list/actions/workflows/main.yml/badge.svg?branch=main)](https://github.com/mertguvencli/http-proxy-list/actions/workflows/main.yml)
![GitHub](https://img.shields.io/github/license/mertguvencli/http-proxy-list)
![GitHub last commit](https://img.shields.io/github/last-commit/mertguvencli/http-proxy-list)

It is a lightweight project that hourly scrapes lots of free-proxy sites, validates if it works, and serves a clean proxy list.


> Scraper found **3808** proxies at the latest update. Usable proxies are below.

## Usage

Click the file format that you want and copy the URL.


|File|Content|Count|
|----|-------|-----|
|[data.txt](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.txt)|`ip_address:port` combined (seperated new line)|194|
|[data.json](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.json)|`ip, port`|194|
|[data-with-geolocation.json](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data-with-geolocation.json)|`ip, port, geolocation`|194|

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
|[proxyscrape.com](https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all)|315|✅|
|[github.com/clarketm/proxy-list](https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt)|400|✅|
|[github.com/monosans/proxy-list](https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt)|187|✅|
|[github.com/TheSpeedX/PROXY-List](https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt)|1923|✅|


## Sample Proxies With Geolocation Info

|#|Ip|Port|Country|City|Internet Service Provider|
|-|--|----|-------|----|-------------------------|
|1|160.16.242.164|3128|Japan|Tokyo|SAKURA Internet Inc.|
|2|119.76.142.161|8080|Thailand|Nakhon Ratchasima|True Internet Co., Ltd.|
|3|139.99.88.19|8080|Singapore|Singapore|OVH SAS|
|4|191.242.177.114|3128|Brazil|Salvador|Conect Telecom|
|5|186.67.230.45|3128|Chile|Santiago|Entel Chile S.A.|
|6|183.88.16.164|8080|Thailand|Ban Du|Triple T Broadband Public Company Limited|
|7|91.240.211.180|8081|Russia|Kursk|AVANT Ltd.|
|8|177.87.114.159|8080|Brazil|Sabara|Wirelessconection Serv. Telecomunicações Ltda -EPP|
|9|190.26.201.194|8080|Colombia|Bogotá|ETB - Colombia|
|10|190.26.201.194|8080|Colombia|Bogotá|ETB - Colombia|
|11|62.3.30.25|8080|Georgia|K'alak'i T'bilisi|Enbinet Ltd.|
|12|116.110.21.87|8080|Vietnam|Da Nang|Viettel Corporation|
|13|218.106.63.83|21080|China|Jinrongjie|China Unicom CncNet|
|14|163.172.64.42|8080|France|Paris|Online S.A.S.|
|15|123.24.51.176|19132|Vietnam|Hanoi|VietNam Post and Telecom Corporation|
|16|190.121.21.211|1081|Chile|Valdivia|Telefonica del Sur S.A.|
|17|45.32.150.229|3128|France|Aubervilliers|The Constant Company|
|18|5.153.234.91|3128|Sweden|Stockholm|Inter Connects Inc|
|19|160.16.242.164|3128|Japan|Tokyo|SAKURA Internet Inc.|
|20|5.39.189.39|3128|Netherlands|Rotterdam|ColoCenter b.v.|



## Contributing

Contributions are welcome, and they are greatly appreciated! Every
little bit helps, and credit will always be given.

