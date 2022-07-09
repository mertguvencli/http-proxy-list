
# Free HTTP Proxy List 🌍

[![Hourly Update](https://github.com/mertguvencli/http-proxy-list/actions/workflows/main.yml/badge.svg?branch=main)](https://github.com/mertguvencli/http-proxy-list/actions/workflows/main.yml)
![GitHub](https://img.shields.io/github/license/mertguvencli/http-proxy-list)
![GitHub last commit](https://img.shields.io/github/last-commit/mertguvencli/http-proxy-list)

It is a lightweight project that hourly scrapes lots of free-proxy sites, validates if it works, and serves a clean proxy list.


> Scraper found **4003** proxies at the latest update. Usable proxies are below.

## Usage

Click the file format that you want and copy the URL.


|File|Content|Count|
|----|-------|-----|
|[data.txt](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.txt)|`ip_address:port` combined (seperated new line)|206|
|[data.json](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.json)|`ip, port`|206|
|[data-with-geolocation.json](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data-with-geolocation.json)|`ip, port, geolocation`|206|

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
|[proxyscrape.com](https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all)|388|✅|
|[github.com/clarketm/proxy-list](https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt)|400|✅|
|[github.com/monosans/proxy-list](https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt)|308|✅|
|[github.com/TheSpeedX/PROXY-List](https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt)|2024|✅|


## Sample Proxies With Geolocation Info

|#|Ip|Port|Country|City|Internet Service Provider|
|-|--|----|-------|----|-------------------------|
|1|20.47.108.204|8888|United States|Boydton|Microsoft Corporation|
|2|198.41.67.18|8080|United States|Lafayette|Cox Communications Inc.|
|3|20.81.62.32|3128|United States|Boydton|Microsoft Corporation|
|4|20.81.62.32|3128|United States|Boydton|Microsoft Corporation|
|5|95.217.208.163|8118|Finland|Helsinki|Hetzner Online GmbH|
|6|210.115.46.228|3128|South Korea|Chuncheon|Kangwon National University|
|7|49.48.114.180|8080|Thailand|Kuchinarai|Triple T Broadband Public Company Limited|
|8|115.96.208.124|8080|India|Mumbai|Hathway IP over Cable Internet Access|
|9|138.68.238.19|31028|United States|Santa Clara|DigitalOcean, LLC|
|10|188.40.15.7|8080|Germany|Falkenstein|Hetzner Online GmbH|
|11|8.210.66.212|3128|Hong Kong|Hong Kong|Alibaba.com LLC|
|12|43.154.161.208|59394|Hong Kong|Hong Kong|Shenzhen Tencent Computer Systems Company Limited|
|13|41.186.44.106|3128|Rwanda|Kigali|MTN Rwandacell|
|14|206.189.195.74|8080|United States|North Bergen|DigitalOcean, LLC|
|15|103.75.35.202|53281|India|Faridabad|Elyzium Softech|
|16|47.241.165.133|443|Singapore|Singapore|Alibaba.com LLC|
|17|191.6.133.22|2356|Brazil|Inconfidentes|NET.COM TELECOMUNICACOES EIRELI|
|18|154.13.5.41|59394|Canada|Montreal|Zhihua Lu trading as HostHub|
|19|154.13.5.41|59394|Canada|Montreal|Zhihua Lu trading as HostHub|
|20|51.250.80.131|80|Russia|Moscow|Yandex.Cloud LLC|



## Contributing

Contributions are welcome, and they are greatly appreciated! Every
little bit helps, and credit will always be given.

