# Developed by: Ariana F
# Date: March 8, 2023
# Desc: A PC shop program that allows users to choose between custom PCs or pre-built PCs or both! Then the user
#       can check out and the price of what they ordered will be shown in a list.
# Inputs: 1, 2, 3, x, X ("x"s stands for no, user can input invalid options and program will
#         repeat the question until valid response.)
# Outputs: order questions and cost details.

# function to store the items available for the custom PC
def pickItems():
    SSD = [['1', '250 GB', 69.99], ['2', '500 GB', 93.99], ['3', '4 TB', 219.99]]
    HDD = [['1', '500 GB', 106.33], ['2', '1 TB', 134.33]]
    CPU = [['1', 'Intel Core i7-11700K', 499.99], ['2', 'AMD Ryzen 7 5800X', 312.99]]
    MOTHERBOARD = [['1', 'MSI B550-A PRO', 197.46], ['2', 'MSI Z490-A PRO', 262.30]]
    RAM = [['1', '16 GB', 82.99], ['2', '32 GB', 174.99]]
    GRAPHICS_CARD = [['1', 'MSI GeForce RTX 3060 12GB', 539.99]]
    PSU = [['1', 'Corsair RM750', 164.99]]
    CASE = [['1', 'Full Tower (black)', 149.99], ['2', 'Full Tower (red)', 149.99]]
    PREBUILTS = [['1', 'Legion Tower Gen 7 with RTX 3080 Ti', 3699.99], ['2', 'SkyTech Prism II Gaming PC', 2839.99], ['3', 'ASUS ROG Strix G10CE Gaming PC', 1099.99]]
    return SSD, HDD, CPU, MOTHERBOARD, RAM, GRAPHICS_CARD, PSU, CASE, PREBUILTS

#variables "price" stores price for customPC and "pricePreBuilts" stores price for pre-built PCs.
#"totals" is an empty list. Global choice so it can be used within other functions.
global choice
price = 0.0
pricePreBuilts = 0.0
totals = []

# function for custom PC
def customPC():
    # function for CPU
    def pickCPU():
        global choice
        global price
        items=pickItems()                 #items are SSD,HDD,CPU etc in the pickItems function, items[2] selects CPU
        CPU=items[2]
        print("\nGreat! Let's start building your PC!\n\nFirst, let's pick a CPU.")
        for proc in CPU:
            print(f'{proc[0]} : {proc[1]}, ${proc[2]}')

#asks user to choose number, if number is not 1 or 2, it asks again because CPU is required for custom PC (user cannot select "x" or "X")
        choice= input('Choose the number that corresponds with the part you want: ')
        while choice !='1' and choice !='2':
            choice = input('Choose the number that corresponds with the part you want: ')
        for cpu in CPU:
            if cpu[0] == choice:
                price+=cpu[2]

#function for Motherboard because the allowable user inputs are different from CPU, for example, if CPU1 is chosen then
#user have to pick 2 for motherboard. Seperate function allows for alterations in allowable inputs.
    def pickMotherboard():
        global choice
        global price
        items = pickItems()
        motherboard = items[3]

        print("\nNext, let's pick a compatible motherboard.")
        if choice == '1':
            print(f'{motherboard[1][0]} : {motherboard[1][1]}, ${motherboard[1][2]}')
            choice = input('Choose the number that corresponds with the part you want: ')
            while choice != '2':
                choice = input('Choose the number that corresponds with the part you want: ')
            for option in motherboard:
                if option[0] == '2':
                    price += option[2]
        else:
            print(f'{motherboard[0][0]} : {motherboard[0][1]}, ${motherboard[0][2]}')
            choice = input('Choose the number that corresponds with the part you want: ')
            while choice != '1':
                choice = input('Choose the number that corresponds with the part you want: ')
            for option in motherboard:
                if option[0] == '1':
                    price += option[2]


    def pickRAM():
        global choice
        global price
        items=pickItems()
        RAM=items[4]
        print("\nNext, let's pick your RAM.")
        for proc in RAM:
            print(f'{proc[0]} : {proc[1]}, ${proc[2]}')
        choice= input('Choose the number that corresponds with the part you want: ')
        while choice !='1' and choice !='2':
            choice = input('Choose the number that corresponds with the part you want: ')
        for option in RAM:
            if option[0]== choice:
                price+=option[2]


    def pickPSU():
        global choice
        global price
        items=pickItems()
        PSU=items[6]
        print("\nNext, let's pick your PSU.")
        for proc in PSU:
            print(f'{proc[0]} : {proc[1]}, ${proc[2]}')
        choice= input('Choose the number that corresponds with the part you want: ')
        while choice !='1':
            choice = input('Choose the number that corresponds with the part you want: ')
        price += PSU[0][2]


    def pickCase():
        global choice
        global price
        items = pickItems()
        case = items[7]
        print("\nNext, let's pick your case.")
        for proc in case:
            print(f'{proc[0]} : {proc[1]}, ${proc[2]}')

        choice = input('Choose the number that corresponds with the part you want: ')
        while choice != '1' and choice != '2':
            choice = input('Choose the number that corresponds with the part you want: ')
        for cs in case:
            if cs[0] == choice:
                price += cs[2]


    def pickSSDorHDD():
        global price
        items = pickItems()
        SSD = items[0]
        HDD = items[1]
        print("\nNext, let's pick an SSD (optional, but you must have at least one SSD or HDD).")
        for proc in SSD:
            print(f'{proc[0]} : {proc[1]}, ${proc[2]}')
        SSDchoice = input('Choose the number that corresponds with the part you want (or X to not get an SSD): ')
