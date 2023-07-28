weekDays = {1: "Monday", 2: "Tuesday", 3: "Wednesday", 4: "Thursday", 5: "Friday", 6: "Saturday", 7: "Sunday"}

dayNumber = int(input("Enter the day number: "))
no_day = 'There is no such day'

print(weekDays.get(dayNumber, no_day))