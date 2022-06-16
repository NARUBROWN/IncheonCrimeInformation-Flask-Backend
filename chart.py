import pandas as pd
import matplotlib.pyplot as plt

crimeType = []
occur = []


def crime_chart(data_name):
    df = pd.read_csv('data/crime/' + data_name + '.csv')

    for name in df['type']:
        crimeType.append(name)

    for value in df['occur']:
        occur.append(value)

    plt.rcParams['font.family'] = 'AppleGothic'
    plt.plot(crimeType, occur, 'bo--')
    plt.xlabel('범죄유형')
    plt.ylabel('발생건수')
    plt.title(data_name + ' 범죄 데이터')
    plt.show()


userIn = int(input("값을 입력해주세요. 1: 부평, 2: 연수, 3: 남동, 4: 동구\n : "))

if userIn == 1:
    crime_chart("bupyeonggu")
elif userIn == 2:
    crime_chart("yeonsugu")
elif userIn == 3:
    crime_chart("namdonggu")
elif userIn == 4:
    crime_chart("donggu")
else:
    print("올바른 값을 입력해주세요")
