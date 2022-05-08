
# Free HTTP Proxy List 🌍

[![Hourly Update](https://github.com/mertguvencli/http-proxy-list/actions/workflows/main.yml/badge.svg?branch=main)](https://github.com/mertguvencli/http-proxy-list/actions/workflows/main.yml)
![GitHub](https://img.shields.io/github/license/mertguvencli/http-proxy-list)
![GitHub last commit](https://img.shields.io/github/last-commit/mertguvencli/http-proxy-list)

It is a lightweight project that hourly scrapes lots of free-proxy sites, validates if it works, and serves a clean proxy list.


> Scraper found **3487** proxies at the latest update. Usable proxies are below.

## Usage

Click the file format that you want and copy the URL.


|File|Content|Count|
|----|-------|-----|
|[data.txt](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.txt)|`ip_address:port` combined (seperated new line)|123|
|[data.json](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.json)|`ip, port`|123|
|[data-with-geolocation.json](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data-with-geolocation.json)|`ip, port, geolocation`|123|

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
|[proxyscrape.com](https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all)|312|✅|
|[github.com/clarketm/proxy-list](https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt)|400|✅|
|[github.com/monosans/proxy-list](https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt)|209|✅|
|[github.com/TheSpeedX/PROXY-List](https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt)|1883|✅|


## Sample Proxies With Geolocation Info

|#|Ip|Port|Country|City|Internet Service Provider|
|-|--|----|-------|----|-------------------------|
|1|144.202.116.156|59394|United States|Los Angeles|The Constant Company|
|2|119.42.86.87|8080|Thailand|Samphanthawong|CAT-BB|
|3|40.70.172.110|80|United States|Boydton|Microsoft Corporation|
|4|196.200.48.92|8080|Mali|Bamako|Afribone Mali SA|
|5|40.70.172.110|80|United States|Boydton|Microsoft Corporation|
|6|186.67.230.45|3128|Chile|Santiago|Entel Chile S.A.|
|7|149.248.5.225|59394|United States|Los Angeles|The Constant Company|
|8|189.237.69.110|999|Mexico|Chihuahua City|Uninet S.A. de C.V.|
|9|186.225.229.191|8080|Brazil|Tijucas|Unetvale Servicos e Equipamentos LTDA|
|10|190.26.201.194|8080|Colombia|Bogotá|ETB - Colombia|
|11|189.157.126.4|999|Mexico|Ciudad Valles|Uninet S.A. de C.V|
|12|183.89.91.239|8080|Thailand|Bang Na|Triple T Broadband Public Company Limited|
|13|58.8.143.3|8080|Thailand|Nonthaburi|True Internet Corporation CO. Ltd.|
|14|91.121.42.14|1081|France|Roubaix|OVH SAS|
|15|116.110.21.87|8080|Vietnam|Da Nang|Viettel Corporation|
|16|172.105.6.190|3128|Canada|Toronto|Linode, LLC|
|17|189.157.126.4|999|Mexico|Ciudad Valles|Uninet S.A. de C.V|
|18|13.127.170.8|3128|India|Mumbai|Amazon Technologies Inc.|
|19|181.196.241.198|9100|Ecuador|Guayaquil|Corporacion Nacional De Telecomunicaciones - CNT EP|
|20|184.82.197.17|8080|Thailand|Bangkok|AIS-Fibre|



## Contributing

Contributions are welcome, and they are greatly appreciated! Every
little bit helps, and credit will always be given.

