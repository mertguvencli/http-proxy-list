
# Free HTTP Proxy List 🌍

[![Hourly Update](https://github.com/mertguvencli/http-proxy-list/actions/workflows/main.yml/badge.svg?branch=main)](https://github.com/mertguvencli/http-proxy-list/actions/workflows/main.yml)
![GitHub](https://img.shields.io/github/license/mertguvencli/http-proxy-list)
![GitHub last commit](https://img.shields.io/github/last-commit/mertguvencli/http-proxy-list)

It is a lightweight project that hourly scrapes lots of free-proxy sites, validates if it works, and serves a clean proxy list.


> Scraper found **3870** proxies at the latest update. Usable proxies are below.

## Usage

Click the file format that you want and copy the URL.


|File|Content|Count|
|----|-------|-----|
|[data.txt](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.txt)|`ip_address:port` combined (seperated new line)|287|
|[data.json](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.json)|`ip, port`|287|
|[data-with-geolocation.json](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data-with-geolocation.json)|`ip, port, geolocation`|287|

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
|[proxyscrape.com](https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all)|472|✅|
|[github.com/clarketm/proxy-list](https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt)|400|✅|
|[github.com/monosans/proxy-list](https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt)|176|✅|
|[github.com/TheSpeedX/PROXY-List](https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt)|1939|✅|


## Sample Proxies With Geolocation Info

|#|Ip|Port|Country|City|Internet Service Provider|
|-|--|----|-------|----|-------------------------|
|1|34.82.235.224|3128|United States|The Dalles|Google LLC|
|2|45.76.13.167|59394|United States|Piscataway|The Constant Company|
|3|202.182.117.88|59394|Japan|Heiwajima|The Constant Company|
|4|34.82.235.224|3128|United States|The Dalles|Google LLC|
|5|177.184.149.37|8080|Brazil|Criciúma|Unifique TelecomunicaÔÔes SA|
|6|128.199.94.96|3128|Singapore|Singapore|DigitalOcean, LLC|
|7|198.52.241.12|999|Puerto Rico|Corozal|OSNET Wireless|
|8|77.238.129.14|55443|Russia|Voronezh|LLC Intercon|
|9|186.67.230.45|3128|Chile|Santiago|Entel Chile S.A.|
|10|45.76.13.167|59394|United States|Piscataway|The Constant Company|
|11|189.63.232.244|3128|Brazil|Ribeirão Preto|Claro S.A.|
|12|103.155.156.46|1080|Indonesia|Bogor|Mulkan|
|13|188.133.153.143|8080|Russia|Moscow|Enforta-MSK|
|14|47.74.226.8|5001|Singapore|Singapore|Alibaba Cloud (Singapore) Private Limited|
|15|143.208.57.58|8080|Guatemala|Guatemala City|Comunicaciones Metropolitanas Cablecolor|
|16|62.205.169.74|53281|Russia|Moscow|CORBINA|
|17|20.47.108.204|8888|United States|Boydton|Microsoft Corporation|
|18|92.255.187.47|8080|Russia|Omsk|JSC "ER-Telecom Holding"|
|19|87.103.175.250|9812|Russia|Irkutsk|PJSC Rostelecom|
|20|190.26.201.194|8080|Colombia|Bogotá|ETB - Colombia|



## Contributing

Contributions are welcome, and they are greatly appreciated! Every
little bit helps, and credit will always be given.

