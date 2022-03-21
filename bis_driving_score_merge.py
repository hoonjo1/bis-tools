import pandas as pd
import datetime as dt
from route_id import *
from route_name import *
from route_name_set import *

def bis_driving_score_merge_f(company,dates):

    result_list = list()

    if company == "경진여객":
        route_ids = kj_route_id
        route_names = kj_route_name
        route_name_sets = kj_route_name_set
        read_driver_id = pd.read_csv(rf"\\kjnas\KJNAS\1.기획부\9.개발팀\ERP_DRIVER_ID\driver_id_kj.csv", encoding="euc-kr")[["성명", "운전자ID"]]
    elif company == "용남고속":
        route_ids = yn_route_id
        route_names = yn_route_name
        route_name_sets = yn_route_name_set
        read_driver_id = pd.read_csv(rf"\\kjnas\KJNAS\1.기획부\9.개발팀\ERP_DRIVER_ID\driver_id_yn.csv", encoding="euc-kr")[["성명", "운전자ID"]]
    elif company == "제부여객":
        route_ids = jb_route_id
        route_names = jb_route_name
        route_name_sets = jb_route_name_set
        read_driver_id = pd.read_csv(rf"\\kjnas\KJNAS\1.기획부\9.개발팀\ERP_DRIVER_ID\driver_id_jb.csv", encoding="euc-kr")[["성명", "운전자ID"]]
    elif company =="ALL":
        route_ids = all_route_id
        route_names = all_route_name
        route_name_sets = all_route_name_set
        read_driver_kj_id = pd.read_csv(rf"\\kjnas\KJNAS\1.기획부\9.개발팀\ERP_DRIVER_ID\driver_id_kj.csv", encoding="euc-kr")[["성명", "운전자ID"]]
        read_driver_yn_id = pd.read_csv(rf"\\kjnas\KJNAS\1.기획부\9.개발팀\ERP_DRIVER_ID\driver_id_yn.csv", encoding="euc-kr")[["성명", "운전자ID"]]
        read_driver_jb_id = pd.read_csv(rf"\\kjnas\KJNAS\1.기획부\9.개발팀\ERP_DRIVER_ID\driver_id_jb.csv", encoding="euc-kr")[["성명", "운전자ID"]]
        read_driver_id = pd.concat([read_driver_kj_id, read_driver_yn_id, read_driver_jb_id], axis = 0)

    for date in dates:
        try:
            for route_id, route_name, c in zip(route_ids, route_names, route_name_sets):
                read_data = pd.read_csv(rf"\\kjnas\KJNAS\1.기획부\9.개발팀\BIS_DRIVING_SCORE_EDIT\{route_id}_{route_name}_{date}_운행기록표.csv", header=4, encoding="euc-kr")
                iloc_data = read_data.iloc[:,1:13]
                iloc_data.columns = ["날짜", "노선번호", "차량번호", "운행회차", "운전자ID", "운행시간_분", "운행시작시간", "운행종료시간", "검지수", "수집률", "운행거리_KM", "비고"]
                del_unnecessary_data = iloc_data[iloc_data.운행회차 !=" "]

                start_time = del_unnecessary_data["운행시작시간"]
                end_time = del_unnecessary_data["운행종료시간"]
                start_time_edit = start_time.str.split(":")
                end_time_edit = end_time.str.split(":")

                time_list = list()

                for start, end in zip(start_time_edit, end_time_edit):
                    start_time_hour = start[0]
                    start_time_minute = start[1]
                    start_time_second = start[2]
                    end_time_hour = end[0] 
                    end_time_minute = end[1]
                    end_time_second = end[2]
                    start_time_read = dt.datetime(year=1900, month=1, day=1,  hour=int(start_time_hour), minute=int(start_time_minute), second=int(start_time_second))
                    end_time_read = dt.datetime(year=1900, month=1, day=1,  hour=int(end_time_hour), minute=int(end_time_minute), second=int(end_time_second))
                    time_calculation = (end_time_read - start_time_read).total_seconds() 
                    time_calculation_edit = time_calculation + 60 * 60 * 24 if time_calculation < 0 else time_calculation
                    time_calculation_set = (f"{dt.timedelta(seconds=time_calculation_edit)}")
                    time_list.append(time_calculation_set)

                del_unnecessary_data.insert(8,"운행시간",time_list)

                merge_data = pd.merge(del_unnecessary_data, read_driver_id, how="left", on="운전자ID")
                reindex_data = merge_data.reindex(columns = ["날짜", "노선번호", "차량번호", "운행회차", "운전자ID", "성명", "운행시간_분", "운행시작시간", "운행종료시간", "운행시간","검지수","수집률", "운행거리_KM", "비고"])
                result_list.append(reindex_data)
                print(f"COMPLETE__{route_id}_{route_name}_{date}_운행기록표")
        except:
            pass

    result = pd.concat(result_list)

    start_date_name = dates[0]
    end_date_name = dates[-1]
    result.to_csv(rf"\\kjnas\KJNAS\1.기획부\9.개발팀\BIS_DRIVING_DATA_MERGE\{company}_{start_date_name}_{end_date_name}_운행기록표.csv", encoding="euc-kr")
    print("ALL_COMPLETE")