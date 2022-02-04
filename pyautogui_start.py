import sys
import pyautogui as pg
import pandas
from datetime import datetime

def will_work():
    will_worl_check = pg.confirm(text="WILL_WORK", title ="will_work_select", buttons=["BIS 운행기록표 다운로드", "BIS 운행기록표 EDIT", "BIS 운행기록표 MERGE", "BIS 버스운행정보 다운로드"])
    if will_worl_check == None:
        sys.exit
    return will_worl_check

def company_sel():
    company = pg.confirm(text="COMPANY_SELECT", title ="company_select", buttons=["경진여객", "용남고속", "제부여객", "ALL"])
    check = f"YOUR_SELECT : {company}"
    if company == None:
        sys.exit()
    company_check = pg.confirm(text=check, title='your_select_check', buttons=["YES", "NO"])
    if company_check == "NO":
        company_sel()
    elif company_check == None:
        sys.exit()
    return company

def company_sel_bus_info():
    company = pg.confirm(text="COMPANY_SELECT", title ="company_select", buttons=["경진여객", "용남고속", "제부여객"])
    check = f"YOUR_SELECT : {company}"
    if company == None:
        sys.exit()
    company_check = pg.confirm(text=check, title='your_select_check', buttons=["YES", "NO"])
    if company_check == "NO":
        company_sel()
    elif company_check == None:
        sys.exit()
    return company

def start_date_sel():
    start_date = pg.prompt(text="START_DATE ex)20220101 ", title="start_date_select", default="")
    if start_date != None:
        if len(start_date) == 8 and start_date.isdigit():
            return str(start_date)
        else:
            start_date_sel()
    elif start_date == None:
        sys.exit()
    else:
        start_date_sel()

def end_date_sel():
    end_date = pg.prompt(text="END_DATE ex)20220101 ", title="end_date_select", default="")
    if end_date != None:
        if len(end_date) == 8 and end_date.isdigit():
            return str(end_date)
        else:
            end_date_sel()
    elif end_date == None:
        sys.exit()
    else:
        end_date_sel()

def last_check(company, start_date, end_date):
    strat_date_edit = f"{start_date[0:4]}-{start_date[4:6]}-{start_date[6:8]}"
    end_date_edit = f"{end_date[0:4]}-{end_date[4:6]}-{end_date[6:8]}"
    check = f"YOUR_SELECT\nCOMPANY : {company}\nSTART DATE : {strat_date_edit}\nEND DATE : {end_date_edit}"
    company_check = pg.confirm(text=check, title='your_select_check', buttons=["YES", "NO"])
    user_seleect = [company,start_date,end_date]
    return user_seleect

def date_range(start, end):
    start = datetime.strptime(start, "%Y%m%d")
    end = datetime.strptime(end, "%Y%m%d")
    dates = [date.strftime("%Y%m%d") for date in pandas.date_range(start, periods=(end-start).days+1)]
    return dates