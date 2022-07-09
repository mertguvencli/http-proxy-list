
# Free HTTP Proxy List 🌍

[![Hourly Update](https://github.com/mertguvencli/http-proxy-list/actions/workflows/main.yml/badge.svg?branch=main)](https://github.com/mertguvencli/http-proxy-list/actions/workflows/main.yml)
![GitHub](https://img.shields.io/github/license/mertguvencli/http-proxy-list)
![GitHub last commit](https://img.shields.io/github/last-commit/mertguvencli/http-proxy-list)

It is a lightweight project that hourly scrapes lots of free-proxy sites, validates if it works, and serves a clean proxy list.


> Scraper found **4030** proxies at the latest update. Usable proxies are below.

## Usage

Click the file format that you want and copy the URL.


|File|Content|Count|
|----|-------|-----|
|[data.txt](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.txt)|`ip_address:port` combined (seperated new line)|277|
|[data.json](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.json)|`ip, port`|277|
|[data-with-geolocation.json](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data-with-geolocation.json)|`ip, port, geolocation`|277|

## Sources

|Source|Found Proxies|Succeed|
|------|-------------|-------|
|[free-proxy-list.net](https://free-proxy-list.net)|300|✅|
|[us-proxy.org](https://www.us-proxy.org)|200|✅|
|[proxydb.net](http://proxydb.net)|15|✅|
|[free-proxy-list.com](https://free-proxy-list.com/?page=&port=&type%5B%5D=http&type%5B%5D=https&up_time=0&search=Search)|10|✅|
|[proxy-list.download](https://www.proxy-list.download/HTTP)|0|🚫|
|[vpnoverview.com](https://vpnoverview.com/privacy/anonymous-browsing/free-proxy-servers)|32|✅|
|[proxyscan.io](https://www.proxyscan.io)|100|✅|
|[proxylist.geonode.com](https://proxylist.geonode.com/api/proxy-list?limit=300&page=1&sort_by=lastChecked&sort_type=desc&protocols=http,https)|300|✅|
|[proxyscrape.com](https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all)|389|✅|
|[github.com/clarketm/proxy-list](https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt)|400|✅|
|[github.com/monosans/proxy-list](https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt)|307|✅|
|[github.com/TheSpeedX/PROXY-List](https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt)|1977|✅|


## Sample Proxies With Geolocation Info

|#|Ip|Port|Country|City|Internet Service Provider|
|-|--|----|-------|----|-------------------------|
|1|45.152.188.246|3128|United States|Ashburn|Sprint|
|2|198.41.67.18|8080|United States|Lafayette|Cox Communications Inc.|
|3|20.81.62.32|3128|United States|Boydton|Microsoft Corporation|
|4|20.47.108.204|8888|United States|Boydton|Microsoft Corporation|
|5|157.245.222.183|80|United States|Clifton|DigitalOcean, LLC|
|6|35.178.134.102|80|United Kingdom|London|Amazon Technologies Inc.|
|7|45.152.188.246|3128|United States|Ashburn|Sprint|
|8|198.41.67.18|8080|United States|Lafayette|Cox Communications Inc.|
|9|20.47.108.204|8888|United States|Boydton|Microsoft Corporation|
|10|209.97.152.208|8888|United States|Clifton|DigitalOcean, LLC|
|11|20.81.62.32|3128|United States|Boydton|Microsoft Corporation|
|12|190.152.5.17|39888|Ecuador|Guayaquil|Corporacion Nacional De Telecomunicaciones - CNT EP|
|13|47.74.226.8|5001|Singapore|Singapore|Alibaba Cloud (Singapore) Private Limited|
|14|158.69.71.245|9300|Canada|Montreal|OVH SAS|
|15|45.172.111.18|999|Argentina|Caucete|GPS SANJUAN SRL.|
|16|103.87.170.237|45585|India|Jaipur|Tejays Industries Pvt Ltd|
|17|154.13.5.42|59394|Canada|Montreal|Zhihua Lu trading as HostHub|
|18|154.13.5.41|59394|Canada|Montreal|Zhihua Lu trading as HostHub|
|19|144.91.75.133|3128|Germany|Nuremberg|Contabo GmbH|
|20|157.185.163.54|59394|United States|Monrovia|Quantil Networks Inc|



## Contributing

Contributions are welcome, and they are greatly appreciated! Every
little bit helps, and credit will always be given.

