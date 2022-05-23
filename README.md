
# Free HTTP Proxy List 🌍

[![Hourly Update](https://github.com/mertguvencli/http-proxy-list/actions/workflows/main.yml/badge.svg?branch=main)](https://github.com/mertguvencli/http-proxy-list/actions/workflows/main.yml)
![GitHub](https://img.shields.io/github/license/mertguvencli/http-proxy-list)
![GitHub last commit](https://img.shields.io/github/last-commit/mertguvencli/http-proxy-list)

It is a lightweight project that hourly scrapes lots of free-proxy sites, validates if it works, and serves a clean proxy list.


> Scraper found **4080** proxies at the latest update. Usable proxies are below.

## Usage

Click the file format that you want and copy the URL.


|File|Content|Count|
|----|-------|-----|
|[data.txt](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.txt)|`ip_address:port` combined (seperated new line)|226|
|[data.json](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.json)|`ip, port`|226|
|[data-with-geolocation.json](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data-with-geolocation.json)|`ip, port, geolocation`|226|

## Sources

|Source|Found Proxies|Succeed|
|------|-------------|-------|
|[free-proxy-list.net](https://free-proxy-list.net)|300|✅|
|[us-proxy.org](https://www.us-proxy.org)|200|✅|
|[proxydb.net](http://proxydb.net)|15|✅|
|[free-proxy-list.com](https://free-proxy-list.com/?page=&port=&type%5B%5D=http&type%5B%5D=https&up_time=0&search=Search)|0|🚫|
|[proxy-list.download](https://www.proxy-list.download/HTTP)|26|✅|
|[vpnoverview.com](https://vpnoverview.com/privacy/anonymous-browsing/free-proxy-servers)|32|✅|
|[proxyscan.io](https://www.proxyscan.io)|100|✅|
|[proxylist.geonode.com](https://proxylist.geonode.com/api/proxy-list?limit=300&page=1&sort_by=lastChecked&sort_type=desc&protocols=http,https)|300|✅|
|[proxyscrape.com](https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all)|484|✅|
|[github.com/clarketm/proxy-list](https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt)|400|✅|
|[github.com/monosans/proxy-list](https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt)|238|✅|
|[github.com/TheSpeedX/PROXY-List](https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt)|1985|✅|


## Sample Proxies With Geolocation Info

|#|Ip|Port|Country|City|Internet Service Provider|
|-|--|----|-------|----|-------------------------|
|1|168.8.209.253|80|United States|Roswell|Board of Regents of the University System of Georgia|
|2|81.4.102.223|8081|Netherlands|Amsterdam|WeservIT|
|3|168.8.209.253|80|United States|Roswell|Board of Regents of the University System of Georgia|
|4|148.251.66.8|3128|Germany|Falkenstein|Hetzner Online GmbH|
|5|121.254.195.12|8080|South Korea|Yongsan-dong|LG DACOM Corporation|
|6|177.141.99.50|8080|Brazil|São Paulo|Claro S.A.|
|7|190.97.226.236|999|Venezuela|Barinas|NetLink América C.A.|
|8|139.99.88.19|8080|Singapore|Singapore|OVH SAS|
|9|118.99.73.208|8080|Indonesia|Jakarta|BIZNET|
|10|113.53.60.55|8080|Thailand|Chanthaburi|TOT Public Company Limited|
|11|5.167.141.239|3128|Russia|Tula|CJSC "ER-Telecom Holding" Tula branch|
|12|190.128.231.146|8080|Paraguay|Asunción|Telecel S.A.|
|13|5.189.184.6|80|Germany|Nuremberg|Contabo GmbH|
|14|47.91.25.94|80|Japan|Tokyo|Alibaba.com LLC|
|15|80.85.58.55|8080|Hungary|Bacsbokod|TV Cabletelevison Ltd.|
|16|45.195.76.150|8080|Dominican Republic|Santo Domingo Este|Orbitek SRL|
|17|5.131.243.11|8080|Russia|Moscow|Novotelecom Ltd|
|18|201.120.27.15|53281|Mexico|Hermosillo|Uninet S.A. de C.V|
|19|180.183.1.27|8080|Thailand|Bang Lamung|Triple T Broadband Public Company Limited|
|20|182.253.168.172|8080|Indonesia|Jakarta|BIZNET|



## Contributing

Contributions are welcome, and they are greatly appreciated! Every
little bit helps, and credit will always be given.

