my_dictionary = {
    5: "int",
    True: "bool",
    "txt": 7,
    2.7: "flt"
}
print(my_dictionary["txt"])
print(my_dictionary[2.7])
print(my_dictionary.get(True))
print(my_dictionary.keys())

my_dictionary.update({10: "number"})  # add another value to the dictionary
print(my_dictionary.keys())

for k, v in my_dictionary.items():
    if k == 5:
        print(f"Keys: {k}")
        print(f"Values: {v}")

my_dict = {
    "users": [
        {
            "username": "Oana",
            "password": "asdf1234",
            "email": "oanamaria@yahoo.com"},
        {
            "username": "User2",
            "password": "asdf1234",
            "email": "user2@yahoo.com"},
        {
            "username": "User3",
            "password": "asdf1234",
            "email": "user3@yahoo.com",
            "home": [1, "Calea Victoriei", "Medgidia"]}
    ],
    "Administrator": {
        "User": "Admin",
        "pass": "1234",
        "email": "admin@yahoo.com"
    }
}


print(my_dict["users"][2]["home"][2])

for k, v in my_dict.items():
    if k == "users":
        for user in v:
            print(user)
            for k2, v2 in user.items():
                print(k2)
                print(v2)
            #print(f"Keys: {k}")
            #print(f"Values: {v}")
