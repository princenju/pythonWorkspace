from HTMLParser import HTMLParser
import urllib
class MyParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.images = []
 
    def handle_starttag(self, tag, attrs):
        # print "Encountered the beginning of a %s tag" % tag
        if tag == "a":
#             print tag
            if len(attrs) == 0: pass
            else:
                for (variable, value)  in attrs:
                    if variable == "href":
                        self.images.append(value)            
                        
url = "http://www.unitedcn.com/01ZGZZ/jfzztj.htm"
web = urllib.urlopen(url)
content = web.read()
# print content
hp = MyParser()
hp.feed(content)
filepath = 'f://pictures//pythonCrawler//'
for url in hp.images:
    if 'images' in url:
        url='http://www.unitedcn.com/01ZGZZ/'+url
        urllib.urlretrieve(url,filepath+url.split('/')[-1])
hp.close()
