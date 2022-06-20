
# Free HTTP Proxy List 🌍

[![Hourly Update](https://github.com/mertguvencli/http-proxy-list/actions/workflows/main.yml/badge.svg?branch=main)](https://github.com/mertguvencli/http-proxy-list/actions/workflows/main.yml)
![GitHub](https://img.shields.io/github/license/mertguvencli/http-proxy-list)
![GitHub last commit](https://img.shields.io/github/last-commit/mertguvencli/http-proxy-list)

It is a lightweight project that hourly scrapes lots of free-proxy sites, validates if it works, and serves a clean proxy list.


> Scraper found **4096** proxies at the latest update. Usable proxies are below.

## Usage

Click the file format that you want and copy the URL.


|File|Content|Count|
|----|-------|-----|
|[data.txt](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.txt)|`ip_address:port` combined (seperated new line)|312|
|[data.json](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.json)|`ip, port`|312|
|[data-with-geolocation.json](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data-with-geolocation.json)|`ip, port, geolocation`|312|

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
|[proxyscrape.com](https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all)|473|✅|
|[github.com/clarketm/proxy-list](https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt)|400|✅|
|[github.com/monosans/proxy-list](https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt)|135|✅|
|[github.com/TheSpeedX/PROXY-List](https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt)|2105|✅|


## Sample Proxies With Geolocation Info

|#|Ip|Port|Country|City|Internet Service Provider|
|-|--|----|-------|----|-------------------------|
|1|189.164.118.26|3128|Mexico|Ciudad de Atlixco|Uninet S.A. de C.V|
|2|20.47.108.204|8888|United States|Boydton|Microsoft Corporation|
|3|157.90.222.231|8080|Germany|Falkenstein|Hetzner Online GmbH|
|4|167.235.63.238|3128|Germany|Falkenstein|Hetzner Online GmbH|
|5|152.32.218.99|8000|Singapore|Singapore|UCLOUD INFORMATION TECHNOLOGY (HK) LIMITED|
|6|110.170.126.13|3128|Thailand|Din Daeng|True Internet Corporation CO. Ltd.|
|7|103.215.24.190|9812|Indonesia|Pamulang|PT.Indonesia Comnets Plus|
|8|51.83.253.59|3128|Poland|Warsaw|OVH SAS|
|9|66.94.97.238|443|United States|New York|Contabo Inc.|
|10|75.72.76.3|8118|United States|Minnetonka|Comcast Cable Communications, LLC|
|11|183.88.21.218|8080|Thailand|Chiang Rai|Triple T Broadband Public Company Limited|
|12|47.240.160.90|10001|Hong Kong|Central|Alibaba.com LLC|
|13|66.94.120.161|443|United States|Seattle|Contabo Inc.|
|14|79.142.95.90|55443|Kazakhstan|Nur-Sultan|Obit Telecommunications|
|15|149.255.26.228|9090|Russia|Stavropol|OOO Set Network|
|16|66.94.120.161|443|United States|Seattle|Contabo Inc.|
|17|50.231.95.3|8080|United States|Marietta|Comcast Cable Communications, LLC|
|18|85.173.165.36|46330|Russia|Cherkessk|Karachaevo-Cherkesskelektrosvyaz|
|19|41.193.84.196|3128|South Africa|Johannesburg|Vox Telecom|
|20|95.0.90.243|8080|Turkey|Istanbul|Turk Telekomunikasyon Anonim Sirketi|



## Contributing

Contributions are welcome, and they are greatly appreciated! Every
little bit helps, and credit will always be given.

