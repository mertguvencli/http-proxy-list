
# Free HTTP Proxy List 🌍

[![Hourly Update](https://github.com/mertguvencli/http-proxy-list/actions/workflows/main.yml/badge.svg?branch=main)](https://github.com/mertguvencli/http-proxy-list/actions/workflows/main.yml)
![GitHub](https://img.shields.io/github/license/mertguvencli/http-proxy-list)
![GitHub last commit](https://img.shields.io/github/last-commit/mertguvencli/http-proxy-list)

It is a lightweight project that hourly scrapes lots of free-proxy sites, validates if it works, and serves a clean proxy list.


> Scraper found **3987** proxies at the latest update. Usable proxies are below.

## Usage

Click the file format that you want and copy the URL.


|File|Content|Count|
|----|-------|-----|
|[data.txt](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.txt)|`ip_address:port` combined (seperated new line)|146|
|[data.json](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.json)|`ip, port`|146|
|[data-with-geolocation.json](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data-with-geolocation.json)|`ip, port, geolocation`|146|

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
|[proxyscrape.com](https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all)|406|✅|
|[github.com/clarketm/proxy-list](https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt)|400|✅|
|[github.com/monosans/proxy-list](https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt)|446|✅|
|[github.com/TheSpeedX/PROXY-List](https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt)|2052|✅|


## Sample Proxies With Geolocation Info

|#|Ip|Port|Country|City|Internet Service Provider|
|-|--|----|-------|----|-------------------------|
|1|20.47.108.204|8888|United States|Boydton|Microsoft Corporation|
|2|103.73.194.2|80|Hong Kong|Wanchai|TouchPal HK Co., Limited|
|3|194.233.69.41|443|Singapore|Singapore|Contabo Asia Private Limited|
|4|78.38.100.121|8080|Iran|Tehran|Iran Telecommunication Company PJS|
|5|188.138.11.48|5566|France|Strasbourg|Host Europe GmbH|
|6|103.178.43.14|8181|Indonesia|Jakarta|PT Jaring Solusi Persada|
|7|190.26.201.194|8080|Colombia|Bogotá|ETB - Colombia|
|8|103.209.36.57|8080|India|Mumbai|Syscon Infoway Pvt. Ltd.|
|9|75.119.197.10|1081|United States|Brea|New Dream Network, LLC|
|10|85.25.132.9|5566|France|Strasbourg|Host Europe GmbH|
|11|85.25.93.136|5566|France|Strasbourg|Host Europe GmbH|
|12|20.47.108.204|8888|United States|Boydton|Microsoft Corporation|
|13|93.185.123.154|3128|Italy|Pove del Grappa|Omegacom S.R.L.S.|
|14|122.155.165.191|3128|Thailand|Ratchathewi|CAT Telecom Public Company Limited|
|15|14.207.62.221|8080|Thailand|Pak Kret|Triple T Broadband Public Company Limited|
|16|192.241.158.51|1081|United States|North Bergen|DigitalOcean, LLC|
|17|54.39.102.233|3128|Canada|Beauharnois|OVH SAS|
|18|212.64.72.199|8080|China|Haidian|Shenzhen Tencent Computer Systems Company Limited|
|19|45.234.63.218|999|Venezuela|Caracas|SOLUCIONES INSTALRED CH&C C.A.|
|20|200.68.23.188|999|Chile|Placilla|CTC. CORP S.A. (TELEFONICA EMPRESAS)|



## Contributing

Contributions are welcome, and they are greatly appreciated! Every
little bit helps, and credit will always be given.

