
# Free HTTP Proxy List 🌍

[![Hourly Update](https://github.com/mertguvencli/http-proxy-list/actions/workflows/main.yml/badge.svg?branch=main)](https://github.com/mertguvencli/http-proxy-list/actions/workflows/main.yml)
![GitHub](https://img.shields.io/github/license/mertguvencli/http-proxy-list)
![GitHub last commit](https://img.shields.io/github/last-commit/mertguvencli/http-proxy-list)

It is a lightweight project that hourly scrapes lots of free-proxy sites, validates if it works, and serves a clean proxy list.


> Scraper found **3302** proxies at the latest update. Usable proxies are below.

## Usage

Click the file format that you want and copy the URL.


|File|Content|Count|
|----|-------|-----|
|[data.txt](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.txt)|`ip_address:port` combined (seperated new line)|61|
|[data.json](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.json)|`ip, port`|61|
|[data-with-geolocation.json](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data-with-geolocation.json)|`ip, port, geolocation`|61|

## Sources

|Source|Found Proxies|Succeed|
|------|-------------|-------|
|[free-proxy-list.net](https://free-proxy-list.net)|300|✅|
|[us-proxy.org](https://www.us-proxy.org)|200|✅|
|[proxydb.net](http://proxydb.net)|15|✅|
|[free-proxy-list.com](https://free-proxy-list.com/?page=&port=&type%5B%5D=http&type%5B%5D=https&up_time=0&search=Search)|10|✅|
|[proxy-list.download](https://www.proxy-list.download/HTTP)|26|✅|
|[vpnoverview.com](https://vpnoverview.com/privacy/anonymous-browsing/free-proxy-servers)|32|✅|
|[proxyscan.io](https://www.proxyscan.io)|72|✅|
|[proxylist.geonode.com](https://proxylist.geonode.com/api/proxy-list?limit=300&page=1&sort_by=lastChecked&sort_type=desc&protocols=http,https)|300|✅|
|[proxyscrape.com](https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all)|133|✅|
|[github.com/clarketm/proxy-list](https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt)|400|✅|
|[github.com/monosans/proxy-list](https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt)|37|✅|
|[github.com/TheSpeedX/PROXY-List](https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt)|1777|✅|


## Sample Proxies With Geolocation Info

|#|Ip|Port|Country|City|Internet Service Provider|
|-|--|----|-------|----|-------------------------|
|1|157.100.12.138|999|Ecuador|Quito|Telconet S.A|
|2|190.97.226.236|999|Venezuela|Barinas|NetLink América C.A.|
|3|190.26.201.194|8080|Colombia|Bogotá|ETB - Colombia|
|4|144.76.60.220|8118|Germany|Falkenstein|Hetzner Online GmbH|
|5|135.181.255.194|80|Finland|Helsinki|Hetzner Online GmbH|
|6|190.97.226.236|999|Venezuela|Barinas|NetLink América C.A.|
|7|95.217.72.253|3128|Finland|Helsinki|Hetzner Online GmbH|
|8|103.214.9.13|3128|Vietnam|Hanoi|MEGACORE|
|9|84.201.254.47|3128|Russia|Izhevsk|JSC "ER-Telecom Holding"|
|10|95.217.72.253|3128|Finland|Helsinki|Hetzner Online GmbH|
|11|64.225.8.192|80|United States|Clifton|DigitalOcean, LLC|
|12|95.217.72.247|3128|Finland|Helsinki|Hetzner Online GmbH|
|13|157.100.12.138|999|Ecuador|Quito|Telconet S.A|
|14|47.74.226.8|5001|Singapore|Singapore|Alibaba Cloud (Singapore) Private Limited|
|15|190.128.225.117|999|Paraguay|Asunción|Telecel S.A.|
|16|46.188.53.7|8004|Russia|Moscow|2COM|
|17|45.190.249.100|8080|Brazil|Passo Fundo|RK Telecom Provedor Internet LTDA|
|18|218.1.142.84|57114|China|Shanghai|China Telecom|
|19|157.90.222.231|8080|Germany|Falkenstein|Hetzner Online GmbH|
|20|103.124.137.40|8080|Indonesia|Purbayan|PT.Global Media Data Prima|



## Contributing

Contributions are welcome, and they are greatly appreciated! Every
little bit helps, and credit will always be given.

