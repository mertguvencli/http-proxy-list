
# Free HTTP Proxy List 🌍

[![Hourly Update](https://github.com/mertguvencli/http-proxy-list/actions/workflows/main.yml/badge.svg?branch=main)](https://github.com/mertguvencli/http-proxy-list/actions/workflows/main.yml)
![GitHub](https://img.shields.io/github/license/mertguvencli/http-proxy-list)
![GitHub last commit](https://img.shields.io/github/last-commit/mertguvencli/http-proxy-list)

It is a lightweight project that hourly scrapes lots of free-proxy sites, validates if it works, and serves a clean proxy list.


> Scraper found **4003** proxies at the latest update. Usable proxies are below.

## Usage

Click the file format that you want and copy the URL.


|File|Content|Count|
|----|-------|-----|
|[data.txt](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.txt)|`ip_address:port` combined (seperated new line)|172|
|[data.json](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.json)|`ip, port`|172|
|[data-with-geolocation.json](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data-with-geolocation.json)|`ip, port, geolocation`|172|

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
|[proxyscrape.com](https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all)|291|✅|
|[github.com/clarketm/proxy-list](https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt)|400|✅|
|[github.com/monosans/proxy-list](https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt)|427|✅|
|[github.com/TheSpeedX/PROXY-List](https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt)|1902|✅|


## Sample Proxies With Geolocation Info

|#|Ip|Port|Country|City|Internet Service Provider|
|-|--|----|-------|----|-------------------------|
|1|174.138.116.12|80|United States|Clifton|DigitalOcean, LLC|
|2|178.124.189.174|3128|Belarus|Minsk|Republican Unitary Telecommunication Enterprise Beltelecom|
|3|103.214.9.13|3128|Vietnam|Hanoi|MEGACORE|
|4|45.77.86.30|59394|United States|Los Angeles|The Constant Company|
|5|177.99.206.234|3128|Brazil|Brasília|Vivo|
|6|5.189.184.6|80|Germany|Nuremberg|Contabo GmbH|
|7|119.76.142.136|8080|Thailand|Nakhon Ratchasima|True Internet Co., Ltd.|
|8|190.158.69.35|9812|Colombia|Pereira|Telmex Colombia S.A.|
|9|85.25.91.141|15333|Germany|Cologne|PlusServer GmbH|
|10|45.77.86.30|59394|United States|Los Angeles|The Constant Company|
|11|186.67.230.45|3128|Chile|Santiago|Entel Chile S.A.|
|12|190.26.201.194|8080|Colombia|Bogotá|ETB - Colombia|
|13|194.44.104.242|31280|Ukraine|Kyiv|State Enterprise Scientific and Telecommunication Centre "Ukrainian Academic an|
|14|202.51.124.138|9812|Indonesia|Duren Sawit|PT iForte Global Internet|
|15|217.79.181.49|3128|Germany|Düsseldorf|myLoc managed IT AG|
|16|51.81.32.81|8888|United States|Reston|OVH SAS|
|17|124.122.85.183|8888|Thailand|Bangkok|True Internet Co., Ltd.|
|18|45.17.249.223|8080|United States|Royse City|AT&T Services, Inc.|
|19|185.103.181.43|8080|Spain|Alcoletge|Vola los del Internet S.L.|
|20|177.53.152.137|999|Peru|Lima|Moreno Yanoc Nemias Bernardo|



## Contributing

Contributions are welcome, and they are greatly appreciated! Every
little bit helps, and credit will always be given.

