import pandas as pd
from route_id import *
from route_name import *
from route_name_set import *


def bis_driving_score_edit_f(company,dates):

    if company == "경진여객":
        route_ids = kj_route_id
        route_names = kj_route_name
        route_name_sets = kj_route_name_set
    elif company == "용남고속":
        route_ids = yn_route_id
        route_names = yn_route_name
        route_name_sets = yn_route_name_set
    elif company == "제부여객":
        route_ids = jb_route_id
        route_names = jb_route_name
        route_name_sets = jb_route_name_set
    elif company =="ALL":
        route_ids = all_route_id
        route_names = all_route_name
        route_name_sets = all_route_name_set

    for date in dates:
        for route_id, route_name, route_name_set in zip(route_ids, route_names, route_name_sets):
            try:
                read_data = pd.read_csv(rf"\\kjnas\KJNAS\1.기획부\9.개발팀\BIS_DRIVING_SCORE\{route_id}_{route_name}_{date}_운행기록표.csv", encoding="euc-kr", header=None)
                read_data_transpose = read_data.transpose()

                read_date_len = []
                read_route_len = []
                for date_len in range(len(read_data_transpose)):
                    read_date_len.append(f"{date}")
                    read_route_len.append(route_name)
                read_data_transpose.insert(0, "날짜", read_date_len)
                read_data_transpose.insert(1, "노선", route_name_set)
                read_data_transpose.to_csv(rf"\\kjnas\KJNAS\1.기획부\9.개발팀\BIS_DRIVING_SCORE_EDIT\{route_id}_{route_name}_{date}_운행기록표.csv", encoding="euc-kr")
                print(f"COMPLETE__{route_id}_{route_name}_{date}_운행기록표")
            except:
                print(f"ERROR_____{route_id}_{route_name}_{date}_운행기록표")

    print("ALL_COMPLETE")