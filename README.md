
# Free HTTP Proxy List 🌍

[![Hourly Update](https://github.com/mertguvencli/http-proxy-list/actions/workflows/main.yml/badge.svg?branch=main)](https://github.com/mertguvencli/http-proxy-list/actions/workflows/main.yml)
![GitHub](https://img.shields.io/github/license/mertguvencli/http-proxy-list)
![GitHub last commit](https://img.shields.io/github/last-commit/mertguvencli/http-proxy-list)

It is a lightweight project that hourly scrapes lots of free-proxy sites, validates if it works, and serves a clean proxy list.


> Scraper found **3803** proxies at the latest update. Usable proxies are below.

## Usage

Click the file format that you want and copy the URL.


|File|Content|Count|
|----|-------|-----|
|[data.txt](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.txt)|`ip_address:port` combined (seperated new line)|131|
|[data.json](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.json)|`ip, port`|131|
|[data-with-geolocation.json](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data-with-geolocation.json)|`ip, port, geolocation`|131|

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
|[proxyscrape.com](https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all)|289|✅|
|[github.com/clarketm/proxy-list](https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt)|400|✅|
|[github.com/monosans/proxy-list](https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt)|170|✅|
|[github.com/TheSpeedX/PROXY-List](https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt)|2061|✅|


## Sample Proxies With Geolocation Info

|#|Ip|Port|Country|City|Internet Service Provider|
|-|--|----|-------|----|-------------------------|
|1|20.47.108.204|8888|United States|Boydton|Microsoft Corporation|
|2|20.47.108.204|8888|United States|Boydton|Microsoft Corporation|
|3|93.158.214.153|3128|Netherlands|Amsterdam|Serverius Holding B.V.|
|4|185.88.158.34|3128|Russia|St Petersburg|LLC Country Online|
|5|47.240.160.90|10001|Hong Kong|Central|Alibaba.com LLC|
|6|89.107.197.165|3128|Russia|Tula|LLC TK Altair|
|7|200.105.215.18|33630|Bolivia|La Paz|AXS Bolivia S. A.|
|8|93.158.214.155|3128|Netherlands|Amsterdam|Serverius Holding B.V.|
|9|95.216.137.15|31337|Finland|Helsinki|Hetzner Online GmbH|
|10|41.60.239.199|8080|Kenya|Nairobi|Maintainer Liquid Telecommunications Operations Limited|
|11|139.59.95.209|80|India|Bengaluru|DIGITALOCEAN|
|12|190.26.201.194|8080|Colombia|Bogotá|ETB - Colombia|
|13|134.209.25.223|3128|United Kingdom|London|DigitalOcean, LLC|
|14|157.100.12.138|999|Ecuador|Quito|Telconet S.A|
|15|5.167.141.239|3128|Russia|Tula|CJSC "ER-Telecom Holding" Tula branch|
|16|195.43.168.10|3128|Italy|Fusignano|Irideos S.P.A.|
|17|47.89.185.178|8888|United States|Charlottesville|Alibaba.com LLC|
|18|183.111.25.253|8080|South Korea|Seongnam-si|Korea Telecom|
|19|173.212.245.135|3128|Germany|Nuremberg|Contabo GmbH|
|20|37.120.192.154|8080|Netherlands|Amsterdam|M247 Ltd|



## Contributing

Contributions are welcome, and they are greatly appreciated! Every
little bit helps, and credit will always be given.

