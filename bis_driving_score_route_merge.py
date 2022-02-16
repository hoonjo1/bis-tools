import pandas as pd
from route_id import *
from route_name import *


def bis_driving_score_route_merge_f(company, dates):

    if company == "경진여객":
        route_ids = kj_route_id
        route_names = kj_route_name

    elif company == "용남고속":
        route_ids = yn_route_id
        route_names = yn_route_name
    
    elif company == "제부여객":
        route_ids = jb_route_id
        route_names = jb_route_name
    
    elif company =="ALL":
        route_ids = all_route_id
        route_names = all_route_name

    for route_id, route_name in zip(route_ids, route_names):
        result_list = list()
        for date in dates:
            print(f"{route_id}_{route_name}_{date} 진행")
            read_data = pd.read_csv(rf"\\kjnas\KJNAS\1.기획부\9.개발팀\BIS_DRIVING_SCORE_EDIT\{route_id}_{route_name}_{date}_운행기록표.csv", encoding="euc-kr", header=4)
            read_data = read_data.iloc[:, 3:]

            date_list = []
            round_list = []
            route_name_list = []

            for date_len in range(len(read_data)):
                date_list.append(date)
                round_list.append(date_len+1)
                route_name_list.append(route_name)
            
            read_data.insert(0, "날짜", date_list)
            read_data.insert(1, "회수", round_list)
            read_data.insert(2, "노선", route_name + "번")

            result_list.append(read_data)
            result = pd.concat(result_list)


            start_date_name = dates[0]
            end_date_name = dates[-1]
            result.to_csv(rf"\\kjnas\KJNAS\1.기획부\9.개발팀\BIS_DRIVING_SCORE_ROUTE_MERGE\{start_date_name}_{end_date_name}_{route_id}_{route_name}_운행기록표.csv", encoding="euc-kr")
    print("ALL_COMPLETE")