
# Free HTTP Proxy List 🌍

[![Hourly Update](https://github.com/mertguvencli/http-proxy-list/actions/workflows/main.yml/badge.svg?branch=main)](https://github.com/mertguvencli/http-proxy-list/actions/workflows/main.yml)
![GitHub](https://img.shields.io/github/license/mertguvencli/http-proxy-list)
![GitHub last commit](https://img.shields.io/github/last-commit/mertguvencli/http-proxy-list)

It is a lightweight project that hourly scrapes lots of free-proxy sites, validates if it works, and serves a clean proxy list.


> Scraper found **3142** proxies at the latest update. Usable proxies are below.

## Usage

Click the file format that you want and copy the URL.


|File|Content|Count|
|----|-------|-----|
|[data.txt](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.txt)|`ip_address:port` combined (seperated new line)|61|
|[data.json](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.json)|`ip, port`|61|
|[data-with-geolocation.json](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data-with-geolocation.json)|`ip, port, geolocation`|61|

## Sources

|Source|Found Proxies|Succeed|
|------|-------------|-------|
|[free-proxy-list.net](https://free-proxy-list.net)|300|✅|
|[us-proxy.org](https://www.us-proxy.org)|200|✅|
|[proxydb.net](http://proxydb.net)|15|✅|
|[free-proxy-list.com](https://free-proxy-list.com/?page=&port=&type%5B%5D=http&type%5B%5D=https&up_time=0&search=Search)|10|✅|
|[proxy-list.download](https://www.proxy-list.download/HTTP)|26|✅|
|[vpnoverview.com](https://vpnoverview.com/privacy/anonymous-browsing/free-proxy-servers)|32|✅|
|[proxyscan.io](https://www.proxyscan.io)|92|✅|
|[proxylist.geonode.com](https://proxylist.geonode.com/api/proxy-list?limit=300&page=1&sort_by=lastChecked&sort_type=desc&protocols=http,https)|0|🚫|
|[proxyscrape.com](https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all)|143|✅|
|[github.com/clarketm/proxy-list](https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt)|400|✅|
|[github.com/monosans/proxy-list](https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt)|29|✅|
|[github.com/TheSpeedX/PROXY-List](https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt)|1895|✅|


## Sample Proxies With Geolocation Info

|#|Ip|Port|Country|City|Internet Service Provider|
|-|--|----|-------|----|-------------------------|
|1|159.223.90.238|3129|Singapore|Singapore|DigitalOcean, LLC|
|2|110.78.138.59|8080|Thailand|Samphanthawong|CAT-BB|
|3|200.105.215.18|33630|Bolivia|La Paz|AXS Bolivia S. A.|
|4|103.155.196.23|8080|Indonesia|Sukabumi|JEMBATANDATA|
|5|183.88.192.232|8080|Thailand|Si Maha Phot|Triple T Broadband Public Company Limited|
|6|66.94.97.238|443|United States|New York|Contabo Inc.|
|7|201.174.239.18|8080|Mexico|General Escobedo|Transtelco Inc|
|8|46.98.251.182|8081|Ukraine|Dnipro|ISP "Fregat"|
|9|157.100.12.138|999|Ecuador|Quito|Telconet S.A|
|10|111.77.46.152|9002|China|Jiujiang|Chinanet|
|11|194.169.167.204|8080|Albania|Cerrik|Kadri Haxhiaj trading as "B.I."|
|12|47.252.4.64|8888|United States|Charlottesville|Alibaba.com LLC|
|13|5.167.141.239|3128|Russia|Tula|CJSC "ER-Telecom Holding" Tula branch|
|14|61.4.102.151|3128|Malaysia|Ampang|Gigabit Hosting Sdn Bhd|
|15|194.182.64.18|8081|Czechia|Prague|INTERNET CZ, a.s.|
|16|202.107.231.156|60000|China|Yiwu|Chinanet|
|17|120.42.132.233|3712|China|Quanzhou|Chinanet|
|18|45.94.73.89|8080|Ireland|Dublin|Model Telecom Ltd|
|19|170.83.242.250|999|Paraguay|Asunción|Ufinet Panama S.A.|
|20|218.1.142.142|57114|China|Shanghai|China Telecom|



## Contributing

Contributions are welcome, and they are greatly appreciated! Every
little bit helps, and credit will always be given.

