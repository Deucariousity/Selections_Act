# python program to find out Chinese Zodiac sign for a given year

# creating a loop
while True:

    # starting a program by collecting the user's information
    print("Discover your Chinese Zodiac sign")
    user_name = input("What is your name? ")
    user_age = input("How old are you? ")

    print("Let's start!")

    # providing choices whether to continue or not
    user_input = input("To unravel the truth...\nMay I know your birth of date?(yes/no): ")
    if user_input == 'no':
        print("Bye, see you next time!")
    elif user_input == 'yes':
        print("proceed...")
    else:
        print("ERROR 404")
        break

    # user birthdate input
    month = input("Month: ")
    day = input("Day: ")
    birth_year = int(input("Year: "))

    # formula to calculate the Chinese Zodiac sign
    zodiac_signs = (birth_year - 1000) % 12

    # using a Multi-Way if-elif-else statement to construct program
    # displays result
    if zodiac_signs == 0:
        print("Based on my calculation")
        print(f"Sir/Ma'am, {user_name} you are {user_age} years old and born on "
              f'{month} {day}, {birth_year}\nYour Chinese Zodiac Sign is "Year of the RAT"')

    elif zodiac_signs == 1:
        print("Based on my calculation")
        print(f"Sir/Ma'am, {user_name} you are {user_age} years old and born on "
              f'{month} {day}, {birth_year}\nYour Chinese Zodiac Sign is "Year of the OX"')

    elif zodiac_signs == 2:
        print("Based on my calculation")
        print(f"Sir/Ma'am, {user_name} you are {user_age} years old and born on "
              f'{month} {day}, {birth_year}\nYour Chinese Zodiac Sign is "Year of the TIGER"')

    elif zodiac_signs == 3:
        print("Based on my calculation")
        print(f"Sir/Ma'am, {user_name} you are {user_age} years old and born on "
              f'{month} {day}, {birth_year}\nYour Chinese Zodiac Sign is "Year of the RABBIT"')

    elif zodiac_signs == 4:
        print("Based on my calculation")
        print(f"Sir/Ma'am, {user_name} you are {user_age} years old and born on "
              f'{month} {day}, {birth_year}\nYour Chinese Zodiac Sign is "Year of the DRAGON"')

    elif zodiac_signs == 5:
        print("Based on my calculation")
        print(f"Sir/Ma'am, {user_name} you are {user_age} years old and born on "
              f'{month} {day}, {birth_year}\nYour Chinese Zodiac Sign is "Year of the SNAKE"')

    elif zodiac_signs == 6:
        print("Based on my calculation")
        print(f"Sir/Ma'am, {user_name} you are {user_age} years old and born on "
              f'{month} {day}, {birth_year}\nYour Chinese Zodiac Sign is "Year of the HORSE"')

    elif zodiac_signs == 7:
        print("Based on my calculation")
        print(f"Sir/Ma'am, {user_name} you are {user_age} years old and born on "
              f'{month} {day}, {birth_year}\nYour Chinese Zodiac Sign is "Year of the SHEEP"')

    elif zodiac_signs == 8:
        print("Based on my calculation")
        print(f"Sir/Ma'am, {user_name} you are {user_age} years old and born on "
              f'{month} {day}, {birth_year}\nYour Chinese Zodiac Sign is "Year of the MONKEY"')

    elif zodiac_signs == 9:
        print("Based on my calculation")
        print(f"Sir/Ma'am, {user_name} you are {user_age} years old and born on "
              f'{month} {day}, {birth_year}\nYour Chinese Zodiac Sign is "Year of the ROOSTER"')

    elif zodiac_signs == 10:
        print("Based on my calculation")
        print(f"Sir/Ma'am, {user_name} you are {user_age} years old and born on "
              f'{month} {day}, {birth_year}\nYour Chinese Zodiac Sign is "Year of the DOG"')

    elif zodiac_signs == 11:
        print("Based on my calculation")
        print(f"Sir/Ma'am, {user_name} you are {user_age} years old and born on "
              f'{month} {day}, {birth_year}\nYour Chinese Zodiac Sign is "Year of the PIG"')

    # if user put invalid input
    else:
        print('ERROR 404')

    print()

    # option to try again, if no = end of loop
    another = input("Do you want to try again?(yes/no): ")
    if another != 'yes':
        break
