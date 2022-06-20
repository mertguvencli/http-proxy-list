
# Free HTTP Proxy List 🌍

[![Hourly Update](https://github.com/mertguvencli/http-proxy-list/actions/workflows/main.yml/badge.svg?branch=main)](https://github.com/mertguvencli/http-proxy-list/actions/workflows/main.yml)
![GitHub](https://img.shields.io/github/license/mertguvencli/http-proxy-list)
![GitHub last commit](https://img.shields.io/github/last-commit/mertguvencli/http-proxy-list)

It is a lightweight project that hourly scrapes lots of free-proxy sites, validates if it works, and serves a clean proxy list.


> Scraper found **3941** proxies at the latest update. Usable proxies are below.

## Usage

Click the file format that you want and copy the URL.


|File|Content|Count|
|----|-------|-----|
|[data.txt](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.txt)|`ip_address:port` combined (seperated new line)|331|
|[data.json](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.json)|`ip, port`|331|
|[data-with-geolocation.json](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data-with-geolocation.json)|`ip, port, geolocation`|331|

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
|[github.com/monosans/proxy-list](https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt)|110|✅|
|[github.com/TheSpeedX/PROXY-List](https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt)|2072|✅|


## Sample Proxies With Geolocation Info

|#|Ip|Port|Country|City|Internet Service Provider|
|-|--|----|-------|----|-------------------------|
|1|20.47.108.204|8888|United States|Boydton|Microsoft Corporation|
|2|35.170.197.3|8888|United States|Ashburn|Amazon.com, Inc.|
|3|47.240.160.90|10001|Hong Kong|Central|Alibaba.com LLC|
|4|189.164.118.26|3128|Mexico|Ciudad de Atlixco|Uninet S.A. de C.V|
|5|45.167.124.5|9992|Colombia|Guapi|Sepcom Comunicaciones SAS|
|6|183.111.25.253|8080|South Korea|Seongnam-si|Korea Telecom|
|7|173.212.224.134|3128|Germany|Nuremberg|Contabo GmbH|
|8|65.21.206.151|3128|Finland|Helsinki|Hetzner Online GmbH|
|9|171.97.36.80|8080|Thailand|Bang Na|True Internet Corporation CO. Ltd.|
|10|152.32.218.99|8000|Singapore|Singapore|UCLOUD INFORMATION TECHNOLOGY (HK) LIMITED|
|11|157.100.12.138|999|Ecuador|Quito|Telconet S.A|
|12|47.74.226.8|5001|Singapore|Singapore|Alibaba Cloud (Singapore) Private Limited|
|13|138.2.93.172|8888|Singapore|Singapore|Oracle Corporation|
|14|187.49.190.41|999|Honduras|Juticalpa|Olancho NET S.r.l. De C.V.|
|15|45.70.236.123|999|Ecuador|Palestina|Nedetel S.A.|
|16|182.52.83.176|8080|Thailand|Satun|TOT Public Company Limited|
|17|195.182.133.107|3128|Russia|St Petersburg|Comlink Telecom Ltd.|
|18|185.15.172.212|3128|Russia|Moscow|SafeData LLC|
|19|144.217.75.65|8800|Canada|Beauharnois|OVH SAS|
|20|203.150.113.124|8080|Thailand|Watthana|Internet Thailand Company Ltd.|



## Contributing

Contributions are welcome, and they are greatly appreciated! Every
little bit helps, and credit will always be given.

