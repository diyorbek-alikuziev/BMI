print("BMI haqida ma'lumot olish uchun marhamat!")

weight = float(input("Vazningizni kiriting (kg): "))
height = float(input("Bo'yingizni kiriting (m): "))

bmi = round(weight / (height**2), 1)

if bmi < 18.5:
  print(f"Sizning BMI ko'rsatgichingiz {bmi}, siz yengil vaznli ekansiz!")
elif bmi < 25:
  print(f"Sizning BMI ko'rsatgichingiz {bmi}, siz normal vaznli ekansiz!")
elif bmi < 30:
  print(f"Sizning BMI ko'rsatgichingiz {bmi}, siz biroz semiz ekansiz!")
elif bmi < 35:
  print(f"Sizning BMI ko'rsatgichingiz {bmi}, siz semiz ekansiz!")
else:
  print(f"Sizning BMI ko'rsatgichingiz {bmi}, siz haddan tashqari semiz ekansiz!")
