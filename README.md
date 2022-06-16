
# Free HTTP Proxy List 🌍

[![Hourly Update](https://github.com/mertguvencli/http-proxy-list/actions/workflows/main.yml/badge.svg?branch=main)](https://github.com/mertguvencli/http-proxy-list/actions/workflows/main.yml)
![GitHub](https://img.shields.io/github/license/mertguvencli/http-proxy-list)
![GitHub last commit](https://img.shields.io/github/last-commit/mertguvencli/http-proxy-list)

It is a lightweight project that hourly scrapes lots of free-proxy sites, validates if it works, and serves a clean proxy list.


> Scraper found **3678** proxies at the latest update. Usable proxies are below.

## Usage

Click the file format that you want and copy the URL.


|File|Content|Count|
|----|-------|-----|
|[data.txt](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.txt)|`ip_address:port` combined (seperated new line)|305|
|[data.json](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.json)|`ip, port`|305|
|[data-with-geolocation.json](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data-with-geolocation.json)|`ip, port, geolocation`|305|

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
|[proxyscrape.com](https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all)|359|✅|
|[github.com/clarketm/proxy-list](https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt)|400|✅|
|[github.com/monosans/proxy-list](https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt)|98|✅|
|[github.com/TheSpeedX/PROXY-List](https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt)|1938|✅|


## Sample Proxies With Geolocation Info

|#|Ip|Port|Country|City|Internet Service Provider|
|-|--|----|-------|----|-------------------------|
|1|170.39.118.187|3128|United States|Ashburn|Rackdog, LLC|
|2|34.145.226.144|8080|United States|Washington|Google LLC|
|3|209.250.253.162|59394|Netherlands|Amsterdam|The Constant Company|
|4|170.39.118.187|3128|United States|Ashburn|Rackdog, LLC|
|5|66.94.116.111|3128|United States|New York|Contabo Inc.|
|6|168.232.36.222|3128|El Salvador|Mejicanos|Navega.com S.A.|
|7|34.145.226.144|8080|United States|Washington|Google LLC|
|8|45.167.124.5|9992|Colombia|Guapi|Sepcom Comunicaciones SAS|
|9|110.170.126.13|3128|Thailand|Din Daeng|True Internet Corporation CO. Ltd.|
|10|157.100.12.138|999|Ecuador|Quito|Telconet S.A|
|11|183.111.25.253|80|South Korea|Seongnam-si|Korea Telecom|
|12|157.245.222.183|80|United States|Clifton|DigitalOcean, LLC|
|13|66.94.116.111|3128|United States|New York|Contabo Inc.|
|14|167.235.63.238|3128|Germany|Falkenstein|Hetzner Online GmbH|
|15|65.21.206.151|3128|Finland|Helsinki|Hetzner Online GmbH|
|16|134.209.111.123|3128|Singapore|Singapore|DigitalOcean, LLC|
|17|178.128.121.57|3128|Singapore|Singapore|DigitalOcean, LLC|
|18|194.233.73.109|443|Singapore|Singapore|Contabo Asia Private Limited|
|19|94.242.54.119|3128|Russia|St Petersburg|Veesp datacenter|
|20|194.233.73.104|443|Singapore|Singapore|Contabo Asia Private Limited|



## Contributing

Contributions are welcome, and they are greatly appreciated! Every
little bit helps, and credit will always be given.

