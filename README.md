
# Free HTTP Proxy List 🌍

[![Hourly Update](https://github.com/mertguvencli/http-proxy-list/actions/workflows/main.yml/badge.svg?branch=main)](https://github.com/mertguvencli/http-proxy-list/actions/workflows/main.yml)
![GitHub](https://img.shields.io/github/license/mertguvencli/http-proxy-list)
![GitHub last commit](https://img.shields.io/github/last-commit/mertguvencli/http-proxy-list)

It is a lightweight project that hourly scrapes lots of free-proxy sites, validates if it works, and serves a clean proxy list.


> Scraper found **3805** proxies at the latest update. Usable proxies are below.

## Usage

Click the file format that you want and copy the URL.


|File|Content|Count|
|----|-------|-----|
|[data.txt](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.txt)|`ip_address:port` combined (seperated new line)|207|
|[data.json](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.json)|`ip, port`|207|
|[data-with-geolocation.json](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data-with-geolocation.json)|`ip, port, geolocation`|207|

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
|[proxylist.geonode.com](https://proxylist.geonode.com/api/proxy-list?limit=300&page=1&sort_by=lastChecked&sort_type=desc&protocols=http,https)|300|✅|
|[proxyscrape.com](https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all)|370|✅|
|[github.com/clarketm/proxy-list](https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt)|400|✅|
|[github.com/monosans/proxy-list](https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt)|228|✅|
|[github.com/TheSpeedX/PROXY-List](https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt)|1934|✅|


## Sample Proxies With Geolocation Info

|#|Ip|Port|Country|City|Internet Service Provider|
|-|--|----|-------|----|-------------------------|
|1|121.254.195.12|8080|South Korea|Yongsan-dong|LG DACOM Corporation|
|2|136.243.37.84|9090|Germany|Falkenstein|Hetzner Online GmbH|
|3|47.91.25.174|80|Japan|Tokyo|Alibaba.com LLC|
|4|51.161.51.195|9090|Colombia|Bogotá|OVH Hosting|
|5|206.161.97.118|31337|United States|Ashburn|PCCW Global, Inc.|
|6|110.77.236.225|8080|Thailand|Samphanthawong|CAT Telecom Public Company Limited|
|7|47.91.24.231|80|Japan|Tokyo|Alibaba.com LLC|
|8|51.161.51.196|9090|Colombia|Bogotá|OVH Hosting|
|9|47.245.56.201|80|Japan|Tokyo|Alibaba.com LLC|
|10|5.189.184.6|80|Germany|Nuremberg|Contabo GmbH|
|11|5.167.141.239|3128|Russia|Tula|CJSC "ER-Telecom Holding" Tula branch|
|12|181.78.20.69|999|Colombia|San Carlos|IFX Networks Argentina S.R.L|
|13|115.96.208.124|8080|India|Kalyan|Hathway IP over Cable Internet Access|
|14|201.151.62.21|999|Mexico|Comalcalco|Alestra, S. de R.L. de C.V.|
|15|47.245.54.114|80|Japan|Tokyo|Alibaba.com LLC|
|16|202.162.194.70|41766|Indonesia|Medan|Media Antar Nusa PT.|
|17|20.47.108.204|8888|United States|Boydton|Microsoft Corporation|
|18|190.63.35.30|9812|Ecuador|Guayaquil|CONECEL|
|19|158.255.215.50|16993|France|Paris|Edis France|
|20|172.86.63.205|9812|United States|Fairbank|Eastern Iowa IP, LLC|



## Contributing

Contributions are welcome, and they are greatly appreciated! Every
little bit helps, and credit will always be given.

