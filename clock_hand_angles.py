def clock_hand_angles(seconds):

    my_hours = round(float(seconds)/float(3600), 8)
    my_minutes = round(float(seconds)/float(60), 8)
    my_dict = {
        'hours': my_hours,
        'minutes': my_minutes,
        'seconds': seconds 
    }
    print(my_dict)
    if seconds >= 43200:
        new_seconds = seconds % 43200
        hour_angle = float(new_seconds) / float(43200) * 360
    else:
        hour_angle = float(seconds) / float(43200) * 360
    if seconds >= 3600:
        new_seconds = seconds % 3600
        minute_angle = float(new_seconds) / float(3600) * 360
    else:
        minute_angle = float(seconds) / float(3600) * 360
    if seconds >= 60:
        new_seconds = seconds % 60
        second_angle = float(new_seconds) / float(60) * 360
    else:
        second_angle = float(seconds) / float(60) * 360
    
    my_angles = {
        'hour_angle': hour_angle,
        'minute_angle': minute_angle,
        'second_angle': second_angle

    }
    
    print(my_angles)

clock_hand_angles(11745)