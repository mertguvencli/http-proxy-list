
# Free HTTP Proxy List 🌍

[![Hourly Update](https://github.com/mertguvencli/http-proxy-list/actions/workflows/main.yml/badge.svg?branch=main)](https://github.com/mertguvencli/http-proxy-list/actions/workflows/main.yml)
![GitHub](https://img.shields.io/github/license/mertguvencli/http-proxy-list)
![GitHub last commit](https://img.shields.io/github/last-commit/mertguvencli/http-proxy-list)

It is a lightweight project that hourly scrapes lots of free-proxy sites, validates if it works, and serves a clean proxy list.


> Scraper found **3583** proxies at the latest update. Usable proxies are below.

## Usage

Click the file format that you want and copy the URL.


|File|Content|Count|
|----|-------|-----|
|[data.txt](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.txt)|`ip_address:port` combined (seperated new line)|170|
|[data.json](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.json)|`ip, port`|170|
|[data-with-geolocation.json](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data-with-geolocation.json)|`ip, port, geolocation`|170|

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
|[proxyscrape.com](https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all)|390|✅|
|[github.com/clarketm/proxy-list](https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt)|400|✅|
|[github.com/monosans/proxy-list](https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt)|158|✅|
|[github.com/TheSpeedX/PROXY-List](https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt)|1952|✅|


## Sample Proxies With Geolocation Info

|#|Ip|Port|Country|City|Internet Service Provider|
|-|--|----|-------|----|-------------------------|
|1|162.243.159.46|3128|United States|San Francisco|DigitalOcean, LLC|
|2|20.47.108.204|8888|United States|Boydton|Microsoft Corporation|
|3|162.243.159.46|3128|United States|San Francisco|DigitalOcean, LLC|
|4|67.206.202.145|999|Puerto Rico|San Juan|Skynet Wireless|
|5|189.112.10.242|3128|Brazil|São Paulo|ALGAR TELECOM S/A|
|6|186.233.186.60|8080|United States|Chicago|Maxihost LTDA|
|7|181.129.14.166|999|Colombia|Medellín|EPM Telecomunicaciones S.A. E.S.P.|
|8|186.96.116.12|999|Colombia|Flandes|TV AZTECA SUCURSAL COLOMBIA|
|9|92.60.190.22|50335|Ukraine|Kyiv|Komtel|
|10|80.244.226.92|8080|Russia|Moscow|Enforta-MSK|
|11|167.250.223.63|999|Guatemala|Guatemala City|Ufinet Panama S.A.|
|12|190.26.201.194|8080|Colombia|Bogotá|ETB - Colombia|
|13|5.39.189.39|3128|Netherlands|Rotterdam|ColoCenter b.v.|
|14|89.109.252.129|8080|Russia|Balashikha|CTC-IPOE|
|15|201.159.113.163|999|El Salvador|San Salvador|Ufinet Panama S.A.|
|16|177.234.208.73|8080|Ecuador|Guayaquil|Nedetel S.A.|
|17|5.16.0.174|8080|Russia|St Petersburg|Enforta-MSK|
|18|149.91.80.206|3128|France|Nanterre|Serverd SAS|
|19|176.119.134.164|23500|Spain|Puerto Serrano|Electro Puerto SUR SL|
|20|203.153.125.246|8080|Indonesia|Tangerang|GMNUSANTARA|



## Contributing

Contributions are welcome, and they are greatly appreciated! Every
little bit helps, and credit will always be given.

