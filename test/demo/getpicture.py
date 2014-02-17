import urllib

def method1(url,filepath):
    urllib.urlretrieve(url,filepath)

url='http://fmn.xnpic.com/fmn056/20130629/1855/original_h91T_23d1000061191191.jpg'
filepath = 'test.jpg'
method1(url,filepath)