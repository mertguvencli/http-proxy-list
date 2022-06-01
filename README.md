
# Free HTTP Proxy List 🌍

[![Hourly Update](https://github.com/mertguvencli/http-proxy-list/actions/workflows/main.yml/badge.svg?branch=main)](https://github.com/mertguvencli/http-proxy-list/actions/workflows/main.yml)
![GitHub](https://img.shields.io/github/license/mertguvencli/http-proxy-list)
![GitHub last commit](https://img.shields.io/github/last-commit/mertguvencli/http-proxy-list)

It is a lightweight project that hourly scrapes lots of free-proxy sites, validates if it works, and serves a clean proxy list.


> Scraper found **3678** proxies at the latest update. Usable proxies are below.

## Usage

Click the file format that you want and copy the URL.


|File|Content|Count|
|----|-------|-----|
|[data.txt](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.txt)|`ip_address:port` combined (seperated new line)|168|
|[data.json](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.json)|`ip, port`|168|
|[data-with-geolocation.json](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data-with-geolocation.json)|`ip, port, geolocation`|168|

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
|[proxylist.geonode.com](https://proxylist.geonode.com/api/proxy-list?limit=300&page=1&sort_by=lastChecked&sort_type=desc&protocols=http,https)|300|✅|
|[proxyscrape.com](https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all)|335|✅|
|[github.com/clarketm/proxy-list](https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt)|400|✅|
|[github.com/monosans/proxy-list](https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt)|118|✅|
|[github.com/TheSpeedX/PROXY-List](https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt)|1942|✅|


## Sample Proxies With Geolocation Info

|#|Ip|Port|Country|City|Internet Service Provider|
|-|--|----|-------|----|-------------------------|
|1|54.193.249.144|8080|United States|San Jose|Amazon.com, Inc.|
|2|147.75.68.201|80|United States|Sunnyvale|Packet Host, Inc.|
|3|117.20.216.218|8080|South Korea|Gumi|HYUNDAI COMMUNICATIONS & NETWORK|
|4|147.75.68.201|80|United States|Sunnyvale|Packet Host, Inc.|
|5|45.167.125.209|9992|Colombia|Popayán|Sepcom Comunicaciones SAS|
|6|190.97.226.236|999|Venezuela|Barinas|NetLink América C.A.|
|7|5.189.184.6|80|Germany|Nuremberg|Contabo GmbH|
|8|128.199.214.87|3128|Singapore|Singapore|Partner Communications Ltd.|
|9|157.100.12.138|999|Ecuador|Quito|Telconet S.A|
|10|157.100.52.146|999|Ecuador|Nulti|Nedetel S.A.|
|11|45.70.14.58|999|Ecuador|San Jacinto de Buena Fe|Nedetel S.A.|
|12|61.7.138.244|8080|Thailand|Nakhon Pathom|CAT-BB|
|13|80.84.176.110|8080|Ukraine|Zaporizhzhya|Express Radio Networks|
|14|45.148.145.56|3128|United Kingdom|London|Serverius B.V.|
|15|206.189.33.35|80|Singapore|Singapore|DigitalOcean, LLC|
|16|170.79.235.3|999|Chile|Santiago|TNA Solutions SpA|
|17|45.225.8.0|40033|Brazil|São Paulo|Rede Megas Internet|
|18|45.190.249.100|8080|Brazil|Passo Fundo|RK Telecom Provedor Internet LTDA|
|19|43.230.131.123|8083|Indonesia|Embongkaliasin|Internet Ini Saja|
|20|176.58.119.35|3128|United Kingdom|London|Linode, LLC|



## Contributing

Contributions are welcome, and they are greatly appreciated! Every
little bit helps, and credit will always be given.

