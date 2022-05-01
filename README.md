
# Free HTTP Proxy List 🌍

[![Hourly Update](https://github.com/mertguvencli/http-proxy-list/actions/workflows/main.yml/badge.svg?branch=main)](https://github.com/mertguvencli/http-proxy-list/actions/workflows/main.yml)
![GitHub](https://img.shields.io/github/license/mertguvencli/http-proxy-list)
![GitHub last commit](https://img.shields.io/github/last-commit/mertguvencli/http-proxy-list)

It is a lightweight project that hourly scrapes lots of free-proxy sites, validates if it works, and serves a clean proxy list.


> Scraper found **3324** proxies at the latest update. Usable proxies are below.

## Usage

Click the file format that you want and copy the URL.


|File|Content|Count|
|----|-------|-----|
|[data.txt](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.txt)|`ip_address:port` combined (seperated new line)|91|
|[data.json](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.json)|`ip, port`|91|
|[data-with-geolocation.json](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data-with-geolocation.json)|`ip, port, geolocation`|91|

## Sources

|Source|Found Proxies|Succeed|
|------|-------------|-------|
|[free-proxy-list.net](https://free-proxy-list.net)|300|✅|
|[us-proxy.org](https://www.us-proxy.org)|200|✅|
|[proxydb.net](http://proxydb.net)|15|✅|
|[free-proxy-list.com](https://free-proxy-list.com/?page=&port=&type%5B%5D=http&type%5B%5D=https&up_time=0&search=Search)|10|✅|
|[proxy-list.download](https://www.proxy-list.download/HTTP)|26|✅|
|[vpnoverview.com](https://vpnoverview.com/privacy/anonymous-browsing/free-proxy-servers)|32|✅|
|[proxyscan.io](https://www.proxyscan.io)|93|✅|
|[proxylist.geonode.com](https://proxylist.geonode.com/api/proxy-list?limit=300&page=1&sort_by=lastChecked&sort_type=desc&protocols=http,https)|0|🚫|
|[proxyscrape.com](https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all)|211|✅|
|[github.com/clarketm/proxy-list](https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt)|400|✅|
|[github.com/monosans/proxy-list](https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt)|124|✅|
|[github.com/TheSpeedX/PROXY-List](https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt)|1913|✅|


## Sample Proxies With Geolocation Info

|#|Ip|Port|Country|City|Internet Service Provider|
|-|--|----|-------|----|-------------------------|
|1|45.80.149.43|23456|Netherlands|Amsterdam|Hostgw SRL|
|2|34.82.235.224|3128|United States|The Dalles|Google LLC|
|3|192.99.144.208|8080|Canada|Beauharnois|OVH SAS|
|4|122.155.165.191|3128|Thailand|Ratchathewi|CAT Telecom Public Company Limited|
|5|186.233.186.60|8080|United States|Chicago|Maxihost LTDA|
|6|181.224.207.19|999|Dominican Republic|Santiago de los Caballeros|BW TELECOM|
|7|62.138.7.104|5566|France|Strasbourg|Host Europe Group|
|8|201.222.45.65|999|Chile|Santiago|GRUPO ULLOA SpA|
|9|190.26.201.194|8080|Colombia|Bogotá|ETB - Colombia|
|10|149.34.7.65|8080|Spain|Bellvis|Adamo Telecom Iberia S.A.|
|11|85.25.139.22|5566|France|Strasbourg|Host Europe GmbH|
|12|103.209.36.56|8080|India|Mumbai|Syscon Infoway Pvt. Ltd.|
|13|77.242.16.30|8080|Albania|Tirana|Abissnet ISP|
|14|79.120.177.106|8080|Hungary|Budapest|Invitech ICT Services Kft.|
|15|201.91.82.155|3128|Brazil|São Paulo|Vivo|
|16|216.176.32.79|3128|United Kingdom|Slough|Rackdog, LLC|
|17|123.163.55.123|3128|China|Zhoukou|Chinanet|
|18|206.189.139.241|8080|India|Bengaluru|DigitalOcean, LLC|
|19|164.70.122.6|3128|Japan|Chiyoda|NTT PC Communications, Inc.|
|20|61.7.195.194|8080|Thailand|Samphanthawong|CAT-ISP|



## Contributing

Contributions are welcome, and they are greatly appreciated! Every
little bit helps, and credit will always be given.

