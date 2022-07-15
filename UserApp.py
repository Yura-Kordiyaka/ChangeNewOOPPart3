import json

from user_functions import check_email




class userApp():
    def __init__(self, first_name, last_name, Email):
        self.first_name = first_name
        self.last_name = last_name
        self.Email = Email

    def check_email(self, email, all_users_data):
        for user in all_users_data:
            if email == user['Email']:
                return True
        return False

    def user_add(self, user):
        file = open('database/users.json', 'r')
        all_users_data_json = file.read()
        all_users_data = json.loads(all_users_data_json)
        file.close()
        if len(all_users_data) > 0:
            user['id'] = all_users_data[-1]['id'] + 1
        else:
            user['id'] = 1
        if check_email(user['Email'], all_users_data) == False:
            all_users_data.append(user)
            with open('database/users.json', 'w') as file:
                file.write(json.dumps(all_users_data))
        else:
            print("User with this email already exist!!!")

    @staticmethod
    def get_all():
        with open('database/users.json', 'r') as file:
            users = json.loads(file.read())
            for user in users:
                print("User #" + str(user['id']))
                print("First Name: " + user['first_name'])
                print("Last Name: " + user['last_name'])
                print("Email: " + user['Email'])

    def search_by(self, search_str, what_to_search):
        with open('database/users.json', 'r') as file:
            users = json.loads(file.read())
            for user in users:
                if str(user[what_to_search]).lower() == str(search_str).lower():
                    print("User #" + str(user['id']))
                    print("First Name: " + user['first_name'])
                    print("Last Name: " + user['last_name'])
                    print("Email: " + user['Email'])

    @staticmethod
    def update_user():
        file = open('database/users.json', 'r')
        users = json.loads(file.read())
        file.close()
        id = int(input("Type id of user which you want to update: "))
        first_name = input("First Name: ")
        last_name = input("Last Name: ")
        email = input("Email: ")
        for user in users:
            if user['id'] == id:
                user['first_name'] = first_name
                user['last_name'] = last_name
                user['Email'] = email

        with open('database/users.json', 'w') as file:
            file.write(json.dumps(users))
