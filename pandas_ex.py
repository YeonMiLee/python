import pandas as pd
pd.__version__
data1 = [10, 20, 30, 40, 50]
data2 = ['1반', '2반', '3반', '4반', '5반']
sr1 = pd.Series(data1)
sr1
sr2 = pd.Series(data2)
sr2
sr3 = pd.Series([101, 102, 103, 104, 105])
sr3
sr4 = pd.Series(['월', '화', '수', '목', '금'])
sr4
sr5 = pd.Series(data1, index = [1000, 1001, 1002, 1003, 1004])
sr5
sr6 = pd.Series(data1, index = data2)
sr6
sr8 = pd.Series(data2, index = sr4)
sr8
sr8[2]
sr8['수']
sr8[-1]
sr8[0:4]
sr8.values
sr1 + sr3
sr4 + sr2


import pandas as pd
data_dic = {
  'year': [2018, 2019, 2020],
  'sales': [350, 480 ,1099]
}
data_dic
df1 = pd.DataFrame(data_dic)
df1

df2 = pd.DataFrame([[89.2, 92.5, 90.8], [92.8, 89.9, 95.2]],
              index = ['중간고사', '기말고사'], columns = data2[0:3])
df2

data_df = [['20201102', 'Hong', '90', '95'], ['20201102', 'Kim', '93', '94'], ['20201103', 'Lee', '87', '97']]
df3 = pd.DataFrame(data_df)
df3
df3.columns = ['학번', '이름', '중간고사', '기말고사']
df3.head(2)
df3.tail(2)
df3['이름']


data = {
  "2015": [9904312, 3448737, 2890451, 2466052],
  "2010": [9631482, 3393191, 2632035, 2431774], 
  "2005": [9762546, 3512547, 2517680, 2456016], 
  "2000": [9853972, 3655437, 2466338, 2473990],
  "지역": ["수도권", "경상권", "수도권", "경상권"],
  "2010-2015 증가율": [0.0283, 0.0163, 0.0982, 0.0141]
}
columns = ["지역", "2015", "2010", "2005", "2000", "2010-2015 증가율"]
index = ["서울", "부산", "인천", "대구"]
df = pd.DataFrame(data, index=index,columns=columns)
df

df.values
df.index
df.index.name = "도시"
df.columns.name = "특성"
df

# "2010-2015증가율"이라는 이름의 열 갱신
df["2010-2015 증가율"] = df["2010-2015 증가율"] * 100
df

# "2010-2015증가율"이라는 이름의 열 추가
df["2010-2015 증가율"] = ((df["2010"] - df["2005"]) / df["2005"] * 100).round(2)
df

# 2010이라는 열을 반환하면서 데이터프레임 자료형을 유지
df[["2010"]]
type(df[["2010"]])

# 여러개의 열을 인덱싱하면 부분적인 데이터프레임이 반환된다
df[["2010", "2015"]]

#"2010-2015 증가율"이라는 이름의 열 삭제
del df["2010-2015 증가율"]
df

# 데이터프레임은 전치(transpose)를 포함하여 넘파이 2차원 배열이 가지는 대부분의 속성이나 메서드 지원
df.T        # 행과 열이 바뀜
df[0]
df4 = pd.DataFrame([[89.8, 92.5, 90.8], [92.8, 89.9, 95.2]])
df4[2]

# 행 단위로 인덱싱을 하고자 하면 항상 슬라이싱
df[:1]
df[1:2]
df["서울":"부산"]

# 개별 데이터 인덱싱
df["2015"]["서울"]

# csv 파일 생성
df.to_csv('c:/workspace/score.csv', header = 'False')

# csv 파일 로드
df5 = pd.read_csv('c:/workspace/score.csv', encoding='utf-8', index_col=0, engine='python')
df5