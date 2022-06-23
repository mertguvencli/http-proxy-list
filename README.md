
# Free HTTP Proxy List 🌍

[![Hourly Update](https://github.com/mertguvencli/http-proxy-list/actions/workflows/main.yml/badge.svg?branch=main)](https://github.com/mertguvencli/http-proxy-list/actions/workflows/main.yml)
![GitHub](https://img.shields.io/github/license/mertguvencli/http-proxy-list)
![GitHub last commit](https://img.shields.io/github/last-commit/mertguvencli/http-proxy-list)

It is a lightweight project that hourly scrapes lots of free-proxy sites, validates if it works, and serves a clean proxy list.


> Scraper found **3976** proxies at the latest update. Usable proxies are below.

## Usage

Click the file format that you want and copy the URL.


|File|Content|Count|
|----|-------|-----|
|[data.txt](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.txt)|`ip_address:port` combined (seperated new line)|252|
|[data.json](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.json)|`ip, port`|252|
|[data-with-geolocation.json](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data-with-geolocation.json)|`ip, port, geolocation`|252|

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
|[proxyscrape.com](https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all)|373|✅|
|[github.com/clarketm/proxy-list](https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt)|400|✅|
|[github.com/monosans/proxy-list](https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt)|198|✅|
|[github.com/TheSpeedX/PROXY-List](https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt)|2122|✅|


## Sample Proxies With Geolocation Info

|#|Ip|Port|Country|City|Internet Service Provider|
|-|--|----|-------|----|-------------------------|
|1|216.37.138.177|3128|United States|Pittsburgh|Frontier Communications of America|
|2|66.196.238.180|3128|United States|Houston|Logix|
|3|81.4.102.223|8081|Netherlands|Amsterdam|WeservIT|
|4|81.4.102.233|8081|Netherlands|Amsterdam|WeservIT|
|5|80.85.86.240|1235|United Kingdom|London|Linode, LLC|
|6|45.131.251.234|3129|United States|Los Angeles|DediPath|
|7|121.156.109.108|8080|South Korea|Seongnam-si|Korea Telecom|
|8|183.111.25.253|80|South Korea|Seongnam-si|Korea Telecom|
|9|105.112.191.250|3128|Nigeria|Lagos|Airtel Networks Limited|
|10|181.129.243.100|999|Colombia|Santiago de Cali|EPM Telecomunicaciones S.A. E.S.P.|
|11|200.110.168.159|8080|Colombia|Trujillo|Media Commerce Partners S.A|
|12|115.96.208.124|8080|India|Mumbai|Hathway IP over Cable Internet Access|
|13|220.132.0.156|8787|Taiwan|Taipei|Chunghwa Telecom Co., Ltd.|
|14|176.62.188.10|8123|Russia|Moscow|OOO Istranet|
|15|37.29.74.117|8080|Russia|Kuznechikha|MegaFon|
|16|216.37.138.177|3128|United States|Pittsburgh|Frontier Communications of America|
|17|179.97.51.242|80|Brazil|Sao Goncalo|Vipnet Baixada Telecom. e InformÔtica Ltda|
|18|103.211.219.58|3128|India|Mumbai|PDRO1|
|19|147.75.113.231|8080|Colombia|Quibdó|TV AZTECA SUCURSAL COLOMBIA|
|20|212.112.127.20|8080|Kyrgyzstan|Bishkek|AKNET Ltd.|



## Contributing

Contributions are welcome, and they are greatly appreciated! Every
little bit helps, and credit will always be given.

