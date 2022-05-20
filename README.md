
# Free HTTP Proxy List 🌍

[![Hourly Update](https://github.com/mertguvencli/http-proxy-list/actions/workflows/main.yml/badge.svg?branch=main)](https://github.com/mertguvencli/http-proxy-list/actions/workflows/main.yml)
![GitHub](https://img.shields.io/github/license/mertguvencli/http-proxy-list)
![GitHub last commit](https://img.shields.io/github/last-commit/mertguvencli/http-proxy-list)

It is a lightweight project that hourly scrapes lots of free-proxy sites, validates if it works, and serves a clean proxy list.


> Scraper found **3903** proxies at the latest update. Usable proxies are below.

## Usage

Click the file format that you want and copy the URL.


|File|Content|Count|
|----|-------|-----|
|[data.txt](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.txt)|`ip_address:port` combined (seperated new line)|271|
|[data.json](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.json)|`ip, port`|271|
|[data-with-geolocation.json](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data-with-geolocation.json)|`ip, port, geolocation`|271|

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
|[proxyscrape.com](https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all)|491|✅|
|[github.com/clarketm/proxy-list](https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt)|400|✅|
|[github.com/monosans/proxy-list](https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt)|330|✅|
|[github.com/TheSpeedX/PROXY-List](https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt)|1999|✅|


## Sample Proxies With Geolocation Info

|#|Ip|Port|Country|City|Internet Service Provider|
|-|--|----|-------|----|-------------------------|
|1|168.8.209.253|80|United States|Roswell|Board of Regents of the University System of Georgia|
|2|66.196.238.178|3128|United States|Tomball|Logix|
|3|51.81.32.81|8888|United States|Reston|OVH SAS|
|4|64.184.92.8|80|United States|Amboy|Intelligent Fiber Network|
|5|190.97.226.236|999|Venezuela|Barinas|NetLink América C.A.|
|6|121.254.195.12|8080|South Korea|Yongsan-dong|LG DACOM Corporation|
|7|168.8.209.253|80|United States|Roswell|Board of Regents of the University System of Georgia|
|8|18.118.139.123|3128|United States|Dublin|Amazon.com, Inc.|
|9|66.196.238.178|3128|United States|Tomball|Logix|
|10|51.81.32.81|8888|United States|Reston|OVH SAS|
|11|139.59.228.95|8118|Singapore|Singapore|DIGITALOCEAN|
|12|185.103.168.78|8080|Kazakhstan|Nur-Sultan|JSC Alma Telecommunications|
|13|128.199.214.87|3128|Singapore|Singapore|Partner Communications Ltd.|
|14|95.0.219.240|8080|Turkey|Kayseri|TurkTelecom|
|15|109.238.222.5|40387|Czechia|Libis|Planet A, a.s.|
|16|18.118.139.123|3128|United States|Dublin|Amazon.com, Inc.|
|17|45.189.254.26|999|Mexico|Alvarado|Tracered SA De CV|
|18|41.193.63.89|8080|South Africa|Empangeni|Vox Telecom|
|19|177.87.144.122|5566|Brazil|Sao Jose do Rio Pardo|Rosimara Bertoluci Sassi Sampaio Eireli|
|20|5.189.184.6|80|Germany|Nuremberg|Contabo GmbH|



## Contributing

Contributions are welcome, and they are greatly appreciated! Every
little bit helps, and credit will always be given.

