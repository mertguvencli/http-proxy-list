
# Free HTTP Proxy List 🌍

[![Hourly Update](https://github.com/mertguvencli/http-proxy-list/actions/workflows/main.yml/badge.svg?branch=main)](https://github.com/mertguvencli/http-proxy-list/actions/workflows/main.yml)
![GitHub](https://img.shields.io/github/license/mertguvencli/http-proxy-list)
![GitHub last commit](https://img.shields.io/github/last-commit/mertguvencli/http-proxy-list)

It is a lightweight project that hourly scrapes lots of free-proxy sites, validates if it works, and serves a clean proxy list.


> Scraper found **4378** proxies at the latest update. Usable proxies are below.

## Usage

Click the file format that you want and copy the URL.


|File|Content|Count|
|----|-------|-----|
|[data.txt](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.txt)|`ip_address:port` combined (seperated new line)|367|
|[data.json](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.json)|`ip, port`|367|
|[data-with-geolocation.json](https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data-with-geolocation.json)|`ip, port, geolocation`|367|

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
|[proxyscrape.com](https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all)|525|✅|
|[github.com/clarketm/proxy-list](https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt)|400|✅|
|[github.com/monosans/proxy-list](https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt)|464|✅|
|[github.com/TheSpeedX/PROXY-List](https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt)|2106|✅|


## Sample Proxies With Geolocation Info

|#|Ip|Port|Country|City|Internet Service Provider|
|-|--|----|-------|----|-------------------------|
|1|20.47.108.204|8888|United States|Boydton|Microsoft Corporation|
|2|198.245.55.142|8080|Canada|Beauharnois|OVH SAS|
|3|66.196.238.178|3128|United States|Tomball|Logix|
|4|20.47.108.204|8888|United States|Boydton|Microsoft Corporation|
|5|3.128.120.252|80|United States|Dublin|Amazon.com, Inc.|
|6|3.128.120.252|80|United States|Dublin|Amazon.com, Inc.|
|7|121.254.195.12|8080|South Korea|Yongsan-dong|LG DACOM Corporation|
|8|185.105.108.208|8080|Netherlands|Amsterdam|Serverius|
|9|95.216.26.66|3128|Finland|Helsinki|Hetzner Online GmbH|
|10|190.97.226.236|999|Venezuela|Barinas|NetLink América C.A.|
|11|201.120.27.15|53281|Mexico|Hermosillo|Uninet S.A. de C.V|
|12|102.130.79.1|3128|South Africa|Johannesburg|Adnexus Celerity Networks (Proprietary) Limited|
|13|24.106.221.230|53281|United States|Pine Knoll Shores|Spectrum|
|14|185.3.214.3|80|Iran|Shahrīār|Pouya shabakeh Asr Co. (LTD.)|
|15|181.224.255.42|8080|Peru|Lima|Econocable Media SAC|
|16|175.100.16.143|9812|Cambodia|Phnom Penh|VIETTEL (CAMBODIA) PTE., LTD|
|17|185.208.172.196|8080|Germany|Frankfurt am Main|BitCommand|
|18|45.229.33.27|999|Dominican Republic|Santo Domingo Este|Gold Data C.A.|
|19|139.255.74.125|8080|Indonesia|Cibuntu|PT. LINKNET|
|20|103.178.43.2|8181|Indonesia|Jakarta|PT Jaring Solusi Persada|



## Contributing

Contributions are welcome, and they are greatly appreciated! Every
little bit helps, and credit will always be given.

