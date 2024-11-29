def convertToLunar(solarYear):
    # Code to convert solar year to lunar year
    lunarYear = solarYear * 1.0306812089059
    return lunarYear

def convertToSolar(lunarYear):
    # Code to convert lunar year to solar year
    solarYear = lunarYear / 1.0306812089059
    return solarYear

if __name__ == "__main__":
    print("Welcome to the small tool that converts year input")
    while True:
        print("Enter 1 to convert from solar to lunar year")
        print("Enter 2 to convert from lunar to solar year")
        print("Enter 3 to exit")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            solarYear = int(input("Enter the solar year: "))
            lunarYear = convertToLunar(solarYear)
            print(f"The lunar year is {lunarYear}")
        elif choice == 2:
            lunarYear = int(input("Enter the lunar year: "))
            solarYear = convertToSolar(lunarYear)
            print(f"The solar year is {solarYear}")
        elif choice == 3:
            print("Goodbye")
            quit()
        else:
            print("Invalid choice")
        print()
    