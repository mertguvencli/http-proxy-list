
# Free HTTP Proxy List 🌍

[![Hourly Update](https://github.com/mertguvencli/http-proxy-list/actions/workflows/main.yml/badge.svg?branch=main)](https://github.com/mertguvencli/http-proxy-list/actions/workflows/main.yml)
![GitHub](https://img.shields.io/github/license/mertguvencli/http-proxy-list)
![GitHub last commit](https://img.shields.io/github/last-commit/mertguvencli/http-proxy-list)

It is a lightweight project that hourly scrapes lots of free-proxy sites, validates if it works, and serves a clean proxy list.


> Scraper found **3687** proxies at the latest update. Usable proxies are below.

## Usage

Click the file format that you want and copy the URL.


|File|Content|Count|
|----|-------|-----|
|[data.txt](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.txt)|`ip_address:port` combined (seperated new line)|131|
|[data.json](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.json)|`ip, port`|131|
|[data-with-geolocation.json](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data-with-geolocation.json)|`ip, port, geolocation`|131|

## Sources

|Source|Found Proxies|Succeed|
|------|-------------|-------|
|[free-proxy-list.net](https://free-proxy-list.net)|300|✅|
|[us-proxy.org](https://www.us-proxy.org)|200|✅|
|[proxydb.net](http://proxydb.net)|15|✅|
|[free-proxy-list.com](https://free-proxy-list.com/?page=&port=&type%5B%5D=http&type%5B%5D=https&up_time=0&search=Search)|0|🚫|
|[proxy-list.download](https://www.proxy-list.download/HTTP)|26|✅|
|[vpnoverview.com](https://vpnoverview.com/privacy/anonymous-browsing/free-proxy-servers)|32|✅|
|[proxyscan.io](https://www.proxyscan.io)|99|✅|
|[proxylist.geonode.com](https://proxylist.geonode.com/api/proxy-list?limit=300&page=1&sort_by=lastChecked&sort_type=desc&protocols=http,https)|271|✅|
|[proxyscrape.com](https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all)|323|✅|
|[github.com/clarketm/proxy-list](https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt)|400|✅|
|[github.com/monosans/proxy-list](https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt)|184|✅|
|[github.com/TheSpeedX/PROXY-List](https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt)|1837|✅|


## Sample Proxies With Geolocation Info

|#|Ip|Port|Country|City|Internet Service Provider|
|-|--|----|-------|----|-------------------------|
|1|168.8.209.253|80|United States|Roswell|Board of Regents of the University System of Georgia|
|2|121.254.195.12|8080|South Korea|Yongsan-dong|LG DACOM Corporation|
|3|168.8.209.253|80|United States|Roswell|Board of Regents of the University System of Georgia|
|4|117.20.216.218|8080|South Korea|Gumi|HYUNDAI COMMUNICATIONS & NETWORK|
|5|47.91.25.174|80|Japan|Tokyo|Alibaba.com LLC|
|6|181.143.235.100|12345|Colombia|Santiago de Cali|EPM Telecomunicaciones S.A. E.S.P.|
|7|186.233.186.60|8080|United States|Chicago|Maxihost LTDA|
|8|18.218.45.35|3128|United States|Dublin|Amazon.com, Inc.|
|9|102.130.79.1|3128|South Africa|Johannesburg|Adnexus Celerity Networks (Proprietary) Limited|
|10|136.243.37.84|9090|Germany|Falkenstein|Hetzner Online GmbH|
|11|75.72.76.3|8118|United States|Hopkins|Comcast Cable Communications, LLC|
|12|103.147.118.66|8080|Indonesia|Arjasa|PT.Bestcamp Prima Data|
|13|47.91.25.94|80|Japan|Tokyo|Alibaba.com LLC|
|14|103.105.212.106|53281|Philippines|Sibulan|Fil Products Service Television Incorporated|
|15|47.245.53.132|80|Japan|Tokyo|Alibaba.com LLC|
|16|188.72.0.117|8080|Iraq|Sulaymaniyah|SAWAD LAND for Information Technology Ltd|
|17|157.100.144.27|999|Ecuador|Hacienda El Triunfo|Telconet S.A|
|18|36.37.160.242|8080|Cambodia|Phnom Penh|VIETTEL (CAMBODIA) PTE.|
|19|201.174.239.18|8080|Mexico|General Escobedo|Transtelco Inc|
|20|103.124.104.139|3128|United States|Los Angeles|DediPath|



## Contributing

Contributions are welcome, and they are greatly appreciated! Every
little bit helps, and credit will always be given.

