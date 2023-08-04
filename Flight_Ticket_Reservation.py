#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
import numpy as np
import random
import sys

indigo = pd.read_csv(r"C:\Users\Dell\OneDrive\Desktop\2nd Year\OOP Project\Indigo.csv")
air_india = pd.read_csv(r"C:\Users\Dell\OneDrive\Desktop\2nd Year\OOP Project\Air India.csv")
spice_jet = pd.read_csv(r"C:\Users\Dell\OneDrive\Desktop\2nd Year\OOP Project\SpiceJet.csv")


# In[ ]:


#212 seats - air india
seat_eco_air, seat_bus_air, seat_first_air = 175, 25, 10

#200 seats - indigo
seat_eco_indigo, seat_first_indigo, seat_bus_indigo = 175, 25, 10

#218 seats - spice
seat_eco_spice, seat_bus_spice, seat_first_spice = 175, 25, 10

#cost
business_air, economy_air, first_air = 2500, 1200, 2490
busi_indigo, eco_indigo, first_indigo = 2340, 1090, 2500
busi_spice, eco_spice, first_spice = 2449, 1100, 2499


# In[ ]:


def seat_count(flight,seat, no_of_pass):
    flag = 0 # 0 continue, 1 stop
    if flight.lower() == 'air india':
        if seat.lower() == 'business':
            if (seat_bus_air - no_of_pass) > 0:
                flag = 0
            else:
                flag = 1

        elif seat.lower() == 'economy':
            if (seat_eco_air - no_of_pass) > 0:
                flag = 0
            else:
                flag = 1
        else:
            if (seat_first_air - no_of_pass) > 0:
                flag = 0
            else:
                flag = 1
    elif flight.lower() == 'indigo':
        if seat.lower() == 'business':
            if (seat_bus_indigo - no_of_pass) > 0:
                flag = 0
            else:
                flag = 1

        elif seat.lower() == 'economy':
            if (seat_eco_indigo - no_of_pass) > 0:
                flag = 0
            else:
                flag = 1
        else:
            if (seat_first_indigo - no_of_pass) > 0:
                flag = 0
            else:
                flag = 1

    elif flight.lower() == 'spice':
        if seat.lower() == 'business':
            if (seat_bus_indigo - no_of_pass) > 0:
                flag = 0
            else:
                flag = 1

        elif seat.lower() == 'economy':
            if (seat_eco_indigo - no_of_pass) > 0:
                flag = 0
            else:
                flag = 1
        else:
            if (seat_first_indigo - no_of_pass) > 0:
                flag = 0
            else:
                flag = 1

    return flag


# In[ ]:


def seat_numbers(seat):
    if seat.lower() == 'economy':
        rows = np.arange(1, 36)
        columns = ['A', 'B', 'C', 'D', 'E']
        seats = [['{}{}'.format(row, col) for col in columns] for row in rows]
        from pprint import pprint
        pprint(seats)
        seat_no = input("Please choose seat for passenger:")

        for i, x in enumerate(seats):
            for j, a in enumerate(x):
                if seat_no in a:
                    seats[i][j] = a.replace(seat_no, '-')
    elif seat.lower() == 'business':
        rows = np.arange(1, 6)
        columns = ['A', 'B', 'C', 'D', 'E']
        seats = [['{}{}'.format(row, col) for col in columns] for row in rows]
        from pprint import pprint
        pprint(seats)
        seat_no = input("Please choose seat for passenger:")

        for i, x in enumerate(seats):
            for j, a in enumerate(x):
                if seat_no in a:
                    seats[i][j] = a.replace(seat_no, '-')
                    
    else:
        rows = np.arange(1, 3)
        columns = ['A', 'B', 'C', 'D', 'E']
        seats = [['{}{}'.format(row, col) for col in columns] for row in rows]
        from pprint import pprint
        pprint(seats)
        seat_no = input("Please choose seat for passenger:")

        for i, x in enumerate(seats):
            for j, a in enumerate(x):
                if seat_no in a:
                    seats[i][j] = a.replace(seat_no, '-')
                    
    return seat_no


