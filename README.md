
# Free HTTP Proxy List 🌍

[![Hourly Update](https://github.com/mertguvencli/http-proxy-list/actions/workflows/main.yml/badge.svg?branch=main)](https://github.com/mertguvencli/http-proxy-list/actions/workflows/main.yml)
![GitHub](https://img.shields.io/github/license/mertguvencli/http-proxy-list)
![GitHub last commit](https://img.shields.io/github/last-commit/mertguvencli/http-proxy-list)

It is a lightweight project that hourly scrapes lots of free-proxy sites, validates if it works, and serves a clean proxy list.


> Scraper found **3650** proxies at the latest update. Usable proxies are below.

## Usage

Click the file format that you want and copy the URL.


|File|Content|Count|
|----|-------|-----|
|[data.txt](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.txt)|`ip_address:port` combined (seperated new line)|190|
|[data.json](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.json)|`ip, port`|190|
|[data-with-geolocation.json](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data-with-geolocation.json)|`ip, port, geolocation`|190|

## Sources

|Source|Found Proxies|Succeed|
|------|-------------|-------|
|[free-proxy-list.net](https://free-proxy-list.net)|300|✅|
|[us-proxy.org](https://www.us-proxy.org)|200|✅|
|[proxydb.net](http://proxydb.net)|15|✅|
|[free-proxy-list.com](https://free-proxy-list.com/?page=&port=&type%5B%5D=http&type%5B%5D=https&up_time=0&search=Search)|0|🚫|
|[proxy-list.download](https://www.proxy-list.download/HTTP)|26|✅|
|[vpnoverview.com](https://vpnoverview.com/privacy/anonymous-browsing/free-proxy-servers)|32|✅|
|[proxyscan.io](https://www.proxyscan.io)|0|🚫|
|[proxylist.geonode.com](https://proxylist.geonode.com/api/proxy-list?limit=300&page=1&sort_by=lastChecked&sort_type=desc&protocols=http,https)|300|✅|
|[proxyscrape.com](https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all)|326|✅|
|[github.com/clarketm/proxy-list](https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt)|400|✅|
|[github.com/monosans/proxy-list](https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt)|214|✅|
|[github.com/TheSpeedX/PROXY-List](https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt)|1837|✅|


## Sample Proxies With Geolocation Info

|#|Ip|Port|Country|City|Internet Service Provider|
|-|--|----|-------|----|-------------------------|
|1|168.8.209.253|80|United States|Roswell|Board of Regents of the University System of Georgia|
|2|186.233.186.60|8080|United States|Chicago|Maxihost LTDA|
|3|18.218.45.35|3128|United States|Dublin|Amazon.com, Inc.|
|4|168.8.209.253|80|United States|Roswell|Board of Regents of the University System of Georgia|
|5|186.233.186.60|8080|United States|Chicago|Maxihost LTDA|
|6|121.254.195.12|8080|South Korea|Yongsan-dong|LG DACOM Corporation|
|7|117.20.216.218|8080|South Korea|Gumi|HYUNDAI COMMUNICATIONS & NETWORK|
|8|66.70.178.214|9300|Canada|Beauharnois|OVH SAS|
|9|47.91.24.231|80|Japan|Tokyo|Alibaba.com LLC|
|10|45.190.249.100|8080|Brazil|Passo Fundo|RK Telecom Provedor Internet LTDA|
|11|122.155.165.191|3128|Thailand|Ratchathewi|CAT Telecom Public Company Limited|
|12|136.243.37.84|9090|Germany|Falkenstein|Hetzner Online GmbH|
|13|190.71.64.180|8080|Colombia|Santiago de Cali|EPM Telecomunicaciones S.A. E.S.P|
|14|47.245.53.132|80|Japan|Tokyo|Alibaba.com LLC|
|15|190.107.224.150|3128|Chile|Santiago|WOM S.A.|
|16|181.143.235.100|12345|Colombia|Santiago de Cali|EPM Telecomunicaciones S.A. E.S.P.|
|17|47.245.54.114|80|Japan|Tokyo|Alibaba.com LLC|
|18|177.53.152.138|999|Peru|Lima|Moreno Yanoc Nemias Bernardo|
|19|148.0.121.171|999|Dominican Republic|La Romana|Compañía Dominicana de Teléfonos S. A.|
|20|200.92.152.50|999|Mexico|Culiacán|Mega Cable, S.A. de C.V.|



## Contributing

Contributions are welcome, and they are greatly appreciated! Every
little bit helps, and credit will always be given.

