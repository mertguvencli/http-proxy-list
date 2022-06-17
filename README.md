
# Free HTTP Proxy List 🌍

[![Hourly Update](https://github.com/mertguvencli/http-proxy-list/actions/workflows/main.yml/badge.svg?branch=main)](https://github.com/mertguvencli/http-proxy-list/actions/workflows/main.yml)
![GitHub](https://img.shields.io/github/license/mertguvencli/http-proxy-list)
![GitHub last commit](https://img.shields.io/github/last-commit/mertguvencli/http-proxy-list)

It is a lightweight project that hourly scrapes lots of free-proxy sites, validates if it works, and serves a clean proxy list.


> Scraper found **4142** proxies at the latest update. Usable proxies are below.

## Usage

Click the file format that you want and copy the URL.


|File|Content|Count|
|----|-------|-----|
|[data.txt](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.txt)|`ip_address:port` combined (seperated new line)|239|
|[data.json](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.json)|`ip, port`|239|
|[data-with-geolocation.json](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data-with-geolocation.json)|`ip, port, geolocation`|239|

## Sources

|Source|Found Proxies|Succeed|
|------|-------------|-------|
|[free-proxy-list.net](https://free-proxy-list.net)|300|✅|
|[us-proxy.org](https://www.us-proxy.org)|200|✅|
|[proxydb.net](http://proxydb.net)|15|✅|
|[free-proxy-list.com](https://free-proxy-list.com/?page=&port=&type%5B%5D=http&type%5B%5D=https&up_time=0&search=Search)|10|✅|
|[proxy-list.download](https://www.proxy-list.download/HTTP)|26|✅|
|[vpnoverview.com](https://vpnoverview.com/privacy/anonymous-browsing/free-proxy-servers)|32|✅|
|[proxyscan.io](https://www.proxyscan.io)|89|✅|
|[proxylist.geonode.com](https://proxylist.geonode.com/api/proxy-list?limit=300&page=1&sort_by=lastChecked&sort_type=desc&protocols=http,https)|300|✅|
|[proxyscrape.com](https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all)|468|✅|
|[github.com/clarketm/proxy-list](https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt)|400|✅|
|[github.com/monosans/proxy-list](https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt)|259|✅|
|[github.com/TheSpeedX/PROXY-List](https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt)|2043|✅|


## Sample Proxies With Geolocation Info

|#|Ip|Port|Country|City|Internet Service Provider|
|-|--|----|-------|----|-------------------------|
|1|170.39.118.187|3128|United States|Ashburn|Rackdog, LLC|
|2|34.145.226.144|8080|United States|Washington|Google LLC|
|3|198.12.254.161|3128|United States|Ashburn|GoDaddy.com, LLC|
|4|200.110.168.159|8080|Colombia|Trujillo|Media Commerce Partners S.A|
|5|189.164.118.26|3128|Mexico|Ciudad de Atlixco|Uninet S.A. de C.V|
|6|186.5.5.125|8080|Ecuador|Guayaquil|Telconet S.A|
|7|170.39.118.187|3128|United States|Ashburn|Rackdog, LLC|
|8|51.250.80.131|80|Russia|Moscow|Yandex.Cloud LLC|
|9|20.122.177.165|3128|United States|Boydton|Microsoft Corporation|
|10|198.12.254.161|3128|United States|Ashburn|GoDaddy.com, LLC|
|11|34.145.226.144|8080|United States|Washington|Google LLC|
|12|35.170.197.3|8888|United States|Ashburn|Amazon.com, Inc.|
|13|104.131.109.98|3128|United States|Clifton|DigitalOcean, LLC|
|14|207.148.118.14|3128|Singapore|Singapore|The Constant Company|
|15|66.94.116.111|3128|United States|New York|Contabo Inc.|
|16|95.217.72.247|3128|Finland|Helsinki|Hetzner Online GmbH|
|17|157.100.12.138|999|Ecuador|Quito|Telconet S.A|
|18|183.111.25.253|8080|South Korea|Seongnam-si|Korea Telecom|
|19|62.171.161.88|2018|Germany|Nuremberg|Contabo GmbH|
|20|67.212.83.55|1080|Canada|Saint-Hyacinthe|eStruxture Data Centers Inc.|



## Contributing

Contributions are welcome, and they are greatly appreciated! Every
little bit helps, and credit will always be given.