# In[ ]:


def flights(ori_place, dest_place):
    f_1, f_2, f_3 = 0, 0, 0
    df_1 = air_india["Origin"].str.contains(ori_place) & air_india['Destination(D)'].str.contains(dest_place)
    if df_1:
        print('\nAIR INDIA')
        print(air_india.loc[
                  air_india['Origin'].str.contains(ori_place) & air_india['Destination(D)'].str.contains(dest_place)])
    else:
        print('\n Sorry no flights available in AIR INDIA')
        f_1 = 1

    df_2 = indigo['Origin'].str.contains(ori_place) & indigo['Destination(D)'].str.contains(dest_place)
    if df_2:
        print('\nINDIGO')
        print(indigo.loc[indigo['Origin'].str.contains(ori_place) & indigo['Destination(D)'].str.contains(dest_place)])
    else:
        print('\n Sorry no flights available in INDIGO')
        f_2 = 1

    df_3 = spice_jet['Origin'].str.contains(ori_place) & spice_jet['Destination(D)'].str.contains(dest_place)
    if df_3:
        print('\nSPICE JET')
        print(spice_jet.loc[
                  spice_jet['Origin'].str.contains(ori_place) & spice_jet['Destination(D)'].str.contains(dest_place)])
    else:
        print('\n Sorry no flights available in SPICE JET')
        f_3 = 1
    
    if f_1 == 0 or f_2 == 0 or f_3 == 0:
        details(ori_place, dest_place)
    else:
        print("Sorry!! No flights available.")

    
