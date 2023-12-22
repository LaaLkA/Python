from functions import *


CONTACTS = 'contacts.txt'


def interface():
      while True:
            print('Выберете действие:  \
                  \n 0 - Выйти \
                  \n 1 - Добавить контакт \
                  \n 2 - Вывести все контакты \
                  \n 3 - Найти контакт')
            command = int(input())
            match command:
                  case 0: 
                        break 
                  case 1: 
                        add_contact(CONTACTS)
                  case 2:
                        print_contacts(CONTACTS)
                  case 3:
                        find_contact(CONTACTS)

if __name__ == '__main__':
      interface()     