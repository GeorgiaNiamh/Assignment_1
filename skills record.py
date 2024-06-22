
# a function that will insert the users data into the database
def insert_user(skills_record):
    firstname = input("Enter a first name: ")
    skill = input("Enter the name of the skill: ")
    level = input("Enter the level for the skill from 1 - 10 (For example: 1 = Novice, 10 = Advanced): ")
    level = int(level)
    user_info = {
        "Name": firstname,
        "Skill": skill,
        "level": level
    }
    skills_record.append(user_info)
    print(f"User {firstname} was added successfully!")

# a function that allows a user to be deleted from the database
def delete_user(skills_record, firstname):
    skills_record = [user for user in skills_record if user['Name'] != firstname]
    print(f"User {firstname} was deleted successfully from the skills database!")
    return skills_record

#a function to search for users within the database by name
def search_user(skills_record, firstname):
    results = [user for user in skills_record if user['Name']== firstname]
    return results

def showrecord(skills_record):  
    print("Current skills record contains: ")
    for user in skills_record:
        print(user)

def sort_record(old_record):
    #create an empty list called new_list
    sort_record = []
    #while old_record has items in it
    while(len(old_record) > 0):
        #iterate over old_record
        lowest_skill_index = 0
        lowest_skill_level = 9999999
        for i in range(0, len(old_record)):
            #keep track of earliest name and index
            if (old_record[i]["level"] < lowest_skill_level):
                lowest_skill_index = i
                lowest_skill_level = old_record[i]["level"]
        #pop earliest name and add to new list
        lowest_skill_person = old_record.pop(lowest_skill_index)
        sort_record.append(lowest_skill_person)
    return sort_record

#adding a navigation menu to the skills record
def main_menu():

    # create an empty list to store the users information inside
    skills_record = []

    while True:
        print("\nSkills record main menu:")
        print("\n1- Insert a user")
        print("\n2- Delete a user")
        print("\n3- Search for a user")
        print("\n4- Display the contents of the record")
        print("\n5- Sort the record based on 'skill level'")
        print("\n6- Exit the skills record")     

        choice = input("\nEnter what you want to do (1-6): ")

        if choice == '1':
            insert_user(skills_record)
        elif choice == '2':
            firstname = input("Enter the name of the user you wish to delete: ")
            skills_record = delete_user(skills_record, firstname)
        elif choice == '3':
            firstname = input("Enter the name of someone you want to search: ")
            results = search_user(skills_record, firstname)
            if results:
                print("Search results: ")
                for user in results:
                    print(user)
            else:
                print("There were no users found under that name!")
        elif choice == '4':
            showrecord(skills_record)
        elif choice == '5':
            #sorting the record
            skills_record = sort_record(skills_record)
            print("Sorted Skills Record:", skills_record)   
        elif choice == '6':
            print("Exiting the skills record....")
            break 
        else:
            print('That was an invalid choice. Please try again.')

#run the main menu
if __name__ == "__main__":
    main_menu()