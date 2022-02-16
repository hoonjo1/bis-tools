from pyautogui_start import company_sel, start_date_sel, end_date_sel, last_check, date_range, will_work, company_sel_bus_info
from selenium_start import selenuim_start_f, selenuim_start_f_bus_info
from bis_driving_score_download import bis_driving_score_download_f
from bis_driving_score_edit import bis_driving_score_edit_f
from bis_driving_score_merge import bis_driving_score_merge_f
from bis_bus_driving_info_download import bis_bus_driving_info_download_f
from bis_driving_score_route_merge import bis_driving_score_route_merge_f

work_sel = will_work()
if work_sel =="BIS 운행기록표 다운로드":
    user_company_sel = company_sel()
    user_start_date_sel = start_date_sel()
    user_end_date_sel = end_date_sel()
    user_last_check = last_check(user_company_sel, user_start_date_sel, user_end_date_sel)
    dates = date_range(user_start_date_sel, user_end_date_sel)
    driver = selenuim_start_f()
    download = bis_driving_score_download_f(driver,dates,user_company_sel)

elif work_sel =="BIS 운행기록표 EDIT":
    user_company_sel = company_sel()
    user_start_date_sel = start_date_sel()
    user_end_date_sel = end_date_sel()
    user_last_check = last_check(user_company_sel, user_start_date_sel, user_end_date_sel)
    dates = date_range(user_start_date_sel, user_end_date_sel)
    edit = bis_driving_score_edit_f(user_company_sel, dates)

elif work_sel =="BIS 운행기록표 MERGE":
    user_company_sel = company_sel()
    user_start_date_sel = start_date_sel()
    user_end_date_sel = end_date_sel()
    user_last_check = last_check(user_company_sel, user_start_date_sel, user_end_date_sel)
    dates = date_range(user_start_date_sel, user_end_date_sel)
    merge = bis_driving_score_merge_f(user_company_sel, dates)

elif work_sel=="BIS 운행기록표 노선별 MERGE":
    user_company_sel = company_sel()
    user_start_date_sel = start_date_sel()
    user_end_date_sel = end_date_sel()
    user_last_check = last_check(user_company_sel, user_start_date_sel, user_end_date_sel)
    dates = date_range(user_start_date_sel, user_end_date_sel)
    merge = bis_driving_score_route_merge_f(user_company_sel, dates)

elif work_sel =="BIS 버스운행정보 다운로드":
    user_company_sel = company_sel_bus_info()
    user_start_date_sel = start_date_sel()
    user_end_date_sel = end_date_sel()
    user_last_check = last_check(user_company_sel, user_start_date_sel, user_end_date_sel)
    dates = date_range(user_start_date_sel, user_end_date_sel)
    driver = selenuim_start_f_bus_info()
    download = bis_bus_driving_info_download_f(driver, dates, user_company_sel)