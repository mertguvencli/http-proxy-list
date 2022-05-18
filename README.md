
# Free HTTP Proxy List 🌍

[![Hourly Update](https://github.com/mertguvencli/http-proxy-list/actions/workflows/main.yml/badge.svg?branch=main)](https://github.com/mertguvencli/http-proxy-list/actions/workflows/main.yml)
![GitHub](https://img.shields.io/github/license/mertguvencli/http-proxy-list)
![GitHub last commit](https://img.shields.io/github/last-commit/mertguvencli/http-proxy-list)

It is a lightweight project that hourly scrapes lots of free-proxy sites, validates if it works, and serves a clean proxy list.


> Scraper found **4231** proxies at the latest update. Usable proxies are below.

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
|[free-proxy-list.com](https://free-proxy-list.com/?page=&port=&type%5B%5D=http&type%5B%5D=https&up_time=0&search=Search)|10|✅|
|[proxy-list.download](https://www.proxy-list.download/HTTP)|26|✅|
|[vpnoverview.com](https://vpnoverview.com/privacy/anonymous-browsing/free-proxy-servers)|32|✅|
|[proxyscan.io](https://www.proxyscan.io)|100|✅|
|[proxylist.geonode.com](https://proxylist.geonode.com/api/proxy-list?limit=300&page=1&sort_by=lastChecked&sort_type=desc&protocols=http,https)|300|✅|
|[proxyscrape.com](https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all)|356|✅|
|[github.com/clarketm/proxy-list](https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt)|400|✅|
|[github.com/monosans/proxy-list](https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt)|429|✅|
|[github.com/TheSpeedX/PROXY-List](https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt)|2063|✅|


## Sample Proxies With Geolocation Info

|#|Ip|Port|Country|City|Internet Service Provider|
|-|--|----|-------|----|-------------------------|
|1|185.105.108.208|8080|Netherlands|Amsterdam|Serverius|
|2|186.67.230.45|3128|Chile|Santiago|Entel Chile S.A.|
|3|194.233.86.75|7777|Singapore|Singapore|Contabo Asia Private Limited|
|4|45.189.252.130|999|Mexico|Alvarado|Tracered SA De CV|
|5|87.103.175.250|9812|Russia|Irkutsk|PJSC Rostelecom|
|6|121.254.195.12|8080|South Korea|Yongsan-dong|LG DACOM Corporation|
|7|103.121.199.142|8080|Indonesia|Lumajang|PT Parsaoran Global Datatrans|
|8|64.225.8.192|80|United States|Clifton|DigitalOcean, LLC|
|9|105.112.134.209|8080|Nigeria|Lagos|Airtel Networks Limited|
|10|110.78.143.206|80|Thailand|Ban Kha|CAT-BB|
|11|177.141.99.50|8080|Brazil|São Paulo|Claro S.A.|
|12|200.172.255.195|8080|Brazil|Rio de Janeiro|Claro S.A.|
|13|41.60.232.92|8080|Kenya|Nairobi|Maintainer Liquid Telecommunications Operations Limited|
|14|135.181.1.241|50057|Finland|Helsinki|Hetzner Online GmbH|
|15|103.209.248.86|8080|Indonesia|Panjangjiwo|Indonesia Network Information Center|
|16|186.67.192.246|8080|Chile|Las Condes|Entel Chile S.A.|
|17|51.79.152.70|80|Singapore|Singapore|OVH SAS|
|18|148.251.66.8|3128|Germany|Falkenstein|Hetzner Online GmbH|
|19|82.114.97.157|1256|Russia|Moscow|Enforta-MSK|
|20|101.133.231.6|80|China|Shanghai|Hangzhou Alibaba Advertising Co|



## Contributing

Contributions are welcome, and they are greatly appreciated! Every
little bit helps, and credit will always be given.

