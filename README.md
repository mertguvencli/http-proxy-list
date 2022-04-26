
# Free HTTP Proxy List 🌍

[![Hourly Update](https://github.com/mertguvencli/http-proxy-list/actions/workflows/main.yml/badge.svg?branch=main)](https://github.com/mertguvencli/http-proxy-list/actions/workflows/main.yml)
![GitHub](https://img.shields.io/github/license/mertguvencli/http-proxy-list)
![GitHub last commit](https://img.shields.io/github/last-commit/mertguvencli/http-proxy-list)

It is a lightweight project that hourly scrapes lots of free-proxy sites, validates if it works, and serves a clean proxy list.


> Scraper found **3483** proxies at the latest update. Usable proxies are below.

## Usage

Click the file format that you want and copy the URL.


|File|Content|Count|
|----|-------|-----|
|[data.txt](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.txt)|`ip_address:port` combined (seperated new line)|204|
|[data.json](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.json)|`ip, port`|204|
|[data-with-geolocation.json](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data-with-geolocation.json)|`ip, port, geolocation`|204|

## Sources

|Source|Found Proxies|Succeed|
|------|-------------|-------|
|[free-proxy-list.net](https://free-proxy-list.net)|300|✅|
|[us-proxy.org](https://www.us-proxy.org)|200|✅|
|[proxydb.net](http://proxydb.net)|15|✅|
|[free-proxy-list.com](https://free-proxy-list.com/?page=&port=&type%5B%5D=http&type%5B%5D=https&up_time=0&search=Search)|10|✅|
|[proxy-list.download](https://www.proxy-list.download/HTTP)|26|✅|
|[vpnoverview.com](https://vpnoverview.com/privacy/anonymous-browsing/free-proxy-servers)|32|✅|
|[proxyscan.io](https://www.proxyscan.io)|100|✅|
|[proxylist.geonode.com](https://proxylist.geonode.com/api/proxy-list?limit=300&page=1&sort_by=lastChecked&sort_type=desc&protocols=http,https)|0|🚫|
|[proxyscrape.com](https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all)|298|✅|
|[github.com/clarketm/proxy-list](https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt)|400|✅|
|[github.com/monosans/proxy-list](https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt)|168|✅|
|[github.com/TheSpeedX/PROXY-List](https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt)|1934|✅|


## Sample Proxies With Geolocation Info

|#|Ip|Port|Country|City|Internet Service Provider|
|-|--|----|-------|----|-------------------------|
|1|66.70.178.214|9300|Canada|Beauharnois|OVH SAS|
|2|85.25.93.136|5566|France|Strasbourg|Host Europe GmbH|
|3|194.233.86.75|1234|Singapore|Singapore|Contabo Asia Private Limited|
|4|194.233.69.90|443|Singapore|Singapore|Contabo Asia Private Limited|
|5|85.25.199.122|5566|France|Strasbourg|Host Europe GmbH|
|6|176.119.134.38|23500|Spain|Puerto Serrano|Electro Puerto SUR SL|
|7|36.92.140.113|80|Indonesia|Bekasi|PT. Telekomunikasi Indonesia|
|8|134.209.148.107|8081|India|Bengaluru|DigitalOcean, LLC|
|9|69.163.252.140|1081|United States|Brea|New Dream Network, LLC|
|10|190.26.201.194|8080|Colombia|Castilla La Nueva|ETB - Colombia|
|11|5.167.141.239|3128|Russia|Tula|CJSC "ER-Telecom Holding" Tula branch|
|12|194.233.88.38|3128|Singapore|Singapore|Contabo Asia Private Limited|
|13|85.25.93.136|5566|France|Strasbourg|Host Europe GmbH|
|14|37.204.157.91|41890|Russia|Moscow|NCNET|
|15|85.25.150.32|5566|France|Strasbourg|Host Europe GmbH|
|16|103.153.148.111|80|Indonesia|Malang|JARINGANKU|
|17|186.96.158.213|999|Mexico|Hermosillo|Total Play Telecomunicaciones SA De CV|
|18|85.25.119.221|5566|France|Strasbourg|BSB-SERVICE|
|19|85.25.242.142|5566|France|Strasbourg|Host Europe GmbH|
|20|31.42.57.1|8080|Ukraine|Kyiv|Limited Liability Company AVATOR ISP|



## Contributing

Contributions are welcome, and they are greatly appreciated! Every
little bit helps, and credit will always be given.

