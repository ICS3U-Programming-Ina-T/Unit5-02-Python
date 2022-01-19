#!/usr/bin/env python3

# Created by: Ina Tolo
# Created on: Jan. 18, 2021
# This program asks the user for the base and
# and height, then determines the area of a triangle.

# this function calculates the area of a triangle
def calc_area(base_float, height_float):
    area = (base_float * height_float) / 2
    print("With a base of {:,.2f}cm and a height of {:,.2f}cm,"
          .format(base_float, height_float))
    print("the area of the triangle is {:,.2f}cm^2" .format(area))


# checks for invalid input
def main():

    # displays the opening message
    print("Today we will calculate the area of a triangle!")
    print("")

    # gets base and height from the user
    base_string = input("Enter the base (cm): ")
    height_string = input("Enter the base (cm): ")
    print("")

    try:
        # converts input values to floats
        base_float_user = float(base_string)
        height_float_user = float(height_string)

        # makes sure input is greater than 0
        if base_float_user > 0 and height_float_user > 0:
            # calls function calculate the area
            calc_area(base_float_user, height_float_user)
        else:
            print("The base and height must be greater than 0.")
    except Exception:
        print("Invalid data entered! Only numbers can be accepted!")


if __name__ == "__main__":
    main()
