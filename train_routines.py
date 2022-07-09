def light_run():
    return 'light_run'

def interval_training (week_distance, week_number):
    """
    Функция принимает объем в километрах прошлой недели, номер недели и возвращает
    интервальную тренировку в форме кортежа (продолжительность отрезка в мин, 
    продолжительность отдыха в мин, количество отрезков)
    """
    
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

def repeat_training (week_distance, week_number):
    """
    Функция принимает объем в километрах прошлой недели, номер недели и возвращает
    повторную тренировку в форме кортежа (продолжительность отрезка в мин, 
    продолжительность отдыха в мин, количество отрезков)
    """
    repeat_value = week_distance * 0.05

    length_lap_minutes = 0.5
    length_lap_kilometres = 0.2
    count_repeat = int(repeat_value / length_lap_kilometres)
    repeat_recovery = length_lap_minutes * 3

    train = (length_lap_minutes, repeat_recovery, count_repeat)
    return train 

def tempo_training(week_distance, week_number):

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
        count_tempo = int(tempo_value / length_lap_kilometres)

    train = (length_lap_minutes, tempo_recovery, count_tempo)
    
    return train

def increase_week_distance(week_distance, week_number):

    previous_week_distance = week_distance
    new_week_distance = previous_week_distance * 1.1
    
    return new_week_distance

'''def get_week_trainday(train_in_week, week_number):

    if train_in_week == 3:
        first_train = train_T1
        second_train = train_T2
       
        if week_number % 2 == 0:
            third_train = 'light_run'
        else:
            third_train = train_T3

    return (first_train, second_train, third_train)


    if train_in_week == 4:
        first_train = train_T1
        second_train = 'light_run'
        third_train = train_T2
        if week_number % 2 == 0:
            fourth_train = 'long_run'
        else:
            fourth_train = train_T3
       
    return (first_train, second_train, third_train, fourth_train)'''

def calculate_train_phases(week_for_train):

    phase_1 = [1, 2, 3, 13, 21, 23]
    phase_2 = [10, 11, 12, 18, 19, 22]
    phase_3 = [7, 8 ,9, 14, 15, 16]
    phase_4 = [4, 5, 6, 17, 22, 24]

    
    train_weeks = []
    for week in range(1, week_for_train + 1):
        train_weeks.append(week)

    current_phase_1 = 0
    current_phase_2 = 0
    current_phase_3 = 0
    current_phase_4 = 0

    for i in phase_1:
        for j in train_weeks:
            if i == j:
                current_phase_1 += 1

    for i in phase_2:
        for j in train_weeks:
            if i == j:
                current_phase_2 += 1

    for i in phase_3:
        for j in train_weeks:
            if i == j:
                current_phase_3 += 1

    for i in phase_4:
        for j in train_weeks:
            if i == j:
                current_phase_4 += 1

    train_phases = (current_phase_1, current_phase_2, current_phase_3, current_phase_4)
     
    return train_phases

def create_week_plan(week_number, week_distance, train_in_week, train_phases):

    if week_number <= train_phases[0]:
        train_T1 = light_run()
        train_T2 = light_run()
        train_T3 = light_run()
    elif week_number <= train_phases[0] + train_phases[1]:
        train_T1 = repeat_training(week_distance, week_number)
        train_T2 = interval_training(week_distance, week_number)
        train_T3 = tempo_training(week_distance, week_number)

    elif week_number <= train_phases[0] + train_phases[1] + train_phases[2]:
        train_T1 = interval_training(week_distance, week_number) 
        train_T2 = repeat_training(week_distance, week_number)
        train_T3 = tempo_training(week_distance, week_number)

    elif week_number <= train_phases[0] + train_phases[1] + train_phases[2] + train_phases[3]:
        train_T1 = repeat_training(week_distance, week_number) 
        train_T2 = tempo_training(week_distance, week_number) 
        train_T3 = interval_training(week_distance, week_number)

    if train_in_week == 3:
        first_train = train_T1
        second_train = train_T2
       
        if week_number % 2 == 0:
            third_train = light_run()
        else:
            third_train = train_T3

    return (first_train, second_train, third_train)


    if train_in_week == 4:
        first_train = train_T1
        second_train = light_run()
        third_train = train_T2
        if week_number % 2 == 0:
            fourth_train = 'long_run'
        else:
            fourth_train = train_T3
       
    return (first_train, second_train, third_train, fourth_train)
   







