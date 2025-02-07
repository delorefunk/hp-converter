# ASCII Art Header
print("\n"
      "██   ██  ██████    █████   █████    ███      ██  ██████   █████  ███████  █████  ████████  ███████   █████ \n"
      "██   ██  ██   ██  ██      ██   ██   ██ ██    ██    ██      ██    ██       ██  ██    ██     ██        ██  ██\n"
      "███████  ██████   ██     ██     ██  ██  ██   ██     ██    ██     ███████  █████     ██     ███████   █████\n"
      "██   ██  ██       ██      ██   ██   ██   ██  ██      ██  ██      ██       ██  ██    ██     ██        ██  ██\n"
      "██   ██  ██        █████   █████    ██    █████       ████       ███████  ██   ██   ██     ███████   ██   ██\n")

print("Brought to you by:")
print("\n\033[1m@delorefunk\033[0m")

print("==============================================================================\n")
print("Horse Power <-> Brake Horse Power <-> Wheel Horsepower <-> PS <-> KW Converter\n")
print("==============================================================================\n")

description = "This is a tool made for converting one unit measure of power to another."
print(description)

# Conversion factors (direct conversion rates)
conversion_factors = {
    ("HP", "BHP"): 1.01387,
    ("HP", "KW"): 0.746,
    ("HP", "PS"): 1.01387,
    
    ("BHP", "HP"): 1 / 1.01387,
    ("BHP", "KW"): 0.746,
    ("BHP", "PS"): 1.01387,
    
    ("KW", "HP"): 1.341,
    ("KW", "BHP"): 1.341,
    ("KW", "PS"): 1.36,
    
    ("PS", "HP"): 0.9863,
    ("PS", "BHP"): 0.9863,
    ("PS", "KW"): 0.7355
}

# Drivetrain loss multipliers
drivetrain_loss = {
    "FWD": 0.10,
    "RWD": 0.15,
    "AWD": 0.25
}

units = ["HP", "BHP", "WHP", "PS", "KW"]

# Function to factor in drivetrain loss
def get_drivetrain_loss(amount, conversion_type):
    drivetrain = input("Select your drivetrain (FWD, RWD, AWD): ").strip().upper()
    
    if drivetrain in drivetrain_loss:
        loss_factor = drivetrain_loss[drivetrain]
        if conversion_type == "WHP_to_X":
            return amount / (1 - loss_factor)
        else:  # Others_to_WHP
            return amount * (1 - loss_factor)
    else:
        print("Invalid drivetrain selection.")
        return None

# Function to convert power
def power_conversion(amount, origin, target):
    if origin == target:
        print("You picked the same unit!")
        return
    
    if (origin, target) in conversion_factors:
        converted = amount * conversion_factors[(origin, target)]
        print(f"{amount} {origin} = {converted:.2f} {target}")
    
    elif (target, origin) in conversion_factors:  # Reverse conversion
        converted = amount / conversion_factors[(target, origin)]
        print(f"{amount} {origin} = {converted:.2f} {target}")

    elif origin == "WHP":
        converted = get_drivetrain_loss(amount, "WHP_to_X")
        if converted is not None:
            print(f"{amount} WHP = {converted:.2f} {target}")
    
    elif target == "WHP":
        converted = get_drivetrain_loss(amount, "X_to_WHP")
        if converted is not None:
            print(f"{amount} {origin} = {converted:.2f} WHP")
    
    else:
        print("Conversion not supported.")

# User input
print("\nChoose the original unit:")
for idx, unit in enumerate(units, 1):
    print(f"{idx}) {unit}")

origin_idx = int(input("\nEnter the number corresponding to your unit: ")) - 1
target_idx = int(input("\nEnter the number of the unit you want to convert to: ")) - 1

if 0 <= origin_idx < len(units) and 0 <= target_idx < len(units):
    origin_unit = units[origin_idx]
    target_unit = units[target_idx]
    
    user_power = float(input("\nEnter how much power your vehicle is making: "))
    power_conversion(user_power, origin_unit, target_unit)
else:
    print("Invalid unit selection.")
