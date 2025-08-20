import holidays

#
# def get_holidays(country, year):
#     return holidays.CountryHoliday(country, years=year)
#
# feriados = get_holidays("CR", 2024)
# print(feriados)

feriadis_CR = holidays.CostaRica(years=2025)
print("Los feriados de Costa Rica en 2024 son:")

for date, name in sorted(feriadis_CR.items()):
    dia_semana = date.strftime("%A")
    print(f"{date}: {name} ({dia_semana})")