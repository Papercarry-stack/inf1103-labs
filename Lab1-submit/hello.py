Username = input("Enter your username: ")
Age = input("Enter your age: ")
Category = input("Enter your content category: ")

print ("================================")
print ("\nInstagram Profile")
print ("================================")
print ("username: ", Username)
print ("age: ", Age)
print ("content category: ", Category)

if int(Age) > 40 and Category == "fun" :
    print ("You are too old what is fun for you?")