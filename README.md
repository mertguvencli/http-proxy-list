
# Free HTTP Proxy List 🌍

[![Hourly Update](https://github.com/mertguvencli/http-proxy-list/actions/workflows/main.yml/badge.svg?branch=main)](https://github.com/mertguvencli/http-proxy-list/actions/workflows/main.yml)
![GitHub](https://img.shields.io/github/license/mertguvencli/http-proxy-list)
![GitHub last commit](https://img.shields.io/github/last-commit/mertguvencli/http-proxy-list)

It is a lightweight project that hourly scrapes lots of free-proxy sites, validates if it works, and serves a clean proxy list.


> Scraper found **3971** proxies at the latest update. Usable proxies are below.

## Usage

Click the file format that you want and copy the URL.


|File|Content|Count|
|----|-------|-----|
|[data.txt](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.txt)|`ip_address:port` combined (seperated new line)|300|
|[data.json](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.json)|`ip, port`|300|
|[data-with-geolocation.json](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data-with-geolocation.json)|`ip, port, geolocation`|300|

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
|[proxyscrape.com](https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all)|392|✅|
|[github.com/clarketm/proxy-list](https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt)|400|✅|
|[github.com/monosans/proxy-list](https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt)|173|✅|
|[github.com/TheSpeedX/PROXY-List](https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt)|2123|✅|


## Sample Proxies With Geolocation Info

|#|Ip|Port|Country|City|Internet Service Provider|
|-|--|----|-------|----|-------------------------|
|1|206.189.23.38|8048|United Kingdom|London|DigitalOcean, LLC|
|2|133.242.237.138|3128|Japan|Chiyoda|SAKURA Internet Inc.|
|3|45.131.251.234|3129|United States|Los Angeles|DediPath|
|4|14.207.122.103|8080|Thailand|Bangkok|Triple T Broadband Public Company Limited|
|5|167.172.173.210|36951|Germany|Frankfurt am Main|DigitalOcean, LLC|
|6|203.116.44.134|3128|Singapore|Singapore|Starhub Internet Pte Ltd|
|7|200.105.215.18|33630|Bolivia|La Paz|AXS Bolivia S. A.|
|8|1.20.169.206|8080|Thailand|Chanthaburi|TOT Public Company Limited|
|9|47.240.160.90|10001|Hong Kong|Central|Alibaba.com LLC|
|10|142.93.24.89|3128|United States|Santa Clara|DigitalOcean, LLC|
|11|103.164.12.66|1080|Indonesia|Jakarta|PT Milenial Inti Telekomunikasi|
|12|110.170.126.13|3128|Thailand|Din Daeng|True Internet Corporation CO. Ltd.|
|13|45.131.251.234|3129|United States|Los Angeles|DediPath|
|14|95.217.72.247|3128|Finland|Helsinki|Hetzner Online GmbH|
|15|200.146.77.133|80|Brazil|Curitiba|Vivo|
|16|152.228.128.48|8118|France|Strasbourg|OVH SAS|
|17|183.111.25.253|80|South Korea|Seongnam-si|Korea Telecom|
|18|47.252.4.64|8888|United States|Charlottesville|Alibaba.com LLC|
|19|95.217.72.247|3128|Finland|Helsinki|Hetzner Online GmbH|
|20|114.4.104.254|3128|Indonesia|Jakarta|PT. INDOSAT Tbk|



## Contributing

Contributions are welcome, and they are greatly appreciated! Every
little bit helps, and credit will always be given.

