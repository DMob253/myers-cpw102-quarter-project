from vehicle_makes import get_makes_and_models


def main():
    makes_and_models = get_makes_and_models()

    make = input("Enter vehicle make: ")

    if make in makes_and_models:
        print(makes_and_models[make])
    else:
        print("Vehicle make not found.")

main()
