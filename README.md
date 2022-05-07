
# Free HTTP Proxy List 🌍

[![Hourly Update](https://github.com/mertguvencli/http-proxy-list/actions/workflows/main.yml/badge.svg?branch=main)](https://github.com/mertguvencli/http-proxy-list/actions/workflows/main.yml)
![GitHub](https://img.shields.io/github/license/mertguvencli/http-proxy-list)
![GitHub last commit](https://img.shields.io/github/last-commit/mertguvencli/http-proxy-list)

It is a lightweight project that hourly scrapes lots of free-proxy sites, validates if it works, and serves a clean proxy list.


> Scraper found **3888** proxies at the latest update. Usable proxies are below.

## Usage

Click the file format that you want and copy the URL.


|File|Content|Count|
|----|-------|-----|
|[data.txt](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.txt)|`ip_address:port` combined (seperated new line)|255|
|[data.json](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.json)|`ip, port`|255|
|[data-with-geolocation.json](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data-with-geolocation.json)|`ip, port, geolocation`|255|

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
|[proxyscrape.com](https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all)|393|✅|
|[github.com/clarketm/proxy-list](https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt)|400|✅|
|[github.com/monosans/proxy-list](https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt)|323|✅|
|[github.com/TheSpeedX/PROXY-List](https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt)|1889|✅|


## Sample Proxies With Geolocation Info

|#|Ip|Port|Country|City|Internet Service Provider|
|-|--|----|-------|----|-------------------------|
|1|20.47.108.204|8888|United States|Boydton|Microsoft Corporation|
|2|20.47.108.204|8888|United States|Boydton|Microsoft Corporation|
|3|155.138.232.110|59394|United States|Atlanta|The Constant Company|
|4|201.120.27.15|53281|Mexico|Hermosillo|Uninet S.A. de C.V|
|5|45.76.26.132|59394|United States|Elk Grove Village|The Constant Company|
|6|194.233.69.90|443|Singapore|Singapore|Contabo Asia Private Limited|
|7|138.219.14.214|9812|El Salvador|Chalatenango|ENLACEVISION|
|8|155.138.232.110|59394|United States|Atlanta|The Constant Company|
|9|45.76.13.167|59394|United States|Piscataway|The Constant Company|
|10|77.43.201.16|8080|Russia|Perm|MTS PJSC|
|11|54.205.203.231|80|United States|Ashburn|Amazon.com, Inc.|
|12|201.174.239.18|8080|Mexico|Monterrey|Transtelco Inc|
|13|190.26.201.194|8080|Colombia|Bogotá|ETB - Colombia|
|14|54.205.203.231|80|United States|Ashburn|Amazon.com, Inc.|
|15|209.97.188.59|3128|United Kingdom|London|DigitalOcean, LLC|
|16|163.172.64.42|8080|France|Paris|Online S.A.S.|
|17|45.76.26.132|59394|United States|Elk Grove Village|The Constant Company|
|18|198.144.149.82|3128|Canada|Toronto|Netminders Server Hosting|
|19|186.96.116.12|999|Colombia|Flandes|TV AZTECA SUCURSAL COLOMBIA|
|20|170.239.223.27|8080|Brazil|Itabira|Companhia Itabirana TelecomunicaÔÔes Ltda|



## Contributing

Contributions are welcome, and they are greatly appreciated! Every
little bit helps, and credit will always be given.

