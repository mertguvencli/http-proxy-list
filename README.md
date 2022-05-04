
# Free HTTP Proxy List 🌍

[![Hourly Update](https://github.com/mertguvencli/http-proxy-list/actions/workflows/main.yml/badge.svg?branch=main)](https://github.com/mertguvencli/http-proxy-list/actions/workflows/main.yml)
![GitHub](https://img.shields.io/github/license/mertguvencli/http-proxy-list)
![GitHub last commit](https://img.shields.io/github/last-commit/mertguvencli/http-proxy-list)

It is a lightweight project that hourly scrapes lots of free-proxy sites, validates if it works, and serves a clean proxy list.


> Scraper found **3568** proxies at the latest update. Usable proxies are below.

## Usage

Click the file format that you want and copy the URL.


|File|Content|Count|
|----|-------|-----|
|[data.txt](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.txt)|`ip_address:port` combined (seperated new line)|149|
|[data.json](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.json)|`ip, port`|149|
|[data-with-geolocation.json](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data-with-geolocation.json)|`ip, port, geolocation`|149|

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
|[proxylist.geonode.com](https://proxylist.geonode.com/api/proxy-list?limit=300&page=1&sort_by=lastChecked&sort_type=desc&protocols=http,https)|0|🚫|
|[proxyscrape.com](https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all)|309|✅|
|[github.com/clarketm/proxy-list](https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt)|400|✅|
|[github.com/monosans/proxy-list](https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt)|232|✅|
|[github.com/TheSpeedX/PROXY-List](https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt)|1944|✅|


## Sample Proxies With Geolocation Info

|#|Ip|Port|Country|City|Internet Service Provider|
|-|--|----|-------|----|-------------------------|
|1|45.76.26.132|59394|United States|Elk Grove Village|The Constant Company|
|2|45.76.20.210|59394|United States|Elk Grove Village|The Constant Company|
|3|202.182.117.88|59394|Japan|Heiwajima|The Constant Company|
|4|167.114.96.27|9300|Canada|Montreal|OVH SAS|
|5|49.48.126.219|8080|Thailand|Ban Kho|Triple T Broadband Public Company Limited|
|6|181.118.158.131|999|Colombia|Paipa|Media Commerce Partners S.A|
|7|45.76.26.132|59394|United States|Elk Grove Village|The Constant Company|
|8|103.168.29.228|9812|Indonesia|Kampungbaru|Dinas Komunikasi Informatika Persandian dan Statistik Kabuapten Bueleleng|
|9|201.20.104.206|666|Brazil|Baturite|MOB SERVICOS DE TELECOMUNICACOES S.A|
|10|45.76.20.210|59394|United States|Elk Grove Village|The Constant Company|
|11|45.76.13.167|59394|United States|Piscataway|The Constant Company|
|12|45.63.69.252|59394|United States|Elk Grove Village|The Constant Company|
|13|85.25.91.141|15333|Germany|Cologne|PlusServer GmbH|
|14|102.68.128.214|8080|Libya|Tripoli|Aljeel Aljadeed For Technology|
|15|45.76.13.167|59394|United States|Piscataway|The Constant Company|
|16|176.241.89.244|53583|Iraq|Baghdad|Hayat ISP|
|17|182.253.158.243|8080|Indonesia|Bandung|BIZNET|
|18|190.26.201.194|8080|Colombia|Bogotá|ETB - Colombia|
|19|123.56.124.235|3128|China|Beijing|Hangzhou Alibaba Advertising Co|
|20|122.155.165.191|3128|Thailand|Ratchathewi|CAT Telecom Public Company Limited|



## Contributing

Contributions are welcome, and they are greatly appreciated! Every
little bit helps, and credit will always be given.

