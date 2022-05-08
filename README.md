
# Free HTTP Proxy List 🌍

[![Hourly Update](https://github.com/mertguvencli/http-proxy-list/actions/workflows/main.yml/badge.svg?branch=main)](https://github.com/mertguvencli/http-proxy-list/actions/workflows/main.yml)
![GitHub](https://img.shields.io/github/license/mertguvencli/http-proxy-list)
![GitHub last commit](https://img.shields.io/github/last-commit/mertguvencli/http-proxy-list)

It is a lightweight project that hourly scrapes lots of free-proxy sites, validates if it works, and serves a clean proxy list.


> Scraper found **3228** proxies at the latest update. Usable proxies are below.

## Usage

Click the file format that you want and copy the URL.


|File|Content|Count|
|----|-------|-----|
|[data.txt](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.txt)|`ip_address:port` combined (seperated new line)|157|
|[data.json](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.json)|`ip, port`|157|
|[data-with-geolocation.json](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data-with-geolocation.json)|`ip, port, geolocation`|157|

## Sources

|Source|Found Proxies|Succeed|
|------|-------------|-------|
|[free-proxy-list.net](https://free-proxy-list.net)|300|✅|
|[us-proxy.org](https://www.us-proxy.org)|200|✅|
|[proxydb.net](http://proxydb.net)|15|✅|
|[free-proxy-list.com](https://free-proxy-list.com/?page=&port=&type%5B%5D=http&type%5B%5D=https&up_time=0&search=Search)|10|✅|
|[proxy-list.download](https://www.proxy-list.download/HTTP)|26|✅|
|[vpnoverview.com](https://vpnoverview.com/privacy/anonymous-browsing/free-proxy-servers)|32|✅|
|[proxyscan.io](https://www.proxyscan.io)|68|✅|
|[proxylist.geonode.com](https://proxylist.geonode.com/api/proxy-list?limit=300&page=1&sort_by=lastChecked&sort_type=desc&protocols=http,https)|300|✅|
|[proxyscrape.com](https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all)|335|✅|
|[github.com/clarketm/proxy-list](https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt)|400|✅|
|[github.com/monosans/proxy-list](https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt)|212|✅|
|[github.com/TheSpeedX/PROXY-List](https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt)|1330|✅|


## Sample Proxies With Geolocation Info

|#|Ip|Port|Country|City|Internet Service Provider|
|-|--|----|-------|----|-------------------------|
|1|45.77.86.30|59394|United States|Los Angeles|The Constant Company|
|2|149.248.5.225|59394|United States|Los Angeles|The Constant Company|
|3|40.70.172.110|80|United States|Boydton|Microsoft Corporation|
|4|180.183.3.101|8080|Thailand|Bang Lamung|Triple T Broadband Public Company Limited|
|5|40.70.172.110|80|United States|Boydton|Microsoft Corporation|
|6|128.199.94.96|3128|Singapore|Singapore|DigitalOcean, LLC|
|7|186.67.230.45|3128|Chile|Santiago|Entel Chile S.A.|
|8|83.220.47.146|8080|Russia|Moscow|GARS|
|9|174.138.116.12|80|United States|Clifton|DigitalOcean, LLC|
|10|190.26.201.194|8080|Colombia|Bogotá|ETB - Colombia|
|11|217.79.181.43|3128|Germany|Düsseldorf|myLoc managed IT AG|
|12|159.65.133.175|31280|Singapore|Singapore|DigitalOcean, LLC|
|13|161.35.126.221|3128|United States|North Bergen|DigitalOcean, LLC|
|14|181.49.217.254|8080|Colombia|Medellín|Telmex Colombia S.A.|
|15|189.148.166.94|999|Mexico|Nacajuca|Uninet S.A. de C.V|
|16|171.5.165.118|34599|Thailand|Kathu|Triple T Broadband Public Company Limited|
|17|58.8.143.3|8080|Thailand|Nonthaburi|True Internet Corporation CO. Ltd.|
|18|222.74.73.202|42055|China|Bieligutai|Chinanet|
|19|51.77.141.29|1081|France|Strasbourg|OVH SAS|
|20|58.82.154.3|8080|Thailand|Watthana Nakhon|CUST-COPP-JASTEL|



## Contributing

Contributions are welcome, and they are greatly appreciated! Every
little bit helps, and credit will always be given.

