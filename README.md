
# Free HTTP Proxy List 🌍

[![Hourly Update](https://github.com/mertguvencli/http-proxy-list/actions/workflows/main.yml/badge.svg?branch=main)](https://github.com/mertguvencli/http-proxy-list/actions/workflows/main.yml)
![GitHub](https://img.shields.io/github/license/mertguvencli/http-proxy-list)
![GitHub last commit](https://img.shields.io/github/last-commit/mertguvencli/http-proxy-list)

It is a lightweight project that hourly scrapes lots of free-proxy sites, validates if it works, and serves a clean proxy list.


> Scraper found **3170** proxies at the latest update. Usable proxies are below.

## Usage

Click the file format that you want and copy the URL.


|File|Content|Count|
|----|-------|-----|
|[data.txt](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.txt)|`ip_address:port` combined (seperated new line)|68|
|[data.json](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.json)|`ip, port`|68|
|[data-with-geolocation.json](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data-with-geolocation.json)|`ip, port, geolocation`|68|

## Sources

|Source|Found Proxies|Succeed|
|------|-------------|-------|
|[free-proxy-list.net](https://free-proxy-list.net)|300|✅|
|[us-proxy.org](https://www.us-proxy.org)|200|✅|
|[proxydb.net](http://proxydb.net)|15|✅|
|[free-proxy-list.com](https://free-proxy-list.com/?page=&port=&type%5B%5D=http&type%5B%5D=https&up_time=0&search=Search)|0|🚫|
|[proxy-list.download](https://www.proxy-list.download/HTTP)|26|✅|
|[vpnoverview.com](https://vpnoverview.com/privacy/anonymous-browsing/free-proxy-servers)|32|✅|
|[proxyscan.io](https://www.proxyscan.io)|0|🚫|
|[proxylist.geonode.com](https://proxylist.geonode.com/api/proxy-list?limit=300&page=1&sort_by=lastChecked&sort_type=desc&protocols=http,https)|217|✅|
|[proxyscrape.com](https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all)|128|✅|
|[github.com/clarketm/proxy-list](https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt)|400|✅|
|[github.com/monosans/proxy-list](https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt)|62|✅|
|[github.com/TheSpeedX/PROXY-List](https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt)|1790|✅|


## Sample Proxies With Geolocation Info

|#|Ip|Port|Country|City|Internet Service Provider|
|-|--|----|-------|----|-------------------------|
|1|45.167.125.209|9992|Colombia|Popayán|Sepcom Comunicaciones SAS|
|2|47.252.4.64|8888|United States|Charlottesville|Alibaba.com LLC|
|3|128.199.214.87|3128|Singapore|Singapore|Partner Communications Ltd.|
|4|157.100.12.138|999|Ecuador|Quito|Telconet S.A|
|5|209.250.253.162|59394|Netherlands|Amsterdam|The Constant Company|
|6|47.252.4.64|8888|United States|Charlottesville|Alibaba.com LLC|
|7|190.97.226.236|999|Venezuela|Barinas|NetLink América C.A.|
|8|144.217.7.157|9300|Canada|Beauharnois|OVH SAS|
|9|45.167.125.209|9992|Colombia|Popayán|Sepcom Comunicaciones SAS|
|10|118.67.150.13|3128|South Korea|Seongnam-si|NBP|
|11|209.250.253.162|59394|Netherlands|Amsterdam|The Constant Company|
|12|134.0.63.134|8000|Albania|Tirana|Agjencia Kombetare Shoqerise se Informacionit|
|13|189.39.16.42|5566|Brazil|São Paulo|ALGAR TELECOM S/A|
|14|121.151.223.96|1337|South Korea|Suseong-gu|Korea Telecom|
|15|171.103.58.122|8080|Thailand|Bangkok|True Internet Co., Ltd.|
|16|45.167.125.209|9992|Colombia|Popayán|Sepcom Comunicaciones SAS|
|17|18.218.45.35|3128|United States|Dublin|Amazon.com, Inc.|
|18|170.83.242.250|999|Paraguay|Asunción|Ufinet Panama S.A.|
|19|177.141.99.50|8080|Brazil|São Paulo|Claro S.A.|
|20|181.225.68.27|999|Colombia|Villavicencio|Media Commerce Partners S.A|



## Contributing

Contributions are welcome, and they are greatly appreciated! Every
little bit helps, and credit will always be given.

