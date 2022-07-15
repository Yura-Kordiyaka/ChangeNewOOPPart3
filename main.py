from user_functions import *
from UserApp import userApp

while True:
    print("1. Add New User\n"
          + "2. Get All Users\n"
          + "3. Search\n"
          + "4. Update User By Id"
          )
    menu_flag = int(input("Type your choose: "))
    if menu_flag == 1:
        first_name = input("First Name: ")
        last_name = input("Last Name: ")
        Email = input("Email: ")
        f = userApp(first_name, last_name, Email)
        user = {
            "first_name": first_name,
            "last_name": last_name,
            "Email": Email,
        }
        f.user_add(user)
    elif menu_flag == 2:
        f = userApp.get_all()
    elif menu_flag == 3:
        what_to_search = input('By Which Parametr you want to search: ')
        search_str = input('Search: ')
        f = userApp.search_by(search_str, what_to_search)
    #   search_by(search_str, what_to_search)
    elif menu_flag == 4:
        f = userApp.update_user()
