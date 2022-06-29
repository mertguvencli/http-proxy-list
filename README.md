
# Free HTTP Proxy List 🌍

[![Hourly Update](https://github.com/mertguvencli/http-proxy-list/actions/workflows/main.yml/badge.svg?branch=main)](https://github.com/mertguvencli/http-proxy-list/actions/workflows/main.yml)
![GitHub](https://img.shields.io/github/license/mertguvencli/http-proxy-list)
![GitHub last commit](https://img.shields.io/github/last-commit/mertguvencli/http-proxy-list)

It is a lightweight project that hourly scrapes lots of free-proxy sites, validates if it works, and serves a clean proxy list.


> Scraper found **3366** proxies at the latest update. Usable proxies are below.

## Usage

Click the file format that you want and copy the URL.


|File|Content|Count|
|----|-------|-----|
|[data.txt](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.txt)|`ip_address:port` combined (seperated new line)|66|
|[data.json](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.json)|`ip, port`|66|
|[data-with-geolocation.json](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data-with-geolocation.json)|`ip, port, geolocation`|66|

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
|[proxyscrape.com](https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all)|264|✅|
|[github.com/clarketm/proxy-list](https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt)|400|✅|
|[github.com/monosans/proxy-list](https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt)|97|✅|
|[github.com/TheSpeedX/PROXY-List](https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt)|1922|✅|


## Sample Proxies With Geolocation Info

|#|Ip|Port|Country|City|Internet Service Provider|
|-|--|----|-------|----|-------------------------|
|1|35.234.248.49|3128|Canada|Montreal|Google LLC|
|2|45.167.124.5|9992|Colombia|Guapi|Sepcom Comunicaciones SAS|
|3|51.250.80.131|80|Russia|Moscow|Yandex.Cloud LLC|
|4|157.100.12.138|999|Ecuador|Loja|Telconet S.A|
|5|38.108.119.176|59394|United States|New York|Cogent Communications|
|6|47.240.160.90|10001|Hong Kong|Central|Alibaba.com LLC|
|7|47.241.165.133|443|Singapore|Singapore|Alibaba.com LLC|
|8|200.110.168.159|8080|Colombia|Trujillo|Media Commerce Partners S.A|
|9|185.221.134.234|3129|United States|Los Angeles|DediPath|
|10|201.174.239.18|8080|Mexico|General Escobedo|Transtelco Inc|
|11|64.138.255.146|80|United States|Conway|Horry Telephone Cooperative, Inc.|
|12|157.100.12.138|999|Ecuador|Loja|Telconet S.A|
|13|45.167.124.5|9992|Colombia|Guapi|Sepcom Comunicaciones SAS|
|14|51.250.80.131|80|Russia|Moscow|Yandex.Cloud LLC|
|15|47.240.160.90|10001|Hong Kong|Central|Alibaba.com LLC|
|16|116.253.208.239|33080|China|Guangxi|CHINATELECOM Guangxi Nanning IDC networkdescr: Nanning, Guangxi Province, P.R.|
|17|45.70.236.124|999|Ecuador|Puebloviejo|Nedetel S.A.|
|18|34.136.99.66|3128|United States|Council Bluffs|Google LLC|
|19|123.56.124.235|3128|China|Beijing|Hangzhou Alibaba Advertising Co|
|20|200.24.157.119|999|Ecuador|Azogues|Nedetel S.A.|



## Contributing

Contributions are welcome, and they are greatly appreciated! Every
little bit helps, and credit will always be given.

