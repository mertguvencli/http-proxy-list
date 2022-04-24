
# Free HTTP Proxy List 🌍

[![Hourly Update](https://github.com/mertguvencli/http-proxy-list/actions/workflows/main.yml/badge.svg?branch=main)](https://github.com/mertguvencli/http-proxy-list/actions/workflows/main.yml)
![GitHub](https://img.shields.io/github/license/mertguvencli/http-proxy-list)
![GitHub last commit](https://img.shields.io/github/last-commit/mertguvencli/http-proxy-list)

It is a lightweight project that hourly scrapes lots of free-proxy sites, validates if it works, and serves a clean proxy list.


> Scraper found **2715** proxies at the latest update. Usable proxies are below.

## Usage

Click the file format that you want and copy the URL.


|File|Content|Count|
|----|-------|-----|
|[data.txt](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.txt)|`ip_address:port` combined (seperated new line)|71|
|[data.json](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.json)|`ip, port`|71|
|[data-with-geolocation.json](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data-with-geolocation.json)|`ip, port, geolocation`|71|

## Sources

|Source|Found Proxies|Succeed|
|------|-------------|-------|
|[free-proxy-list.net](https://free-proxy-list.net)|0|🚫|
|[us-proxy.org](https://www.us-proxy.org)|0|🚫|
|[proxydb.net](http://proxydb.net)|0|🚫|
|[free-proxy-list.com](https://free-proxy-list.com/?page=&port=&type%5B%5D=http&type%5B%5D=https&up_time=0&search=Search)|0|🚫|
|[proxy-list.download](https://www.proxy-list.download/HTTP)|0|🚫|
|[vpnoverview.com](https://vpnoverview.com/privacy/anonymous-browsing/free-proxy-servers)|0|🚫|
|[proxyscan.io](https://www.proxyscan.io)|0|🚫|
|[proxylist.geonode.com](https://proxylist.geonode.com/api/proxy-list?limit=300&page=1&sort_by=lastChecked&sort_type=desc&protocols=http,https)|0|🚫|
|[proxyscrape.com](https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all)|207|✅|
|[github.com/clarketm/proxy-list](https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt)|400|✅|
|[github.com/monosans/proxy-list](https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt)|117|✅|
|[github.com/TheSpeedX/PROXY-List](https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt)|1991|✅|


## Sample Proxies With Geolocation Info

|#|Ip|Port|Country|City|Internet Service Provider|
|-|--|----|-------|----|-------------------------|
|1|63.161.104.189|3128|United States|Itasca|Sprint|
|2|52.90.182.59|16133|United States|Ashburn|Amazon.com, Inc.|
|3|95.216.12.141|22214|Finland|Helsinki|Hetzner Online GmbH|
|4|52.236.90.60|3128|Ireland|Dublin|Microsoft Corporation|
|5|181.224.207.20|999|Dominican Republic|Santiago de los Caballeros|BW TELECOM|
|6|122.155.165.191|3128|Thailand|Ratchathewi|CAT Telecom Public Company Limited|
|7|123.163.55.123|3128|China|Zhoukou|Chinanet|
|8|62.138.7.104|5566|France|Strasbourg|Host Europe Group|
|9|181.196.241.198|9100|Ecuador|Guayaquil|Corporacion Nacional De Telecomunicaciones - CNT EP|
|10|85.25.133.28|5566|France|Strasbourg|Host Europe GmbH|
|11|85.25.117.134|5566|France|Strasbourg|BSB-SERVICE|
|12|201.174.239.18|8080|Mexico|Monterrey|Transtelco Inc|
|13|165.16.27.17|1981|Libya|Tripoli|Aljeel Aljadeed For Technology|
|14|116.254.119.31|8080|Indonesia|Yogyakarta|PT Media Sarana Data|
|15|45.195.76.114|999|Dominican Republic|Santo Domingo Este|Orbitek SRL|
|16|104.223.89.137|8118|United States|Atlanta|QuadraNet Enterprises LLC|
|17|190.26.201.194|8080|Colombia|Castilla La Nueva|ETB - Colombia|
|18|89.250.152.76|8080|Russia|Tyumen|JSC "ER-Telecom Holding"|
|19|65.51.178.92|3128|United States|Weehawken|Cablevision Systems Corp.|
|20|177.93.41.158|999|Colombia|Ibague|TV AZTECA SUCURSAL COLOMBIA|



## Contributing

Contributions are welcome, and they are greatly appreciated! Every
little bit helps, and credit will always be given.

