'''Это дневник тренировок. сюда можно добавить тренировку и просмотреть
добавленные тренировки. Параметры тренировки: дата и сама тренировка, которая
включает в себя разминку, работу, заминку'''
def start():
    start_text = "\
    Hello! I'm your train diary. Enter number of menu:\n\
    (1) - add train\n\
    (2) - view traines\n\
    (3) - remove train\n"

    choose_menu = input(start_text)

    if choose_menu == '1':

        add_train()

    elif choose_menu == '2':

        view_train()

    elif choose_menu == '3':

        remove_train()

    else:

        start()

def add_train():
    date = input('Please enter the date train in format DD-MM-YYYY\n')
    warm_up = input('Enter your warm up\n')
    train_session = []
    recovery_session = []
    
    flag = ''
    i = 0

    while flag != 'end':

        train_session = input('Enter length of cut in secund\n')
        recovery_session = input('Enter length of recovery in secund\n')
        i +=1
        flag = input('Add new cut? Enter "end" if cuts is end')

    series = input('How many series you do?')

    

start()



