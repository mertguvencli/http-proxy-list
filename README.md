
# Free HTTP Proxy List 🌍

[![Hourly Update](https://github.com/mertguvencli/http-proxy-list/actions/workflows/main.yml/badge.svg?branch=main)](https://github.com/mertguvencli/http-proxy-list/actions/workflows/main.yml)
![GitHub](https://img.shields.io/github/license/mertguvencli/http-proxy-list)
![GitHub last commit](https://img.shields.io/github/last-commit/mertguvencli/http-proxy-list)

It is a lightweight project that hourly scrapes lots of free-proxy sites, validates if it works, and serves a clean proxy list.


> Scraper found **4025** proxies at the latest update. Usable proxies are below.

## Usage

Click the file format that you want and copy the URL.


|File|Content|Count|
|----|-------|-----|
|[data.txt](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.txt)|`ip_address:port` combined (seperated new line)|192|
|[data.json](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.json)|`ip, port`|192|
|[data-with-geolocation.json](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data-with-geolocation.json)|`ip, port, geolocation`|192|

## Sources

|Source|Found Proxies|Succeed|
|------|-------------|-------|
|[free-proxy-list.net](https://free-proxy-list.net)|300|✅|
|[us-proxy.org](https://www.us-proxy.org)|200|✅|
|[proxydb.net](http://proxydb.net)|15|✅|
|[free-proxy-list.com](https://free-proxy-list.com/?page=&port=&type%5B%5D=http&type%5B%5D=https&up_time=0&search=Search)|10|✅|
|[proxy-list.download](https://www.proxy-list.download/HTTP)|0|🚫|
|[vpnoverview.com](https://vpnoverview.com/privacy/anonymous-browsing/free-proxy-servers)|32|✅|
|[proxyscan.io](https://www.proxyscan.io)|100|✅|
|[proxylist.geonode.com](https://proxylist.geonode.com/api/proxy-list?limit=300&page=1&sort_by=lastChecked&sort_type=desc&protocols=http,https)|300|✅|
|[proxyscrape.com](https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all)|450|✅|
|[github.com/clarketm/proxy-list](https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt)|400|✅|
|[github.com/monosans/proxy-list](https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt)|230|✅|
|[github.com/TheSpeedX/PROXY-List](https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt)|1988|✅|


## Sample Proxies With Geolocation Info

|#|Ip|Port|Country|City|Internet Service Provider|
|-|--|----|-------|----|-------------------------|
|1|144.202.116.156|59394|United States|Los Angeles|The Constant Company|
|2|212.108.144.67|8080|Cyprus|Kyrenia|Lifecell Digital LTD|
|3|154.49.216.33|3128|France|Vélizy-Villacoublay|Cogent Communications|
|4|38.130.249.137|999|United States|Dallas|Cogent Communications|
|5|102.130.79.1|3128|South Africa|Pretoria|Adnexus Celerity Networks (Proprietary) Limited|
|6|45.77.86.30|59394|United States|Los Angeles|The Constant Company|
|7|144.202.116.156|59394|United States|Los Angeles|The Constant Company|
|8|186.67.230.45|3128|Chile|Santiago|Entel Chile S.A.|
|9|194.233.69.41|443|Singapore|Singapore|Contabo Asia Private Limited|
|10|121.101.131.142|9090|Indonesia|Yogyakarta|TERABIT|
|11|45.77.86.30|59394|United States|Los Angeles|The Constant Company|
|12|103.125.56.15|3127|Indonesia|Bekasi|PT. Eka Mas Republik|
|13|177.229.210.66|8080|Mexico|Vega de Alatorre|Mega Cable, S.A. de C.V.|
|14|20.47.108.204|8888|United States|Boydton|Microsoft Corporation|
|15|154.49.216.33|3128|France|Vélizy-Villacoublay|Cogent Communications|
|16|38.130.249.137|999|United States|Dallas|Cogent Communications|
|17|51.81.32.81|8888|United States|Reston|OVH SAS|
|18|103.156.15.25|8080|Indonesia|Pinrang|PT Lintas Jaringan Nusantara|
|19|85.214.124.194|5001|Germany|Berlin|Strato AG|
|20|52.26.90.29|3128|United States|Portland|Amazon Technologies Inc.|



## Contributing

Contributions are welcome, and they are greatly appreciated! Every
little bit helps, and credit will always be given.

