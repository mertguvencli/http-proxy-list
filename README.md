
# Free HTTP Proxy List 🌍

[![Hourly Update](https://github.com/mertguvencli/http-proxy-list/actions/workflows/main.yml/badge.svg?branch=main)](https://github.com/mertguvencli/http-proxy-list/actions/workflows/main.yml)
![GitHub](https://img.shields.io/github/license/mertguvencli/http-proxy-list)
![GitHub last commit](https://img.shields.io/github/last-commit/mertguvencli/http-proxy-list)

It is a lightweight project that hourly scrapes lots of free-proxy sites, validates if it works, and serves a clean proxy list.


> Scraper found **3670** proxies at the latest update. Usable proxies are below.

## Usage

Click the file format that you want and copy the URL.


|File|Content|Count|
|----|-------|-----|
|[data.txt](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.txt)|`ip_address:port` combined (seperated new line)|120|
|[data.json](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.json)|`ip, port`|120|
|[data-with-geolocation.json](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data-with-geolocation.json)|`ip, port, geolocation`|120|

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
|[proxyscrape.com](https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all)|380|✅|
|[github.com/clarketm/proxy-list](https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt)|400|✅|
|[github.com/monosans/proxy-list](https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt)|116|✅|
|[github.com/TheSpeedX/PROXY-List](https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt)|1891|✅|


## Sample Proxies With Geolocation Info

|#|Ip|Port|Country|City|Internet Service Provider|
|-|--|----|-------|----|-------------------------|
|1|66.196.238.179|3128|United States|Tomball|Logix|
|2|110.170.126.13|3128|Thailand|Din Daeng|True Internet Corporation CO. Ltd.|
|3|102.130.79.1|3128|South Africa|Johannesburg|Adnexus Celerity Networks (Proprietary) Limited|
|4|209.80.129.2|3128|United States|Medford|HopOne Internet Corporation|
|5|209.80.129.2|3128|United States|Medford|HopOne Internet Corporation|
|6|200.105.215.18|33630|Bolivia|La Paz|AXS Bolivia S. A.|
|7|35.157.249.83|39593|Germany|Frankfurt am Main|Amazon Technologies Inc.|
|8|85.15.152.39|3128|Russia|Tyumen|Rostelecom networks|
|9|203.153.198.4|8080|Australia|Melbourne|World Without Wires Pty Ltd|
|10|201.174.239.18|8080|Mexico|Ciudad Juárez|Transtelco Inc|
|11|190.26.201.194|8080|Colombia|Bogotá|ETB - Colombia|
|12|45.160.78.9|999|Argentina|Mendoza|Wan Developments|
|13|209.80.129.2|3128|United States|Medford|HopOne Internet Corporation|
|14|47.74.24.169|80|Japan|Tokyo|Alibaba.com LLC|
|15|123.163.55.123|3128|China|Zhoukou|Chinanet|
|16|106.52.63.77|3128|China|Shenzhen|Shenzhen Tencent Computer Systems Company Limited|
|17|190.107.224.150|3128|Chile|Santiago|WOM S.A.|
|18|119.15.95.158|8080|Cambodia|Phnom Penh|WiCAM Corporation Ltd|
|19|94.23.241.200|3128|France|Roubaix|OVH SAS|
|20|47.89.185.178|8888|United States|Charlottesville|Alibaba.com LLC|



## Contributing

Contributions are welcome, and they are greatly appreciated! Every
little bit helps, and credit will always be given.

