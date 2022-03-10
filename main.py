import sys
import os
from UserInformation import UserFactory
from pymongo import MongoClient
from migrations import db_insert, get_all_collection


def create_email(first_name, last_name,client):
    """
    Given a first and last name, create an email for the user
    """
    DB_NAME = os.environ["DB_NAME"]
    user = UserFactory(first=first_name, last=last_name)
    db_insert("USERS",user.to_dict(), DB_NAME, client=client)
    print(f'Creating user {user}...')

def display_plans(memberships):
    """
    Take a list of memberships and displays them to the user
    """
    print('Memberships:')
    for i in memberships:
        print('\t', i)
    return
def main():
    client = MongoClient(os.environ["DB_URL"])
    arg = sys.argv[1:]
    if len(arg) > 0 and arg[0] == 'list-memberships':
        return display_plans(arg[1:])
    elif arg[0] == 'create-email':
        return create_email(arg[1], arg[2])
    elif arg[0] == 'list-users':
        for user in get_all_collection("USERS", os.environ["DB_NAME"], client=client):
            print(user)
        return
    else:
        raise Exception("Invalid Request.")
        

if __name__ == '__main__':
    main()