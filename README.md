
# Free HTTP Proxy List 🌍

[![Hourly Update](https://github.com/mertguvencli/http-proxy-list/actions/workflows/main.yml/badge.svg?branch=main)](https://github.com/mertguvencli/http-proxy-list/actions/workflows/main.yml)
![GitHub](https://img.shields.io/github/license/mertguvencli/http-proxy-list)
![GitHub last commit](https://img.shields.io/github/last-commit/mertguvencli/http-proxy-list)

It is a lightweight project that hourly scrapes lots of free-proxy sites, validates if it works, and serves a clean proxy list.


> Scraper found **4200** proxies at the latest update. Usable proxies are below.

## Usage

Click the file format that you want and copy the URL.


|File|Content|Count|
|----|-------|-----|
|[data.txt](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.txt)|`ip_address:port` combined (seperated new line)|416|
|[data.json](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.json)|`ip, port`|416|
|[data-with-geolocation.json](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data-with-geolocation.json)|`ip, port, geolocation`|416|

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
|[proxyscrape.com](https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all)|531|✅|
|[github.com/clarketm/proxy-list](https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt)|400|✅|
|[github.com/monosans/proxy-list](https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt)|246|✅|
|[github.com/TheSpeedX/PROXY-List](https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt)|2040|✅|


## Sample Proxies With Geolocation Info

|#|Ip|Port|Country|City|Internet Service Provider|
|-|--|----|-------|----|-------------------------|
|1|170.39.118.187|3128|United States|Ashburn|Rackdog, LLC|
|2|20.47.108.204|8888|United States|Boydton|Microsoft Corporation|
|3|34.145.226.144|8080|United States|Washington|Google LLC|
|4|35.170.197.3|8888|United States|Ashburn|Amazon.com, Inc.|
|5|104.131.109.98|3128|United States|Clifton|DigitalOcean, LLC|
|6|66.196.238.178|3128|United States|Houston|Logix|
|7|200.110.168.159|8080|Colombia|Trujillo|Media Commerce Partners S.A|
|8|45.167.124.5|9992|Colombia|Guapi|Sepcom Comunicaciones SAS|
|9|170.39.118.187|3128|United States|Ashburn|Rackdog, LLC|
|10|189.164.118.26|3128|Mexico|Ciudad de Atlixco|Uninet S.A. de C.V|
|11|20.47.108.204|8888|United States|Boydton|Microsoft Corporation|
|12|173.212.224.134|3128|Germany|Nuremberg|Contabo GmbH|
|13|35.170.197.3|8888|United States|Ashburn|Amazon.com, Inc.|
|14|65.21.206.151|3128|Finland|Helsinki|Hetzner Online GmbH|
|15|34.145.226.144|8080|United States|Washington|Google LLC|
|16|104.131.109.98|3128|United States|Clifton|DigitalOcean, LLC|
|17|45.89.65.128|3128|Russia|Moscow|Network Management Ltd|
|18|157.100.12.138|999|Ecuador|Quito|Telconet S.A|
|19|66.196.238.178|3128|United States|Houston|Logix|
|20|95.0.168.50|1981|Turkey|Mugla|Turk Telekomunikasyon Anonim Sirketi|



## Contributing

Contributions are welcome, and they are greatly appreciated! Every
little bit helps, and credit will always be given.

