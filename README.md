
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
|[data.txt](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.txt)|`ip_address:port` combined (seperated new line)|132|
|[data.json](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.json)|`ip, port`|132|
|[data-with-geolocation.json](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data-with-geolocation.json)|`ip, port, geolocation`|132|

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
|[proxyscrape.com](https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all)|266|✅|
|[github.com/clarketm/proxy-list](https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt)|400|✅|
|[github.com/monosans/proxy-list](https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt)|139|✅|
|[github.com/TheSpeedX/PROXY-List](https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt)|1836|✅|


## Sample Proxies With Geolocation Info

|#|Ip|Port|Country|City|Internet Service Provider|
|-|--|----|-------|----|-------------------------|
|1|189.237.69.110|999|Mexico|Chihuahua City|Uninet S.A. de C.V.|
|2|40.70.172.110|80|United States|Boydton|Microsoft Corporation|
|3|144.202.116.156|59394|United States|Los Angeles|The Constant Company|
|4|119.42.86.87|8080|Thailand|Samphanthawong|CAT-BB|
|5|190.55.17.234|8181|Argentina|San Isidro|Telecentro S.A.|
|6|110.78.186.66|8080|Thailand|Samphanthawong|CAT-BB|
|7|45.77.86.30|59394|United States|Los Angeles|The Constant Company|
|8|200.155.142.98|8080|Brazil|São Paulo|Telium TelecomunicaÔÔes Ltda|
|9|91.81.127.186|9812|Italy|Palermo|VODAFONE|
|10|3.126.207.18|3128|Germany|Frankfurt am Main|Amazon Technologies Inc.|
|11|179.118.199.171|9812|Brazil|Campinas|Vivo|
|12|182.16.171.65|43188|Indonesia|Jakarta|PT iForte Global Internet|
|13|83.220.47.146|8080|Russia|Moscow|GARS|
|14|36.238.95.229|53281|Taiwan|Kaohsiung City|Chunghwa Telecom Co., Ltd.|
|15|195.189.123.213|3128|Russia|Moscow|Iptp LTD|
|16|149.248.5.225|59394|United States|Los Angeles|The Constant Company|
|17|68.183.58.145|5566|United States|Clifton|DigitalOcean, LLC|
|18|45.225.106.99|999|Ecuador|Vinces|Nedetel S.A.|
|19|103.175.238.130|8181|Indonesia|Pamanukan|PT Uliz Netmedia Solusindo|
|20|181.118.158.131|999|Colombia|Paipa|Media Commerce Partners S.A|



## Contributing

Contributions are welcome, and they are greatly appreciated! Every
little bit helps, and credit will always be given.

