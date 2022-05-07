
# Free HTTP Proxy List 🌍

[![Hourly Update](https://github.com/mertguvencli/http-proxy-list/actions/workflows/main.yml/badge.svg?branch=main)](https://github.com/mertguvencli/http-proxy-list/actions/workflows/main.yml)
![GitHub](https://img.shields.io/github/license/mertguvencli/http-proxy-list)
![GitHub last commit](https://img.shields.io/github/last-commit/mertguvencli/http-proxy-list)

It is a lightweight project that hourly scrapes lots of free-proxy sites, validates if it works, and serves a clean proxy list.


> Scraper found **3720** proxies at the latest update. Usable proxies are below.

## Usage

Click the file format that you want and copy the URL.


|File|Content|Count|
|----|-------|-----|
|[data.txt](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.txt)|`ip_address:port` combined (seperated new line)|172|
|[data.json](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.json)|`ip, port`|172|
|[data-with-geolocation.json](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data-with-geolocation.json)|`ip, port, geolocation`|172|

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
|[proxyscrape.com](https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all)|440|✅|
|[github.com/clarketm/proxy-list](https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt)|400|✅|
|[github.com/monosans/proxy-list](https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt)|270|✅|
|[github.com/TheSpeedX/PROXY-List](https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt)|1927|✅|


## Sample Proxies With Geolocation Info

|#|Ip|Port|Country|City|Internet Service Provider|
|-|--|----|-------|----|-------------------------|
|1|186.67.230.45|3128|Chile|Santiago|Entel Chile S.A.|
|2|200.105.215.18|33630|Bolivia|La Paz|AXS Bolivia S. A.|
|3|94.253.104.223|55443|Russia|Noginsk|for Flex Ltd|
|4|194.233.69.38|443|Singapore|Singapore|Contabo Asia Private Limited|
|5|200.6.254.254|999|Guatemala|Quetzaltenango|Telgua|
|6|187.94.98.222|8080|Brazil|Sao Jose|Unifique Telecomunicações SA|
|7|194.233.69.41|443|Singapore|Singapore|Contabo Asia Private Limited|
|8|41.60.233.229|8080|Kenya|Nairobi|Maintainer Liquid Telecommunications Operations Limited|
|9|20.47.108.204|8888|United States|Boydton|Microsoft Corporation|
|10|179.107.25.14|8080|Brazil|Ponta Grossa|Nova Fibra Telecom S.A.|
|11|190.26.201.194|8080|Colombia|Bogotá|ETB - Colombia|
|12|190.26.201.194|8080|Colombia|Bogotá|ETB - Colombia|
|13|95.0.168.56|1981|Turkey|Dalyan|Turk Telekomunikasyon Anonim Sirketi|
|14|158.255.212.55|10434|Austria|Vienna|EDIS GmbH|
|15|186.233.186.60|8080|United States|Chicago|Maxihost LTDA|
|16|190.107.224.150|3128|Chile|Santiago|WOM S.A.|
|17|186.67.230.45|3128|Chile|Santiago|Entel Chile S.A.|
|18|72.47.152.224|55443|United States|Ben Wheeler|Suddenlink Communications|
|19|51.89.33.32|20000|United Kingdom|London|OVH SAS|
|20|122.155.165.191|3128|Thailand|Ratchathewi|CAT Telecom Public Company Limited|



## Contributing

Contributions are welcome, and they are greatly appreciated! Every
little bit helps, and credit will always be given.

