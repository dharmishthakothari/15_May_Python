contact_dict = {"Suraj":78904443,"Shivani":78453212,"Deep":567845678,"Parth":456345345}
print(len(contact_dict))
print(contact_dict["Shivani"])
print(contact_dict.get("Partjhjghjh"))
name = "Shivani"
for i in contact_dict.keys():
    if i==name:
        print(contact_dict[i])