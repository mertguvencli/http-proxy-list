
# Free HTTP Proxy List 🌍

[![Hourly Update](https://github.com/mertguvencli/http-proxy-list/actions/workflows/main.yml/badge.svg?branch=main)](https://github.com/mertguvencli/http-proxy-list/actions/workflows/main.yml)
![GitHub](https://img.shields.io/github/license/mertguvencli/http-proxy-list)
![GitHub last commit](https://img.shields.io/github/last-commit/mertguvencli/http-proxy-list)

It is a lightweight project that hourly scrapes lots of free-proxy sites, validates if it works, and serves a clean proxy list.


> Scraper found **3445** proxies at the latest update. Usable proxies are below.

## Usage

Click the file format that you want and copy the URL.


|File|Content|Count|
|----|-------|-----|
|[data.txt](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.txt)|`ip_address:port` combined (seperated new line)|175|
|[data.json](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.json)|`ip, port`|175|
|[data-with-geolocation.json](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data-with-geolocation.json)|`ip, port, geolocation`|175|

## Sources

|Source|Found Proxies|Succeed|
|------|-------------|-------|
|[free-proxy-list.net](https://free-proxy-list.net)|300|✅|
|[us-proxy.org](https://www.us-proxy.org)|200|✅|
|[proxydb.net](http://proxydb.net)|15|✅|
|[free-proxy-list.com](https://free-proxy-list.com/?page=&port=&type%5B%5D=http&type%5B%5D=https&up_time=0&search=Search)|10|✅|
|[proxy-list.download](https://www.proxy-list.download/HTTP)|26|✅|
|[vpnoverview.com](https://vpnoverview.com/privacy/anonymous-browsing/free-proxy-servers)|32|✅|
|[proxyscan.io](https://www.proxyscan.io)|88|✅|
|[proxylist.geonode.com](https://proxylist.geonode.com/api/proxy-list?limit=300&page=1&sort_by=lastChecked&sort_type=desc&protocols=http,https)|0|🚫|
|[proxyscrape.com](https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all)|335|✅|
|[github.com/clarketm/proxy-list](https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt)|400|✅|
|[github.com/monosans/proxy-list](https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt)|198|✅|
|[github.com/TheSpeedX/PROXY-List](https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt)|1841|✅|


## Sample Proxies With Geolocation Info

|#|Ip|Port|Country|City|Internet Service Provider|
|-|--|----|-------|----|-------------------------|
|1|20.47.108.204|8888|United States|Boydton|Microsoft Corporation|
|2|20.47.108.204|8888|United States|Boydton|Microsoft Corporation|
|3|157.100.12.138|999|Ecuador|Loja|Telconet S.A|
|4|177.22.88.224|3128|Brazil|Passo Fundo|Coprel Telecom Ltda|
|5|8.219.97.248|80|Singapore|Singapore|Alibaba (US) Technology Co., Ltd.|
|6|13.125.238.23|3128|South Korea|Seoul|Amazon Technologies Inc.|
|7|187.188.108.114|8080|Mexico|Mexico City|Total Play Telecomunicaciones SA De CV|
|8|51.250.80.131|80|Russia|Moscow|Yandex.Cloud LLC|
|9|2.187.214.221|8080|Iran|Urmia|Iran Telecommunication Company PJS|
|10|110.78.138.81|8080|Thailand|Bangkok|CAT-BB|
|11|103.152.232.162|8080|Indonesia|Subang|PT Kingpolah Network Solutions|
|12|144.202.61.154|8888|United States|Elk Grove Village|The Constant Company|
|13|143.244.133.78|80|India|Bengaluru|DigitalOcean, LLC|
|14|200.105.215.18|33630|Bolivia|La Paz|AXS Bolivia S. A.|
|15|41.193.84.196|3128|South Africa|Johannesburg|Vox Telecom|
|16|20.81.62.32|3128|United States|Boydton|Microsoft Corporation|
|17|20.81.62.32|3128|United States|Boydton|Microsoft Corporation|
|18|91.227.183.110|80|Ukraine|Kyiv|SPD Polyudov Aleksandr Igorevich|
|19|20.47.108.204|8888|United States|Boydton|Microsoft Corporation|
|20|168.227.56.96|8080|Brazil|Votuporanga|RF connect provedor de acesso ltda-me|



## Contributing

Contributions are welcome, and they are greatly appreciated! Every
little bit helps, and credit will always be given.

