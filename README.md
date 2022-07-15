
# Free HTTP Proxy List 🌍

[![Hourly Update](https://github.com/mertguvencli/http-proxy-list/actions/workflows/main.yml/badge.svg?branch=main)](https://github.com/mertguvencli/http-proxy-list/actions/workflows/main.yml)
![GitHub](https://img.shields.io/github/license/mertguvencli/http-proxy-list)
![GitHub last commit](https://img.shields.io/github/last-commit/mertguvencli/http-proxy-list)

It is a lightweight project that hourly scrapes lots of free-proxy sites, validates if it works, and serves a clean proxy list.


> Scraper found **3536** proxies at the latest update. Usable proxies are below.

## Usage

Click the file format that you want and copy the URL.


|File|Content|Count|
|----|-------|-----|
|[data.txt](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.txt)|`ip_address:port` combined (seperated new line)|162|
|[data.json](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.json)|`ip, port`|162|
|[data-with-geolocation.json](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data-with-geolocation.json)|`ip, port, geolocation`|162|

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
|[proxyscrape.com](https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all)|243|✅|
|[github.com/clarketm/proxy-list](https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt)|400|✅|
|[github.com/monosans/proxy-list](https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt)|169|✅|
|[github.com/TheSpeedX/PROXY-List](https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt)|1841|✅|


## Sample Proxies With Geolocation Info

|#|Ip|Port|Country|City|Internet Service Provider|
|-|--|----|-------|----|-------------------------|
|1|170.39.194.16|3128|United States|Ashburn|Rackdog, LLC|
|2|138.68.238.19|31028|United States|Santa Clara|DigitalOcean, LLC|
|3|167.71.190.253|80|United States|Clifton|DigitalOcean, LLC|
|4|170.39.194.16|3128|United States|Ashburn|Rackdog, LLC|
|5|138.68.238.19|31028|United States|Santa Clara|DigitalOcean, LLC|
|6|5.189.184.6|80|Germany|Nuremberg|Contabo GmbH|
|7|8.219.97.248|80|Singapore|Singapore|Alibaba (US) Technology Co., Ltd.|
|8|167.235.63.238|3128|Germany|Falkenstein|Hetzner Online GmbH|
|9|206.189.195.74|8080|United States|North Bergen|DigitalOcean, LLC|
|10|216.238.82.41|59394|Mexico|Mexico City|The Constant Company|
|11|183.88.135.151|8080|Thailand|Chiang Mai|Triple T Broadband Public Company Limited|
|12|206.189.195.74|8080|United States|North Bergen|DigitalOcean, LLC|
|13|209.97.152.208|8888|United States|Clifton|DigitalOcean, LLC|
|14|185.42.241.171|8080|Spain|Puerto Lumbreras|Telplay - 2|
|15|186.97.182.5|999|Colombia|Medellín|Colombia Móvil|
|16|209.166.175.201|8080|United States|Pittsburgh|CONTINENTAL BROADBAND PENNSYLVANIA, INC.|
|17|200.146.77.133|80|Brazil|Curitiba|Vivo|
|18|201.218.158.79|999|Peru|Lima|M & B Soluciones Peru S.A.C.|
|19|173.212.245.135|3128|Germany|Nuremberg|Contabo GmbH|
|20|201.182.249.114|999|Colombia|Pasto|SP SISTEMAS PALACIOS LTDA|



## Contributing

Contributions are welcome, and they are greatly appreciated! Every
little bit helps, and credit will always be given.

