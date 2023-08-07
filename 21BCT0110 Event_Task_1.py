def calculate_cooling_load(area, numOccupants, buildingType, outdoorTemp, indoorTemp):
    if buildingType.lower() == "residential":
        coolingLoad = 100 * numOccupants
    elif buildingType.lower() == "commercial":
        coolingLoad = 150 * numOccupants
    else:
        raise ValueError("Invalid building type. Supported types: residential, commercial")

    uCoefficient = 30
    qConduction = uCoefficient * area * (outdoorTemp - indoorTemp)
    sensibleCoolingLoad = qConduction + coolingLoad

    return sensibleCoolingLoad

def main():
    try:
        area = float(input("Enter the area of the building (in square meters): "))
        numOccupants = int(input("Enter the number of occupants in the building: "))
        buildingType = input("Enter the type of building (residential/commercial): ")
        outdoorTemp = float(input("Enter the outdoor temperature (in Celsius): "))
        indoorTemp = float(input("Enter the indoor desired temperature (in Celsius): "))

        coolingLoad = calculate_cooling_load(area, numOccupants, buildingType, outdoorTemp, indoorTemp)
        print(f"The sensible cooling load is: {coolingLoad} W")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
