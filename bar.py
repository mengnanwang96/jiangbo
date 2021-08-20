import requests
import re
from lxml import etree
import re
from lxml.html import tostring
from selenium import webdriver
import time
def askurl(url,headers):
    req=requests.get(url=url,headers=headers)
    content=req.text
    bv_num=re.findall(r'"bvid":"(.*?)","mid"',content)
    list1.extend(bv_num)
    return list1
def chrome():
    for k in b:
        url='https://www.bilibili.com/video/'+k
        chromeOptions=webdriver.ChromeOptions()
        #chromeOptions.add_argument("--proxy-server=121.232.148.133:3256")
        driver=webdriver.Chrome(options=chromeOptions)
        driver.get(url)
        time.sleep(5)
        Video_Time = driver.find_element_by_xpath("//div[@name='time_textarea']/span[3]").text
        element=driver.find_element_by_xpath("//button[@class='bilibili-player-video-btn-speed-name']")
        webdriver.ActionChains(driver).move_to_element(element).click(element).perform()
        element=driver.find_element_by_xpath("//ul[@class='bilibili-player-video-btn-speed-menu']/li[1]")
        webdriver.ActionChains(driver).move_to_element(element).click(element).perform()
        #element=driver.find_element_by_xpath("//button[@class='bilibili-player-iconfont']")
        #webdriver.ActionChains(driver).move_to_element(element).click(element).perform()
        time.sleep(40)
        driver.close()
def getbv():
    a=askurl(url,headers)
    html1=etree.HTML(a)
    bv1=html1.xpath('//a[@class="cover-wrp"]/@href')
    #bv2=html.tostring(bv1)
    
    print(bv1)
if __name__=="__main__":
    list1=[]
    for i in range(1,18):
        url='https://member.bilibili.com/x/web/archives?status=is_pubing%2Cpubed%2Cnot_pubed&order=click&pn='+str(i)+'&ps=10&coop=1&interactive=1'
        headers={
        'cookie':'_uuid=7F13E9BA-3609-CB4F-6067-41D6FAFF7C2A53975infoc;buvid3=C10DB5BC-7D41-436A-B264-5B8A0EDEC35B34759infoc;buvid_fp=C10DB5BC-7D41-436A-B264-5B8A0EDEC35B34759infoc;buvid_fp_plain=C10DB5BC-7D41-436A-B264-5B8A0EDEC35B34759infoc;DedeUserID=93416779;DedeUserID__ckMd5=59abad8f29cade2b;CURRENT_FNVAL=80;rpdid=|(k|kYYkY~|k0J\'uYkk~mJ|u);LIVE_BUVID=AUTO9016240812887565; CURRENT_BLACKGAP=1; blackside_state=1; SESSDATA=14d878cf%2C1644252203%2C70db9%2A81; bili_jct=f326c765e469cc78c743fac13ffaa884; sid=kaen3sch; bp_t_offset_93416779=559180063063353710; fingerprint3=c6832aebdb58886c429719108e823a56; fingerprint=f4715a33071ff80a5563c6299fc9b8bc; fingerprint_s=95377579a295570932c3c06a2fa3ffbb; bsource=search_google; innersign=1; CURRENT_QUALITY=112; PVID=21; bp_video_offset_93416779=560873517127567081',
        'origin':'https://www.bilibili.com',
        'referer':'https://member.bilibili.com/platform/upload-manager/article?page='+str(i)+'&order=click',
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36'
        }
        askurl(url,headers)
        #getbv()
    b=askurl(url,headers)
    chrome()
        
#################


