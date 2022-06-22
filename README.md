
# Free HTTP Proxy List 🌍

[![Hourly Update](https://github.com/mertguvencli/http-proxy-list/actions/workflows/main.yml/badge.svg?branch=main)](https://github.com/mertguvencli/http-proxy-list/actions/workflows/main.yml)
![GitHub](https://img.shields.io/github/license/mertguvencli/http-proxy-list)
![GitHub last commit](https://img.shields.io/github/last-commit/mertguvencli/http-proxy-list)

It is a lightweight project that hourly scrapes lots of free-proxy sites, validates if it works, and serves a clean proxy list.


> Scraper found **3696** proxies at the latest update. Usable proxies are below.

## Usage

Click the file format that you want and copy the URL.


|File|Content|Count|
|----|-------|-----|
|[data.txt](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.txt)|`ip_address:port` combined (seperated new line)|201|
|[data.json](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.json)|`ip, port`|201|
|[data-with-geolocation.json](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data-with-geolocation.json)|`ip, port, geolocation`|201|

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
|[proxyscrape.com](https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all)|343|✅|
|[github.com/clarketm/proxy-list](https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt)|400|✅|
|[github.com/monosans/proxy-list](https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt)|187|✅|
|[github.com/TheSpeedX/PROXY-List](https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt)|2083|✅|


## Sample Proxies With Geolocation Info

|#|Ip|Port|Country|City|Internet Service Provider|
|-|--|----|-------|----|-------------------------|
|1|20.47.108.204|8888|United States|Boydton|Microsoft Corporation|
|2|47.240.160.90|10001|Hong Kong|Central|Alibaba.com LLC|
|3|36.90.173.194|8080|Indonesia|Kediri|PT. Telekomunikasi Indonesia|
|4|101.109.158.73|8080|Thailand|Bang Lamung|TOT Public Company Limited|
|5|194.233.73.108|443|Singapore|Singapore|Contabo Asia Private Limited|
|6|182.253.173.50|8080|Indonesia|Jakarta|Biznet Metronet|
|7|41.78.215.1|8787|South Africa|Sandton|Broadband Infraco SOC|
|8|200.110.168.159|8080|Colombia|Trujillo|Media Commerce Partners S.A|
|9|67.212.83.55|1080|Canada|Saint-Hyacinthe|eStruxture Data Centers Inc.|
|10|85.25.91.141|15333|Germany|Cologne|PlusServer GmbH|
|11|20.47.108.204|8888|United States|Boydton|Microsoft Corporation|
|12|47.252.4.64|8888|United States|Charlottesville|Alibaba.com LLC|
|13|64.138.255.146|80|United States|Conway|Horry Telephone Cooperative, Inc.|
|14|201.174.239.18|8080|Mexico|General Escobedo|Transtelco Inc|
|15|168.119.170.87|33009|Germany|Nuremberg|Hetzner Online GmbH|
|16|130.185.122.92|3535|Netherlands|Dronten|Softqloud GmbH|
|17|183.111.25.253|80|South Korea|Seongnam-si|Korea Telecom|
|18|144.76.241.45|7890|Germany|Falkenstein|Hetzner Online GmbH|
|19|177.141.99.50|8080|Brazil|São Paulo|Claro S.A.|
|20|104.131.109.98|3128|United States|Clifton|DigitalOcean, LLC|



## Contributing

Contributions are welcome, and they are greatly appreciated! Every
little bit helps, and credit will always be given.

