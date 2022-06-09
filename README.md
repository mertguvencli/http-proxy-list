
# Free HTTP Proxy List 🌍

[![Hourly Update](https://github.com/mertguvencli/http-proxy-list/actions/workflows/main.yml/badge.svg?branch=main)](https://github.com/mertguvencli/http-proxy-list/actions/workflows/main.yml)
![GitHub](https://img.shields.io/github/license/mertguvencli/http-proxy-list)
![GitHub last commit](https://img.shields.io/github/last-commit/mertguvencli/http-proxy-list)

It is a lightweight project that hourly scrapes lots of free-proxy sites, validates if it works, and serves a clean proxy list.


> Scraper found **3366** proxies at the latest update. Usable proxies are below.

## Usage

Click the file format that you want and copy the URL.


|File|Content|Count|
|----|-------|-----|
|[data.txt](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.txt)|`ip_address:port` combined (seperated new line)|61|
|[data.json](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.json)|`ip, port`|61|
|[data-with-geolocation.json](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data-with-geolocation.json)|`ip, port, geolocation`|61|

## Sources

|Source|Found Proxies|Succeed|
|------|-------------|-------|
|[free-proxy-list.net](https://free-proxy-list.net)|300|✅|
|[us-proxy.org](https://www.us-proxy.org)|200|✅|
|[proxydb.net](http://proxydb.net)|15|✅|
|[free-proxy-list.com](https://free-proxy-list.com/?page=&port=&type%5B%5D=http&type%5B%5D=https&up_time=0&search=Search)|10|✅|
|[proxy-list.download](https://www.proxy-list.download/HTTP)|26|✅|
|[vpnoverview.com](https://vpnoverview.com/privacy/anonymous-browsing/free-proxy-servers)|32|✅|
|[proxyscan.io](https://www.proxyscan.io)|75|✅|
|[proxylist.geonode.com](https://proxylist.geonode.com/api/proxy-list?limit=300&page=1&sort_by=lastChecked&sort_type=desc&protocols=http,https)|268|✅|
|[proxyscrape.com](https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all)|154|✅|
|[github.com/clarketm/proxy-list](https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt)|400|✅|
|[github.com/monosans/proxy-list](https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt)|47|✅|
|[github.com/TheSpeedX/PROXY-List](https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt)|1839|✅|


## Sample Proxies With Geolocation Info

|#|Ip|Port|Country|City|Internet Service Provider|
|-|--|----|-------|----|-------------------------|
|1|47.74.0.7|80|Japan|Tokyo|Alibaba.com LLC|
|2|157.100.12.138|999|Ecuador|Quito|Telconet S.A|
|3|103.214.9.13|3128|Vietnam|Hanoi|MEGACORE|
|4|64.225.8.192|80|United States|Clifton|DigitalOcean, LLC|
|5|122.3.41.154|8090|Philippines|Dasmarinas|Philippine Long Distance Telephone Co.|
|6|46.166.185.98|3128|Netherlands|Roosendaal|NFOrce Entertainment BV|
|7|190.217.101.79|999|Colombia|San Vicente del Caguan|Level 3 Colombia S.A|
|8|183.166.118.249|8089|China|Huangpu|Chinanet|
|9|36.94.58.243|8080|Indonesia|Sidoarjo|PT. Telekomunikasi Indonesia|
|10|47.74.0.7|80|Japan|Tokyo|Alibaba.com LLC|
|11|190.121.21.211|1081|Chile|Valdivia|Telefonica del Sur S.A.|
|12|157.100.12.138|999|Ecuador|Quito|Telconet S.A|
|13|200.61.16.80|8080|Argentina|Buenos Aires|Silica Networks Argentina S.A|
|14|47.74.0.7|80|Japan|Tokyo|Alibaba.com LLC|
|15|202.62.10.51|8080|Indonesia|Pamulang|Client Jakarta Iconpln|
|16|103.147.77.66|5012|Indonesia|Madiun|TRIDATA|
|17|111.225.153.32|8089|China|Beijing|Chinanet|
|18|85.195.104.71|80|Germany|Frankfurt am Main|Host Europe GmbH|
|19|41.193.63.89|8080|South Africa|Empangeni|Vox Telecom|
|20|177.242.130.90|999|Mexico|San Juan Bautista Tuxtla|Mega Cable, S.A. de C.V.|



## Contributing

Contributions are welcome, and they are greatly appreciated! Every
little bit helps, and credit will always be given.

