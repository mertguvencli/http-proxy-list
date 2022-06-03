
# Free HTTP Proxy List 🌍

[![Hourly Update](https://github.com/mertguvencli/http-proxy-list/actions/workflows/main.yml/badge.svg?branch=main)](https://github.com/mertguvencli/http-proxy-list/actions/workflows/main.yml)
![GitHub](https://img.shields.io/github/license/mertguvencli/http-proxy-list)
![GitHub last commit](https://img.shields.io/github/last-commit/mertguvencli/http-proxy-list)

It is a lightweight project that hourly scrapes lots of free-proxy sites, validates if it works, and serves a clean proxy list.


> Scraper found **3732** proxies at the latest update. Usable proxies are below.

## Usage

Click the file format that you want and copy the URL.


|File|Content|Count|
|----|-------|-----|
|[data.txt](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.txt)|`ip_address:port` combined (seperated new line)|256|
|[data.json](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.json)|`ip, port`|256|
|[data-with-geolocation.json](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data-with-geolocation.json)|`ip, port, geolocation`|256|

## Sources

|Source|Found Proxies|Succeed|
|------|-------------|-------|
|[free-proxy-list.net](https://free-proxy-list.net)|300|✅|
|[us-proxy.org](https://www.us-proxy.org)|200|✅|
|[proxydb.net](http://proxydb.net)|15|✅|
|[free-proxy-list.com](https://free-proxy-list.com/?page=&port=&type%5B%5D=http&type%5B%5D=https&up_time=0&search=Search)|10|✅|
|[proxy-list.download](https://www.proxy-list.download/HTTP)|26|✅|
|[vpnoverview.com](https://vpnoverview.com/privacy/anonymous-browsing/free-proxy-servers)|32|✅|
|[proxyscan.io](https://www.proxyscan.io)|0|🚫|
|[proxylist.geonode.com](https://proxylist.geonode.com/api/proxy-list?limit=300&page=1&sort_by=lastChecked&sort_type=desc&protocols=http,https)|300|✅|
|[proxyscrape.com](https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all)|341|✅|
|[github.com/clarketm/proxy-list](https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt)|400|✅|
|[github.com/monosans/proxy-list](https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt)|182|✅|
|[github.com/TheSpeedX/PROXY-List](https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt)|1926|✅|


## Sample Proxies With Geolocation Info

|#|Ip|Port|Country|City|Internet Service Provider|
|-|--|----|-------|----|-------------------------|
|1|35.157.249.83|39593|Germany|Frankfurt am Main|Amazon Technologies Inc.|
|2|54.93.165.96|39593|Germany|Frankfurt am Main|Amazon Technologies Inc.|
|3|18.196.224.91|36776|Germany|Frankfurt am Main|Amazon Technologies Inc.|
|4|43.130.47.100|8081|United States|Santa Clara|Shenzhen Tencent Computer Systems Company Limited|
|5|20.47.108.204|8888|United States|Boydton|Microsoft Corporation|
|6|3.128.120.252|80|United States|Dublin|Amazon.com, Inc.|
|7|43.130.47.100|8081|United States|Santa Clara|Shenzhen Tencent Computer Systems Company Limited|
|8|128.199.214.87|3128|Singapore|Singapore|Partner Communications Ltd.|
|9|181.224.204.22|22800|Dominican Republic|Santiago de los Caballeros|BW TELECOM|
|10|191.102.107.235|999|Colombia|Malaga|TV AZTECA SUCURSAL COLOMBIA|
|11|125.25.32.15|8080|Thailand|Chiang Mai|TOT Public Company Limited|
|12|162.150.62.96|443|United States|Kincaid|Comcast Cable Communications, LLC|
|13|107.191.48.64|59069|United States|Elk Grove Village|Choopa|
|14|62.94.218.90|8080|Italy|Terni|Clouditalia S.p.A.|
|15|103.214.9.13|3128|Vietnam|Hanoi|MEGACORE|
|16|186.195.252.34|53281|Brazil|Rio das Pedras|Reinaldo Teodora Dutra Informatica ME|
|17|102.68.128.216|8080|Libya|Tripoli|Aljeel Aljadeed For Technology|
|18|5.189.229.42|1081|Russia|St Petersburg|OOO "Network of data-centers "Selectel"|
|19|105.19.63.217|9812|South Africa|Cape Town|SEACOM Limited|
|20|138.197.146.58|31028|Canada|Toronto|DigitalOcean, LLC|



## Contributing

Contributions are welcome, and they are greatly appreciated! Every
little bit helps, and credit will always be given.

