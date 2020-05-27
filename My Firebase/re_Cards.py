from firebase import firebase

myDB = firebase.FirebaseApplication('https://firstproject-c195b.firebaseio.com/', None)


"""RETRIEVE ALL RECORDS"""
allRecords = myDB.get("cards", None)

# Firebase --> {key: {my dictionary of values}}


print("card_id", end="\t")
print("fName", end="\t")
print("lName", end="\t\t")
print("cardNum", end="\t")
print("")
print("")

for i in allRecords:
    print(allRecords[i]['card_id'], end="\t")
    print(allRecords[i]['fName'], end="\t")
    print(allRecords[i]['lName'], end="\t\t")
    print(allRecords[i]['card_num'])











