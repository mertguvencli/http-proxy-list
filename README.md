
# Free HTTP Proxy List 🌍

[![Hourly Update](https://github.com/mertguvencli/http-proxy-list/actions/workflows/main.yml/badge.svg?branch=main)](https://github.com/mertguvencli/http-proxy-list/actions/workflows/main.yml)
![GitHub](https://img.shields.io/github/license/mertguvencli/http-proxy-list)
![GitHub last commit](https://img.shields.io/github/last-commit/mertguvencli/http-proxy-list)

It is a lightweight project that hourly scrapes lots of free-proxy sites, validates if it works, and serves a clean proxy list.


> Scraper found **4048** proxies at the latest update. Usable proxies are below.

## Usage

Click the file format that you want and copy the URL.


|File|Content|Count|
|----|-------|-----|
|[data.txt](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.txt)|`ip_address:port` combined (seperated new line)|307|
|[data.json](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.json)|`ip, port`|307|
|[data-with-geolocation.json](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data-with-geolocation.json)|`ip, port, geolocation`|307|

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
|[proxylist.geonode.com](https://proxylist.geonode.com/api/proxy-list?limit=300&page=1&sort_by=lastChecked&sort_type=desc&protocols=http,https)|300|✅|
|[proxyscrape.com](https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all)|412|✅|
|[github.com/clarketm/proxy-list](https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt)|400|✅|
|[github.com/monosans/proxy-list](https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt)|189|✅|
|[github.com/TheSpeedX/PROXY-List](https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt)|2064|✅|


## Sample Proxies With Geolocation Info

|#|Ip|Port|Country|City|Internet Service Provider|
|-|--|----|-------|----|-------------------------|
|1|216.238.74.45|59394|Mexico|Mexico City|The Constant Company|
|2|12.231.44.251|3128|United States|Racine|AT&T Services, Inc.|
|3|198.41.67.18|8080|United States|Lafayette|Cox Communications Inc.|
|4|157.185.179.70|59394|United States|Los Angeles|Quantil Networks Inc|
|5|150.230.104.199|9090|Japan|Tokyo|Oracle Corporation|
|6|12.231.44.251|3128|United States|Racine|AT&T Services, Inc.|
|7|45.152.188.246|3128|United States|Ashburn|Sprint|
|8|8.219.97.248|80|Singapore|Singapore|Alibaba (US) Technology Co., Ltd.|
|9|193.123.104.244|3128|Brazil|Vinhedo|Oracle Corporation|
|10|157.185.179.70|59394|United States|Los Angeles|Quantil Networks Inc|
|11|216.238.76.66|59394|Mexico|Mexico City|The Constant Company|
|12|171.6.79.182|8080|Thailand|Si Racha|Triple T Broadband Public Company Limited|
|13|180.183.2.62|8080|Thailand|Bang Lamung|Triple T Broadband Public Company Limited|
|14|138.68.238.19|31028|United States|Santa Clara|DigitalOcean, LLC|
|15|8.210.66.212|3128|Hong Kong|Hong Kong|Alibaba.com LLC|
|16|5.189.184.6|80|Germany|Nuremberg|Contabo GmbH|
|17|47.241.165.133|443|Singapore|Singapore|Alibaba.com LLC|
|18|103.144.165.86|8080|Bangladesh|Dhaka|Shine Communication|
|19|103.133.26.107|8181|Indonesia|Pajajaran|PT PHATRIA INTI PERSADA|
|20|201.174.239.18|8080|Mexico|General Escobedo|Transtelco Inc|



## Contributing

Contributions are welcome, and they are greatly appreciated! Every
little bit helps, and credit will always be given.

