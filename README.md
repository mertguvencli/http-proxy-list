
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
|[data.txt](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.txt)|`ip_address:port` combined (seperated new line)|109|
|[data.json](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.json)|`ip, port`|109|
|[data-with-geolocation.json](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data-with-geolocation.json)|`ip, port, geolocation`|109|

## Sources

|Source|Found Proxies|Succeed|
|------|-------------|-------|
|[free-proxy-list.net](https://free-proxy-list.net)|300|✅|
|[us-proxy.org](https://www.us-proxy.org)|200|✅|
|[proxydb.net](http://proxydb.net)|15|✅|
|[free-proxy-list.com](https://free-proxy-list.com/?page=&port=&type%5B%5D=http&type%5B%5D=https&up_time=0&search=Search)|0|🚫|
|[proxy-list.download](https://www.proxy-list.download/HTTP)|26|✅|
|[vpnoverview.com](https://vpnoverview.com/privacy/anonymous-browsing/free-proxy-servers)|32|✅|
|[proxyscan.io](https://www.proxyscan.io)|0|🚫|
|[proxylist.geonode.com](https://proxylist.geonode.com/api/proxy-list?limit=300&page=1&sort_by=lastChecked&sort_type=desc&protocols=http,https)|300|✅|
|[proxyscrape.com](https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all)|226|✅|
|[github.com/clarketm/proxy-list](https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt)|400|✅|
|[github.com/monosans/proxy-list](https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt)|93|✅|
|[github.com/TheSpeedX/PROXY-List](https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt)|1864|✅|


## Sample Proxies With Geolocation Info

|#|Ip|Port|Country|City|Internet Service Provider|
|-|--|----|-------|----|-------------------------|
|1|20.47.108.204|8888|United States|Boydton|Microsoft Corporation|
|2|138.197.69.179|8080|United States|Clifton|DigitalOcean, LLC|
|3|177.229.210.66|8080|Mexico|San Rafael Caleria|Mega Cable, S.A. de C.V.|
|4|103.11.106.167|8181|Indonesia|Magetan|PT. Pascal Indonesia|
|5|103.131.18.58|3125|Indonesia|Tangerang|Global Media Inti Semesta|
|6|194.233.73.104|443|Singapore|Singapore|Contabo Asia Private Limited|
|7|89.107.197.165|3128|Russia|Tula|LLC TK Altair|
|8|182.52.83.47|8080|Thailand|Bangkok|TOT Public Company Limited|
|9|178.255.44.197|41890|Poland|Jozefoslaw|Artnet Sp. z o.o.|
|10|112.78.131.2|8080|Indonesia|Jakarta|Biznet Networks|
|11|195.151.212.21|8080|Russia|Moscow|ROSPRINT|
|12|102.68.134.94|8080|Libya|Tripoli|Aljeel Aljadeed For Technology|
|13|201.174.239.18|8080|Mexico|Ciudad Juárez|Transtelco Inc|
|14|143.255.142.80|8080|Paraguay|Ciudad del Este|GIG@NET SOCIEDAD ANONIMA|
|15|190.97.226.236|999|Venezuela|Barinas|NetLink América C.A.|
|16|103.41.173.47|3128|Nepal|Kathmandu|Vianet Communications Pvt. Ltd|
|17|51.77.246.212|3128|France|Roubaix|OVH SAS|
|18|135.148.15.113|3175|United States|Fremont|OVH US LLC|
|19|122.155.165.191|3128|Thailand|Ratchathewi|CAT Telecom Public Company Limited|
|20|162.150.62.93|443|United States|Kincaid|Comcast Cable Communications, LLC|



## Contributing

Contributions are welcome, and they are greatly appreciated! Every
little bit helps, and credit will always be given.

