def print_contacts(file_name):
      with open(file_name, 'r', encoding='utf8') as file:
            all_contacts = file.readlines()
            if len(all_contacts) != 0:
                  for line in all_contacts:
                        print(line.strip(), end='\n\n')
            else:
                  print('Список контактов пуст')

def connect_with_user():
      print('Введите имя, фамилию и телефон (например: Иванов Иван 89993330011): ')
      contact = input()
      return contact

def add_contact(file_name):
      with open(file_name, 'r', encoding='utf8') as file:
            all_cont = file.readlines()
      new_cont = connect_with_user()
      all_cont.append('\n' + new_cont)
      with open(file_name, 'w', encoding='utf8') as file:
            file.writelines(all_cont)

def find_contact(file_name):
      with open(file_name, 'r', encoding='utf8') as file:
            all_cont = file.readlines()
      print("""
      Выберите критерий для поиска:
      1 - Фамилия 
      2 - Имя
      3 - Номер телефона
      """)
      comm = int(input())
      
      print('Введите данные для поиска: ')
      data = input()
      
      for cont in all_cont:
            cont_as_list = cont.strip().split()
            if cont_as_list[comm - 1] == data:
                  print('Найденные контакты: ')
                  print(*cont_as_list)