def details(ori_place, dest_place):
    # details
    lst = {}
    i = 0
    j = 0
    price = 0
    flight = input("\nWhich airlines do you prefer?")
    if flight.lower() == 'air india':
        Flight_no = input('Flight number:')
        date = input('Date: ')
        i = int(input("No of Passengers: "))
        ticket_num = int(21698000)

        while j < i:
            name = input("Full name:")
            p_num = int(input("Passport number:"))
            ph_num = int(input("Contact number:"))
            age = int(input("Age:"))
            seat = input('Business\Economy\First class: ')
            ct = seat_count(flight,seat, i)
            if ct == 0:
                s = seat_numbers(seat)
                ticket_num = ticket_num+1

                details = [name, p_num, ph_num, age, date, flight, Flight_no, seat, ticket_num]
                lst[j + 1] = details
                j += 1
            else:
                print("Sorry!! Required number of seats are not available.")
                sys.exit()
            
            
            if seat.lower() == 'business':
                price += business_air
            elif seat.lower() == 'economy':
                price += economy_air
            else:
                price += first_air
                
            df = pd.DataFrame.from_dict(lst, orient='index',
                                               columns=['Name', 'Passport No.', 'Contact No.', 'Age','Date', 'Flight',
                                                        'Flight No.', 'Seat',  'Ticket No.'])
            df.to_csv("airindia.csv", index = False)
            
            print("\nTicket price: ", price)
            
            print("\nName of Passenger                    Ticket No.")
            print(name, "                        ",ticket_num)
            print("\nFrom            Flight            Date            Time")
            print(ori_place,"            ",Flight_no,"        ",date, "        ",air_india[air_india['Flight No.'] == Flight_no]['Departure'])
            print("\nTo")
            print(dest_place)
            print("\nGate            Seat")
            print("0"+str(random.randint(1, 21)), "            ", s)
            
            

    elif flight.lower() == 'indigo':
        Flight_no = input('Flight number:')
        date = input('Date: ')
        i = int(input("No of Passengers: "))
        ticket_num = int(30498000)

        while j < i:
            name = input("Full name:")
            p_num = int(input("Passport number:"))
            ph_num = int(input("Contact number:"))
            age = int(input("Age:"))
            seat = input('Business\Economy\First class: ')
            ct = seat_count(flight,seat, i)
            if ct == 0:
                s = seat_numbers(seat)
                ticket_num = ticket_num+1

                details = [name, p_num, ph_num, age, date, flight, Flight_no, seat, ticket_num]
                lst[j + 1] = details
                j += 1
            else:
                print("Sorry!! Required number of seats are not available.")
                sys.exit()
        
            
            if seat.lower() == 'business':
                price += busi_indigo
            elif seat.lower() == 'economy':
                price += eco_indigo
            else:
                price += first_indigo

            df = pd.DataFrame.from_dict(lst, orient='index',
                                               columns=['Name', 'Passport No.', 'Contact No.', 'Age','Date', 'Flight',
                                                        'Flight No.', 'Seat',  'Ticket No.'])
            df.to_csv("indigo.csv", index = False)
            
            print("\nTicket price: ", price)
            
            print("\nName of Passenger                    Ticket No.")
            print(name, "                        ",ticket_num)
            print("\nFrom                Flight            Date            Time")
            print(ori_place,"            ",Flight_no,"        ",date, "        ",air_india[air_india['Flight No.'] == Flight_no]['Departure'])
            print("\nTo")
            print(dest_place)
            print("\nGate            Seat")
            print("0"+str(random.randint(1, 21)), "            ", s)


    else:
        Flight_no = input('Flight number:')
        date = input('Date: ')
        i = int(input("No of Passengers: "))
        ticket_num = int(50098000)

        while j < i:
            name = input("Full name:")
            p_num = int(input("Passport number:"))
            ph_num = int(input("Contact number:"))
            age = int(input("Age:"))
            seat = input('Business\Economy\First class: ')
            ct = seat_count(flight,seat, i)
            if ct == 0:
                s = seat_numbers(seat)
                ticket_num = ticket_num+1

                details = [name, p_num, ph_num, age, date, flight, Flight_no, seat, ticket_num]
                lst[j + 1] = details
                j += 1
            else:
                print("Sorry!! Required number of seats are not available.")
                sys.exit()
            
                
            if seat.lower() == 'business':
                price += busi_spice
            elif seat.lower() == 'economy':
                price += eco_spice
            else:
                price += first_spice

            df = pd.DataFrame.from_dict(lst, orient='index',
                                               columns=['Name', 'Passport No.', 'Contact No.', 'Age','Date', 'Flight',
                                                        'Flight No.', 'Seat',  'Ticket No.'])
            df.to_csv("spice.csv", index = False)
            
            print("\nTicket price: ", price)
            
            print("\nName of Passenger                    Ticket No.")
            print(name, "                        ",ticket_num)
            print("\nFrom                Flight            Date            Time")
            print(ori_place,"            ",Flight_no,"        ",date, "        ",air_india[air_india['Flight No.'] == Flight_no]['Departure'])
            print("\nTo")
            print(dest_place)
            print("\nGate            Seat")
            print("0"+str(random.randint(1, 21)), "            ", s)


# In[ ]:


def start():
    #User's choice
    print("1.Book a Flight \n2.Flight Details ")
    choice = int(input("\nEnter choice: "))
    if choice == 1:
        ori_place = input('Origin(Please enter name with first letter in Caps): ')
        dest_place = input('Destination(Please enter name with first letter in Caps): ')
        flights(ori_place, dest_place)
        
    elif choice == 2:
        flight = input("Which airlines?")
        fl_no = input('Flight No. : ')
        if flight.lower() == 'air india':
            if (air_india['Flight No.'] == fl_no).any(axis = 0):
                print(air_india[air_india['Flight No.'] == fl_no])
            else:
                print("No flights Available.")
        elif flight.lower() == 'indigo':
            if (indigo['Flight No.'] == fl_no).any(axis = 0):
                print(indigo[indigo['Flight No.'] == fl_no])
            else:
                print("No flights Available.")
        else:
            if (spice_jet['Flight No.'] == fl_no).any(axis = 0):
                print(spice_jet[spice_jet['Flight No.'] == fl_no])
            else:
                print("No flights Available.")


# In[ ]:


def main():
    start()
    ans = ''
    ans = input("\nDo you want to continue?(y/n)")
    while ans == 'y':
        start()
        ans = input("\nDo you want to continue?(y/n)")
    print('Thank you!!')
    
main()

