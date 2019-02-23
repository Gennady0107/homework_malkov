l_100km = int(input("Введите расход л/100км "))
fuel_residue = int(input("Введите количество топлива в баке "))
fuel_left_for_km= fuel_residue / l_100km * 100
print(int(fuel_left_for_km))