print("Hello, welcome to the unit converter which converts kilometres into miles!")

# option 1
# while True:
#             km = int(input("Enter km: "))
#             m = km*0.621
#
#             print(km*m)
#
#             option = input("Would you like another conversion (y/n): ")
#             if option == "n" or option == "no":
#                 break
#             elif option == "y" or option == "yes":
#                 print("Let's convert again!")

# option 2

while True:

    print("Please enter the number kilometres you'd like to convert to miles.")
    km = int(input("Kilometres: "))
    m = km*0.621


    print(str(km) + " kilometres" + " " + "is" + " " + str(m) + " miles.")

    option = input("Would you like another conversion (y/n): ")

    if option == "n" or option == "no":
        break
    else:
        print("Let's convert again!")


