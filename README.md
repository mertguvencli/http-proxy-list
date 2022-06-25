
# Free HTTP Proxy List 🌍

[![Hourly Update](https://github.com/mertguvencli/http-proxy-list/actions/workflows/main.yml/badge.svg?branch=main)](https://github.com/mertguvencli/http-proxy-list/actions/workflows/main.yml)
![GitHub](https://img.shields.io/github/license/mertguvencli/http-proxy-list)
![GitHub last commit](https://img.shields.io/github/last-commit/mertguvencli/http-proxy-list)

It is a lightweight project that hourly scrapes lots of free-proxy sites, validates if it works, and serves a clean proxy list.


> Scraper found **3704** proxies at the latest update. Usable proxies are below.

## Usage

Click the file format that you want and copy the URL.


|File|Content|Count|
|----|-------|-----|
|[data.txt](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.txt)|`ip_address:port` combined (seperated new line)|360|
|[data.json](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.json)|`ip, port`|360|
|[data-with-geolocation.json](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data-with-geolocation.json)|`ip, port, geolocation`|360|

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
|[proxyscrape.com](https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all)|395|✅|
|[github.com/clarketm/proxy-list](https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt)|400|✅|
|[github.com/monosans/proxy-list](https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt)|178|✅|
|[github.com/TheSpeedX/PROXY-List](https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt)|2048|✅|


## Sample Proxies With Geolocation Info

|#|Ip|Port|Country|City|Internet Service Provider|
|-|--|----|-------|----|-------------------------|
|1|35.234.248.49|3128|Canada|Montreal|Google LLC|
|2|108.187.44.121|3129|United States|Los Angeles|Leaseweb USA, Inc.|
|3|34.220.50.208|3128|United States|Portland|Amazon.com, Inc.|
|4|50.17.41.16|8080|United States|Ashburn|Amazon.com|
|5|45.175.238.70|999|Mexico|Atitalaquia|Hulux Telecomunicaciones|
|6|45.131.251.224|3129|United States|Los Angeles|DediPath|
|7|45.131.251.233|3129|United States|Los Angeles|DediPath|
|8|209.182.235.252|3128|United States|Los Angeles|HIVELOCITY, Inc.|
|9|206.189.23.38|8048|United Kingdom|London|DigitalOcean, LLC|
|10|148.251.45.123|3128|Germany|Falkenstein|Hetzner Online GmbH|
|11|45.167.124.5|9992|Colombia|Guapi|Sepcom Comunicaciones SAS|
|12|3.10.56.88|3128|United Kingdom|London|Amazon Technologies Inc.|
|13|167.114.185.69|3128|Canada|Montreal|OVH SAS|
|14|78.47.219.204|3128|Germany|Nuremberg|Hetzner Online GmbH|
|15|50.17.41.16|8080|United States|Ashburn|Amazon.com|
|16|185.76.9.123|3128|Sweden|Stockholm|DataCamp Limited|
|17|34.220.50.208|3128|United States|Portland|Amazon.com, Inc.|
|18|211.114.153.184|443|South Korea|Seongnam-si|Korea Telecom|
|19|157.100.12.138|999|Ecuador|Loja|Telconet S.A|
|20|93.84.65.72|3128|Belarus|Gomel|Republican Unitary Telecommunication Enterprise Beltelecom|



## Contributing

Contributions are welcome, and they are greatly appreciated! Every
little bit helps, and credit will always be given.

