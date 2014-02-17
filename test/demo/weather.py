import urllib
def getCityWeather(cityid):
    url="http://www.weather.com.cn/data/cityinfo/"+cityid+".html"
    try:
        web=urllib.urlopen(url)
        content=web.read().decode('utf-8').replace("","")
    except Exception,e:
        content="error"
    print content

if __name__ == "__main__":
    getCityWeather("101110301")
