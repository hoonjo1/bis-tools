import pandas as pd

bis_data = ["경진여객_20220201_20220228_운행기록표"]

read_erp_data = pd.read_csv(rf"\\kjnas\KJNAS\1.기획부\9.개발팀\BIS_DRIVING_SCORE_ERP_MERGE\check_3.csv", encoding="euc-kr")

data = list()


for i in bis_data:
    read_bis_data = pd.read_csv(rf"\\kjnas\KJNAS\1.기획부\9.개발팀\BIS_DRIVING_DATA_MERGE\{i}.csv", encoding="euc-kr")

    data.append(read_bis_data)

    result = pd.concat(data)


merge_data = pd.merge(result, read_erp_data, how="left", on=["노선번호","날짜","차량번호"])

merge_data.to_csv("test.csv", encoding="euc-kr")