from completion_guide import complection
from guide_loggining import read_log_guide


def menu():
    flag = True
    while flag:
        print('Телефонный справочник')
        while True:
            print('Выберете действие:')
            print('1 - Ввести контакт')
            print('2 - Показать записи')
            print('3 - Выход')
            choice = input()
            if choice not in ['1', '2', '3']:
                print('Повторите ввод действия')
                continue
            if choice == '1':
                complection()
                break
            elif choice == '2':
                read_log_guide()
                break
            else:
                flag = False
                break


if __name__ == "__main__": # __name__ - функция, запускающая функцию "напрямую" из данного файла, а не по импорту
    menu()
