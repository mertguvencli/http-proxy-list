
# Free HTTP Proxy List 🌍

[![Hourly Update](https://github.com/mertguvencli/http-proxy-list/actions/workflows/main.yml/badge.svg?branch=main)](https://github.com/mertguvencli/http-proxy-list/actions/workflows/main.yml)
![GitHub](https://img.shields.io/github/license/mertguvencli/http-proxy-list)
![GitHub last commit](https://img.shields.io/github/last-commit/mertguvencli/http-proxy-list)

It is a lightweight project that hourly scrapes lots of free-proxy sites, validates if it works, and serves a clean proxy list.


> Scraper found **3456** proxies at the latest update. Usable proxies are below.

## Usage

Click the file format that you want and copy the URL.


|File|Content|Count|
|----|-------|-----|
|[data.txt](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.txt)|`ip_address:port` combined (seperated new line)|83|
|[data.json](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.json)|`ip, port`|83|
|[data-with-geolocation.json](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data-with-geolocation.json)|`ip, port, geolocation`|83|

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
|[proxyscrape.com](https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all)|284|✅|
|[github.com/clarketm/proxy-list](https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt)|400|✅|
|[github.com/monosans/proxy-list](https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt)|197|✅|
|[github.com/TheSpeedX/PROXY-List](https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt)|1892|✅|


## Sample Proxies With Geolocation Info

|#|Ip|Port|Country|City|Internet Service Provider|
|-|--|----|-------|----|-------------------------|
|1|5.53.16.185|18080|Russia|Surgut|Metroset Ltd|
|2|46.0.114.185|55443|Russia|Samara|CJSC "ER-Telecom Holding" Samara branch|
|3|116.50.30.82|9812|Indonesia|Jakarta|DELTANET|
|4|186.67.230.45|3128|Chile|Santiago|Entel Chile S.A.|
|5|190.26.201.194|8080|Colombia|Bogotá|ETB - Colombia|
|6|201.174.239.18|8080|Mexico|Monterrey|Transtelco Inc|
|7|181.49.217.254|8080|Colombia|Medellín|Telmex Colombia S.A.|
|8|190.186.159.17|999|Bolivia|Santa Cruz|Cotas Ltda.|
|9|51.89.33.32|20000|United Kingdom|London|OVH SAS|
|10|121.156.109.108|8080|South Korea|Seongnam-si|Korea Telecom|
|11|218.1.142.159|57114|China|Shanghai|China Telecom|
|12|38.123.68.152|999|Mexico|Juanacatlan|Cogent Communications|
|13|186.67.230.45|3128|Chile|Santiago|Entel Chile S.A.|
|14|189.4.184.34|8080|Brazil|Santos|Claro S.A.|
|15|45.234.63.218|999|Venezuela|Caracas|SOLUCIONES INSTALRED CH&C C.A.|
|16|41.138.168.2|8080|Nigeria|Lagos|Autonomous System number for Cyber Space|
|17|165.16.60.1|8080|Libya|Tripoli|Aljeel Aljadeed For Technology|
|18|171.103.58.122|8080|Thailand|Bangkok|True Internet Co., Ltd.|
|19|45.70.14.58|999|Ecuador|Baba|Nedetel S.A.|
|20|82.167.253.137|8080|Saudi Arabia|Riyadh|ORBITNET.KSA|



## Contributing

Contributions are welcome, and they are greatly appreciated! Every
little bit helps, and credit will always be given.

