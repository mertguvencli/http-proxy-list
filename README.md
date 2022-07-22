
# Free HTTP Proxy List 🌍

[![Hourly Update](https://github.com/mertguvencli/http-proxy-list/actions/workflows/main.yml/badge.svg?branch=main)](https://github.com/mertguvencli/http-proxy-list/actions/workflows/main.yml)
![GitHub](https://img.shields.io/github/license/mertguvencli/http-proxy-list)
![GitHub last commit](https://img.shields.io/github/last-commit/mertguvencli/http-proxy-list)

It is a lightweight project that hourly scrapes lots of free-proxy sites, validates if it works, and serves a clean proxy list.


> Scraper found **3310** proxies at the latest update. Usable proxies are below.

## Usage

Click the file format that you want and copy the URL.


|File|Content|Count|
|----|-------|-----|
|[data.txt](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.txt)|`ip_address:port` combined (seperated new line)|102|
|[data.json](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.json)|`ip, port`|102|
|[data-with-geolocation.json](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data-with-geolocation.json)|`ip, port, geolocation`|102|

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
|[proxyscrape.com](https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all)|227|✅|
|[github.com/clarketm/proxy-list](https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt)|400|✅|
|[github.com/monosans/proxy-list](https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt)|156|✅|
|[github.com/TheSpeedX/PROXY-List](https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt)|1844|✅|


## Sample Proxies With Geolocation Info

|#|Ip|Port|Country|City|Internet Service Provider|
|-|--|----|-------|----|-------------------------|
|1|8.219.97.248|80|Singapore|Singapore|Alibaba (US) Technology Co., Ltd.|
|2|144.202.61.154|8888|United States|Elk Grove Village|The Constant Company|
|3|157.100.12.138|999|Ecuador|Loja|Telconet S.A|
|4|144.76.241.45|7890|Germany|Falkenstein|Hetzner Online GmbH|
|5|139.59.16.35|31028|India|Bengaluru|DIGITALOCEAN|
|6|20.81.62.32|3128|United States|Boydton|Microsoft Corporation|
|7|116.58.239.10|80|Thailand|Ban Kha|CAT-BB|
|8|139.9.64.238|443|China|Guangzhou|Huawei Cloud Service data center|
|9|8.219.97.248|80|Singapore|Singapore|Alibaba (US) Technology Co., Ltd.|
|10|181.224.207.19|999|Dominican Republic|Santiago de los Caballeros|BW TELECOM|
|11|8.219.97.248|80|Singapore|Singapore|Alibaba (US) Technology Co., Ltd.|
|12|36.67.241.26|8080|Indonesia|Jakarta|PT. Telekomunikasi Indonesia|
|13|159.65.133.175|31280|Singapore|Singapore|DigitalOcean, LLC|
|14|157.100.12.138|999|Ecuador|Loja|Telconet S.A|
|15|187.19.102.22|3128|Brazil|Cascavel|CERTTO TELECOMUNICAÇÕES LTDA EPP|
|16|47.242.84.173|3128|Hong Kong|Hong Kong|Alibaba.com LLC|
|17|103.178.13.137|3125|Indonesia|Pasuruan|PT Amerta Asa Media|
|18|182.160.108.188|8090|Bangladesh|Dhaka|Aamra Networks Limited|
|19|200.29.108.225|8080|Colombia|Santiago de Cali|Empresas Municipales De Cali E.i.c.e. E.S.P.|
|20|141.147.95.36|3128|United Kingdom|London|Oracle Corporation|



## Contributing

Contributions are welcome, and they are greatly appreciated! Every
little bit helps, and credit will always be given.

