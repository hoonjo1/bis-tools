import os
import time
from selenium.webdriver.common.keys import Keys
from route_id import *

def bis_bus_driving_info_download_f(driver,dates,company):
    url = "http://office.busrang.com/login"
    loginid = "4100800"
    loginpw = "4100800" 
    driver.get(url) 
    driver.implicitly_wait(5)
    driver.find_element_by_id("loginid").send_keys(loginid)
    driver.find_element_by_id("loginpw").send_keys(loginpw)
    driver.find_element_by_class_name("btnGray.button").send_keys(Keys.ENTER)
    driver.switch_to.window(driver.window_handles[0])

    if company == "경진여객":
        company_id = "4100800"
    elif company == "용남고속":
        company_id = "4103600"
    elif company == "제부여객":
        company_id = "4106100"
        
    for date in dates:
        driver.get(f"http://office.busrang.com/status/information_busroute/list?districtId=&transpBizrId={company_id}&isExcel=Y&stDate={date}")

    print("WAIT_30s")
    time.sleep(30)

    date_count = int(len(dates))
    before_file_name = []
    after_file_name = dates

    for date in range(date_count):
        if date == 0:
            before_file_name.append("버스운행정보")
        else:
            before_file_name.append(f"버스운행정보 ({date})")

    for before, after in zip(before_file_name, after_file_name):
        before_Name = os.path.join(rf"\\kjnas\KJNAS\1.기획부\9.개발팀\BIS_BUS_DRIVING_INFO\BEFORE\{before}.xls")
        after_Name = os.path.join(rf"\\kjnas\KJNAS\1.기획부\9.개발팀\BIS_BUS_DRIVING_INFO\ATFER\{company}_{after}_버스운행정보.xls")
        print(f"BEFOR : {before} _____ AFTER : {company}_{after}_버스운행정보")
        os.rename(before_Name, after_Name)
