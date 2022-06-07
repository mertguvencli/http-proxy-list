
# Free HTTP Proxy List 🌍

[![Hourly Update](https://github.com/mertguvencli/http-proxy-list/actions/workflows/main.yml/badge.svg?branch=main)](https://github.com/mertguvencli/http-proxy-list/actions/workflows/main.yml)
![GitHub](https://img.shields.io/github/license/mertguvencli/http-proxy-list)
![GitHub last commit](https://img.shields.io/github/last-commit/mertguvencli/http-proxy-list)

It is a lightweight project that hourly scrapes lots of free-proxy sites, validates if it works, and serves a clean proxy list.


> Scraper found **3579** proxies at the latest update. Usable proxies are below.

## Usage

Click the file format that you want and copy the URL.


|File|Content|Count|
|----|-------|-----|
|[data.txt](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.txt)|`ip_address:port` combined (seperated new line)|155|
|[data.json](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.json)|`ip, port`|155|
|[data-with-geolocation.json](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data-with-geolocation.json)|`ip, port, geolocation`|155|

## Sources

|Source|Found Proxies|Succeed|
|------|-------------|-------|
|[free-proxy-list.net](https://free-proxy-list.net)|300|✅|
|[us-proxy.org](https://www.us-proxy.org)|200|✅|
|[proxydb.net](http://proxydb.net)|15|✅|
|[free-proxy-list.com](https://free-proxy-list.com/?page=&port=&type%5B%5D=http&type%5B%5D=https&up_time=0&search=Search)|10|✅|
|[proxy-list.download](https://www.proxy-list.download/HTTP)|26|✅|
|[vpnoverview.com](https://vpnoverview.com/privacy/anonymous-browsing/free-proxy-servers)|32|✅|
|[proxyscan.io](https://www.proxyscan.io)|50|✅|
|[proxylist.geonode.com](https://proxylist.geonode.com/api/proxy-list?limit=300&page=1&sort_by=lastChecked&sort_type=desc&protocols=http,https)|300|✅|
|[proxyscrape.com](https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all)|304|✅|
|[github.com/clarketm/proxy-list](https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt)|400|✅|
|[github.com/monosans/proxy-list](https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt)|106|✅|
|[github.com/TheSpeedX/PROXY-List](https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt)|1836|✅|


## Sample Proxies With Geolocation Info

|#|Ip|Port|Country|City|Internet Service Provider|
|-|--|----|-------|----|-------------------------|
|1|66.196.238.179|3128|United States|Tomball|Logix|
|2|20.47.108.204|8888|United States|Boydton|Microsoft Corporation|
|3|54.93.165.96|30001|Germany|Frankfurt am Main|Amazon Technologies Inc.|
|4|51.15.166.107|3128|France|Paris|SCALEWAY|
|5|118.174.175.86|8080|Thailand|Khwaeng Thung Song Hong|TOT Public Company Limited|
|6|101.109.176.145|8080|Thailand|Kanchanaburi|TOT Public Company Limited|
|7|190.61.61.70|8080|Colombia|Buriticá|Ufinet Panama S.A.|
|8|94.155.221.220|3128|Bulgaria|Sofia|"Cooolbox" AD|
|9|138.197.69.179|8080|United States|Clifton|DigitalOcean, LLC|
|10|181.129.248.141|999|Colombia|Santiago de Cali|EPM Telecomunicaciones S.A. E.S.P.|
|11|110.170.126.13|3128|Thailand|Din Daeng|True Internet Corporation CO. Ltd.|
|12|35.157.249.83|33128|Germany|Frankfurt am Main|Amazon Technologies Inc.|
|13|103.103.212.222|53281|India|Indore|Five Net Service Provider Pvt. Ltd.|
|14|54.93.165.96|30001|Germany|Frankfurt am Main|Amazon Technologies Inc.|
|15|190.97.226.236|999|Venezuela|Barinas|NetLink América C.A.|
|16|54.93.165.96|30001|Germany|Frankfurt am Main|Amazon Technologies Inc.|
|17|41.60.234.250|8080|Kenya|Nairobi|Maintainer Liquid Telecommunications Operations Limited|
|18|91.205.49.71|8080|Kyrgyzstan|Bishkek|SR-FASTNET|
|19|101.200.127.149|3129|China|Beijing|Hangzhou Alibaba Advertising Co|
|20|95.217.72.253|3128|Finland|Helsinki|Hetzner Online GmbH|



## Contributing

Contributions are welcome, and they are greatly appreciated! Every
little bit helps, and credit will always be given.

