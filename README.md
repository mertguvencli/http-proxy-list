
# Free HTTP Proxy List 🌍

[![Hourly Update](https://github.com/mertguvencli/http-proxy-list/actions/workflows/main.yml/badge.svg?branch=main)](https://github.com/mertguvencli/http-proxy-list/actions/workflows/main.yml)
![GitHub](https://img.shields.io/github/license/mertguvencli/http-proxy-list)
![GitHub last commit](https://img.shields.io/github/last-commit/mertguvencli/http-proxy-list)

It is a lightweight project that hourly scrapes lots of free-proxy sites, validates if it works, and serves a clean proxy list.


> Scraper found **3662** proxies at the latest update. Usable proxies are below.

## Usage

Click the file format that you want and copy the URL.


|File|Content|Count|
|----|-------|-----|
|[data.txt](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.txt)|`ip_address:port` combined (seperated new line)|257|
|[data.json](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.json)|`ip, port`|257|
|[data-with-geolocation.json](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data-with-geolocation.json)|`ip, port, geolocation`|257|

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
|[proxyscrape.com](https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all)|298|✅|
|[github.com/clarketm/proxy-list](https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt)|400|✅|
|[github.com/monosans/proxy-list](https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt)|273|✅|
|[github.com/TheSpeedX/PROXY-List](https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt)|2008|✅|


## Sample Proxies With Geolocation Info

|#|Ip|Port|Country|City|Internet Service Provider|
|-|--|----|-------|----|-------------------------|
|1|20.47.108.204|8888|United States|Boydton|Microsoft Corporation|
|2|20.47.108.204|8888|United States|Boydton|Microsoft Corporation|
|3|66.42.125.237|59394|United States|Elk Grove Village|The Constant Company|
|4|66.42.125.237|59394|United States|Elk Grove Village|The Constant Company|
|5|147.135.134.57|9300|France|Gravelines|OVH SAS|
|6|66.94.120.161|443|United States|Seattle|Contabo Inc.|
|7|182.160.116.114|9812|Bangladesh|Dhaka|Aamra Networks Limited|
|8|81.23.151.27|8080|Russia|Kazan’|Rostelecom networks|
|9|119.82.25.58|10001|Japan|Chiyoda|JMF Investment & Technology PTY LTD|
|10|66.94.120.161|443|United States|Seattle|Contabo Inc.|
|11|95.216.182.127|31289|Finland|Helsinki|Hetzner Online GmbH|
|12|202.69.38.82|8080|Pakistan|Lahore|Advertiese Flag|
|13|190.26.201.194|8080|Colombia|Bogotá|ETB - Colombia|
|14|190.26.201.194|8080|Colombia|Bogotá|ETB - Colombia|
|15|129.215.41.142|3128|United Kingdom|Edinburgh|University of Edinburgh|
|16|103.147.52.237|3127|Indonesia|Batam|KejoraNet|
|17|186.67.230.45|3128|Chile|Santiago|Entel Chile S.A.|
|18|189.90.248.31|8080|Brazil|Mariana|Companhia Itabirana TelecomunicaÔÔes Ltda|
|19|121.156.109.108|8080|South Korea|Seongnam-si|Korea Telecom|
|20|93.185.123.154|3128|Italy|Pove del Grappa|Omegacom S.R.L.S.|



## Contributing

Contributions are welcome, and they are greatly appreciated! Every
little bit helps, and credit will always be given.

