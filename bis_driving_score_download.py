from selenium.webdriver.common.keys import Keys
from route_id import *

def bis_driving_score_download_f(driver,dates,company):
    url = "http://office.busrang.com/login"
    loginid = "4100800"
    loginpw = "4100800" 

    if company == "경진여객":
        routes = kj_route_id
    elif company == "용남고속":
        routes = yn_route_id
    elif company == "제부여객":
        routes = jb_route_id
    elif company =="ALL":
        routes = all_route_id

    driver.get(url) 
    driver.implicitly_wait(5)
    driver.find_element_by_id("loginid").send_keys(loginid)
    driver.find_element_by_id("loginpw").send_keys(loginpw)
    driver.find_element_by_class_name("btnGray.button").send_keys(Keys.ENTER)
    driver.switch_to.window(driver.window_handles[0])

    for date in dates:
        for route in routes:
            driver.get(f"http://office.busrang.com/status/route_record/download?routeId={route}&stDate={date}&edDate={date}")
            print(f"COMPLETE__{route}_{date}운행기록표")