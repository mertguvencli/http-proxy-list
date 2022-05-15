
# Free HTTP Proxy List 🌍

[![Hourly Update](https://github.com/mertguvencli/http-proxy-list/actions/workflows/main.yml/badge.svg?branch=main)](https://github.com/mertguvencli/http-proxy-list/actions/workflows/main.yml)
![GitHub](https://img.shields.io/github/license/mertguvencli/http-proxy-list)
![GitHub last commit](https://img.shields.io/github/last-commit/mertguvencli/http-proxy-list)

It is a lightweight project that hourly scrapes lots of free-proxy sites, validates if it works, and serves a clean proxy list.


> Scraper found **3565** proxies at the latest update. Usable proxies are below.

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
|[proxyscrape.com](https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all)|290|✅|
|[github.com/clarketm/proxy-list](https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt)|400|✅|
|[github.com/monosans/proxy-list](https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt)|274|✅|
|[github.com/TheSpeedX/PROXY-List](https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt)|1918|✅|


## Sample Proxies With Geolocation Info

|#|Ip|Port|Country|City|Internet Service Provider|
|-|--|----|-------|----|-------------------------|
|1|186.67.230.45|3128|Chile|Santiago|Entel Chile S.A.|
|2|66.42.125.237|59394|United States|Elk Grove Village|The Constant Company|
|3|188.166.158.18|8080|United Kingdom|London|DigitalOcean|
|4|85.25.91.141|15333|Germany|Cologne|PlusServer GmbH|
|5|85.195.104.71|80|Germany|Frankfurt am Main|Host Europe GmbH|
|6|118.99.103.250|8080|Indonesia|Jakarta|Biznet Metronet|
|7|145.40.73.102|10004|Singapore|Singapore|Packet Host, Inc.|
|8|46.105.35.193|8080|France|Roubaix|OVH SAS|
|9|47.242.176.219|3128|Hong Kong|Hong Kong|Alibaba.com LLC|
|10|145.40.73.107|10001|Singapore|Singapore|Packet Host, Inc.|
|11|190.26.201.194|8080|Colombia|Bogotá|ETB - Colombia|
|12|178.128.117.234|8080|Singapore|Singapore|DigitalOcean, LLC|
|13|20.47.108.204|8888|United States|Boydton|Microsoft Corporation|
|14|181.78.18.93|999|Colombia|Barranquilla|IFX Networks Argentina S.R.L|
|15|165.16.60.1|8080|Libya|Tripoli|Aljeel Aljadeed For Technology|
|16|122.155.165.191|3128|Thailand|Ratchathewi|CAT Telecom Public Company Limited|
|17|123.163.55.123|3128|China|Zhoukou|Chinanet|
|18|85.235.184.186|3129|Russia|Moscow|MTS PJSC|
|19|164.92.213.29|8080|Netherlands|Amsterdam|DigitalOcean, LLC|
|20|102.130.79.1|3128|South Africa|Johannesburg|Adnexus Celerity Networks (Proprietary) Limited|



## Contributing

Contributions are welcome, and they are greatly appreciated! Every
little bit helps, and credit will always be given.

