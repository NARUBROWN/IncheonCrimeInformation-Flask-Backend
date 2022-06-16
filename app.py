import pandas as pd
from datetime import datetime
from flask import Flask, jsonify
from flask_cors import CORS

# cctv csv 로드
cctv_df = pd.read_csv("data/cctv/municipality_cctv.csv")
# people csv 로드
people_df = pd.read_csv("data/people/all_people.csv")
# crime csv 로드
crime_df = pd.read_csv("data/crime/crime_status.csv")

people = []


def person_cctv_num():
    # 인구당 (1000명당) CCTV 설치 대수를 구하여 person_cctv_num_result에 리스트로 저장
    cctv = []
    person_cctv_num_result = []
    for i in range(len(cctv_df)):
        cctv.append(cctv_df.loc[i][1])
        people.append(people_df.loc[i][1])
    for a in range(len(cctv)):
        first = cctv[a]
        second = people[a]
        result = first / second * 1000
        # 2번째 까지 반 올림
        person_cctv_num_result.append(round(result, 2))
    return person_cctv_num_result


print(f'인구당 (1000명당) CCTV 설치 대수 {person_cctv_num()}')


def person_crime_status():
    # 인구당 (1000명당) 범죄 발생률
    crime = []
    person_crime_num_result = []
    for i in range(len(people_df)):
        crime.append(crime_df.loc[i][1])
    for a in range(len(crime)):
        first = crime[a]
        second = people[a]
        result = first / second * 1000
        person_crime_num_result.append(round(result, 2))
    return person_crime_num_result


print(f'인구당 (1000명당) 범죄 발생률 {person_crime_status()}')

cctv_result = person_cctv_num()
danger_result = person_crime_status()
final_result = []
nowDate = f"{datetime.now()}"
for i in range(len(cctv_df.index)):
    final_result.append(
        {'average_danger': danger_result[i], 'cctv_num': cctv_result[i], 'municipality': people_df.loc[i][0],
         'danger_year': int(crime_df.loc[i][2]), 'cctv_year': int(cctv_df.loc[i][2])})

# with open(f'{nowDate[0:10]}_{nowDate[11:16]}_result.json', 'w', encoding='utf8') as outfile:
#   json_file = json.dumps(final_result, indent=4, sort_keys=True, ensure_ascii=False)
#   outfile.write(json_file)

app = Flask(__name__)
CORS(app)

@app.route('/data', methods=['GET'])  # test api
def post_echo_call():
    param = final_result
    return jsonify(param)


if __name__ == "__main__":
    app.run()
    app.run(host='localhost', port=5000)
