
# Free HTTP Proxy List 🌍

[![Hourly Update](https://github.com/mertguvencli/http-proxy-list/actions/workflows/main.yml/badge.svg?branch=main)](https://github.com/mertguvencli/http-proxy-list/actions/workflows/main.yml)
![GitHub](https://img.shields.io/github/license/mertguvencli/http-proxy-list)
![GitHub last commit](https://img.shields.io/github/last-commit/mertguvencli/http-proxy-list)

It is a lightweight project that hourly scrapes lots of free-proxy sites, validates if it works, and serves a clean proxy list.


> Scraper found **3682** proxies at the latest update. Usable proxies are below.

## Usage

Click the file format that you want and copy the URL.


|File|Content|Count|
|----|-------|-----|
|[data.txt](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.txt)|`ip_address:port` combined (seperated new line)|101|
|[data.json](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.json)|`ip, port`|101|
|[data-with-geolocation.json](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data-with-geolocation.json)|`ip, port, geolocation`|101|

## Sources

|Source|Found Proxies|Succeed|
|------|-------------|-------|
|[free-proxy-list.net](https://free-proxy-list.net)|300|✅|
|[us-proxy.org](https://www.us-proxy.org)|200|✅|
|[proxydb.net](http://proxydb.net)|15|✅|
|[free-proxy-list.com](https://free-proxy-list.com/?page=&port=&type%5B%5D=http&type%5B%5D=https&up_time=0&search=Search)|0|🚫|
|[proxy-list.download](https://www.proxy-list.download/HTTP)|26|✅|
|[vpnoverview.com](https://vpnoverview.com/privacy/anonymous-browsing/free-proxy-servers)|32|✅|
|[proxyscan.io](https://www.proxyscan.io)|100|✅|
|[proxylist.geonode.com](https://proxylist.geonode.com/api/proxy-list?limit=300&page=1&sort_by=lastChecked&sort_type=desc&protocols=http,https)|300|✅|
|[proxyscrape.com](https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all)|259|✅|
|[github.com/clarketm/proxy-list](https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt)|400|✅|
|[github.com/monosans/proxy-list](https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt)|128|✅|
|[github.com/TheSpeedX/PROXY-List](https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt)|1922|✅|


## Sample Proxies With Geolocation Info

|#|Ip|Port|Country|City|Internet Service Provider|
|-|--|----|-------|----|-------------------------|
|1|18.206.33.119|8888|United States|Ashburn|Amazon.com, Inc.|
|2|47.252.3.228|21016|United States|Charlottesville|Alibaba.com LLC|
|3|95.216.249.203|83|Finland|Helsinki|Hetzner Online GmbH|
|4|18.196.34.179|36228|Germany|Frankfurt am Main|Amazon Technologies Inc.|
|5|3.105.250.121|26009|Australia|Sydney|Amazon Technologies Inc.|
|6|177.93.48.74|999|Colombia|Puerto Gaitan|TV AZTECA SUCURSAL COLOMBIA|
|7|84.205.17.234|8080|Poland|Szczecinek|Gawex Media Sp.zoo|
|8|77.50.104.110|3128|Russia|Moscow|StarLink Telecom Network|
|9|49.231.140.120|8080|Thailand|Ratchathewi|Advanced Wireless Network Company Limited|
|10|202.137.15.253|3888|Indonesia|Jakarta|LINKNET|
|11|91.232.241.114|8080|Ukraine|Lviv|LEOTEL Ltd.|
|12|139.180.129.113|14097|Singapore|Singapore|The Constant Company, LLC|
|13|201.174.239.18|8080|Mexico|General Escobedo|Transtelco Inc|
|14|103.155.54.73|83|India|Murshidabad|Pegasuswave Private Limited|
|15|14.1.102.41|3127|Bangladesh|Faridpurahati|Windstream Communication Ltd|
|16|212.12.69.43|8080|Russia|Moscow|Telecommunication Center Ostankino|
|17|162.150.62.93|443|United States|Kincaid|Comcast Cable Communications, LLC|
|18|122.155.165.191|3128|Thailand|Ratchathewi|CAT Telecom Public Company Limited|
|19|179.70.107.119|8080|Brazil|Salvador|Telemar Norte Leste S.A.|
|20|121.156.109.108|8080|South Korea|Seongnam-si|Korea Telecom|



## Contributing

Contributions are welcome, and they are greatly appreciated! Every
little bit helps, and credit will always be given.

