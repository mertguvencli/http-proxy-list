
# Free HTTP Proxy List 🌍

[![Hourly Update](https://github.com/mertguvencli/http-proxy-list/actions/workflows/main.yml/badge.svg?branch=main)](https://github.com/mertguvencli/http-proxy-list/actions/workflows/main.yml)
![GitHub](https://img.shields.io/github/license/mertguvencli/http-proxy-list)
![GitHub last commit](https://img.shields.io/github/last-commit/mertguvencli/http-proxy-list)

It is a lightweight project that hourly scrapes lots of free-proxy sites, validates if it works, and serves a clean proxy list.


> Scraper found **3980** proxies at the latest update. Usable proxies are below.

## Usage

Click the file format that you want and copy the URL.


|File|Content|Count|
|----|-------|-----|
|[data.txt](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.txt)|`ip_address:port` combined (seperated new line)|204|
|[data.json](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.json)|`ip, port`|204|
|[data-with-geolocation.json](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data-with-geolocation.json)|`ip, port, geolocation`|204|

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
|[proxyscrape.com](https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all)|435|✅|
|[github.com/clarketm/proxy-list](https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt)|400|✅|
|[github.com/monosans/proxy-list](https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt)|228|✅|
|[github.com/TheSpeedX/PROXY-List](https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt)|1934|✅|


## Sample Proxies With Geolocation Info

|#|Ip|Port|Country|City|Internet Service Provider|
|-|--|----|-------|----|-------------------------|
|1|20.47.108.204|8888|United States|Boydton|Microsoft Corporation|
|2|144.202.48.244|59394|United States|Elk Grove Village|Choopa|
|3|212.112.113.178|3128|Kyrgyzstan|Bishkek|AkNet|
|4|144.217.240.185|9300|Canada|Beauharnois|OVH SAS|
|5|103.73.194.2|80|Hong Kong|Wanchai|TouchPal HK Co., Limited|
|6|201.120.27.15|53281|Mexico|Hermosillo|Uninet S.A. de C.V|
|7|102.130.79.254|3128|South Africa|Pretoria|Adnexus Celerity Networks (Proprietary) Limited|
|8|167.249.180.42|8080|Brazil|Manaus|Eyes Nwhere Sistemas Inteligentes de Imagem Ltda|
|9|23.224.198.13|59394|United States|Los Angeles|Cnservers LLC|
|10|194.233.86.75|1234|Singapore|Singapore|Contabo Asia Private Limited|
|11|190.26.201.194|8080|Colombia|Castilla La Nueva|ETB - Colombia|
|12|93.86.63.73|8080|Serbia|Kraljevo|TELEKOM-SRBIJA|
|13|65.51.178.93|3128|United States|Weehawken|Cablevision Systems Corp.|
|14|174.81.78.64|48678|United States|Wallace|Charter Communications|
|15|66.94.120.161|443|United States|Seattle|Contabo Inc.|
|16|159.65.133.175|31280|Singapore|Singapore|DigitalOcean, LLC|
|17|185.65.253.161|8080|Iraq|Baghdad|IQ Band|
|18|91.121.42.14|1081|France|Roubaix|OVH SAS|
|19|5.167.141.239|3128|Russia|Tula|CJSC "ER-Telecom Holding" Tula branch|
|20|130.61.95.193|3128|Germany|Frankfurt am Main|Oracle Corporation|



## Contributing

Contributions are welcome, and they are greatly appreciated! Every
little bit helps, and credit will always be given.

