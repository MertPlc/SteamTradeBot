from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time 

class SteamTradeBot:
    def __init__(self,username,password,bekle=5):
        self.username = username
        self.password = password
        self.bekle = bekle
        self.girisYap()
        


    def girisYap(self):
        self.browser = webdriver.Chrome(executable_path=r"Driver\chromedriver.exe")
        self.browser.get("https://store.steampowered.com/login/?l=turkish")
        time.sleep(self.bekle)
        steamID = self.browser.find_element_by_name("username")
        steamSifre = self.browser.find_element_by_name("password")
        steamID.send_keys(self.username)
        steamSifre.send_keys(self.password)
        steamSifre.send_keys(Keys.ENTER)
        time.sleep(15)
        steamGuard = self.browser.find_element_by_xpath("/html/body/div[3]/div[3]/div/div/div/form/div[4]/div[1]/div[1]")
        steamGuard.click()
        
        
    def autoTrade(self):
        
        while True:
            self.browser.get("https://store.steampowered.com/?l=turkish")
            time.sleep(self.bekle)

            dugme2 = self.browser.find_element_by_xpath("/html/body/div[1]/div[7]/div[1]/div/div[3]/div/span")   # profil ismi
            dugme2.click()
            time.sleep(2)

            dugme3 = self.browser.find_element_by_xpath("/html/body/div[1]/div[7]/div[1]/div/div[3]/div/div[3]/div/a[1]")   # profilimi görüntüle
            dugme3.click()
            time.sleep(2)

            self.browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")
            time.sleep(2)

            dugme4 = self.browser.find_element_by_xpath("/html/body/div[1]/div[7]/div[6]/div[1]/div[2]/div/div[1]/div[3]/div/div[2]/div/a")  # CS GO Trading 
            dugme4.click()
            time.sleep(2)

            self.browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")
            time.sleep(2)

            dugme5 = self.browser.find_element_by_xpath("/html/body/div[1]/div[7]/div[3]/div[1]/div[3]/div/div[1]/div[4]/div[1]/div/a")  # Popüler Tartışmalar - tümünü gör
            dugme5.click()
            time.sleep(2)

            dugme6 = self.browser.find_element_by_xpath("/html/body/div[1]/div[7]/div[7]/div[1]/div[2]/div/div[2]/div[2]/div[1]/a/span") # Yeni bir başlık aç
            dugme6.click()
            time.sleep(2)

            kutucuk2 = self.browser.find_element_by_name("topic")
            baslik = "HEADER OF TOPIC"
            kutucuk2.send_keys(baslik)
            time.sleep(2)

            kutucuk3 = self.browser.find_element_by_name("text")
            trade_link = "TRADE-URL"
            kutucuk3.send_keys(trade_link)
            time.sleep(2)

            dugme7 = self.browser.find_element_by_xpath("/html/body/div[1]/div[7]/div[7]/div[1]/div[2]/div/div[1]/div[2]/div[1]/div/div[2]/form/div[3]/button/span")  # Başlık Aç
            dugme7.click()
            time.sleep(2)

            dugmex = self.browser.find_element_by_xpath("/html/body/div[1]/div[7]/div[1]/div/div[3]/div/span")   # profil ismi
            dugmex.click()
            time.sleep(2)

            dugmex1 = self.browser.find_element_by_xpath("/html/body/div[1]/div[7]/div[1]/div/div[3]/div/div[3]/div/a[1]")   # profilimi görüntüle
            dugmex1.click()
            time.sleep(2)

            self.browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")
            time.sleep(2)

            dugmex2 = self.browser.find_element_by_xpath("/html/body/div[1]/div[7]/div[6]/div[1]/div[2]/div/div[1]/div[3]/div/div[2]/div[2]/a")  # CS GO Lounge 
            dugmex2.click()
            time.sleep(2)

            dugmex3 = self.browser.find_element_by_xpath("/html/body/div[1]/div[7]/div[3]/div[1]/div[3]/div/div[1]/div[4]/div[1]/div/a")  # Popüler Tartışmalar - tümünü gör
            dugmex3.click()
            time.sleep(2)

            dugmex4 = self.browser.find_element_by_xpath("/html/body/div[1]/div[7]/div[7]/div[1]/div[2]/div/div[2]/div[2]/div[1]/a/span") # Yeni bir başlık aç
            dugmex4.click()
            time.sleep(2)

            kutucukx = self.browser.find_element_by_name("topic")
            baslik1 = "HEADER OF TOPIC"
            kutucukx.send_keys(baslik1)
            time.sleep(2)

            kutucukx1 = self.browser.find_element_by_name("text")
            trade_link1 = "TRADE-URL"
            kutucukx1.send_keys(trade_link1)
            time.sleep(2)

            dugmex5 = self.browser.find_element_by_xpath("/html/body/div[1]/div[7]/div[7]/div[1]/div[2]/div/div[1]/div[3]/div[1]/div/div[2]/form/div[4]/button/span")  # Başlık Aç
            dugmex5.click()
            time.sleep(2400)