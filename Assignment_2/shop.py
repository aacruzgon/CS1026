# Invetory of PC components for custom builds
SSD = [['1', '250 GB', 69.99], ['2', '500 GB', 93.99], ['3', '4 TB', 219.99]]
HDD = [['1', '500 GB', 106.33], ['2', '1 TB', 134.33]]
CPU = [['1', 'Intel Core i7-11700K', 499.99],
       ['2', 'AMD Ryzen 7 5800X', 312.99]]
MOTHERBOARD = [['1', 'MSI B550-A PRO', 197.46],
               ['2', 'MSI Z490-A PRO', 262.30]]
RAM = [['1', '16 GB', 82.99], ['2', '32 GB', 174.99]]
GRAPHICS_CARD = [['1', 'MSI GeForce RTX 3060 12GB', 539.99]]
PSU = [['1', 'Corsair RM750', 164.99]]
CASE = [['1', 'Full Tower (black)', 149.99], ['2', 'Full Tower (red)', 149.99]]

# Inventory of pre-built machines
PREBUILTS = [
    ['1', 'Legion Tower Gen 7 with RTX 3080 Ti', 3699.99],
    ['2', 'SkyTech Prism II Gaming PC', 2839.99],
    ['3', 'ASUS ROG Strix G10CE Gaming PC', 1099.99]
]

# Compatibility
CPU_COMPATIBILITY = {
    "1": "2",
    "2": "1"
}

# dynamic helper function that prints the requested inventory


def print_components(component_list):
    for list in component_list:
        print(f'{list[0]} : {list[1]}, ${list[2]}')

# dynamic helper function that extracts IDs and price of requested inventory


def extract(inventory, id):
    component_options = []
    component_price = 0
    if id == "getIDs":
        for list in inventory:
            component_options.append(list[0])
        return (component_options)
    else:
        for list in inventory:
            if list[0] == id:
                component_price = list[2]
                return (component_price)

# helper function that builds and prices a costume build PC


def priceCustomBuild():
    custombuilt_price = 0
    CPU_id = ""
    MBOARD_id = ""
    RAM_id = ""
    PSU_id = ""
    CASE_id = ""
    SSD_ids = ""
    HDD_id = ""
    SSD_id = bool(0)
    GC_id = ""

    print("First, let's pick a CPU.")
    print_components(CPU)
    # ask the user for a CPU option
    while (CPU_id not in extract(CPU, "getIDs")):
        CPU_id = input(
            'Choose the number that corresponds with the part you want: ')
    custombuilt_price += extract(CPU, CPU_id)

    print("\nNext, let's pick a compatible motherboard.")
    # guarantees motherboard compatibility
    compatible_mboard = CPU_COMPATIBILITY[CPU_id]
    for list in MOTHERBOARD:
        if list[0] == compatible_mboard:
            print(f'{list[0]} : {list[1]}, ${list[2]}')
    while (MBOARD_id != compatible_mboard):
        MBOARD_id = input(
            'Choose the number that corresponds with the part you want: ')
    custombuilt_price += extract(MOTHERBOARD, MBOARD_id)

    # asks the user for RAM option
    print("\nNext, let's pick your RAM.")
    print_components(RAM)
    while (RAM_id not in extract(RAM, "getIDs")):
        RAM_id = input(
            'Choose the number that corresponds with the part you want: ')
    custombuilt_price += extract(RAM, RAM_id)

    # asks the user for PSU option
    print("\nNext, let's pick your PSU.")
    print_components(PSU)
    while (PSU_id not in extract(PSU, "getIDs")):
        PSU_id = input(
            'Choose the number that corresponds with the part you want: ')
    custombuilt_price += extract(PSU, PSU_id)

    # ask the user for computer case
    print("\nNext, let's pick your case.")
    print_components(CASE)
    while (CASE_id not in extract(CASE, "getIDs")):
        CASE_id = input(
            'Choose the number that corresponds with the part you want: ')
    custombuilt_price += extract(CASE, CASE_id)

    # ask the user for storage and stores if storage was purchased or not
    print("\nNext, let's pick an SSD (optional, but you must have at least one SSD or HDD).")
    print_components(SSD)
    while (SSD_ids not in extract(SSD, "getIDs") and SSD_ids != "x" and SSD_ids != "X"):
        SSD_ids = input(
            'Choose the number that corresponds with the part you want (or X to not get an SSD): ')
    if SSD_ids == "x" or SSD_ids == "X":
        SSD_id = False
    else:
        SSD_id = True

    if SSD_id:
        custombuilt_price += extract(SSD, SSD_ids)
    # ask the user for HDD and if user hasn't bought an SSD it will make him pick an HDD
    print("\nNext, let's pick an HDD (optional, but you must have at least one SSD or HDD).")
    print_components(HDD)
    if SSD_id:
        while (HDD_id not in extract(HDD, "getIDs") and HDD_id != "x" and HDD_id != "X"):
            HDD_id = input(
                'Choose the number that corresponds with the part you want (or X to not get an HDD): ')

    else:
        while (HDD_id not in extract(HDD, "getIDs")):
            HDD_id = input(
                'Choose the number that corresponds with the part you want (since you did not get an SSD, you must get an HDD): ')

    if HDD_id != "x" and HDD_id != "X":
        custombuilt_price += extract(HDD, HDD_id)

    # gives the user the option to purchase a graphics card
    print("\nFinally, let's pick your graphics card (or X to not get a graphics card).")
    print_components(GRAPHICS_CARD)
    while (GC_id not in extract(GRAPHICS_CARD, "getIDs") and GC_id != "x" and GC_id != "X"):
        GC_id = input(
            'Choose the number that corresponds with the part you want: ')
    if GC_id != "x" and GC_id != "X":
        custombuilt_price += extract(GRAPHICS_CARD, GC_id)

    print(
        f"\nYou have selected all of the required parts! Your total for this PC is ${custombuilt_price:.2f}")
    return custombuilt_price

# helper function that calculates the total price of the pre-built


def pricePreBuiltInventory():
    PREBUILTS_picks = ""
    custombuilt_price = 0
    print_components(PREBUILTS)
    while (PREBUILTS_picks not in extract(PREBUILTS, "getIDs")):
        PREBUILTS_picks = input(
            "Choose the number that corresponds with the part you want: ")
    custombuilt_price += extract(PREBUILTS, PREBUILTS_picks)
    print(f"\nYour total price for this prebuilt is ${custombuilt_price:.2f}")
    return custombuilt_price

# Main function of the program


def pickitems():
    print("Welcome to my PC shop!")
    print()
    finalPrice = []
    # loop that will keep going until the user decides to check out
    while True:
        userOrder = input(
            "\nWould you like to build a custom PC (1), purchase a pre-built PC (2), or would you like to checkout (3)? ")
        total = 0  # resets after every interation
        if userOrder == "1":
            print("\nGreat! Let's start building your PC!")
            print()
            total += priceCustomBuild()
            # adds price of the computer to the final total price of the purchase into a list
            finalPrice.append(total)
        elif userOrder == "2":
            print("\nGreat! Let's pick a pre-built PC!")
            print()
            print("Which prebuilt would you like to order?")
            total += pricePreBuiltInventory()
            # adds price of the computer to the final total price of the purchase into a list
            finalPrice.append(total)
        elif userOrder == "3":
            break
    print(finalPrice)


pickitems()
