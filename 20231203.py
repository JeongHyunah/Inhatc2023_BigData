# -*- coding: utf-8 -*-
"""Untitled0.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1G57yXAlk5ON8mF68xUw2A2Mzq8vMl3pd
"""

import pandas as pd
from sklearn.linear_model import LinearRegression


# 데이터를 저장할 딕셔너리 생성
data_2021 = {}
data_2022 = {}

# 빈 리스트 생성
average_humidity_2021 = []
average_soil_moisture_2021 = []
average_temp_hourly_2021 = []
average_wind_speed_hourly_2021 = []
average_ground_temp_2021 = []
average_surface_temp_2021 = []
average_underground_temp_2021 = []

average_humidity_2022 = []
average_soil_moisture_2022 = []
average_temp_hourly_2022 = []
average_wind_speed_hourly_2022 = []
average_ground_temp_2022 = []
average_surface_temp_2022 = []
average_underground_temp_2022 = []

for year in range(2021, 2023):  # 2021과 2022년 반복
    for month in range(1, 13):  # 1부터 12까지 반복
        file_path = f'/content/data/{year}_{month}.xlsx'  # 파일 경로 설정

        # 파일 불러오기
        data = pd.read_excel(file_path)

        # 각 행에 대해 숫자로 변환하고 평균 계산 후 반올림
        avg_humidity = pd.to_numeric(data.iloc[3:5].stack(), errors='coerce').mean()
        avg_soil_moisture = pd.to_numeric(data.iloc[5:9].stack(), errors='coerce').mean()
        avg_temp_hourly = pd.to_numeric(data.iloc[9:13].stack(), errors='coerce').mean()
        avg_wind_speed_hourly = pd.to_numeric(data.iloc[12:14].stack(), errors='coerce').mean()
        avg_ground_temp = pd.to_numeric(data.iloc[14:15].stack(), errors='coerce').mean()
        avg_surface_temp = pd.to_numeric(data.iloc[15:16].stack(), errors='coerce').mean()
        avg_underground_temp = pd.to_numeric(data.iloc[16:25].stack(), errors='coerce').mean()

        # 평균 값을 반올림하여 리스트에 추가
        if year == 2021:
            average_humidity_2021.append(round(avg_humidity, 1))
            average_soil_moisture_2021.append(round(avg_soil_moisture, 1))
            average_temp_hourly_2021.append(round(avg_temp_hourly, 1))
            average_wind_speed_hourly_2021.append(round(avg_wind_speed_hourly, 1))
            average_ground_temp_2021.append(round(avg_ground_temp, 1))
            average_surface_temp_2021.append(round(avg_surface_temp, 1))
            average_underground_temp_2021.append(round(avg_underground_temp, 1))
        elif year == 2022:
            average_humidity_2022.append(round(avg_humidity, 1))
            average_soil_moisture_2022.append(round(avg_soil_moisture, 1))
            average_temp_hourly_2022.append(round(avg_temp_hourly, 1))
            average_wind_speed_hourly_2022.append(round(avg_wind_speed_hourly, 1))
            average_ground_temp_2022.append(round(avg_ground_temp, 1))
            average_surface_temp_2022.append(round(avg_surface_temp, 1))
            average_underground_temp_2022.append(round(avg_underground_temp, 1))

# 각 연도별 데이터 저장
data_2021['Average Humidity'] = average_humidity_2021
data_2021['Average Soil Moisture'] = average_soil_moisture_2021
data_2021['Average Temp Hourly'] = average_temp_hourly_2021
data_2021['Average Wind Speed Hourly'] = average_wind_speed_hourly_2021
data_2021['Average Ground Temp'] = average_ground_temp_2021
data_2021['Average Surface Temp'] = average_surface_temp_2021
data_2021['Average Underground Temp'] = average_underground_temp_2021

data_2022['Average Humidity'] = average_humidity_2022
data_2022['Average Soil Moisture'] = average_soil_moisture_2022
data_2022['Average Temp Hourly'] = average_temp_hourly_2022
data_2022['Average Wind Speed Hourly'] = average_wind_speed_hourly_2022
data_2022['Average Ground Temp'] = average_ground_temp_2022
data_2022['Average Surface Temp'] = average_surface_temp_2022
data_2022['Average Underground Temp'] = average_underground_temp_2022

# 2021년과 2022년의 데이터프레임 생성
df_2021 = pd.DataFrame(data_2021)
df_2022 = pd.DataFrame(data_2022)

# 각 연도별 총 생산량 데이터 계속
total_production_2021 = [3882000] * 12  # 2021년의 총 생산량
total_production_2022 = [3764000] * 12  # 2022년의 총 생산량

# 2021년과 2022년 데이터프레임에 각 연도별 총 생산량 추가
df_2021['Total Production'] = total_production_2021
df_2022['Total Production'] = total_production_2022

import matplotlib.pyplot as plt

# 연도별 데이터 시각화
months = range(1, 13)

# 2021년 데이터 그래프
plt.figure(figsize=(10, 6))
plt.plot(months, df_2021['Total Production'], marker='o', label='2021 Total Production')
plt.xlabel('Month')
plt.ylabel('Total Production')
plt.title('2021 Total Production per Month')
plt.xticks(months)
plt.legend()
plt.show()

# 2022년 데이터 그래프
plt.figure(figsize=(10, 6))
plt.plot(months, df_2022['Total Production'], marker='o', label='2022 Total Production')
plt.xlabel('Month')
plt.ylabel('Total Production')
plt.title('2022 Total Production per Month')
plt.xticks(months)
plt.legend()
plt.show()