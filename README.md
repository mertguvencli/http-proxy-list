
# Free HTTP Proxy List 🌍

[![Hourly Update](https://github.com/mertguvencli/http-proxy-list/actions/workflows/main.yml/badge.svg?branch=main)](https://github.com/mertguvencli/http-proxy-list/actions/workflows/main.yml)
![GitHub](https://img.shields.io/github/license/mertguvencli/http-proxy-list)
![GitHub last commit](https://img.shields.io/github/last-commit/mertguvencli/http-proxy-list)

It is a lightweight project that hourly scrapes lots of free-proxy sites, validates if it works, and serves a clean proxy list.


> Scraper found **4057** proxies at the latest update. Usable proxies are below.

## Usage

Click the file format that you want and copy the URL.


|File|Content|Count|
|----|-------|-----|
|[data.txt](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.txt)|`ip_address:port` combined (seperated new line)|213|
|[data.json](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.json)|`ip, port`|213|
|[data-with-geolocation.json](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data-with-geolocation.json)|`ip, port, geolocation`|213|

## Sources

|Source|Found Proxies|Succeed|
|------|-------------|-------|
|[free-proxy-list.net](https://free-proxy-list.net)|300|✅|
|[us-proxy.org](https://www.us-proxy.org)|200|✅|
|[proxydb.net](http://proxydb.net)|0|🚫|
|[free-proxy-list.com](https://free-proxy-list.com/?page=&port=&type%5B%5D=http&type%5B%5D=https&up_time=0&search=Search)|10|✅|
|[proxy-list.download](https://www.proxy-list.download/HTTP)|26|✅|
|[vpnoverview.com](https://vpnoverview.com/privacy/anonymous-browsing/free-proxy-servers)|32|✅|
|[proxyscan.io](https://www.proxyscan.io)|100|✅|
|[proxylist.geonode.com](https://proxylist.geonode.com/api/proxy-list?limit=300&page=1&sort_by=lastChecked&sort_type=desc&protocols=http,https)|300|✅|
|[proxyscrape.com](https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all)|437|✅|
|[github.com/clarketm/proxy-list](https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt)|400|✅|
|[github.com/monosans/proxy-list](https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt)|280|✅|
|[github.com/TheSpeedX/PROXY-List](https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt)|1972|✅|


## Sample Proxies With Geolocation Info

|#|Ip|Port|Country|City|Internet Service Provider|
|-|--|----|-------|----|-------------------------|
|1|34.82.235.224|3128|United States|The Dalles|Google LLC|
|2|163.172.83.25|3128|France|Paris|Online S.A.S.|
|3|207.180.221.178|3128|Germany|Nuremberg|Contabo GmbH|
|4|45.76.13.167|59394|United States|Piscataway|The Constant Company|
|5|66.94.97.238|443|United States|New York|Contabo Inc.|
|6|45.167.253.129|999|Mexico|San Luis Potosí City|QDS NETWORKS SA DE CV|
|7|14.207.123.13|8080|Thailand|Bangkok|Triple T Broadband Public Company Limited|
|8|122.155.165.191|3128|Thailand|Ratchathewi|CAT Telecom Public Company Limited|
|9|116.212.155.229|41890|Cambodia|Phnom Penh|MekongNet|
|10|186.150.207.29|9812|Dominican Republic|Santo Domingo Este|Altice Dominicana S.A.|
|11|45.76.26.132|59394|United States|Elk Grove Village|The Constant Company|
|12|190.131.250.105|999|Colombia|Medellín|Columbus Networks Colombia|
|13|186.233.186.60|8080|United States|Chicago|Maxihost LTDA|
|14|103.76.13.134|9812|Indonesia|Bogor|MORATELINDO|
|15|176.193.128.203|53281|Russia|Korolyov|Net By Net Holding LLC|
|16|45.76.26.132|59394|United States|Elk Grove Village|The Constant Company|
|17|197.210.141.218|8080|Nigeria|Lagos|MTN NIGERIA Communication limited|
|18|77.236.236.38|10000|Russia|Moscow|Enforta-MSK|
|19|103.155.198.64|8080|Indonesia|Babakangarut|PT Lintas Jaringan Nusantara|
|20|82.167.253.137|8080|Saudi Arabia|Riyadh|ORBITNET.KSA|



## Contributing

Contributions are welcome, and they are greatly appreciated! Every
little bit helps, and credit will always be given.

