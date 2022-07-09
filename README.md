
# Free HTTP Proxy List 🌍

[![Hourly Update](https://github.com/mertguvencli/http-proxy-list/actions/workflows/main.yml/badge.svg?branch=main)](https://github.com/mertguvencli/http-proxy-list/actions/workflows/main.yml)
![GitHub](https://img.shields.io/github/license/mertguvencli/http-proxy-list)
![GitHub last commit](https://img.shields.io/github/last-commit/mertguvencli/http-proxy-list)

It is a lightweight project that hourly scrapes lots of free-proxy sites, validates if it works, and serves a clean proxy list.


> Scraper found **3753** proxies at the latest update. Usable proxies are below.

## Usage

Click the file format that you want and copy the URL.


|File|Content|Count|
|----|-------|-----|
|[data.txt](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.txt)|`ip_address:port` combined (seperated new line)|128|
|[data.json](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.json)|`ip, port`|128|
|[data-with-geolocation.json](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data-with-geolocation.json)|`ip, port, geolocation`|128|

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
|[proxylist.geonode.com](https://proxylist.geonode.com/api/proxy-list?limit=300&page=1&sort_by=lastChecked&sort_type=desc&protocols=http,https)|228|✅|
|[proxyscrape.com](https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all)|361|✅|
|[github.com/clarketm/proxy-list](https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt)|400|✅|
|[github.com/monosans/proxy-list](https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt)|209|✅|
|[github.com/TheSpeedX/PROXY-List](https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt)|1872|✅|


## Sample Proxies With Geolocation Info

|#|Ip|Port|Country|City|Internet Service Provider|
|-|--|----|-------|----|-------------------------|
|1|198.41.67.18|8080|United States|Lafayette|Cox Communications Inc.|
|2|45.152.188.246|3128|United States|Ashburn|Sprint|
|3|20.47.108.204|8888|United States|Boydton|Microsoft Corporation|
|4|45.152.188.246|3128|United States|Ashburn|Sprint|
|5|85.14.243.31|3128|Germany|Kamp-Lintfort|myLoc managed IT AG|
|6|20.81.62.32|3128|United States|Boydton|Microsoft Corporation|
|7|201.76.56.127|3128|Brazil|Itacoatiara|Locaweb Serviços de Internet S/A|
|8|157.100.12.138|999|Ecuador|Loja|Telconet S.A|
|9|198.41.67.18|8080|United States|Lafayette|Cox Communications Inc.|
|10|157.185.163.54|59394|United States|Monrovia|Quantil Networks Inc|
|11|209.97.152.208|8888|United States|Clifton|DigitalOcean, LLC|
|12|20.81.62.32|3128|United States|Boydton|Microsoft Corporation|
|13|182.253.109.30|8080|Indonesia|Banjaranyar|Biznet Metronet|
|14|45.184.73.16|40033|Brazil|Queimadas|A2 TELECOM PROVEDOR DE INTERNET LTDA|
|15|143.198.182.218|80|United States|North Bergen|DigitalOcean, LLC|
|16|45.229.205.246|55555|Argentina|Dock Sud|Visio RED SRL|
|17|157.185.145.59|59394|United States|Los Angeles|Quantil Networks Inc|
|18|110.170.126.13|3128|Thailand|Din Daeng|True Internet Corporation CO. Ltd.|
|19|154.13.5.41|59394|Canada|Montreal|Zhihua Lu trading as HostHub|
|20|206.189.195.74|8080|United States|North Bergen|DigitalOcean, LLC|



## Contributing

Contributions are welcome, and they are greatly appreciated! Every
little bit helps, and credit will always be given.

