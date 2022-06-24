
# Free HTTP Proxy List 🌍

[![Hourly Update](https://github.com/mertguvencli/http-proxy-list/actions/workflows/main.yml/badge.svg?branch=main)](https://github.com/mertguvencli/http-proxy-list/actions/workflows/main.yml)
![GitHub](https://img.shields.io/github/license/mertguvencli/http-proxy-list)
![GitHub last commit](https://img.shields.io/github/last-commit/mertguvencli/http-proxy-list)

It is a lightweight project that hourly scrapes lots of free-proxy sites, validates if it works, and serves a clean proxy list.


> Scraper found **4205** proxies at the latest update. Usable proxies are below.

## Usage

Click the file format that you want and copy the URL.


|File|Content|Count|
|----|-------|-----|
|[data.txt](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.txt)|`ip_address:port` combined (seperated new line)|279|
|[data.json](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.json)|`ip, port`|279|
|[data-with-geolocation.json](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data-with-geolocation.json)|`ip, port, geolocation`|279|

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
|[proxyscrape.com](https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all)|494|✅|
|[github.com/clarketm/proxy-list](https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt)|400|✅|
|[github.com/monosans/proxy-list](https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt)|305|✅|
|[github.com/TheSpeedX/PROXY-List](https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt)|2123|✅|


## Sample Proxies With Geolocation Info

|#|Ip|Port|Country|City|Internet Service Provider|
|-|--|----|-------|----|-------------------------|
|1|20.47.108.204|8888|United States|Boydton|Microsoft Corporation|
|2|144.217.75.65|8800|Canada|Beauharnois|OVH SAS|
|3|20.47.108.204|8888|United States|Boydton|Microsoft Corporation|
|4|45.167.124.5|9992|Colombia|Guapi|Sepcom Comunicaciones SAS|
|5|85.14.243.31|3128|Germany|Meerbusch|myLoc managed IT AG|
|6|95.217.72.247|3128|Finland|Helsinki|Hetzner Online GmbH|
|7|157.100.12.138|999|Ecuador|Quito|Telconet S.A|
|8|68.183.185.62|80|Singapore|Singapore|DigitalOcean, LLC|
|9|115.96.208.124|8080|India|Mumbai|Hathway IP over Cable Internet Access|
|10|59.124.224.205|3128|Taiwan|Bade District|Chunghwa Telecom Co., Ltd.|
|11|105.112.191.250|3128|Nigeria|Lagos|Airtel Networks Limited|
|12|183.111.25.253|80|South Korea|Seongnam-si|Korea Telecom|
|13|107.172.73.179|7890|United States|Buffalo|ColoCrossing|
|14|50.195.227.153|8080|United States|Indianapolis|Comcast Cable Communications, LLC|
|15|14.207.82.229|8080|Thailand|Bangkok|Triple T Broadband Public Company Limited|
|16|152.32.218.99|8000|Singapore|Singapore|UCLOUD INFORMATION TECHNOLOGY (HK) LIMITED|
|17|189.157.236.197|999|Mexico|Ciudad Valles|Uninet S.A. de C.V|
|18|93.157.163.66|35081|Russia|Volzhskiy|Powernet Ltd|
|19|173.212.229.53|3128|Germany|Nuremberg|Contabo GmbH|
|20|200.110.168.159|8080|Colombia|Trujillo|Media Commerce Partners S.A|



## Contributing

Contributions are welcome, and they are greatly appreciated! Every
little bit helps, and credit will always be given.

