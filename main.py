def add_time(start, duration, day=None):
    days_of_week = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    start_time, period = start.split()
    start_hour, start_minute = map(int, start_time.split(':'))
    duration_hour, duration_minute = map(int, duration.split(':'))

    if period == 'PM':
        start_hour += 12
    total_minutes = start_hour * 60 + start_minute + duration_hour * 60 + duration_minute
    new_hour = (total_minutes // 60) % 24
    new_minute = total_minutes % 60
    days_later = total_minutes // (60 * 24)

    if new_hour >= 12:
        period = 'PM'
        if new_hour > 12:
            new_hour -= 12
    else:
        period = 'AM'
        if new_hour == 0:
            new_hour = 12

    new_time = f"{new_hour}:{new_minute:02d} {period}"

    if day:
        day_index = days_of_week.index(day.lower())
        new_day_index = (day_index + days_later) % 7
        new_day = days_of_week[new_day_index].capitalize()
        new_time += f", {new_day}"

    if days_later == 1:
        new_time += " (next day)"
    elif days_later > 1:
        new_time += f" ({days_later} days later)"

    return new_time