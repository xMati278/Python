def clock_angle(hour: int, minutes: int):

    angle = abs(((360/12)*hour) - ((360/60)*minutes)) - ((360/12)*(minutes/60))

    print(f'Angle between hands at {hour}:{minutes} o\'clock is: {angle}°')


hour_input = int(input("Enter hour: "))
minutes_input = int(input("Enter minutes: "))

if (0 <= hour_input <= 24) and (0 <= minutes_input <= 59):
    if hour_input >= 12:
        hour_input = hour_input % 12
    clock_angle(hour_input, minutes_input)

else:
    print("You entered an incorrect time.")