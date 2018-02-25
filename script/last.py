# -*- coding: UTF-8 -*-
import urllib.parse
import urllib.request
import json
import time
import random
import struct
import socket

userAgents = [
    'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)',
    'Mozilla/5.0(compatible;MSIE9.0;WindowsNT6.1;Trident/5.0;',
    'Mozilla/5.0(WindowsNT6.1;rv:2.0.1)Gecko/20100101Firefox/4.0.1',
    'Opera/9.80(WindowsNT6.1;U;en)Presto/2.8.131Version/11.11',
    'Mozilla/4.0(compatible;MSIE7.0;WindowsNT5.1;TencentTraveler4.0)',
    'Mozilla/4.0(compatible;MSIE7.0;WindowsNT5.1;Trident/4.0;SE2.XMetaSr1.0;SE2.XMetaSr1.0;.NETCLR2.0.50727;SE2.XMetaSr1.0)',
    'Mozilla/4.0(compatible;MSIE7.0;WindowsNT5.1;360SE)',
    'Mozilla/4.0(compatible;MSIE7.0;WindowsNT5.1;Trident/4.0;TencentTraveler4.0;.NETCLR2.0.50727)',
    'MQQBrowser/26Mozilla/5.0(Linux;U;Android2.3.7;zh-cn;MB200Build/GRJ22;CyanogenMod-7)AppleWebKit/533.1(KHTML,likeGecko)Version/4.0MobileSafari/533.1'
]

RANDOM_IP_POOL=['192.168.10.222/0']
def __get_random_ip():
    str_ip = RANDOM_IP_POOL[random.randint(0,len(RANDOM_IP_POOL) - 1)]
    str_ip_addr = str_ip.split('/')[0]
    str_ip_mask = str_ip.split('/')[1]
    ip_addr = struct.unpack('>I',socket.inet_aton(str_ip_addr))[0]
    mask = 0x0
    for i in range(31, 31 - int(str_ip_mask), -1):
        mask = mask | ( 1 << i)
    ip_addr_min = ip_addr & (mask & 0xffffffff)
    ip_addr_max = ip_addr | (~mask & 0xffffffff)
    return socket.inet_ntoa(struct.pack('>I', random.randint(ip_addr_min, ip_addr_max)))

URL_ROOT = r'http://pdfm.eastmoney.com/EM_UBG_PDTI_Fast/api/js?rtntype=5&cb=jQuery183024268883230430283_1509546539162&id=6034581&type=k&authorityType=&_=1509546612612'
user_agent = "Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)"
headers = {
}

# 1. referer 很重要
# 2. Cookie 的值会变

# data = {
    
# }
f = open('test.html', 'a+')
i = 0
while i < 5:
    headers['User-Agent'] = userAgents[random.randint(0, 8)]
    headers['X-Forwarded-For'] = __get_random_ip() #random.randint(0, 8)
    request = urllib.request.Request(URL_ROOT, data=None, headers = headers)
    response = urllib.request.urlopen(request)
    ret_data = bytes.decode(response.read())
    print(ret_data)
    # f.write(response.read())

    time.sleep(2)
    i = i + 1

f.close()
