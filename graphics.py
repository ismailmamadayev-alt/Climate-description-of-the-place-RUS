import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress

# 1. Загрузка данных из файла
file_path = r'C:\Users\Ismail\Downloads\Nurtuhan3.xlsx'
df_all = pd.read_excel(file_path, sheet_name='ALL')
df_years = pd.read_excel(file_path, sheet_name='YEARS')
df_months = pd.read_excel(file_path, sheet_name='MONTHS')

# Настройка индексов для месяцев
df_months.set_index('Unnamed: 0', inplace=True)
months_labels = ['Янв', 'Фев', 'Мар', 'Апр', 'Май', 'Июн', 'Июл', 'Авг', 'Сен', 'Окт', 'Ноя', 'Дек']

# --- РАСЧЕТЫ (Разделы 3, 4, 5) ---
# Среднегодовая температура и амплитуда
mean_annual_temp = df_years['TAVE'].mean()
amp_temp = df_months['TAVE'].max() - df_months['TAVE'].min()
abs_max_t = df_all['TMAX'].max()
abs_min_t = df_all['TMIN'].min()

# Осадки
annual_precip = df_years['PAVE'].mean()

# Тренды и дисперсия (1991-2020)
var_t = df_years['TAVE'].var()
var_p = df_years['PAVE'].var()
slope_t, intercept_t, r_t, p_t, std_err_t = linregress(df_years['Unnamed: 0'], df_years['TAVE'])
slope_p, intercept_p, r_p, p_p, std_err_p = linregress(df_years['Unnamed: 0'], df_years['PAVE'])

# Вывод статистики в консоль
print(f"Среднегодовая температура: {mean_annual_temp:.1f} °C")
print(f"Амплитуда температур: {amp_temp:.1f} °C")
print(f"Абс. макс (ср. мес): {abs_max_t:.1f} °C, Абс. мин: {abs_min_t:.1f} °C")
print(f"Годовая сумма осадков: {annual_precip:.0f} мм")
print(f"Тренд температуры: {slope_t:.4f} °C/год, Дисперсия: {var_t:.2f}")
print(f"Тренд осадков: {slope_p:.2f} мм/год, Дисперсия: {var_p:.1f}")

# --- ПОСТРОЕНИЕ ГРАФИКОВ ---
plt.rcParams.update({'font.size': 12})

# График 1: Климатограмма
fig, ax1 = plt.subplots(figsize=(10, 6))
ax2 = ax1.twinx()
ax1.bar(months_labels, df_months['PAVE'], color='skyblue', label='Осадки (мм)', alpha=0.7)
ax2.plot(months_labels, df_months['TAVE'], color='red', marker='o', label='Ср. темп. (°C)')
ax2.plot(months_labels, df_months['TMAX'], color='orange', linestyle='--', label='Макс. темп. (°C)')
ax2.plot(months_labels, df_months['TMIN'], color='blue', linestyle='--', label='Мин. темп. (°C)')
ax1.set_xlabel('Месяцы')
ax1.set_ylabel('Осадки (мм)')
ax2.set_ylabel('Температура (°C)')
ax1.set_ylim(0, df_months['PAVE'].max() * 1.5)
plt.title('Годовой ход температуры и осадков (Печора, 1991-2020)')
fig.legend(loc='upper right', bbox_to_anchor=(0.85, 0.85))
plt.grid(True, linestyle=':', alpha=0.6)
plt.show()

# График 2: Средние и максимальные осадки
fig, ax = plt.subplots(figsize=(10, 5))
ax.plot(months_labels, df_months['PAVE'], color='blue', marker='o', label='Ср. мес. осадки (мм)')
ax.plot(months_labels, df_months['PMAX'], color='red', marker='s', label='Макс. сут. осадки (мм)')
ax.set_xlabel('Месяцы')
ax.set_ylabel('Осадки (мм)')
plt.title('Годовой ход средних месячных и максимальных суточных осадков')
plt.legend()
plt.grid(True, linestyle=':', alpha=0.6)
plt.show()

# График 3: Тренд температуры
fig, ax = plt.subplots(figsize=(10, 5))
years = df_years['Unnamed: 0']
ax.plot(years, df_years['TAVE'], marker='o', color='red', label='Ср. год. температура')
ax.plot(years, intercept_t + slope_t * years, color='black', linestyle='--', label=f'Тренд: y={slope_t:.3f}x+{intercept_t:.1f}')
ax.set_xlabel('Годы')
ax.set_ylabel('Температура (°C)')
plt.title('Временная изменчивость и тренд среднегодовой температуры (1991-2020)')
plt.legend()
plt.grid(True, linestyle=':', alpha=0.6)
plt.show()

# График 4: Тренд осадков
fig, ax = plt.subplots(figsize=(10, 5))
ax.plot(years, df_years['PAVE'], marker='o', color='blue', label='Годовая сумма осадков')
ax.plot(years, intercept_p + slope_p * years, color='black', linestyle='--', label=f'Тренд: y={slope_p:.1f}x+{intercept_p:.1f}')
ax.set_xlabel('Годы')
ax.set_ylabel('Осадки (мм)')
plt.title('Временная изменчивость и тренд годовых сумм осадков (1991-2020)')
plt.legend()
plt.grid(True, linestyle=':', alpha=0.6)
plt.show()