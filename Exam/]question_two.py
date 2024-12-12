## 2.(i)
student_name = "Gloria Arinda"
student_number = "SEP23/BCS/088U/F"
programming = 90
data_science = 87
computer_applications = 77
sum = 0
result = sum+(programming+data_science+computer_applications)
print(result)


## 2.(ii)

milesdriven = int(input("Enter the number of milesdriven"))
gallonsused = int(input("Enter the number of gallonsused"))
miles_per_gallons_used = milesdriven/gallonsused
print(miles_per_gallons_used)

## 2.(iii)
def numbers_not_divisable_by_2():
    for x in range (1,101):
        if x % 2:
         print(x)
numbers_not_divisable_by_2()