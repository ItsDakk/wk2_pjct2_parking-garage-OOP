##------------- Plan of Execution ------------------##

## Create 2 classees 
    # [Parking Garage (Backend) Car (UI)]
    # 3 Class Attributes
        # 1. Tickets
        # 2. Parking Spaces
        # 3. Current Ticket

##------------ Parking Garage Class -----------------##        

## Create 3 methods inside Parking Garage Class
    # 1. take_ticket()
        # 1. decrease the amnt of tickets available by 1
        # 2. Decrease the amnt of parking spaces available 
    # 2. pay_for_parking()
        # Display input that waits for an amnt from the user and store it in a variable
        # If the payment variable is on empty (ticket has been paid) -> display a message to the user "You have paid and have 15 min to leave"
        # This should update the "currentTicker" dictionary key to True
    # 3. leave_garge()
        # If the ticket has been paid, display "Thank you, have a nice day"
            # If the ticket has not been paid, display input that prompts for payment
        # Update Parking Spaces list to increase by 1 (meaning add to the parking spaces)
        # Update ticket list to increase by 1(meaning add to the tickets)

##--------------------------------------------------##
##----------------- Car (UI) Class -----------------## 

#Lay out options for user 


tickets = ["T1", "T2", "T3", "T4", "T5"]
parking_spaces = ["T1", "T2", "T3", "T4", "T5"]
current_ticket = {
    "T1": False,
    "T2": False,
    "T3": False,
    "T4": False,
    "T5": False,
}

class ParkingGarage():
    
    def __init__(self):
        pass

    def test(self):
        print(current_ticket)
        print(tickets)
        print(parking_spaces)

    def take_ticket(self):
        if tickets and parking_spaces != []:
            ticket = tickets.pop(0)
            parking_spaces.pop(0)
            print(f"Your ticket number is {ticket}")
            current_ticket[f"{ticket}"]=True
        else:
            print("Sorry we are out of available parking at the moment.")
        
    def pay_for_parking(self):
            ticket = input("What is your ticket number? ")                      # Trying to catch a input mistake
            if current_ticket[ticket] == True:
                pay = int(input("The total amount owed is $15: ").strip('$'))
                print("Thank you for the payment, have a great day!")
                ticket = tickets.append(ticket)
                parking_spaces.append(ticket)                                   # Suppose to append 1 available parking space to list but appends None?
                current_ticket[f"{ticket}"]=False                               # Trying to update 1 specific value in the dictionary but adds a new key-value pair?
                while pay != 15:
                    pay = int(input("The total amount owed is $15: ").strip('$'))
            else:
                print("Ticket has been paid - you have 15 min to leave. Thank you!")

    def leave_garage(self):
        ticket = input("What is your ticket number? ")
        if current_ticket[ticket] == True: 
                int(input("The total amount owed is $15: ").strip('$'))
                print("Thank you for the payment, have a great day!")
        else:
            current_ticket[f"{ticket}"]=False                                   # Trying to update 1 specific value in the dictionary
            print("Ticket has been paid - you have 15 min to leave. Thank you!")

class Car():
    
    def __init__(self):
        self.parking_garage = ParkingGarage()
        pass

    def run_the_program(self):
        while True:
            #Lay out options for user
            user_opt = input("What would you like to do? Please enter one [Take/Pay/Leave] ").lower().strip()
            if user_opt == 'take':
                self.parking_garage.take_ticket()
            elif user_opt == 'pay':
                self.parking_garage.pay_for_parking()
            elif user_opt == 'leave':
                self.parking_garage.leave_garage()
            elif user_opt == 'test':
                self.parking_garage.test()
        pass

def main():
    car_1 = Car()
    car_1.run_the_program()

if __name__=="__main__":
    main()     

