
# Free HTTP Proxy List 🌍

[![Hourly Update](https://github.com/mertguvencli/http-proxy-list/actions/workflows/main.yml/badge.svg?branch=main)](https://github.com/mertguvencli/http-proxy-list/actions/workflows/main.yml)
![GitHub](https://img.shields.io/github/license/mertguvencli/http-proxy-list)
![GitHub last commit](https://img.shields.io/github/last-commit/mertguvencli/http-proxy-list)

It is a lightweight project that hourly scrapes lots of free-proxy sites, validates if it works, and serves a clean proxy list.


> Scraper found **3533** proxies at the latest update. Usable proxies are below.

## Usage

Click the file format that you want and copy the URL.


|File|Content|Count|
|----|-------|-----|
|[data.txt](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.txt)|`ip_address:port` combined (seperated new line)|101|
|[data.json](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.json)|`ip, port`|101|
|[data-with-geolocation.json](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data-with-geolocation.json)|`ip, port, geolocation`|101|

## Sources

|Source|Found Proxies|Succeed|
|------|-------------|-------|
|[free-proxy-list.net](https://free-proxy-list.net)|300|✅|
|[us-proxy.org](https://www.us-proxy.org)|200|✅|
|[proxydb.net](http://proxydb.net)|15|✅|
|[free-proxy-list.com](https://free-proxy-list.com/?page=&port=&type%5B%5D=http&type%5B%5D=https&up_time=0&search=Search)|0|🚫|
|[proxy-list.download](https://www.proxy-list.download/HTTP)|26|✅|
|[vpnoverview.com](https://vpnoverview.com/privacy/anonymous-browsing/free-proxy-servers)|32|✅|
|[proxyscan.io](https://www.proxyscan.io)|47|✅|
|[proxylist.geonode.com](https://proxylist.geonode.com/api/proxy-list?limit=300&page=1&sort_by=lastChecked&sort_type=desc&protocols=http,https)|300|✅|
|[proxyscrape.com](https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all)|243|✅|
|[github.com/clarketm/proxy-list](https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt)|400|✅|
|[github.com/monosans/proxy-list](https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt)|135|✅|
|[github.com/TheSpeedX/PROXY-List](https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt)|1835|✅|


## Sample Proxies With Geolocation Info

|#|Ip|Port|Country|City|Internet Service Provider|
|-|--|----|-------|----|-------------------------|
|1|121.254.195.12|8080|South Korea|Yongsan-dong|LG DACOM Corporation|
|2|209.250.253.162|59394|Netherlands|Amsterdam|The Constant Company|
|3|136.243.37.84|9090|Germany|Falkenstein|Hetzner Online GmbH|
|4|195.4.165.41|8080|Germany|Esslingen am Neckar|WORTMANN AG|
|5|190.63.35.30|9812|Ecuador|Guayaquil|CONECEL|
|6|201.174.239.18|8080|Mexico|General Escobedo|Transtelco Inc|
|7|136.243.37.84|9090|Germany|Falkenstein|Hetzner Online GmbH|
|8|190.97.226.236|999|Venezuela|Barinas|NetLink América C.A.|
|9|121.254.195.12|8080|South Korea|Yongsan-dong|LG DACOM Corporation|
|10|36.89.252.155|8080|Indonesia|Jakarta|PT. Telekomunikasi Indonesia|
|11|202.62.49.86|8080|Cambodia|Phnom Penh|COGETEL Co., Ltd|
|12|85.117.239.22|3128|Turkey|Bahçelievler|Taner Temel|
|13|103.4.94.12|3128|Pakistan|Lahore|HEC|
|14|93.185.123.154|3128|Italy|Pove del Grappa|Omegacom S.R.L.S.|
|15|101.43.95.215|7777|China|Haidian|Shenzhen Tencent Computer Systems Company Limited|
|16|49.231.200.212|8080|Thailand|Ratchathewi|Advanced Wireless Network Company Limited|
|17|45.114.118.81|3128|Indonesia|Jakarta|CLDREU|
|18|167.172.239.13|3128|United States|Clifton|DigitalOcean, LLC|
|19|186.96.21.154|999|Mexico|Mérida|Total Play Telecomunicaciones SA De CV|
|20|103.78.170.13|83|India|Pune|Sanjeevan Networks Services Pvt Ltd|



## Contributing

Contributions are welcome, and they are greatly appreciated! Every
little bit helps, and credit will always be given.

