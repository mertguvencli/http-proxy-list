
# Free HTTP Proxy List 🌍

[![Hourly Update](https://github.com/mertguvencli/http-proxy-list/actions/workflows/main.yml/badge.svg?branch=main)](https://github.com/mertguvencli/http-proxy-list/actions/workflows/main.yml)
![GitHub](https://img.shields.io/github/license/mertguvencli/http-proxy-list)
![GitHub last commit](https://img.shields.io/github/last-commit/mertguvencli/http-proxy-list)

It is a lightweight project that hourly scrapes lots of free-proxy sites, validates if it works, and serves a clean proxy list.


> Scraper found **3857** proxies at the latest update. Usable proxies are below.

## Usage

Click the file format that you want and copy the URL.


|File|Content|Count|
|----|-------|-----|
|[data.txt](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.txt)|`ip_address:port` combined (seperated new line)|166|
|[data.json](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.json)|`ip, port`|166|
|[data-with-geolocation.json](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data-with-geolocation.json)|`ip, port, geolocation`|166|

## Sources

|Source|Found Proxies|Succeed|
|------|-------------|-------|
|[free-proxy-list.net](https://free-proxy-list.net)|300|✅|
|[us-proxy.org](https://www.us-proxy.org)|200|✅|
|[proxydb.net](http://proxydb.net)|15|✅|
|[free-proxy-list.com](https://free-proxy-list.com/?page=&port=&type%5B%5D=http&type%5B%5D=https&up_time=0&search=Search)|0|🚫|
|[proxy-list.download](https://www.proxy-list.download/HTTP)|26|✅|
|[vpnoverview.com](https://vpnoverview.com/privacy/anonymous-browsing/free-proxy-servers)|32|✅|
|[proxyscan.io](https://www.proxyscan.io)|74|✅|
|[proxylist.geonode.com](https://proxylist.geonode.com/api/proxy-list?limit=300&page=1&sort_by=lastChecked&sort_type=desc&protocols=http,https)|300|✅|
|[proxyscrape.com](https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all)|353|✅|
|[github.com/clarketm/proxy-list](https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt)|400|✅|
|[github.com/monosans/proxy-list](https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt)|217|✅|
|[github.com/TheSpeedX/PROXY-List](https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt)|1940|✅|


## Sample Proxies With Geolocation Info

|#|Ip|Port|Country|City|Internet Service Provider|
|-|--|----|-------|----|-------------------------|
|1|103.124.104.139|3128|United States|Los Angeles|DediPath|
|2|178.209.51.218|7829|Switzerland|Zurich|Nine Internet Solutions AG|
|3|190.97.226.236|999|Venezuela|Barinas|NetLink América C.A.|
|4|103.124.104.139|3128|United States|Los Angeles|DediPath|
|5|195.201.9.178|3128|Germany|Gunzenhausen|Hetzner Online GmbH|
|6|203.150.128.239|8080|Thailand|Chiang Mai|Internet Thailand Company Ltd|
|7|216.155.89.66|999|Chile|Valdivia|Telefonica del Sur S.A.|
|8|103.140.108.50|8080|Indonesia|Jakarta|PT. Fiber Networks Indonesia|
|9|182.253.168.253|8080|Indonesia|Jakarta|BIZNET|
|10|5.189.229.42|1081|Russia|St Petersburg|OOO "Network of data-centers "Selectel"|
|11|136.243.37.84|9090|Germany|Falkenstein|Hetzner Online GmbH|
|12|196.216.84.94|3346|Kenya|Nairobi|Maintainer Liquid Telecommunications Operations Limited|
|13|201.174.239.18|8080|Mexico|General Escobedo|Transtelco Inc|
|14|103.124.104.14|3128|United States|Los Angeles|DediPath|
|15|190.121.192.42|999|Guatemala|Guatemala City|ISP SOLUTIONS S.A.|
|16|178.47.139.151|35102|Russia|Osa|PJSC Rostelecom|
|17|159.65.133.175|31280|Singapore|Singapore|DigitalOcean, LLC|
|18|128.90.113.253|33080|Argentina|Buenos Aires|Powerhouse Management, Inc.|
|19|197.211.38.94|8080|Nigeria|Lagos|Globacom Limited|
|20|186.233.186.60|8080|United States|Chicago|Maxihost LTDA|



## Contributing

Contributions are welcome, and they are greatly appreciated! Every
little bit helps, and credit will always be given.

