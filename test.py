import train_routines


quantity_trains_in_week = 3  #Количество тренировок в неделю(на данный момент работает только для 3 в неделю)
weeks_for_training = 24      #Количество недель для тренировок(от 3 до 24)
weekly_distance = 23         #Километраж прошлой недели
week_number = 24              #Номер недели(для тренировок в первой(базовой фазе работает некорректно))

train_phases = train_routines.calculate_train_phases(weeks_for_training)
weekly_plan = train_routines.create_week_plan(week_number,\
                                              weekly_distance,\
                                              quantity_trains_in_week,\
                                              train_phases)

#В выводе указываются кортежи формата: (дистанция в минутах, отдых в минутах, количество отрезков)
print(weekly_plan)