#while statement repeats question if user input is not right.
        while SSDchoice not in ['1', '2', '3', 'x', 'X']:
            SSDchoice = input('Choose the number that corresponds with the part you want (or X to not get an SSD): ')
        for ssd in SSD:
#adds 0 to price when 'x' is chosen
            if SSDchoice.lower() == 'x':
                price += 0
            elif int(ssd[0]) == int(SSDchoice):
                price += ssd[2]

        print("\nNext, let's pick an HDD (optional, but you must have at least one SSD or HDD).")
        for proc in HDD:
            print(f'{proc[0]} : {proc[1]}, ${proc[2]}')
        HDDchoice = input('Choose the number that corresponds with the part you want (or X to not get an HDD): ')
        while HDDchoice not in ['1', '2', 'x', 'X']:
            HDDchoice = input('Choose the number that corresponds with the part you want (or X to not get an HDD): ')
#while statement asks the user question again if both inputs for SSD and HDD is "x" or "X". Because you need atleast one.
        while HDDchoice in ['x', 'X'] and SSDchoice in ['x', 'X']:
            HDDchoice = input('Choose the number that corresponds with the part you want (or X to not get an HDD): ')
        while HDDchoice not in ['1', '2', 'x', 'X']:
            HDDchoice = input('Choose the number that corresponds with the part you want (or X to not get an HDD): ')
        for hdd in HDD:
            if HDDchoice.lower() == 'x':
                price += 0
            elif int(hdd[0]) == int(HDDchoice):
                price += hdd[2]


    def pickGraphicsCard():
        global choice
        global price
        items = pickItems()
        graphicsCard = items[5]
        print("\nFinally, let's pick your graphics card (or X to not get a graphics card).")
        for proc in graphicsCard:
            print(f'{proc[0]} : {proc[1]}, ${proc[2]}')
        choice = input('Choose the number that corresponds with the part you want: ')

        if choice == '1':
            price += graphicsCard[0][2]
            price = round(price, 2)
        elif choice.lower() == 'x':
            price += 0
        else:
            choice = input('Choose the number that corresponds with the part you want: ')

#calling the functions
    pickCPU()
    pickMotherboard()
    pickRAM()
    pickPSU()
    pickCase()
    pickSSDorHDD()
    pickGraphicsCard()

#append adds the price to totals list
    totals.append(price)
    print(f"\nYou have selected all of the required parts! Your total for this PC is ${price}")  # 2 decimal places
    userOption()

#function for pre-built PC
def prebuiltPC():
    global choice
    global pricePreBuilts
    items=pickItems()
    prebuilts=items[8]
    print("\nGreat! Let's pick a pre-built PC!\n\nWhich prebuilt would you like to order?")
    for proc in prebuilts:
        print(f'{proc[0]} : {proc[1]}, ${proc[2]}')

    choice= input('Choose the number that corresponds with the part you want: ')
    while choice not in ["1","2","3"]:
        choice = input('Choose the number that corresponds with the part you want: ')
    for option in prebuilts:
        if option[0] == choice:
            pricePreBuilts+=option[2]
# append adds the price for pre-builts to totals list
    totals.append(pricePreBuilts)
    print(f"\nYour total price for this prebuilt is ${pricePreBuilts}")
    userOption()

#checkout function for printing out the totals list, the price appended will depend on the user inputs
def checkout():
    print(totals)

print("Welcome to my PC shop!")

#if,elif statements leads to the specified function
def userOption():
    option = input("\nWould you like to build a custom PC (1), purchase a pre-built PC (2), or would you like to checkout (3)? ")
    if option == "1":
        customPC()
    elif option == "2":
        prebuiltPC()
    elif option == "3":
        checkout()
#else statement asks the question again if the user input is not correct(not 1,2,or 3)
    else:
        while option not in ["1","2","3"]:
            option = input("\nWould you like to build a custom PC (1), purchase a pre-built PC (2), or would you like to checkout (3)? ")
        if option == "1":
            customPC()
        elif option == "2":
            prebuiltPC()
        elif option == "3":
            checkout()
userOption()


