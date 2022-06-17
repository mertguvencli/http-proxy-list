
# Free HTTP Proxy List 🌍

[![Hourly Update](https://github.com/mertguvencli/http-proxy-list/actions/workflows/main.yml/badge.svg?branch=main)](https://github.com/mertguvencli/http-proxy-list/actions/workflows/main.yml)
![GitHub](https://img.shields.io/github/license/mertguvencli/http-proxy-list)
![GitHub last commit](https://img.shields.io/github/last-commit/mertguvencli/http-proxy-list)

It is a lightweight project that hourly scrapes lots of free-proxy sites, validates if it works, and serves a clean proxy list.


> Scraper found **4140** proxies at the latest update. Usable proxies are below.

## Usage

Click the file format that you want and copy the URL.


|File|Content|Count|
|----|-------|-----|
|[data.txt](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.txt)|`ip_address:port` combined (seperated new line)|384|
|[data.json](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.json)|`ip, port`|384|
|[data-with-geolocation.json](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data-with-geolocation.json)|`ip, port, geolocation`|384|

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
|[proxyscrape.com](https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all)|572|✅|
|[github.com/clarketm/proxy-list](https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt)|400|✅|
|[github.com/monosans/proxy-list](https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt)|245|✅|
|[github.com/TheSpeedX/PROXY-List](https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt)|2040|✅|


## Sample Proxies With Geolocation Info

|#|Ip|Port|Country|City|Internet Service Provider|
|-|--|----|-------|----|-------------------------|
|1|170.39.118.187|3128|United States|Ashburn|Rackdog, LLC|
|2|34.145.226.144|8080|United States|Washington|Google LLC|
|3|189.164.118.26|3128|Mexico|Ciudad de Atlixco|Uninet S.A. de C.V|
|4|170.39.118.187|3128|United States|Ashburn|Rackdog, LLC|
|5|66.196.238.178|3128|United States|Houston|Logix|
|6|200.110.168.159|8080|Colombia|Trujillo|Media Commerce Partners S.A|
|7|34.145.226.144|8080|United States|Washington|Google LLC|
|8|157.100.53.100|999|Ecuador|Machala|Nedetel S.A.|
|9|167.235.63.238|3128|Germany|Falkenstein|Hetzner Online GmbH|
|10|194.233.69.90|443|Singapore|Singapore|Contabo Asia Private Limited|
|11|165.154.233.46|8080|Philippines|Manila|Scloud Pte Ltd|
|12|186.5.5.125|8080|Ecuador|Guayaquil|Telconet S.A|
|13|193.122.151.79|3128|United States|Ashburn|Oracle Corporation|
|14|194.233.77.110|1111|Singapore|Singapore|Contabo Asia Private Limited|
|15|193.122.151.79|3128|United States|Ashburn|Oracle Corporation|
|16|66.94.120.161|443|United States|Seattle|Contabo Inc.|
|17|194.233.73.107|443|Singapore|Singapore|Contabo Asia Private Limited|
|18|167.57.53.152|53281|Uruguay|Centro|Administracion Nacional de Telecomunicaciones|
|19|134.122.58.174|80|Netherlands|Amsterdam|DigitalOcean, LLC|
|20|102.33.18.26|8080|South Africa|Pretoria|Metrofibre Networx|



## Contributing

Contributions are welcome, and they are greatly appreciated! Every
little bit helps, and credit will always be given.

