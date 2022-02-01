from selenium import webdriver
from selenium.webdriver.support.ui import Select,WebDriverWait
from selenium.webdriver.firefox.options import Options
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from denemeconfig import *
i=1
ignored=[]
opts=Options()
opts.headless=True
driver = webdriver.Firefox(options=opts)

def getSonuc(ad,numara,url,puanbosluk):
    driver.get(url)

    seviye = Select(driver.find_element("id","seviye"))
    seviye.select_by_visible_text(i_sinif)

    ilkodu = Select(driver.find_element("id","ilkodu"))
    ilkodu.select_by_visible_text(i_sehir)

    okuladi = driver.find_element("id","kurumarama")
    okuladi.send_keys(i_kurum)
    WebDriverWait(driver, 2).until(EC.presence_of_element_located(("id", 'ui-id-2')))
    okulasilad=driver.find_element("id","ui-id-2")
    okulasilad.click()

    ogrnoinp = driver.find_element("id","ogrencino")
    ogrnoinp.send_keys(str(numara))

    ogradinp = driver.find_element("id","isim")
    ogradinp.send_keys(ad)

    driver.find_element("name","bulbtn1").submit()

    WebDriverWait(driver, 3).until(EC.presence_of_element_located(("xpath","/html/body/div[1]/section/div/div/div[5]/div/div[1]/div/div")))

    sinif=driver.find_element("xpath","/html/body/div[1]/section/div/div/div[1]/div[2]/div[3]").text[1:]
    puan=float(driver.find_element("xpath","/html/body/div[1]/section/div/div/div[5]/div/div[1]/div/div").text[puanbosluk:].replace(",","."))
    
    sinifdrc=int(driver.find_element("xpath","/html/body/div[1]/section/div/div/div[5]/div/div[3]/div/div[2]").text)
    kurumdrc=int(driver.find_element("xpath","/html/body/div[1]/section/div/div/div[5]/div/div[3]/div/div[3]").text)
    ildrc=int(driver.find_element("xpath","/html/body/div[1]/section/div/div/div[5]/div/div[3]/div/div[5]").text)
    geneldrc=int(driver.find_element("xpath","/html/body/div[1]/section/div/div/div[5]/div/div[3]/div/div[6]").text)
    
    sorusayi=int(driver.find_element("xpath","/html/body/div[1]/section/div/div/div[6]/div/div/div[1]/div[2]/div[2]/div[1]").text)
    dogrusayi=int(driver.find_element("xpath","/html/body/div[1]/section/div/div/div[6]/div/div/div[1]/div[2]/div[2]/div[2]").text)
    yanlissayi=int(driver.find_element("xpath","/html/body/div[1]/section/div/div/div[6]/div/div/div[1]/div[2]/div[2]/div[3]").text)
    bossayi=sorusayi-dogrusayi-yanlissayi
    netsayi=float(driver.find_element("xpath","/html/body/div[1]/section/div/div/div[6]/div/div/div[1]/div[2]/div[2]/div[4]").text.replace(",","."))

    def getDers(div_id):
        d_ss=int(driver.find_element("xpath",f"/html/body/div[1]/section/div/div/div[7]/div/div[{div_id}]/div[1]/div[2]/div[2]/div[1]").text)
        d_ds=int(driver.find_element("xpath",f"/html/body/div[1]/section/div/div/div[7]/div/div[{div_id}]/div[1]/div[2]/div[2]/div[2]").text)
        d_ys=int(driver.find_element("xpath",f"/html/body/div[1]/section/div/div/div[7]/div/div[{div_id}]/div[1]/div[2]/div[2]/div[3]").text)
        d_bs=d_ss-d_ds-d_ys
        d_ns=float(driver.find_element("xpath",f"/html/body/div[1]/section/div/div/div[7]/div/div[{div_id}]/div[1]/div[2]/div[2]/div[4]").text.replace(",","."))
        return d_ss,d_ds,d_ys,d_bs,d_ns

    edb_s,edb_d,edb_y,edb_b,edb_n=getDers(1)
    trh_s,trh_d,trh_y,trh_b,trh_n=getDers(2)
    cog_s,cog_d,cog_y,cog_b,cog_n=getDers(3)
    din_s,din_d,din_y,din_b,din_n=getDers(4)
    mat_s,mat_d,mat_y,mat_b,mat_n=getDers(6)
    fiz_s,fiz_d,fiz_y,fiz_b,fiz_n=getDers(7)
    kim_s,kim_d,kim_y,kim_b,kim_n=getDers(8)
    biy_s,biy_d,biy_y,biy_b,biy_n=getDers(9)
    
    return {"ad":ad,"no":numara,"9x":sinif,"s_drc":sinifdrc,"k_drc":kurumdrc,"i_drc":ildrc,"g_drc":geneldrc,"pn":puan,"ss":sorusayi,"ds":dogrusayi,"ys":yanlissayi,"bs":bossayi,"ns":netsayi,
    "edb_s":edb_s,"edb_d":edb_d,"edb_y":edb_y,"edb_b":edb_b,"edb_n":edb_n,
    "trh_s":trh_s,"trh_d":trh_d,"trh_y":trh_y,"trh_b":trh_b,"trh_n":trh_n,
    "cog_s":cog_s,"cog_d":cog_d,"cog_y":cog_y,"cog_b":cog_b,"cog_n":cog_n,
    "din_s":din_s,"din_d":din_d,"din_y":din_y,"din_b":din_b,"din_n":din_n,
    "mat_s":mat_s,"mat_d":mat_d,"mat_y":mat_y,"mat_b":mat_b,"mat_n":mat_n,
    "fiz_s":fiz_s,"fiz_d":fiz_d,"fiz_y":fiz_y,"fiz_b":fiz_b,"fiz_n":fiz_n,
    "kim_s":kim_s,"kim_d":kim_d,"kim_y":kim_y,"kim_b":kim_b,"kim_n":kim_n,
    "biy_s":biy_s,"biy_d":biy_d,"biy_y":biy_y,"biy_b":biy_b,"biy_n":biy_n}


def find_ad_from_no(no):
    for i in range(len(sinif9a)):
        if(no==sinif9a[i][1]):
            return sinif9a[i][0]
    for i in range(len(sinif9b)):
        if(no==sinif9b[i][1]):
            return sinif9b[i][0]
    for i in range(len(sinif9c)):
        if(no==sinif9c[i][1]):
            return sinif9c[i][0]
    return -1