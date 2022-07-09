
# Free HTTP Proxy List 🌍

[![Hourly Update](https://github.com/mertguvencli/http-proxy-list/actions/workflows/main.yml/badge.svg?branch=main)](https://github.com/mertguvencli/http-proxy-list/actions/workflows/main.yml)
![GitHub](https://img.shields.io/github/license/mertguvencli/http-proxy-list)
![GitHub last commit](https://img.shields.io/github/last-commit/mertguvencli/http-proxy-list)

It is a lightweight project that hourly scrapes lots of free-proxy sites, validates if it works, and serves a clean proxy list.


> Scraper found **3308** proxies at the latest update. Usable proxies are below.

## Usage

Click the file format that you want and copy the URL.


|File|Content|Count|
|----|-------|-----|
|[data.txt](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.txt)|`ip_address:port` combined (seperated new line)|136|
|[data.json](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.json)|`ip, port`|136|
|[data-with-geolocation.json](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data-with-geolocation.json)|`ip, port, geolocation`|136|

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
|[proxyscrape.com](https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all)|219|✅|
|[github.com/clarketm/proxy-list](https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt)|400|✅|
|[github.com/monosans/proxy-list](https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt)|117|✅|
|[github.com/TheSpeedX/PROXY-List](https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt)|1889|✅|


## Sample Proxies With Geolocation Info

|#|Ip|Port|Country|City|Internet Service Provider|
|-|--|----|-------|----|-------------------------|
|1|45.152.188.246|3128|United States|Ashburn|Sprint|
|2|20.81.62.32|3128|United States|Boydton|Microsoft Corporation|
|3|209.182.235.252|3128|United States|Los Angeles|HIVELOCITY, Inc.|
|4|45.152.188.246|3128|United States|Ashburn|Sprint|
|5|20.47.108.204|8888|United States|Boydton|Microsoft Corporation|
|6|188.40.15.7|8080|Germany|Falkenstein|Hetzner Online GmbH|
|7|189.157.89.26|999|Mexico|San Luis Potosí City|Uninet S.A. de C.V|
|8|20.81.62.32|3128|United States|Boydton|Microsoft Corporation|
|9|185.76.9.87|3128|Sweden|Stockholm|DataCamp Limited|
|10|185.76.9.123|3128|Sweden|Stockholm|DataCamp Limited|
|11|195.201.111.241|3128|Germany|Gunzenhausen|Hetzner Online GmbH|
|12|201.76.56.127|3128|Brazil|Itacoatiara|Locaweb Serviços de Internet S/A|
|13|209.182.235.252|3128|United States|Los Angeles|HIVELOCITY, Inc.|
|14|157.100.12.138|999|Ecuador|Loja|Telconet S.A|
|15|210.115.46.228|3128|South Korea|Chuncheon|Kangwon National University|
|16|64.189.24.250|3129|United States|Chicago|WhiteSky Communications, LLC.|
|17|165.22.250.146|8888|Singapore|Singapore|DigitalOcean, LLC|
|18|64.189.24.250|3129|United States|Chicago|WhiteSky Communications, LLC.|
|19|8.219.97.248|80|Singapore|Singapore|Alibaba (US) Technology Co., Ltd.|
|20|92.118.92.107|8181|Russia|Krasnodar|TSK LLC|



## Contributing

Contributions are welcome, and they are greatly appreciated! Every
little bit helps, and credit will always be given.

