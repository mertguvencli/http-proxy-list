
# Free HTTP Proxy List 🌍

[![Hourly Update](https://github.com/mertguvencli/http-proxy-list/actions/workflows/main.yml/badge.svg?branch=main)](https://github.com/mertguvencli/http-proxy-list/actions/workflows/main.yml)
![GitHub](https://img.shields.io/github/license/mertguvencli/http-proxy-list)
![GitHub last commit](https://img.shields.io/github/last-commit/mertguvencli/http-proxy-list)

It is a lightweight project that hourly scrapes lots of free-proxy sites, validates if it works, and serves a clean proxy list.


> Scraper found **4308** proxies at the latest update. Usable proxies are below.

## Usage

Click the file format that you want and copy the URL.


|File|Content|Count|
|----|-------|-----|
|[data.txt](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.txt)|`ip_address:port` combined (seperated new line)|425|
|[data.json](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.json)|`ip, port`|425|
|[data-with-geolocation.json](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data-with-geolocation.json)|`ip, port, geolocation`|425|

## Sources

|Source|Found Proxies|Succeed|
|------|-------------|-------|
|[free-proxy-list.net](https://free-proxy-list.net)|300|✅|
|[us-proxy.org](https://www.us-proxy.org)|200|✅|
|[proxydb.net](http://proxydb.net)|15|✅|
|[free-proxy-list.com](https://free-proxy-list.com/?page=&port=&type%5B%5D=http&type%5B%5D=https&up_time=0&search=Search)|10|✅|
|[proxy-list.download](https://www.proxy-list.download/HTTP)|26|✅|
|[vpnoverview.com](https://vpnoverview.com/privacy/anonymous-browsing/free-proxy-servers)|32|✅|
|[proxyscan.io](https://www.proxyscan.io)|77|✅|
|[proxylist.geonode.com](https://proxylist.geonode.com/api/proxy-list?limit=300&page=1&sort_by=lastChecked&sort_type=desc&protocols=http,https)|300|✅|
|[proxyscrape.com](https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all)|686|✅|
|[github.com/clarketm/proxy-list](https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt)|400|✅|
|[github.com/monosans/proxy-list](https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt)|345|✅|
|[github.com/TheSpeedX/PROXY-List](https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt)|1917|✅|


## Sample Proxies With Geolocation Info

|#|Ip|Port|Country|City|Internet Service Provider|
|-|--|----|-------|----|-------------------------|
|1|170.39.118.187|3128|United States|Ashburn|Rackdog, LLC|
|2|20.47.108.204|8888|United States|Boydton|Microsoft Corporation|
|3|34.145.226.144|8080|United States|Washington|Google LLC|
|4|20.47.108.204|8888|United States|Boydton|Microsoft Corporation|
|5|170.39.118.187|3128|United States|Ashburn|Rackdog, LLC|
|6|35.170.197.3|8888|United States|Ashburn|Amazon.com, Inc.|
|7|35.170.197.3|8888|United States|Ashburn|Amazon.com, Inc.|
|8|34.145.226.144|8080|United States|Washington|Google LLC|
|9|45.231.170.137|999|Mexico|Playa del Carmen|GigNet, S.A. de C.V.|
|10|45.167.124.5|9992|Colombia|Guapi|Sepcom Comunicaciones SAS|
|11|95.217.72.253|3128|Finland|Helsinki|Hetzner Online GmbH|
|12|161.97.129.98|3128|Germany|Düsseldorf|Contabo GmbH|
|13|207.148.118.14|3128|Singapore|Singapore|The Constant Company|
|14|186.5.5.125|8080|Ecuador|Guayaquil|Telconet S.A|
|15|167.235.63.238|3128|Germany|Falkenstein|Hetzner Online GmbH|
|16|183.111.25.253|80|South Korea|Seongnam-si|Korea Telecom|
|17|194.233.73.104|443|Singapore|Singapore|Contabo Asia Private Limited|
|18|200.110.168.159|8080|Colombia|Trujillo|Media Commerce Partners S.A|
|19|185.143.42.54|8080|Iraq|Ramadi|LinkiWay DMCC|
|20|187.94.16.59|39665|Brazil|Irece|Holistica Provedor Internet Ltda|



## Contributing

Contributions are welcome, and they are greatly appreciated! Every
little bit helps, and credit will always be given.

