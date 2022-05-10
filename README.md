
# Free HTTP Proxy List 🌍

[![Hourly Update](https://github.com/mertguvencli/http-proxy-list/actions/workflows/main.yml/badge.svg?branch=main)](https://github.com/mertguvencli/http-proxy-list/actions/workflows/main.yml)
![GitHub](https://img.shields.io/github/license/mertguvencli/http-proxy-list)
![GitHub last commit](https://img.shields.io/github/last-commit/mertguvencli/http-proxy-list)

It is a lightweight project that hourly scrapes lots of free-proxy sites, validates if it works, and serves a clean proxy list.


> Scraper found **3500** proxies at the latest update. Usable proxies are below.

## Usage

Click the file format that you want and copy the URL.


|File|Content|Count|
|----|-------|-----|
|[data.txt](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.txt)|`ip_address:port` combined (seperated new line)|126|
|[data.json](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.json)|`ip, port`|126|
|[data-with-geolocation.json](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data-with-geolocation.json)|`ip, port, geolocation`|126|

## Sources

|Source|Found Proxies|Succeed|
|------|-------------|-------|
|[free-proxy-list.net](https://free-proxy-list.net)|300|✅|
|[us-proxy.org](https://www.us-proxy.org)|200|✅|
|[proxydb.net](http://proxydb.net)|0|🚫|
|[free-proxy-list.com](https://free-proxy-list.com/?page=&port=&type%5B%5D=http&type%5B%5D=https&up_time=0&search=Search)|10|✅|
|[proxy-list.download](https://www.proxy-list.download/HTTP)|0|🚫|
|[vpnoverview.com](https://vpnoverview.com/privacy/anonymous-browsing/free-proxy-servers)|32|✅|
|[proxyscan.io](https://www.proxyscan.io)|0|🚫|
|[proxylist.geonode.com](https://proxylist.geonode.com/api/proxy-list?limit=300&page=1&sort_by=lastChecked&sort_type=desc&protocols=http,https)|300|✅|
|[proxyscrape.com](https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all)|218|✅|
|[github.com/clarketm/proxy-list](https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt)|400|✅|
|[github.com/monosans/proxy-list](https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt)|221|✅|
|[github.com/TheSpeedX/PROXY-List](https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt)|1819|✅|


## Sample Proxies With Geolocation Info

|#|Ip|Port|Country|City|Internet Service Provider|
|-|--|----|-------|----|-------------------------|
|1|52.60.116.212|80|Canada|Toronto|Amazon Technologies Inc.|
|2|195.39.233.18|8080|Ukraine|Kharkiv|Active Operations LLC|
|3|190.202.111.202|8080|Venezuela|Caracas|CANTV Servicios, Venezuela|
|4|186.67.230.45|3128|Chile|Santiago|Entel Chile S.A.|
|5|103.100.235.233|8080|Bangladesh|Dhaka|MD. Belayat Hossain|
|6|196.15.213.235|3128|South Africa|Christiana|Telkom SA Ltd.|
|7|189.157.126.4|999|Mexico|Ciudad Valles|Uninet S.A. de C.V|
|8|103.79.35.43|34525|India|Raipur|Smart Internet Services|
|9|186.233.186.60|8080|United States|Chicago|Maxihost LTDA|
|10|179.124.31.233|8080|Brazil|Santarém|ZUM TELECOM LTDA- ME|
|11|190.2.212.84|8080|Colombia|Bogotá|TV AZTECA SUCURSAL COLOMBIA|
|12|88.11.39.252|8080|Spain|San Cristóbal de La Laguna|Telefonica de Espana SAU|
|13|110.77.171.56|8080|Thailand|Hat Yai|CAT-BB|
|14|103.247.121.115|8080|Indonesia|Yogyakarta|PT Media Sarana Data|
|15|103.108.75.10|9812|India|Nagpur|Modi infonet digital network Pvt Ltd|
|16|113.189.194.93|19132|Vietnam|Ho Chi Minh City|VNPT|
|17|181.78.0.175|999|Colombia|Chapinero|IFX Networks Argentina S.R.L|
|18|80.244.229.102|10000|Russia|Moscow|Enforta-MSK|
|19|176.214.99.101|1256|Russia|Moscow|Enforta-MSK|
|20|103.84.234.194|8089|Indonesia|Jakarta|PT Maxindo Mitra Solusi|



## Contributing

Contributions are welcome, and they are greatly appreciated! Every
little bit helps, and credit will always be given.

