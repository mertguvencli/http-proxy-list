
# Free HTTP Proxy List 🌍

[![Hourly Update](https://github.com/mertguvencli/http-proxy-list/actions/workflows/main.yml/badge.svg?branch=main)](https://github.com/mertguvencli/http-proxy-list/actions/workflows/main.yml)
![GitHub](https://img.shields.io/github/license/mertguvencli/http-proxy-list)
![GitHub last commit](https://img.shields.io/github/last-commit/mertguvencli/http-proxy-list)

It is a lightweight project that hourly scrapes lots of free-proxy sites, validates if it works, and serves a clean proxy list.


> Scraper found **4228** proxies at the latest update. Usable proxies are below.

## Usage

Click the file format that you want and copy the URL.


|File|Content|Count|
|----|-------|-----|
|[data.txt](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.txt)|`ip_address:port` combined (seperated new line)|304|
|[data.json](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.json)|`ip, port`|304|
|[data-with-geolocation.json](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data-with-geolocation.json)|`ip, port, geolocation`|304|

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
|[proxylist.geonode.com](https://proxylist.geonode.com/api/proxy-list?limit=300&page=1&sort_by=lastChecked&sort_type=desc&protocols=http,https)|300|✅|
|[proxyscrape.com](https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all)|414|✅|
|[github.com/clarketm/proxy-list](https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt)|400|✅|
|[github.com/monosans/proxy-list](https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt)|317|✅|
|[github.com/TheSpeedX/PROXY-List](https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt)|2114|✅|


## Sample Proxies With Geolocation Info

|#|Ip|Port|Country|City|Internet Service Provider|
|-|--|----|-------|----|-------------------------|
|1|144.202.48.244|59394|United States|Elk Grove Village|Choopa|
|2|20.47.108.204|8888|United States|Boydton|Microsoft Corporation|
|3|144.202.48.244|59394|United States|Elk Grove Village|Choopa|
|4|139.162.47.91|8080|Singapore|Singapore|Linode, LLC|
|5|103.73.194.2|80|Hong Kong|Wanchai|TouchPal HK Co., Limited|
|6|194.233.86.75|1234|Singapore|Singapore|Contabo Asia Private Limited|
|7|109.194.101.128|3128|Russia|Surok|CJSC "ER-Telecom Holding" Yoshkar-Ola branch|
|8|178.167.87.200|55443|Russia|Moscow|for Flex Ltd|
|9|138.118.200.112|999|Venezuela|San Francisco|Iguana Network Services C.A.|
|10|66.94.97.238|443|United States|New York|Contabo Inc.|
|11|103.147.77.66|3125|Indonesia|Madiun|TRIDATA|
|12|174.138.116.12|80|United States|Clifton|DigitalOcean, LLC|
|13|41.186.44.106|3128|Rwanda|Kigali|MTN Rwandacell|
|14|139.59.59.122|8118|India|Bengaluru|DigitalOcean|
|15|103.76.160.2|8080|Philippines|Makati City|Infinivan Incorporated|
|16|5.39.189.39|3128|Netherlands|Rotterdam|ColoCenter b.v.|
|17|201.222.40.122|8080|Colombia|Santa Marta|Megaport (Bulgaria) EAD|
|18|103.102.13.103|8080|Indonesia|Ngijo|GLOBALMEDIANET|
|19|89.218.186.134|3128|Kazakhstan|Pavlodar|Kazakhtelecom Data Network Administration|
|20|103.209.248.86|8080|Indonesia|Panjangjiwo|Indonesia Network Information Center|



## Contributing

Contributions are welcome, and they are greatly appreciated! Every
little bit helps, and credit will always be given.

