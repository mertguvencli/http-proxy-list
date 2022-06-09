
# Free HTTP Proxy List 🌍

[![Hourly Update](https://github.com/mertguvencli/http-proxy-list/actions/workflows/main.yml/badge.svg?branch=main)](https://github.com/mertguvencli/http-proxy-list/actions/workflows/main.yml)
![GitHub](https://img.shields.io/github/license/mertguvencli/http-proxy-list)
![GitHub last commit](https://img.shields.io/github/last-commit/mertguvencli/http-proxy-list)

It is a lightweight project that hourly scrapes lots of free-proxy sites, validates if it works, and serves a clean proxy list.


> Scraper found **3763** proxies at the latest update. Usable proxies are below.

## Usage

Click the file format that you want and copy the URL.


|File|Content|Count|
|----|-------|-----|
|[data.txt](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.txt)|`ip_address:port` combined (seperated new line)|208|
|[data.json](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.json)|`ip, port`|208|
|[data-with-geolocation.json](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data-with-geolocation.json)|`ip, port, geolocation`|208|

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
|[proxyscrape.com](https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all)|476|✅|
|[github.com/clarketm/proxy-list](https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt)|400|✅|
|[github.com/monosans/proxy-list](https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt)|139|✅|
|[github.com/TheSpeedX/PROXY-List](https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt)|1865|✅|


## Sample Proxies With Geolocation Info

|#|Ip|Port|Country|City|Internet Service Provider|
|-|--|----|-------|----|-------------------------|
|1|20.47.108.204|8888|United States|Boydton|Microsoft Corporation|
|2|20.47.108.204|8888|United States|Boydton|Microsoft Corporation|
|3|167.71.199.228|8080|Singapore|Singapore|DigitalOcean, LLC|
|4|183.111.25.253|8080|South Korea|Seongnam-si|Korea Telecom|
|5|91.151.89.32|1697|Turkey|Sisli|Talha Bogaz|
|6|68.183.185.62|80|Singapore|Singapore|DigitalOcean, LLC|
|7|95.217.72.253|3128|Finland|Helsinki|Hetzner Online GmbH|
|8|157.100.12.138|999|Ecuador|Quito|Telconet S.A|
|9|183.88.3.16|8080|Thailand|Nakhon Ratchasima|Triple T Broadband Public Company Limited|
|10|188.166.228.110|8080|Singapore|Singapore|DigitalOcean, LLC|
|11|194.233.73.108|443|Singapore|Singapore|Contabo Asia Private Limited|
|12|187.216.93.20|55443|Mexico|Ciudad Obregón|Uninet S.A. de C.V.|
|13|190.97.226.236|999|Venezuela|Barinas|NetLink América C.A.|
|14|183.88.18.206|8080|Thailand|Ban Du|Triple T Broadband Public Company Limited|
|15|203.150.113.57|8080|Thailand|Bangkok|Internet Thailand Company Ltd.|
|16|194.233.73.109|443|Singapore|Singapore|Contabo Asia Private Limited|
|17|178.47.139.151|35102|Russia|Osa|PJSC Rostelecom|
|18|200.42.203.96|8080|Dominican Republic|Santo Domingo|Altice Dominicana S.A.|
|19|182.52.83.48|8080|Thailand|Bangkok|TOT Public Company Limited|
|20|91.107.15.221|53281|Russia|Lytkarino|AVK-computer ltd|



## Contributing

Contributions are welcome, and they are greatly appreciated! Every
little bit helps, and credit will always be given.

