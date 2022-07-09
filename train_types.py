def interval_training (week_distance, week_time_training, week_number):

    #Посчитать общий объем интервальной тренировки
    interval_value = week_distance * 0.08

    if week_number % 2 == 0:
        length_lap_minutes = 3
        length_lap_kilometres = 1
        count_intervals = int(interval_value / length_lap_kilometres)
        interval_recovery = length_lap_minutes

    elif week_number % 3 == 0:
        length_lap_minutes = 4
        length_lap_kilometres = 1.5
        count_intervals = int(interval_value / length_lap_kilometres)
        interval_recovery = length_lap_minutes

    else:
        length_lap_minutes = 1
        length_lap_kilometres = 0.4
        count_intervals = int(interval_value / length_lap_kilometres)
        interval_recovery = length_lap_minutes

    #Сформировать кортеж
    train = (length_lap_minutes, interval_recovery, count_intervals )
    return train

def repeat_training (week_distance, week_time_training, week_number):

    repeat_value = week_distance * 0.05

    length_lap_minutes = 0.5
    length_lap_kilometres = 0.2
    count_repeat = int(repeat_value / length_lap_kilometres)
    repeat_recovery = length_lap_minutes * 3

    train = (length_lap_minutes, repeat_recovery, count_repeat)
    return train 

def tempo_training(week_distance, week_time_training, week_number):

    tempo_value = week_distance * 0.08

    if week_number % 2 == 0:
        length_lap_minutes = 20
        tempo_recovery = 0
        count_tempo = 1

        train = (length_lap_minutes, tempo_recovery, count_tempo)

    else:
        length_lap_kilometres = 1
        length_lap_minutes = 4
        tempo_recovery = length_lap_minutes * 0.25
        count_tempo = tempo_value / length_lap_kilometres

    train = (length_lap_minutes, tempo_recovery, count_tempo)
    return train

