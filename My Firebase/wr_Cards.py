from firebase import firebase


"""My Database Connection"""
myDB = firebase.FirebaseApplication('https://firstproject-c195b.firebaseio.com/', None)


"""WRITING DATA"""
card_id = int(input("Enter card_id: "))
fName = input("Enter first name: ")
lName = input("Enter last name: ")
card_num = input("Enter card_number: ")


record = {
    'card_id': card_id,
    'fName': fName,
    'lName': lName,
    'card_num': card_num
    }


"""POST TO DB"""
myDB.post("cards", record)











