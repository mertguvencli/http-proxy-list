
# Free HTTP Proxy List 🌍

[![Hourly Update](https://github.com/mertguvencli/http-proxy-list/actions/workflows/main.yml/badge.svg?branch=main)](https://github.com/mertguvencli/http-proxy-list/actions/workflows/main.yml)
![GitHub](https://img.shields.io/github/license/mertguvencli/http-proxy-list)
![GitHub last commit](https://img.shields.io/github/last-commit/mertguvencli/http-proxy-list)

It is a lightweight project that hourly scrapes lots of free-proxy sites, validates if it works, and serves a clean proxy list.


> Scraper found **3440** proxies at the latest update. Usable proxies are below.

## Usage

Click the file format that you want and copy the URL.


|File|Content|Count|
|----|-------|-----|
|[data.txt](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.txt)|`ip_address:port` combined (seperated new line)|160|
|[data.json](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.json)|`ip, port`|160|
|[data-with-geolocation.json](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data-with-geolocation.json)|`ip, port, geolocation`|160|

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
|[proxyscrape.com](https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all)|326|✅|
|[github.com/clarketm/proxy-list](https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt)|400|✅|
|[github.com/monosans/proxy-list](https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt)|228|✅|
|[github.com/TheSpeedX/PROXY-List](https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt)|1903|✅|


## Sample Proxies With Geolocation Info

|#|Ip|Port|Country|City|Internet Service Provider|
|-|--|----|-------|----|-------------------------|
|1|198.59.191.234|8080|United States|Carlsbad|TDS TELECOM|
|2|35.230.142.201|8080|United Kingdom|London|Google LLC|
|3|20.47.108.204|8888|United States|Boydton|Microsoft Corporation|
|4|8.219.97.248|80|Singapore|Singapore|Alibaba (US) Technology Co., Ltd.|
|5|51.250.80.131|80|Russia|Moscow|Yandex.Cloud LLC|
|6|117.121.204.9|7998|Indonesia|Banjaran|PT Sekawan Global Komunika|
|7|183.88.228.208|8080|Thailand|Bangkok|Triple T Broadband Public Company Limited|
|8|54.149.196.242|3128|United States|Portland|Amazon.com, Inc.|
|9|20.47.108.204|8888|United States|Boydton|Microsoft Corporation|
|10|54.149.196.242|3128|United States|Portland|Amazon.com, Inc.|
|11|151.181.91.10|80|United States|Buffalo|Fibertech Networks|
|12|5.161.105.105|80|United States|Ashburn|Hetzner Online GmbH|
|13|45.195.76.114|999|Dominican Republic|Santo Domingo Este|Orbitek SRL|
|14|157.100.12.138|999|Ecuador|Loja|Telconet S.A|
|15|8.219.97.248|80|Singapore|Singapore|Alibaba (US) Technology Co., Ltd.|
|16|115.233.221.139|3128|China|Yuzhong Chengguanzhen|China Telecom Next Generation Carrier Network|
|17|188.133.158.145|8080|Russia|Moscow|Enforta-MSK|
|18|80.63.84.58|8081|Denmark|Copenhagen|TDC A/S|
|19|105.112.191.250|3128|Nigeria|Lagos|Airtel Networks Limited|
|20|152.231.25.58|8080|Colombia|Florencia|TV AZTECA SUCURSAL COLOMBIA|



## Contributing

Contributions are welcome, and they are greatly appreciated! Every
little bit helps, and credit will always be given.

