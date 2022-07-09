import train_routines

quantity_trains_in_week = 3
weeks_for_training = 12
weekly_distance = 23
week_number = 12

train_phases = train_routines.calculate_train_phases(weeks_for_training)
weekly_plan = train_routines.create_week_plan(week_number,\
                                              weekly_distance,\
                                              quantity_trains_in_week,\
                                              train_phases)

print(weekly_plan)
