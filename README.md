
# Free HTTP Proxy List 🌍

[![Hourly Update](https://github.com/mertguvencli/http-proxy-list/actions/workflows/main.yml/badge.svg?branch=main)](https://github.com/mertguvencli/http-proxy-list/actions/workflows/main.yml)
![GitHub](https://img.shields.io/github/license/mertguvencli/http-proxy-list)
![GitHub last commit](https://img.shields.io/github/last-commit/mertguvencli/http-proxy-list)

It is a lightweight project that hourly scrapes lots of free-proxy sites, validates if it works, and serves a clean proxy list.


> Scraper found **3558** proxies at the latest update. Usable proxies are below.

## Usage

Click the file format that you want and copy the URL.


|File|Content|Count|
|----|-------|-----|
|[data.txt](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.txt)|`ip_address:port` combined (seperated new line)|144|
|[data.json](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.json)|`ip, port`|144|
|[data-with-geolocation.json](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data-with-geolocation.json)|`ip, port, geolocation`|144|

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
|[proxyscrape.com](https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all)|219|✅|
|[github.com/clarketm/proxy-list](https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt)|400|✅|
|[github.com/monosans/proxy-list](https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt)|125|✅|
|[github.com/TheSpeedX/PROXY-List](https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt)|1931|✅|


## Sample Proxies With Geolocation Info

|#|Ip|Port|Country|City|Internet Service Provider|
|-|--|----|-------|----|-------------------------|
|1|185.221.134.234|3129|United States|Los Angeles|DediPath|
|2|198.206.133.34|8118|United States|Franklin|Wisconsin CyberLynk Network, Inc.|
|3|209.182.235.252|3128|United States|Los Angeles|HIVELOCITY, Inc.|
|4|198.206.133.34|8118|United States|Franklin|Wisconsin CyberLynk Network, Inc.|
|5|144.91.127.126|3128|Germany|Nuremberg|Contabo GmbH|
|6|37.233.99.212|3128|Poland|Warsaw|Techstorage sp. z o.o.|
|7|185.221.134.234|3129|United States|Los Angeles|DediPath|
|8|209.182.235.252|3128|United States|Los Angeles|HIVELOCITY, Inc.|
|9|188.127.237.151|3128|Russia|Moscow|LLC Smart Ape|
|10|216.238.76.66|59394|Mexico|Mexico City|The Constant Company|
|11|157.185.163.54|59394|United States|Monrovia|Quantil Networks Inc|
|12|154.13.5.41|59394|United States|San Jose|Zhihua Lu trading as HostHub|
|13|45.190.79.176|999|Mexico|Yahualica de Gonzalez Gallo|Meta Networks SA De CV|
|14|138.68.238.19|31028|United States|Santa Clara|DigitalOcean, LLC|
|15|8.210.66.212|3128|Hong Kong|Hong Kong|Alibaba.com LLC|
|16|165.16.74.224|8080|Libya|Tripoli|Aljeel Aljadeed Technology|
|17|206.189.195.74|8080|United States|North Bergen|DigitalOcean, LLC|
|18|45.58.168.180|59394|Netherlands|Amsterdam|Sharktech|
|19|12.218.209.130|53281|United States|San Carlos|AT&T Services, Inc.|
|20|185.76.9.123|3128|Sweden|Stockholm|DataCamp Limited|



## Contributing

Contributions are welcome, and they are greatly appreciated! Every
little bit helps, and credit will always be given.

