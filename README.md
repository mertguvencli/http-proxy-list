
# Free HTTP Proxy List 🌍

[![Hourly Update](https://github.com/mertguvencli/http-proxy-list/actions/workflows/main.yml/badge.svg?branch=main)](https://github.com/mertguvencli/http-proxy-list/actions/workflows/main.yml)
![GitHub](https://img.shields.io/github/license/mertguvencli/http-proxy-list)
![GitHub last commit](https://img.shields.io/github/last-commit/mertguvencli/http-proxy-list)

It is a lightweight project that hourly scrapes lots of free-proxy sites, validates if it works, and serves a clean proxy list.


> Scraper found **3665** proxies at the latest update. Usable proxies are below.

## Usage

Click the file format that you want and copy the URL.


|File|Content|Count|
|----|-------|-----|
|[data.txt](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.txt)|`ip_address:port` combined (seperated new line)|104|
|[data.json](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.json)|`ip, port`|104|
|[data-with-geolocation.json](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data-with-geolocation.json)|`ip, port, geolocation`|104|

## Sources

|Source|Found Proxies|Succeed|
|------|-------------|-------|
|[free-proxy-list.net](https://free-proxy-list.net)|300|✅|
|[us-proxy.org](https://www.us-proxy.org)|200|✅|
|[proxydb.net](http://proxydb.net)|15|✅|
|[free-proxy-list.com](https://free-proxy-list.com/?page=&port=&type%5B%5D=http&type%5B%5D=https&up_time=0&search=Search)|10|✅|
|[proxy-list.download](https://www.proxy-list.download/HTTP)|26|✅|
|[vpnoverview.com](https://vpnoverview.com/privacy/anonymous-browsing/free-proxy-servers)|32|✅|
|[proxyscan.io](https://www.proxyscan.io)|98|✅|
|[proxylist.geonode.com](https://proxylist.geonode.com/api/proxy-list?limit=300&page=1&sort_by=lastChecked&sort_type=desc&protocols=http,https)|300|✅|
|[proxyscrape.com](https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all)|159|✅|
|[github.com/clarketm/proxy-list](https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt)|400|✅|
|[github.com/monosans/proxy-list](https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt)|132|✅|
|[github.com/TheSpeedX/PROXY-List](https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt)|1993|✅|


## Sample Proxies With Geolocation Info

|#|Ip|Port|Country|City|Internet Service Provider|
|-|--|----|-------|----|-------------------------|
|1|66.196.238.180|3128|United States|Tomball|Logix|
|2|180.183.114.89|8080|Thailand|Bangkok|Triple T Broadband Public Company Limited|
|3|119.76.142.235|8080|Thailand|Nakhon Ratchasima|True Internet Co., Ltd.|
|4|103.49.228.34|8081|Indonesia|Tigaraksa|NASIONALONLINE|
|5|84.22.198.187|8080|Russia|St Petersburg|JSC "ER-Telecom Holding"|
|6|5.189.184.6|80|Germany|Nuremberg|Contabo GmbH|
|7|65.108.136.229|9090|Finland|Helsinki|Hetzner Online GmbH|
|8|170.80.65.153|8080|Brazil|Belo Horizonte|TelecomDados Ltda|
|9|202.50.53.107|8080|Nepal|Kathmandu|NetMax Technologies Pvt. Ltd.|
|10|157.100.12.138|999|Ecuador|Quito|Telconet S.A|
|11|203.150.113.58|8080|Thailand|Bangkok|Internet Thailand Company Ltd.|
|12|181.224.207.19|999|Dominican Republic|Santiago de los Caballeros|BW TELECOM|
|13|5.39.189.39|3128|Netherlands|Rotterdam|ColoCenter b.v.|
|14|162.150.62.96|443|United States|Kincaid|Comcast Cable Communications, LLC|
|15|65.108.136.229|9090|Finland|Helsinki|Hetzner Online GmbH|
|16|162.150.62.96|443|United States|Kincaid|Comcast Cable Communications, LLC|
|17|203.153.125.245|8080|Indonesia|Tangerang|GMNUSANTARA|
|18|66.196.238.180|3128|United States|Tomball|Logix|
|19|167.114.96.27|9300|Canada|Montreal|OVH SAS|
|20|147.75.68.201|80|United States|Sunnyvale|Packet Host, Inc.|



## Contributing

Contributions are welcome, and they are greatly appreciated! Every
little bit helps, and credit will always be given.

