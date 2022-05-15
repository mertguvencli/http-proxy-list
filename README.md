
# Free HTTP Proxy List 🌍

[![Hourly Update](https://github.com/mertguvencli/http-proxy-list/actions/workflows/main.yml/badge.svg?branch=main)](https://github.com/mertguvencli/http-proxy-list/actions/workflows/main.yml)
![GitHub](https://img.shields.io/github/license/mertguvencli/http-proxy-list)
![GitHub last commit](https://img.shields.io/github/last-commit/mertguvencli/http-proxy-list)

It is a lightweight project that hourly scrapes lots of free-proxy sites, validates if it works, and serves a clean proxy list.


> Scraper found **3344** proxies at the latest update. Usable proxies are below.

## Usage

Click the file format that you want and copy the URL.


|File|Content|Count|
|----|-------|-----|
|[data.txt](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.txt)|`ip_address:port` combined (seperated new line)|308|
|[data.json](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.json)|`ip, port`|308|
|[data-with-geolocation.json](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data-with-geolocation.json)|`ip, port, geolocation`|308|

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
|[proxyscrape.com](https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all)|0|✅|
|[github.com/clarketm/proxy-list](https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt)|400|✅|
|[github.com/monosans/proxy-list](https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt)|222|✅|
|[github.com/TheSpeedX/PROXY-List](https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt)|1739|✅|


## Sample Proxies With Geolocation Info

|#|Ip|Port|Country|City|Internet Service Provider|
|-|--|----|-------|----|-------------------------|
|1|20.47.108.204|8888|United States|Boydton|Microsoft Corporation|
|2|154.49.216.33|3128|France|Vélizy-Villacoublay|Cogent Communications|
|3|20.47.108.204|8888|United States|Boydton|Microsoft Corporation|
|4|186.67.230.45|3128|Chile|Santiago|Entel Chile S.A.|
|5|154.49.216.33|3128|France|Vélizy-Villacoublay|Cogent Communications|
|6|200.58.87.195|8080|Bolivia|Cochabamba|Comteco Ltda|
|7|158.69.27.94|9300|Canada|Montreal|OVH SAS|
|8|185.135.193.38|3128|Poland|Lodz|M3.NET Sp. zoo Sp. K.|
|9|85.195.104.71|80|Germany|Frankfurt am Main|Host Europe GmbH|
|10|177.221.97.154|8080|Brazil|Cuiabá|Bi-Link Telecom|
|11|119.76.142.205|8080|Thailand|Nakhon Ratchasima|True Internet Co., Ltd.|
|12|190.116.90.45|999|Peru|La Victoria|America Movil Peru S.A.C.|
|13|191.242.177.114|3128|Brazil|Camamu|Conect Telecom|
|14|183.81.156.130|8080|Indonesia|Kayu Manis|Internet Service Provider|
|15|203.223.34.2|8090|Cambodia|Phnom Penh|Telecom Cambodia (T.C.)|
|16|103.161.164.119|8181|Indonesia|Ciamis|PT Galuh Multidata Solution|
|17|103.161.164.109|8181|Indonesia|Ciamis|PT Galuh Multidata Solution|
|18|14.170.154.193|19132|Vietnam|Thai Nguyen|VNPT-VNNIC|
|19|178.134.157.215|8080|Georgia|Ts'khinvali|JSC "Silknet"|
|20|113.189.224.208|19132|Vietnam|Hanoi|VNPT|



## Contributing

Contributions are welcome, and they are greatly appreciated! Every
little bit helps, and credit will always be given.

