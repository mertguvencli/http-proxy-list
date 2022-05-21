
# Free HTTP Proxy List 🌍

[![Hourly Update](https://github.com/mertguvencli/http-proxy-list/actions/workflows/main.yml/badge.svg?branch=main)](https://github.com/mertguvencli/http-proxy-list/actions/workflows/main.yml)
![GitHub](https://img.shields.io/github/license/mertguvencli/http-proxy-list)
![GitHub last commit](https://img.shields.io/github/last-commit/mertguvencli/http-proxy-list)

It is a lightweight project that hourly scrapes lots of free-proxy sites, validates if it works, and serves a clean proxy list.


> Scraper found **3575** proxies at the latest update. Usable proxies are below.

## Usage

Click the file format that you want and copy the URL.


|File|Content|Count|
|----|-------|-----|
|[data.txt](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.txt)|`ip_address:port` combined (seperated new line)|194|
|[data.json](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.json)|`ip, port`|194|
|[data-with-geolocation.json](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data-with-geolocation.json)|`ip, port, geolocation`|194|

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
|[proxyscrape.com](https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all)|403|✅|
|[github.com/clarketm/proxy-list](https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt)|400|✅|
|[github.com/monosans/proxy-list](https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt)|241|✅|
|[github.com/TheSpeedX/PROXY-List](https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt)|1948|✅|


## Sample Proxies With Geolocation Info

|#|Ip|Port|Country|City|Internet Service Provider|
|-|--|----|-------|----|-------------------------|
|1|165.232.145.67|3128|United States|Santa Clara|DigitalOcean, LLC|
|2|186.67.230.45|3128|Chile|Santiago|Entel Chile S.A.|
|3|70.186.128.126|8080|United States|Oklahoma City|Cox Communications Inc.|
|4|79.124.78.144|5555|Vanuatu|Port Vila|Verdina Ltd.|
|5|85.195.104.71|80|Germany|Frankfurt am Main|Host Europe GmbH|
|6|47.91.25.174|80|Japan|Tokyo|Alibaba.com LLC|
|7|51.81.32.81|8888|United States|Reston|OVH SAS|
|8|18.218.45.35|3128|United States|Dublin|Amazon.com, Inc.|
|9|31.171.154.199|8118|Albania|Tirana|Keminet Ltd|
|10|148.251.66.8|3128|Germany|Falkenstein|Hetzner Online GmbH|
|11|91.250.83.200|3128|France|Strasbourg|Host Europe GmbH|
|12|51.79.50.46|9300|Canada|Beauharnois|OVH SAS|
|13|95.217.20.255|51222|Finland|Helsinki|Hetzner Online GmbH|
|14|186.250.29.82|8080|Brazil|Santa Helena|KDM INTERNET TELECOMUNICACOES LTDA|
|15|181.129.14.165|999|Colombia|Medellín|EPM Telecomunicaciones S.A. E.S.P.|
|16|58.27.233.34|8080|Pakistan|Lahore|Wateen Telecom Limited|
|17|27.111.45.25|55443|Indonesia|Sunter Jaya|INET-ISP|
|18|201.77.108.130|999|Mexico|Jose Mariano Jimenez|Nidix Networks S.a. De C.V.|
|19|187.62.195.145|8080|Brazil|Montes Claros|UWBR VOX Telecomunicações S/A|
|20|194.44.15.222|8081|Ukraine|Bryukhovychi|UARNET-LL|



## Contributing

Contributions are welcome, and they are greatly appreciated! Every
little bit helps, and credit will always be given.

