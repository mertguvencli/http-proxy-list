
# Free HTTP Proxy List 🌍

[![Hourly Update](https://github.com/mertguvencli/http-proxy-list/actions/workflows/main.yml/badge.svg?branch=main)](https://github.com/mertguvencli/http-proxy-list/actions/workflows/main.yml)
![GitHub](https://img.shields.io/github/license/mertguvencli/http-proxy-list)
![GitHub last commit](https://img.shields.io/github/last-commit/mertguvencli/http-proxy-list)

It is a lightweight project that hourly scrapes lots of free-proxy sites, validates if it works, and serves a clean proxy list.


> Scraper found **3998** proxies at the latest update. Usable proxies are below.

## Usage

Click the file format that you want and copy the URL.


|File|Content|Count|
|----|-------|-----|
|[data.txt](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.txt)|`ip_address:port` combined (seperated new line)|303|
|[data.json](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.json)|`ip, port`|303|
|[data-with-geolocation.json](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data-with-geolocation.json)|`ip, port, geolocation`|303|

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
|[proxyscrape.com](https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all)|513|✅|
|[github.com/clarketm/proxy-list](https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt)|400|✅|
|[github.com/monosans/proxy-list](https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt)|221|✅|
|[github.com/TheSpeedX/PROXY-List](https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt)|1981|✅|


## Sample Proxies With Geolocation Info

|#|Ip|Port|Country|City|Internet Service Provider|
|-|--|----|-------|----|-------------------------|
|1|66.196.238.179|3128|United States|Houston|Logix|
|2|20.47.108.204|8888|United States|Boydton|Microsoft Corporation|
|3|35.170.197.3|8888|United States|Ashburn|Amazon.com, Inc.|
|4|18.188.193.74|3128|United States|Dublin|Amazon.com, Inc.|
|5|44.204.247.143|3128|United States|Ashburn|Amazon.com|
|6|167.114.185.69|3128|Canada|Montreal|OVH SAS|
|7|186.96.103.124|999|Colombia|Ortega|TV AZTECA SUCURSAL COLOMBIA|
|8|66.94.116.111|3128|United States|New York|Contabo Inc.|
|9|206.189.23.38|8048|United Kingdom|London|DigitalOcean, LLC|
|10|35.170.197.3|8888|United States|Ashburn|Amazon.com, Inc.|
|11|45.167.124.5|9992|Colombia|Guapi|Sepcom Comunicaciones SAS|
|12|44.204.247.143|3128|United States|Ashburn|Amazon.com|
|13|35.240.63.166|3128|Belgium|Brussels|Google LLC|
|14|134.209.25.223|3128|United Kingdom|London|DigitalOcean, LLC|
|15|18.188.193.74|3128|United States|Dublin|Amazon.com, Inc.|
|16|37.233.102.189|3128|Poland|Warsaw|Techstorage sp. z o.o.|
|17|183.111.25.253|8080|South Korea|Seongnam-si|Korea Telecom|
|18|37.233.102.188|3128|Poland|Warsaw|Techstorage sp. z o.o.|
|19|37.233.102.184|3128|Poland|Warsaw|Techstorage sp. z o.o.|
|20|172.105.166.114|31282|Australia|Sydney|Linode, LLC|



## Contributing

Contributions are welcome, and they are greatly appreciated! Every
little bit helps, and credit will always be given.

