
# Free HTTP Proxy List 🌍

[![Hourly Update](https://github.com/mertguvencli/http-proxy-list/actions/workflows/main.yml/badge.svg?branch=main)](https://github.com/mertguvencli/http-proxy-list/actions/workflows/main.yml)
![GitHub](https://img.shields.io/github/license/mertguvencli/http-proxy-list)
![GitHub last commit](https://img.shields.io/github/last-commit/mertguvencli/http-proxy-list)

It is a lightweight project that hourly scrapes lots of free-proxy sites, validates if it works, and serves a clean proxy list.


> Scraper found **3438** proxies at the latest update. Usable proxies are below.

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
|[proxyscan.io](https://www.proxyscan.io)|100|✅|
|[proxylist.geonode.com](https://proxylist.geonode.com/api/proxy-list?limit=300&page=1&sort_by=lastChecked&sort_type=desc&protocols=http,https)|0|🚫|
|[proxyscrape.com](https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all)|305|✅|
|[github.com/clarketm/proxy-list](https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt)|400|✅|
|[github.com/monosans/proxy-list](https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt)|129|✅|
|[github.com/TheSpeedX/PROXY-List](https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt)|1921|✅|


## Sample Proxies With Geolocation Info

|#|Ip|Port|Country|City|Internet Service Provider|
|-|--|----|-------|----|-------------------------|
|1|45.152.188.246|3128|United States|Ashburn|Sprint|
|2|198.12.254.161|3128|United States|Ashburn|GoDaddy.com, LLC|
|3|45.152.188.246|3128|United States|Ashburn|Sprint|
|4|200.110.173.118|8080|Colombia|Santiago de Cali|Media Commerce Partners S.A|
|5|198.12.254.161|3128|United States|Ashburn|GoDaddy.com, LLC|
|6|35.86.85.128|3128|United States|Portland|Amazon.com, Inc.|
|7|45.167.124.5|9992|Colombia|Guapi|Sepcom Comunicaciones SAS|
|8|34.215.30.215|3128|United States|Portland|Amazon.com, Inc.|
|9|207.180.217.107|3128|Germany|Nuremberg|Contabo GmbH|
|10|20.203.160.74|3128|Switzerland|Zurich|Microsoft Corporation|
|11|35.86.85.128|3128|United States|Portland|Amazon.com, Inc.|
|12|167.235.63.238|3128|Germany|Falkenstein|Hetzner Online GmbH|
|13|34.215.30.215|3128|United States|Portland|Amazon.com, Inc.|
|14|65.108.233.231|3128|Finland|Helsinki|Hetzner Online GmbH|
|15|157.100.12.138|999|Ecuador|Loja|Telconet S.A|
|16|154.13.5.41|59394|United States|San Jose|Zhihua Lu trading as HostHub|
|17|190.98.1.99|3128|Suriname|Paramaribo|Telecommunicationcompany Suriname - TeleSur|
|18|51.250.80.131|80|Russia|Moscow|Yandex.Cloud LLC|
|19|213.32.75.44|9300|France|Paris|OVH SAS|
|20|114.4.104.254|3128|Indonesia|Jakarta|PT. INDOSAT Tbk|



## Contributing

Contributions are welcome, and they are greatly appreciated! Every
little bit helps, and credit will always be given.

