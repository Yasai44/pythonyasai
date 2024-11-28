"""
 A program that functions as a concert Reservation System
 Author: Sainabou Samba Camara
"""
import sys

# Creating the concert hall
concert_hall = []
number_of_rows = int(input("How many rows are required?: "))
number_of_seats = int(input("How many seats per row are required?: "))

for row in range(number_of_rows + 1):
    rows = []
    for seat in range(number_of_seats + 1):
        if row == 0 or seat == 0:
            rows.append(" ")
        else:
            rows.append(str(seat))
    concert_hall.append(rows)

# Display the seating chart
def display_seating_chart(hall):
    print()
    for i in range(1, number_of_rows + 1):
        print(f"Row {i}:", end=" ")
        for j in range(1, number_of_seats + 1):
            print(hall[i][j], end=" ")
        print()

#Add new reservation
def add_new_reservation(concert):
    display_seating_chart(concert)
    try:
        row_number = int(input("Enter desired row number: "))
        seat_number = int(input("Enter desired seat number: "))
        if row_number < 1 or row_number > number_of_rows or seat_number < 1 or seat_number > number_of_seats:
            raise IndexError("Invalid row or seat number.")
        elif not concert[row_number][seat_number].isdigit():#We used .isdigit() to check if the input contains only digits
            print("Seat is unavailable")                    #True if all characters in the string are digits, False otherwise.
        else:
            name = input("Enter name: ")
            concert[row_number][seat_number] = name
            print(f"Seat {seat_number} in row {row_number} reserved for {name}.")
    except ValueError:
        print("Invalid input, please try again.")
    except IndexError as e:
        print(e)
    except Exception as ex:
        print(ex)

#Edit reservation
def edit_reservation():
    display_seating_chart(concert_hall)
    try:
        row_number = int(input("Enter desired row number: "))
        seat_number = int(input("Enter desired seat number: "))
        if row_number < 1 or row_number >= len(concert_hall) or seat_number < 1 or seat_number >= len(concert_hall[row_number]):
            raise IndexError ("Invalid row or seat number.")
        elif not concert_hall[row_number][seat_number].isdigit():
            new_name = input("Enter your name: ")
            concert_hall[row_number][seat_number] = new_name
            print(f"Reservation for seat {seat_number} in row {row_number} has been updated.")
        else:
            print("No reservation found at this seat.")
    except ValueError:
        print("Invalid input.")
    except IndexError as e:
        print(e)
    except Exception as ex:
        print(ex)


#Cancel reservation
def cancel_existing_reservation():
    display_seating_chart(concert_hall)
    try:
        row_number = int(input("Enter desired row number: "))
        seat_number = int(input("Enter desired seat number: "))
        if row_number < 1 or row_number >= len(concert_hall) or seat_number < 1 or seat_number >= len(concert_hall[row_number]):
            raise ValueError("Invalid row or seat number.")
        elif concert_hall[row_number][seat_number].isdigit(): 
            print("No reservation found.")                    
        else:
            confirm = input("Confirm reservation cancellation(y/n): ")
            if confirm.lower() == "y":
                concert_hall[row_number][seat_number] = str(seat_number)
                print(f"Reservation for seat {seat_number} in row {row_number} has been cancelled")
            else:
                print("Cancellation aborted.")
    except IndexError:
        print("Invalid input")
    except ValueError as e:
        print(e)
    except Exception as ex:
        print(ex)

#Main menu
def main_menu():
    display_seating_chart(concert_hall)
    while True:
        print("\n Main Menu:")
        print("1. Reserve seats")
        print("2. Edit reservation")
        print("3. Cancel reservation")
        print("4. Display all seats")
        print("5. Exit")
        choice = input("Select an option: ")
        try:
            if choice == "1":
                add_new_reservation(concert_hall)
            elif choice == "2":
                edit_reservation()
            elif choice == "3":
                cancel_existing_reservation()
            elif choice == "4":
                display_seating_chart(concert_hall)
            elif choice == "5":
                print("Goodbye!!")
                sys.exit() #We used this function to exit the program because the "break" wasn't working
            else:
                raise ValueError("Invalid choice, try again.")
        except ValueError as e:
            print(e)

#Main code here
main_menu()
display_seating_chart(concert_hall)
add_new_reservation(concert_hall)
edit_reservation()
cancel_existing_reservation()