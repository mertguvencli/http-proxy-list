
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
|[data.txt](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.txt)|`ip_address:port` combined (seperated new line)|135|
|[data.json](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.json)|`ip, port`|135|
|[data-with-geolocation.json](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data-with-geolocation.json)|`ip, port, geolocation`|135|

## Sources

|Source|Found Proxies|Succeed|
|------|-------------|-------|
|[free-proxy-list.net](https://free-proxy-list.net)|300|✅|
|[us-proxy.org](https://www.us-proxy.org)|200|✅|
|[proxydb.net](http://proxydb.net)|15|✅|
|[free-proxy-list.com](https://free-proxy-list.com/?page=&port=&type%5B%5D=http&type%5B%5D=https&up_time=0&search=Search)|10|✅|
|[proxy-list.download](https://www.proxy-list.download/HTTP)|26|✅|
|[vpnoverview.com](https://vpnoverview.com/privacy/anonymous-browsing/free-proxy-servers)|32|✅|
|[proxyscan.io](https://www.proxyscan.io)|96|✅|
|[proxylist.geonode.com](https://proxylist.geonode.com/api/proxy-list?limit=300&page=1&sort_by=lastChecked&sort_type=desc&protocols=http,https)|256|✅|
|[proxyscrape.com](https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all)|194|✅|
|[github.com/clarketm/proxy-list](https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt)|400|✅|
|[github.com/monosans/proxy-list](https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt)|62|✅|
|[github.com/TheSpeedX/PROXY-List](https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt)|2071|✅|


## Sample Proxies With Geolocation Info

|#|Ip|Port|Country|City|Internet Service Provider|
|-|--|----|-------|----|-------------------------|
|1|34.74.238.210|3128|United States|North Charleston|Google LLC|
|2|167.71.131.37|3128|United Kingdom|London|DigitalOcean, LLC|
|3|152.32.218.99|8000|Singapore|Singapore|UCLOUD INFORMATION TECHNOLOGY (HK) LIMITED|
|4|34.74.238.210|3128|United States|North Charleston|Google LLC|
|5|47.240.160.90|10001|Hong Kong|Central|Alibaba.com LLC|
|6|142.93.16.163|3128|United States|Santa Clara|DigitalOcean, LLC|
|7|119.15.86.130|8080|Cambodia|Phnom Penh|WiCAM Corporation Ltd|
|8|45.167.124.5|9992|Colombia|Guapi|Sepcom Comunicaciones SAS|
|9|95.217.72.253|3128|Finland|Helsinki|Hetzner Online GmbH|
|10|181.205.20.194|999|Colombia|Medellín|EPM Telecomunicaciones S.A. E.S.P.|
|11|186.97.182.3|999|Colombia|Medellín|Colombia Móvil|
|12|185.32.6.129|8090|Poland|Warsaw|AS Consulting Sp. z o. o.|
|13|220.247.171.242|8080|Indonesia|Gandul|PT Indonesia Comnets Plus|
|14|107.172.73.179|7890|United States|Buffalo|ColoCrossing|
|15|159.65.133.175|31280|Singapore|Singapore|DigitalOcean, LLC|
|16|158.140.181.148|8081|Indonesia|Bogor|MYREPUBLIC|
|17|119.59.125.189|3128|Thailand|Samphanthawong|Metrabyte Co., Ltd|
|18|207.244.236.144|3128|United States|St Louis|Contabo Inc.|
|19|95.217.72.253|3128|Finland|Helsinki|Hetzner Online GmbH|
|20|207.180.217.107|3128|Germany|Nuremberg|Contabo GmbH|



## Contributing

Contributions are welcome, and they are greatly appreciated! Every
little bit helps, and credit will always be given.

