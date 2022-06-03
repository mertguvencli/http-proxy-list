
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
|[data.txt](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.txt)|`ip_address:port` combined (seperated new line)|202|
|[data.json](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.json)|`ip, port`|202|
|[data-with-geolocation.json](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data-with-geolocation.json)|`ip, port, geolocation`|202|

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
|[proxylist.geonode.com](https://proxylist.geonode.com/api/proxy-list?limit=300&page=1&sort_by=lastChecked&sort_type=desc&protocols=http,https)|0|🚫|
|[proxyscrape.com](https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all)|390|✅|
|[github.com/clarketm/proxy-list](https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt)|400|✅|
|[github.com/monosans/proxy-list](https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt)|156|✅|
|[github.com/TheSpeedX/PROXY-List](https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt)|1909|✅|


## Sample Proxies With Geolocation Info

|#|Ip|Port|Country|City|Internet Service Provider|
|-|--|----|-------|----|-------------------------|
|1|173.82.188.82|9090|United States|Santa Clarita|Multacom Corporation|
|2|154.49.216.33|3128|France|Vélizy-Villacoublay|Cogent Communications|
|3|35.157.249.83|39593|Germany|Frankfurt am Main|Amazon Technologies Inc.|
|4|18.196.224.91|36776|Germany|Frankfurt am Main|Amazon Technologies Inc.|
|5|45.167.125.209|9992|Colombia|Popayán|Sepcom Comunicaciones SAS|
|6|54.93.165.96|39593|Germany|Frankfurt am Main|Amazon Technologies Inc.|
|7|5.189.184.6|80|Germany|Nuremberg|Contabo GmbH|
|8|107.191.48.64|59069|United States|Elk Grove Village|Choopa|
|9|157.100.12.138|999|Ecuador|Quito|Telconet S.A|
|10|163.172.37.158|9741|France|Paris|Online S.A.S.|
|11|173.82.188.82|9090|United States|Santa Clarita|Multacom Corporation|
|12|154.49.216.33|3128|France|Vélizy-Villacoublay|Cogent Communications|
|13|183.111.25.253|8080|South Korea|Seongnam-si|Korea Telecom|
|14|128.199.214.87|3128|Singapore|Singapore|Partner Communications Ltd.|
|15|93.78.190.146|41890|Ukraine|Poltava|Volia Poltava|
|16|171.244.170.205|8080|Vietnam|Ho Chi Minh City|Viettel Corporation|
|17|45.64.99.235|8080|Indonesia|Jakarta|ARGON|
|18|91.185.58.14|8080|Russia|Irkutsk|JSC Irkutsk Business Net, Inc.|
|19|103.214.9.13|3128|Vietnam|Hanoi|MEGACORE|
|20|107.191.48.64|59069|United States|Elk Grove Village|Choopa|



## Contributing

Contributions are welcome, and they are greatly appreciated! Every
little bit helps, and credit will always be given.

