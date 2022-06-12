
# Free HTTP Proxy List 🌍

[![Hourly Update](https://github.com/mertguvencli/http-proxy-list/actions/workflows/main.yml/badge.svg?branch=main)](https://github.com/mertguvencli/http-proxy-list/actions/workflows/main.yml)
![GitHub](https://img.shields.io/github/license/mertguvencli/http-proxy-list)
![GitHub last commit](https://img.shields.io/github/last-commit/mertguvencli/http-proxy-list)

It is a lightweight project that hourly scrapes lots of free-proxy sites, validates if it works, and serves a clean proxy list.


> Scraper found **3221** proxies at the latest update. Usable proxies are below.

## Usage

Click the file format that you want and copy the URL.


|File|Content|Count|
|----|-------|-----|
|[data.txt](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.txt)|`ip_address:port` combined (seperated new line)|84|
|[data.json](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.json)|`ip, port`|84|
|[data-with-geolocation.json](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data-with-geolocation.json)|`ip, port, geolocation`|84|

## Sources

|Source|Found Proxies|Succeed|
|------|-------------|-------|
|[free-proxy-list.net](https://free-proxy-list.net)|300|✅|
|[us-proxy.org](https://www.us-proxy.org)|200|✅|
|[proxydb.net](http://proxydb.net)|15|✅|
|[free-proxy-list.com](https://free-proxy-list.com/?page=&port=&type%5B%5D=http&type%5B%5D=https&up_time=0&search=Search)|10|✅|
|[proxy-list.download](https://www.proxy-list.download/HTTP)|26|✅|
|[vpnoverview.com](https://vpnoverview.com/privacy/anonymous-browsing/free-proxy-servers)|32|✅|
|[proxyscan.io](https://www.proxyscan.io)|62|✅|
|[proxylist.geonode.com](https://proxylist.geonode.com/api/proxy-list?limit=300&page=1&sort_by=lastChecked&sort_type=desc&protocols=http,https)|0|🚫|
|[proxyscrape.com](https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all)|208|✅|
|[github.com/clarketm/proxy-list](https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt)|400|✅|
|[github.com/monosans/proxy-list](https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt)|54|✅|
|[github.com/TheSpeedX/PROXY-List](https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt)|1914|✅|


## Sample Proxies With Geolocation Info

|#|Ip|Port|Country|City|Internet Service Provider|
|-|--|----|-------|----|-------------------------|
|1|149.19.224.38|3128|United States|Sterling|SPRINT|
|2|45.42.177.51|3128|United States|Ashburn|PeaceWeb|
|3|66.196.238.179|3128|United States|Houston|Logix|
|4|149.19.224.38|3128|United States|Sterling|SPRINT|
|5|45.42.177.51|3128|United States|Ashburn|PeaceWeb|
|6|200.105.215.18|33630|Bolivia|La Paz|AXS Bolivia S. A.|
|7|159.197.250.134|3128|United States|Mount Prospect|Sprint|
|8|190.26.201.194|8080|Colombia|Bogotá|ETB - Colombia|
|9|45.167.124.5|9992|Colombia|Guapi|Sepcom Comunicaciones SAS|
|10|157.100.12.138|999|Ecuador|Quito|Telconet S.A|
|11|152.169.106.145|8080|Argentina|Neuquén|Telecom Argentina S.A|
|12|177.53.153.170|999|Peru|Lima|Moreno Yanoc Nemias Bernardo|
|13|157.100.12.138|999|Ecuador|Quito|Telconet S.A|
|14|103.159.90.22|84|India|Karimpur|Pegasuswave Private Limited|
|15|165.22.59.136|43126|Singapore|Singapore|DigitalOcean, LLC|
|16|164.70.122.6|3128|Japan|Chiyoda|NTT PC Communications, Inc.|
|17|177.53.153.168|999|Peru|Lima|Moreno Yanoc Nemias Bernardo|
|18|85.133.232.42|8080|Iran|Tehran|Sepanta Communication Development Co. Ltd|
|19|170.83.242.250|999|Paraguay|Asunción|Ufinet Panama S.A.|
|20|83.220.47.146|8080|Russia|Moscow|GARS|



## Contributing

Contributions are welcome, and they are greatly appreciated! Every
little bit helps, and credit will always be given.

