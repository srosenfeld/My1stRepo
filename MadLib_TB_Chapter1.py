print("THE SUPERHERO")
print("Are you ready? Yes/No")
ready = input().title()
if ready == "Yes":
    print("Ok")

    print("Type a name.")
    name1 = input().title()
    print("Type a noun.")
    noun1 = input().lower()
    print("Type a verb ending in -ing.")
    verb1 = input().lower()
    print("Type a verb ending in -ing.")
    verb2 = input().lower()
    print("Type a city.")
    city1 = input().title()
    print("Type a noun.")
    noun2 = input().lower()
    print("Type a adjective.")
    adj1 = input().lower()
    print("Type a verb.")
    verb3 = input().lower()
    print("Type a name.")
    name2 = input().title()
    print("Type a name.")
    name3 = input().title()
    print("Type an action verb.")
    verb4 = input().lower()
    print("Type a verb ending in -ing.")
    verb5 = input().lower()



    print("My name is " + name1 + ", and I am the " + noun1 + ".")
    print("The superpowers are that I am good at are " + verb1 + " and " + verb2 + ".")
    print("I protect " + city1 + " from the evil " + noun2 + ".")
    print("My " + adj1 + " suit is very cool becuase it can " + verb3 + "!")
    print("I like working with my friends " + name2 + " and " + name3 + ".")
    print("I also like to " + verb4 + ", and my friends always tell me to keep " + verb5 + ".")

elif ready == "No":
    print("Your loss.")
else:
    print("That is not a valid answer.")
