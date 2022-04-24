
# Free HTTP Proxy List 🌍

[![Hourly Update](https://github.com/mertguvencli/http-proxy-list/actions/workflows/main.yml/badge.svg?branch=main)](https://github.com/mertguvencli/http-proxy-list/actions/workflows/main.yml)
![GitHub](https://img.shields.io/github/license/mertguvencli/http-proxy-list)
![GitHub last commit](https://img.shields.io/github/last-commit/mertguvencli/http-proxy-list)

It is a lightweight project that hourly scrapes lots of free-proxy sites, validates if it works, and serves a clean proxy list.


> Scraper found **3500** proxies at the latest update. Usable proxies are below.

## Usage

Click the file format that you want and copy the URL.


|File|Content|Count|
|----|-------|-----|
|[data.txt](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.txt)|`ip_address:port` combined (seperated new line)|102|
|[data.json](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.json)|`ip, port`|102|
|[data-with-geolocation.json](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data-with-geolocation.json)|`ip, port, geolocation`|102|

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
|[proxylist.geonode.com](https://proxylist.geonode.com/api/proxy-list?limit=300&page=1&sort_by=lastChecked&sort_type=desc&protocols=http,https)|0|🚫|
|[proxyscrape.com](https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all)|314|✅|
|[github.com/clarketm/proxy-list](https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt)|400|✅|
|[github.com/monosans/proxy-list](https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt)|172|✅|
|[github.com/TheSpeedX/PROXY-List](https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt)|2031|✅|


## Sample Proxies With Geolocation Info

|#|Ip|Port|Country|City|Internet Service Provider|
|-|--|----|-------|----|-------------------------|
|1|63.161.104.189|3128|United States|Itasca|Sprint|
|2|63.161.104.189|3128|United States|Itasca|Sprint|
|3|103.73.194.2|80|Hong Kong|Wanchai|TouchPal HK Co., Limited|
|4|59.103.236.86|80|Pakistan|Islamabad|Pakistan Telecommunication Company Limited|
|5|14.207.16.138|8080|Thailand|Bang Lamung|Triple T Broadband Public Company Limited|
|6|122.155.165.191|3128|Thailand|Ratchathewi|CAT Telecom Public Company Limited|
|7|212.112.113.178|3128|Kyrgyzstan|Bishkek|AkNet|
|8|62.75.229.165|5566|France|Strasbourg|Host Europe GmbH|
|9|104.238.145.25|59394|United States|Dallas|The Constant Company|
|10|85.25.91.156|5566|Germany|Cologne|PlusServer GmbH|
|11|59.103.236.86|80|Pakistan|Islamabad|Pakistan Telecommunication Company Limited|
|12|2.50.153.41|53281|United Arab Emirates|Abu Dhabi|Emirates Telecommunications Corporation|
|13|63.161.104.189|3128|United States|Itasca|Sprint|
|14|181.224.207.18|999|Dominican Republic|Santiago de los Caballeros|BW TELECOM|
|15|12.144.254.185|9080|United States|Little Rock|AT&T Services, Inc.|
|16|85.25.99.106|5566|France|Strasbourg|PLUSSERVER|
|17|47.96.226.137|3128|China|Hangzhou|Hangzhou Alibaba Advertising Co|
|18|201.174.239.18|8080|Mexico|Monterrey|Transtelco Inc|
|19|85.25.117.171|5566|France|Strasbourg|BSB-SERVICE|
|20|85.25.196.218|5566|France|Strasbourg|Host Europe GmbH|



## Contributing

Contributions are welcome, and they are greatly appreciated! Every
little bit helps, and credit will always be given.

