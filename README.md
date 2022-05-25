
# Free HTTP Proxy List 🌍

[![Hourly Update](https://github.com/mertguvencli/http-proxy-list/actions/workflows/main.yml/badge.svg?branch=main)](https://github.com/mertguvencli/http-proxy-list/actions/workflows/main.yml)
![GitHub](https://img.shields.io/github/license/mertguvencli/http-proxy-list)
![GitHub last commit](https://img.shields.io/github/last-commit/mertguvencli/http-proxy-list)

It is a lightweight project that hourly scrapes lots of free-proxy sites, validates if it works, and serves a clean proxy list.


> Scraper found **4107** proxies at the latest update. Usable proxies are below.

## Usage

Click the file format that you want and copy the URL.


|File|Content|Count|
|----|-------|-----|
|[data.txt](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.txt)|`ip_address:port` combined (seperated new line)|239|
|[data.json](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.json)|`ip, port`|239|
|[data-with-geolocation.json](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data-with-geolocation.json)|`ip, port, geolocation`|239|

## Sources

|Source|Found Proxies|Succeed|
|------|-------------|-------|
|[free-proxy-list.net](https://free-proxy-list.net)|300|✅|
|[us-proxy.org](https://www.us-proxy.org)|200|✅|
|[proxydb.net](http://proxydb.net)|15|✅|
|[free-proxy-list.com](https://free-proxy-list.com/?page=&port=&type%5B%5D=http&type%5B%5D=https&up_time=0&search=Search)|0|🚫|
|[proxy-list.download](https://www.proxy-list.download/HTTP)|26|✅|
|[vpnoverview.com](https://vpnoverview.com/privacy/anonymous-browsing/free-proxy-servers)|32|✅|
|[proxyscan.io](https://www.proxyscan.io)|100|✅|
|[proxylist.geonode.com](https://proxylist.geonode.com/api/proxy-list?limit=300&page=1&sort_by=lastChecked&sort_type=desc&protocols=http,https)|300|✅|
|[proxyscrape.com](https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all)|416|✅|
|[github.com/clarketm/proxy-list](https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt)|400|✅|
|[github.com/monosans/proxy-list](https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt)|291|✅|
|[github.com/TheSpeedX/PROXY-List](https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt)|2027|✅|


## Sample Proxies With Geolocation Info

|#|Ip|Port|Country|City|Internet Service Provider|
|-|--|----|-------|----|-------------------------|
|1|20.47.108.204|8888|United States|Boydton|Microsoft Corporation|
|2|20.47.108.204|8888|United States|Boydton|Microsoft Corporation|
|3|18.206.33.119|8888|United States|Ashburn|Amazon.com, Inc.|
|4|136.243.37.84|9090|Germany|Falkenstein|Hetzner Online GmbH|
|5|69.71.202.178|8080|United States|South Gate|California Telecom|
|6|201.71.159.8|5566|Brazil|Cuiabá|Younet Internet|
|7|43.156.70.173|8001|Singapore|Singapore|Shenzhen Tencent Computer Systems Company Limited|
|8|190.61.57.45|8080|Colombia|Canasgordas|Ufinet Panama S.A.|
|9|192.162.192.148|55443|Russia|Uglich|Sigma-Net Ltd.|
|10|47.241.165.133|443|Singapore|Singapore|Alibaba.com LLC|
|11|187.1.88.106|3128|Brazil|Belo Horizonte|Telbrax Ltda|
|12|121.254.195.12|8080|South Korea|Yongsan-dong|LG DACOM Corporation|
|13|124.158.167.18|8080|Indonesia|Tangerang|ICON+|
|14|179.51.162.8|9812|Peru|Íllimo|Telecable Central Network Sociedad Anonima Cerrada|
|15|202.145.13.109|8080|Indonesia|Puspasari|PT Jala Lintas Media|
|16|121.254.195.12|8080|South Korea|Yongsan-dong|LG DACOM Corporation|
|17|190.181.16.206|999|Bolivia|La Paz|AXS Bolivia S. A.|
|18|122.155.165.191|3128|Thailand|Ratchathewi|CAT Telecom Public Company Limited|
|19|117.34.25.11|55443|China|Chongqing|China Telecom (Group)|
|20|190.97.226.236|999|Venezuela|Barinas|NetLink América C.A.|



## Contributing

Contributions are welcome, and they are greatly appreciated! Every
little bit helps, and credit will always be given.

