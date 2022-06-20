
# Free HTTP Proxy List 🌍

[![Hourly Update](https://github.com/mertguvencli/http-proxy-list/actions/workflows/main.yml/badge.svg?branch=main)](https://github.com/mertguvencli/http-proxy-list/actions/workflows/main.yml)
![GitHub](https://img.shields.io/github/license/mertguvencli/http-proxy-list)
![GitHub last commit](https://img.shields.io/github/last-commit/mertguvencli/http-proxy-list)

It is a lightweight project that hourly scrapes lots of free-proxy sites, validates if it works, and serves a clean proxy list.


> Scraper found **3991** proxies at the latest update. Usable proxies are below.

## Usage

Click the file format that you want and copy the URL.


|File|Content|Count|
|----|-------|-----|
|[data.txt](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.txt)|`ip_address:port` combined (seperated new line)|355|
|[data.json](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.json)|`ip, port`|355|
|[data-with-geolocation.json](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data-with-geolocation.json)|`ip, port, geolocation`|355|

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
|[proxyscrape.com](https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all)|528|✅|
|[github.com/clarketm/proxy-list](https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt)|400|✅|
|[github.com/monosans/proxy-list](https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt)|263|✅|
|[github.com/TheSpeedX/PROXY-List](https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt)|1917|✅|


## Sample Proxies With Geolocation Info

|#|Ip|Port|Country|City|Internet Service Provider|
|-|--|----|-------|----|-------------------------|
|1|172.104.24.22|3128|United States|Cedar Knolls|Linode, LLC|
|2|66.196.238.179|3128|United States|Houston|Logix|
|3|172.104.24.22|3128|United States|Cedar Knolls|Linode, LLC|
|4|66.94.116.111|3128|United States|New York|Contabo Inc.|
|5|5.189.232.13|3128|Russia|St Petersburg|OOO "Network of data-centers "Selectel"|
|6|45.167.124.5|9992|Colombia|Guapi|Sepcom Comunicaciones SAS|
|7|47.252.4.64|8888|United States|Charlottesville|Alibaba.com LLC|
|8|173.212.224.134|3128|Germany|Nuremberg|Contabo GmbH|
|9|47.240.160.90|10001|Hong Kong|Central|Alibaba.com LLC|
|10|95.217.72.253|3128|Finland|Helsinki|Hetzner Online GmbH|
|11|95.217.72.247|3128|Finland|Helsinki|Hetzner Online GmbH|
|12|183.111.25.253|8080|South Korea|Seongnam-si|Korea Telecom|
|13|161.97.129.98|3128|Germany|Düsseldorf|Contabo GmbH|
|14|157.100.12.138|999|Ecuador|Quito|Telconet S.A|
|15|110.170.126.13|3128|Thailand|Din Daeng|True Internet Corporation CO. Ltd.|
|16|194.233.69.90|443|Singapore|Singapore|Contabo Asia Private Limited|
|17|66.94.116.111|3128|United States|New York|Contabo Inc.|
|18|194.233.73.109|443|Singapore|Singapore|Contabo Asia Private Limited|
|19|194.233.73.105|443|Singapore|Singapore|Contabo Asia Private Limited|
|20|191.252.181.61|8888|Brazil|Itacoatiara|Locaweb Serviços de Internet S/A|



## Contributing

Contributions are welcome, and they are greatly appreciated! Every
little bit helps, and credit will always be given.

