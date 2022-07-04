
# Free HTTP Proxy List 🌍

[![Hourly Update](https://github.com/mertguvencli/http-proxy-list/actions/workflows/main.yml/badge.svg?branch=main)](https://github.com/mertguvencli/http-proxy-list/actions/workflows/main.yml)
![GitHub](https://img.shields.io/github/license/mertguvencli/http-proxy-list)
![GitHub last commit](https://img.shields.io/github/last-commit/mertguvencli/http-proxy-list)

It is a lightweight project that hourly scrapes lots of free-proxy sites, validates if it works, and serves a clean proxy list.


> Scraper found **3351** proxies at the latest update. Usable proxies are below.

## Usage

Click the file format that you want and copy the URL.


|File|Content|Count|
|----|-------|-----|
|[data.txt](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.txt)|`ip_address:port` combined (seperated new line)|135|
|[data.json](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.json)|`ip, port`|135|
|[data-with-geolocation.json](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data-with-geolocation.json)|`ip, port, geolocation`|135|

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
|[proxylist.geonode.com](https://proxylist.geonode.com/api/proxy-list?limit=300&page=1&sort_by=lastChecked&sort_type=desc&protocols=http,https)|0|🚫|
|[proxyscrape.com](https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all)|206|✅|
|[github.com/clarketm/proxy-list](https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt)|400|✅|
|[github.com/monosans/proxy-list](https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt)|79|✅|
|[github.com/TheSpeedX/PROXY-List](https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt)|1983|✅|


## Sample Proxies With Geolocation Info

|#|Ip|Port|Country|City|Internet Service Provider|
|-|--|----|-------|----|-------------------------|
|1|45.152.188.246|3128|United States|Ashburn|Sprint|
|2|12.231.44.251|3128|United States|Racine|AT&T Services, Inc.|
|3|158.69.59.125|8888|Canada|Montreal|OVH SAS|
|4|104.255.183.34|999|Puerto Rico|Trujillo Alto|HRCOM|
|5|12.231.44.251|3128|United States|Racine|AT&T Services, Inc.|
|6|45.152.188.246|3128|United States|Ashburn|Sprint|
|7|51.250.80.131|80|Russia|Moscow|Yandex.Cloud LLC|
|8|190.90.95.122|8080|Colombia|Tabio|InterNexa Global Network|
|9|200.110.173.118|8080|Colombia|Santiago de Cali|Media Commerce Partners S.A|
|10|20.47.108.204|8888|United States|Boydton|Microsoft Corporation|
|11|179.49.117.226|999|Honduras|Yore|Asociacion De Servicio De Internet S. De RL.|
|12|45.167.124.5|9992|Colombia|Guapi|Sepcom Comunicaciones SAS|
|13|195.201.111.241|3128|Germany|Gunzenhausen|Hetzner Online GmbH|
|14|200.146.77.133|80|Brazil|Curitiba|Vivo|
|15|20.84.106.205|8214|United States|Boydton|Microsoft Corporation|
|16|210.179.58.236|80|South Korea|Goyang-si|Korea Telecom|
|17|185.76.9.87|3128|Sweden|Stockholm|DataCamp Limited|
|18|190.98.1.99|3128|Suriname|Paramaribo|Telecommunicationcompany Suriname - TeleSur|
|19|204.137.241.253|3129|United States|Towson|Apogee Telecom Inc.|
|20|179.49.117.226|999|Honduras|Yore|Asociacion De Servicio De Internet S. De RL.|



## Contributing

Contributions are welcome, and they are greatly appreciated! Every
little bit helps, and credit will always be given.

