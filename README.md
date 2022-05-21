
# Free HTTP Proxy List 🌍

[![Hourly Update](https://github.com/mertguvencli/http-proxy-list/actions/workflows/main.yml/badge.svg?branch=main)](https://github.com/mertguvencli/http-proxy-list/actions/workflows/main.yml)
![GitHub](https://img.shields.io/github/license/mertguvencli/http-proxy-list)
![GitHub last commit](https://img.shields.io/github/last-commit/mertguvencli/http-proxy-list)

It is a lightweight project that hourly scrapes lots of free-proxy sites, validates if it works, and serves a clean proxy list.


> Scraper found **3378** proxies at the latest update. Usable proxies are below.

## Usage

Click the file format that you want and copy the URL.


|File|Content|Count|
|----|-------|-----|
|[data.txt](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.txt)|`ip_address:port` combined (seperated new line)|141|
|[data.json](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.json)|`ip, port`|141|
|[data-with-geolocation.json](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data-with-geolocation.json)|`ip, port, geolocation`|141|

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
|[proxyscrape.com](https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all)|258|✅|
|[github.com/clarketm/proxy-list](https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt)|400|✅|
|[github.com/monosans/proxy-list](https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt)|199|✅|
|[github.com/TheSpeedX/PROXY-List](https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt)|1938|✅|


## Sample Proxies With Geolocation Info

|#|Ip|Port|Country|City|Internet Service Provider|
|-|--|----|-------|----|-------------------------|
|1|51.81.32.81|8888|United States|Reston|OVH SAS|
|2|121.254.195.12|8080|South Korea|Yongsan-dong|LG DACOM Corporation|
|3|51.81.32.81|8888|United States|Reston|OVH SAS|
|4|128.199.214.87|3128|Singapore|Singapore|Partner Communications Ltd.|
|5|158.255.215.50|11857|France|Paris|Edis France|
|6|24.43.140.138|8080|United States|Palm Springs|Charter Communications|
|7|31.171.154.199|8118|Albania|Tirana|Keminet Ltd|
|8|47.91.25.174|80|Japan|Tokyo|Alibaba.com LLC|
|9|181.36.121.222|999|Dominican Republic|Santo Domingo Este|Altice Dominicana S.A.|
|10|67.212.83.53|1080|Canada|Saint-Hyacinthe|eStruxture Data Centers Inc.|
|11|18.218.45.35|3128|United States|Dublin|Amazon.com, Inc.|
|12|51.161.51.195|9090|Colombia|Bogotá|OVH Hosting|
|13|159.192.131.178|8080|Thailand|Samphanthawong|CAT-BB|
|14|87.103.175.250|9812|Russia|Irkutsk|PJSC Rostelecom|
|15|118.173.56.31|80|Thailand|Khwaeng Thung Song Hong|TOT Public Company Limited|
|16|18.218.45.35|3128|United States|Dublin|Amazon.com, Inc.|
|17|176.57.188.32|443|Germany|Düsseldorf|Contabo GmbH|
|18|148.251.66.8|3128|Germany|Falkenstein|Hetzner Online GmbH|
|19|110.78.81.107|8080|Thailand|Ban Kho|CAT Telecom Public Company Limited|
|20|177.55.57.69|3128|Brazil|Piraju|Webby Tecnologia Ltda|



## Contributing

Contributions are welcome, and they are greatly appreciated! Every
little bit helps, and credit will always be given.

