
# Free HTTP Proxy List 🌍

[![Hourly Update](https://github.com/mertguvencli/http-proxy-list/actions/workflows/main.yml/badge.svg?branch=main)](https://github.com/mertguvencli/http-proxy-list/actions/workflows/main.yml)
![GitHub](https://img.shields.io/github/license/mertguvencli/http-proxy-list)
![GitHub last commit](https://img.shields.io/github/last-commit/mertguvencli/http-proxy-list)

It is a lightweight project that hourly scrapes lots of free-proxy sites, validates if it works, and serves a clean proxy list.


> Scraper found **4123** proxies at the latest update. Usable proxies are below.

## Usage

Click the file format that you want and copy the URL.


|File|Content|Count|
|----|-------|-----|
|[data.txt](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.txt)|`ip_address:port` combined (seperated new line)|282|
|[data.json](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.json)|`ip, port`|282|
|[data-with-geolocation.json](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data-with-geolocation.json)|`ip, port, geolocation`|282|

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
|[proxyscrape.com](https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all)|513|✅|
|[github.com/clarketm/proxy-list](https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt)|400|✅|
|[github.com/monosans/proxy-list](https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt)|151|✅|
|[github.com/TheSpeedX/PROXY-List](https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt)|2076|✅|


## Sample Proxies With Geolocation Info

|#|Ip|Port|Country|City|Internet Service Provider|
|-|--|----|-------|----|-------------------------|
|1|216.74.246.194|3129|United States|Houston|Logix|
|2|20.81.62.32|3128|United States|Boydton|Microsoft Corporation|
|3|50.17.76.20|3128|United States|Ashburn|Amazon.com|
|4|50.17.41.16|8080|United States|Ashburn|Amazon.com|
|5|34.220.50.208|3128|United States|Portland|Amazon.com, Inc.|
|6|54.234.116.166|3128|United States|Ashburn|Amazon.com, Inc.|
|7|216.74.246.194|3129|United States|Houston|Logix|
|8|50.17.41.16|8080|United States|Ashburn|Amazon.com|
|9|54.234.116.166|3128|United States|Ashburn|Amazon.com, Inc.|
|10|50.17.76.20|3128|United States|Ashburn|Amazon.com|
|11|34.220.50.208|3128|United States|Portland|Amazon.com, Inc.|
|12|78.46.123.202|80|Germany|Falkenstein|Hetzner Online GmbH|
|13|3.127.33.188|3128|Germany|Frankfurt am Main|Amazon Technologies Inc.|
|14|162.55.166.114|3128|Germany|Falkenstein|Hetzner Online GmbH|
|15|168.119.58.120|3128|Germany|Falkenstein|Hetzner Online GmbH|
|16|213.136.72.147|3128|Germany|Nuremberg|Contabo GmbH|
|17|65.108.55.63|3128|Finland|Helsinki|Hetzner Online GmbH|
|18|185.76.9.123|3128|Sweden|Stockholm|DataCamp Limited|
|19|20.81.62.32|3128|United States|Boydton|Microsoft Corporation|
|20|110.170.126.13|3128|Thailand|Din Daeng|True Internet Corporation CO. Ltd.|



## Contributing

Contributions are welcome, and they are greatly appreciated! Every
little bit helps, and credit will always be given.

