
# Free HTTP Proxy List 🌍

[![Hourly Update](https://github.com/mertguvencli/http-proxy-list/actions/workflows/main.yml/badge.svg?branch=main)](https://github.com/mertguvencli/http-proxy-list/actions/workflows/main.yml)
![GitHub](https://img.shields.io/github/license/mertguvencli/http-proxy-list)
![GitHub last commit](https://img.shields.io/github/last-commit/mertguvencli/http-proxy-list)

It is a lightweight project that hourly scrapes lots of free-proxy sites, validates if it works, and serves a clean proxy list.


> Scraper found **3610** proxies at the latest update. Usable proxies are below.

## Usage

Click the file format that you want and copy the URL.


|File|Content|Count|
|----|-------|-----|
|[data.txt](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.txt)|`ip_address:port` combined (seperated new line)|191|
|[data.json](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.json)|`ip, port`|191|
|[data-with-geolocation.json](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data-with-geolocation.json)|`ip, port, geolocation`|191|

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
|[proxylist.geonode.com](https://proxylist.geonode.com/api/proxy-list?limit=300&page=1&sort_by=lastChecked&sort_type=desc&protocols=http,https)|289|✅|
|[proxyscrape.com](https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all)|330|✅|
|[github.com/clarketm/proxy-list](https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt)|400|✅|
|[github.com/monosans/proxy-list](https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt)|112|✅|
|[github.com/TheSpeedX/PROXY-List](https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt)|1896|✅|


## Sample Proxies With Geolocation Info

|#|Ip|Port|Country|City|Internet Service Provider|
|-|--|----|-------|----|-------------------------|
|1|64.227.97.114|3128|United States|Santa Clara|DigitalOcean, LLC|
|2|34.70.140.116|80|United States|Council Bluffs|Google LLC|
|3|167.172.133.122|3128|United States|North Bergen|DigitalOcean, LLC|
|4|35.170.197.3|8888|United States|Ashburn|Amazon.com, Inc.|
|5|104.131.109.98|3128|United States|Clifton|DigitalOcean, LLC|
|6|64.227.97.114|3128|United States|Santa Clara|DigitalOcean, LLC|
|7|64.227.67.196|3128|Netherlands|Amsterdam|DigitalOcean, LLC|
|8|81.4.102.223|8081|Netherlands|Amsterdam|WeservIT|
|9|34.70.140.116|80|United States|Council Bluffs|Google LLC|
|10|134.209.201.238|3128|Netherlands|Amsterdam|DigitalOcean, LLC|
|11|81.4.102.233|8081|Netherlands|Amsterdam|WeservIT|
|12|181.205.20.194|999|Colombia|Medellín|EPM Telecomunicaciones S.A. E.S.P.|
|13|167.172.133.122|3128|United States|North Bergen|DigitalOcean, LLC|
|14|45.167.124.5|9992|Colombia|Guapi|Sepcom Comunicaciones SAS|
|15|35.170.197.3|8888|United States|Ashburn|Amazon.com, Inc.|
|16|104.131.109.98|3128|United States|Clifton|DigitalOcean, LLC|
|17|51.79.65.236|8088|Canada|Beauharnois|OVH SAS|
|18|183.111.25.253|80|South Korea|Seongnam-si|Korea Telecom|
|19|121.156.109.108|8080|South Korea|Seongnam-si|Korea Telecom|
|20|85.14.243.31|3128|Germany|Meerbusch|myLoc managed IT AG|



## Contributing

Contributions are welcome, and they are greatly appreciated! Every
little bit helps, and credit will always be given.

