def meal_time(time_12h):
    
    time, period = time_12h.strip().split()
    hour_str, minute_str = time.split(':')

    hour = int(hour_str)
    minute = int(minute_str)

    
    if period.upper() == 'AM':
        if hour == 12:
            hour = 0
    else:  
        if hour != 12:
            hour += 12

    
    decimal_time = hour + minute / 60

    
    if 7 <= decimal_time <= 9:
        return "Breakfast"
    elif 18 <= decimal_time <= 19:
        return "Lunch"
    else:
        return  'Dinner'
time_input = input("What time is it? ")
print(meal_time(time_input))
