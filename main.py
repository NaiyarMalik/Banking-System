# -*- coding: utf-8 -*-
"""
Created on Fri Jan 17 14:43:02 2025

@author: naiya
"""

import os

import time
import copy
import random
import math


class color:
   BOLD = '\033[1m'
   END = '\033[0m'
   UNDER = '\x1B[4m'
   RED = '\033[91m'

# sets file name to a variable 
file_text = "customer_records.txt"

history = []

###
### SCREEN FUNCTIONS

#function will edit images based of lists on the screen
#makes sure the img is in a rectangle and empty spaces should have spaces
#img is the list of the image, x and y is where it is located
#characters are the characters u do not want on the image but are just place holders, the default is just space
def edit_screen(img,x,y,screen,characters = [" "]):
    #gets how many characters are in each row
    x_length = len(img[0])
    #gets how many rows there are
    y_length = len(img)
    
    #adds the img to the screen list
    for i in range(y_length):
        for j in range(x_length):
             #checks if the space is empty before replacing that character on the screen
            if img[i][j] not in characters:
                screen[y+i][x+j] = img[i][j]


#this function will take the a list with every row in a 2d list is a whole row of the ascii code, and will make it so that every character in that row is it's own index
#an example of this function is used in the title screen
def text_to_list(img_list):
    #new list the characters will be stored as each index, as a 2d list
    new_img_list = []
    
    #adds the mo of rows needed to the list
    for i in range(len(img_list)):
        #adds new rows to the list
        new_img_list.append([])

    #adds the characters to the list depending on the mo of rows and columns
    for i in range(len(img_list)):
        
        if len(img_list) > 1:
            #adds the characters to the list
            for j in range(len(img_list[0][0])):
                new_img_list[i].append(img_list[i][0][j])
        elif len(img_list) == 1:
            #adds the characters to the list
            for p in range(len(img_list[0])):
                new_img_list[i].append(img_list[i][p])
    
    
    return new_img_list
    

#function will clear the screen and will remove any characters
def clear_screen(screen):
    #this for loop and nested for loop will iterate through every character on the screen and make it a space
    for i in range(len(screen)):
        for j in range(len(screen[0])):
            #checks if the current character they are on is one of the wall and if it is not then it will make it a space meaning clear it
            if i != 0 and i != 39 and j != 0 and j != 99:
                screen[i][j] = " "
            #"┏","┓","┗","┛","━","┃"
            elif i == 0 and j == 0:
                screen[i][j] = "┏"
            elif i == 0 and j > 0 and j < 99:
                screen[i][j] = "━"
            elif i == 0 and j == 99:
                screen[i][j] = "┓"
            elif i > 0 and i < 39 and (j == 0 or j == 99):
                screen[i][j] = "┃"
            elif i == 39 and j == 0:
                screen[i][j] = "┗"
            elif i == 39 and j > 0 and j < 99:
                screen[i][j] = "━"
            elif i == 39 and j == 99:
                screen[i][j] = "┛"
                


#this function will clear an image on the screen
def clear_img(height,width,x,y,screen):
    
    #iterates through every character in the img on the screen and makes it into a space
    for i in range(height):
        for j in range(width):
            screen[y+i][x+j] = " "


#function to print out the screen
def print_screen(screen):
    #clears the screen first before printing out the screen
    os.system("clear")
    
    val = ""
    #prints the screen out
    for i in range(40):
        for j in range(100):
            val = val + screen[i][j]
        print(val)
        val = ""

#a function that will return what the users choices on based on the button they chose
#heights and widths are for the dimensions of the imgs, x and y are the location of the buttons on the screen and quantity is the mo of buttons on the screen 
#the buttons work that if the set is vertical the top most button is x = 0 or if horizontal the left is x = 0
#the characters are for what the outline of the button is made of those are the default if none are put in
def button(heights,widths,x,y,quantity,button_names,screen,characters = ["┏","┓","┗","┛","━","┃"," "]):
    #the variable used to see what button the user is on right now
    n = 0
    #variable used to contain the characters for the button
    button_list = []
    while True:
        ####################
        #this value stores the what the old button looked like without the outline of the button
        old_button_list = []
        
        #gets the old values into the list
        #this value will be used later to delete the outline around the part under the list
        for i in range((heights[n])):
            old_button_list.append([])
        
        for i in range((heights[n])):
            for j in range((widths[n])):
                old_button_list[i].append(screen[(y[n]+i)][(x[n]+j)])
        
        ####################
        #variable used to contain the characters for the button
        button_list = []
        
        #prints button on n = 0 and each time the while loop iterates this changes to the new value of n
        
        #adds 2 more then the mo of the height to the list
        for i in range((heights[n]+2)):
            button_list.append([])
            
        #adds the first row
        button_list[0].append(characters[0])
        for i in range(widths[n]):
            button_list[0].append(characters[4])
        button_list[0].append(characters[1])
        
        
        #adds the rows in between the first and last row the button
        for i in range(heights[n]):
            for j in range(widths[n]+2):
                if j == 0 or j == (widths[n]+1):
                    button_list[i+1].append(characters[5])
                else:
                    button_list[i+1].append(characters[6])
        
        #adds the last row in the buttons list
        button_list[-1].append(characters[2])
        for i in range(widths[n]):
            button_list[-1].append(characters[4])
        button_list[-1].append(characters[3])
        
        edit_screen(button_list,(x[n]-1),(y[n]-1),screen)
        print_screen(screen)
        #####################
        #asks the user to go, w for up, s for down, or q for picking that option
        user_input = input("").lower()
        
        #these if statements keep track of what button the user is on aswell the one they select
        if user_input == "w" or user_input == "a":
            #clears the button from the screen along with the image under it
            clear_img((heights[n]+2),(widths[n]+2),(x[n]-1),(y[n]-1),screen)
            #adds the old image back
            edit_screen(old_button_list,x[n],y[n],screen)
            
            n = n - 1
            #checks if n went lower then 0 and brings it back to the top
            if n < 0:
                n = quantity - 1
        elif user_input == "s" or user_input == "d":
            #clears the button from the screen along with the image under it
            clear_img((heights[n]+2),(widths[n]+2),(x[n]-1),(y[n]-1),screen)
            #adds the old image back
            edit_screen(old_button_list,x[n],y[n],screen)
            
            n = n + 1
            #checks if n went over the mo of buttons and brings it back to the top
            if n == quantity:
                n = 0
            
        elif user_input == "q":
            #clears the button from the screen along with the image under it
            clear_img((heights[n]+2),(widths[n]+2),(x[n]-1),(y[n]-1),screen)
            #adds the old image back
            edit_screen(old_button_list,x[n],y[n],screen)
            break
    
    #this is the name of the choice the user picked from the buttons
    choice = button_names[n]
    
    return choice

#maps letter to certain font and makes that into an image
def mapping(font,string):
    
    font1 = [[ ["▄▀█"],["█▄▄"],["█▀▀"],["█▀▄"],["█▀▀"],["█▀▀"],["█▀▀"],["█ █"],["▀█▀"],["  █"],["█▄▀"],["█  "],["█▀▄▀█"],["█▄ █"],["█▀█"],["█▀█"],["█▀█"],["█▀█"],["█▀"],["▀█▀"],["█ █"],["█ █"],["█ █ █"],["▀▄▀"],["█▄█"],["▀█"],["▀"],["  "],["▄█"],["▀█"],["▀▀█"],["█ █"],["█▀"],["█▄▄"],["▀▀█"],["█▀█ "],["█▀█"],["█▀█"],["▄█▄"],["▄▄▄"],["█▀▀▀█"],["  "],["  ▄█▀"] ]
            ,[ ["█▀█"],["█▄█"],["█▄▄"],["█▄▀"],["██▄"],["█▀ "],["█▄█"],["█▀█"],["▄█▄"],["█▄█"],["█ █"],["█▄▄"],["█ ▀ █"],["█ ▀█"],["█▄█"],["█▀▀"],["▀▀█"],["█▀▄"],["▄█"],[" █ "],["█▄█"],["▀▄▀"],["▀▄▀▄▀"],["█ █"],[" █ "],["█▄"],["▄"],["  "],[" █"],["█▄"],["▄██"],["▀▀█"],["▄█"],["█▄█"],["  █"],[" █▄█"],["▀▀█"],["█▄█"],[" ▀ "],["   "],["█▄█ █"],["▄▄"],["▄█▀  "] ]]
    
    font2 =[[ ["█▀▀█"],["█▀▀▄"],["█▀▀"],["█▀▀▄"],["█▀▀"],["█▀▀"],["█▀▀▀"],["█  █"],["▀█▀"],[" ▀█"],["█ █"],["█  "],["█▀▄▀█"],["█▀▀▄"],["█▀▀█"],["█▀▀█"],["█▀▀█"],["█▀▀█"],["█▀▀"],["▀▀█▀▀"],["█  █"],["▀█ █▀"],["█   █"],["█ █"],["█  █"],["▀▀█"],["▄"],[" "],["▄█ "],["█▀█"],["█▀▀█"],[" █▀█ "],["█▀▀"],["▄▀▀▄"],["▀▀▀█"],["▄▀▀▄"],["▄▀▀▄"],["█▀▀█"],["  ██  "],["    "] ,["█▀▀▀█"],["  "],["   █▀"]]
           ,[ ["█▄▄█"],["█▀▀▄"],["█  "],["█  █"],["█▀▀"],["█▀▀"],["█ ▀█"],["█▀▀█"],[" █ "],["  █"],["█▀▄"],["█  "],["█ ▀ █"],["█  █"],["█  █"],["█  █"],["█  █"],["█▄▄▀"],["▀▀█"],["  █  "],["█  █"],[" █▄█ "],["█▄█▄█"],["▄▀▄"],["█▄▄█"],["▄▀ "],[" "],[" "],[" █ "],[" ▄▀"],["  ▀▄"],["█▄▄█▄"],["▀▀▄"],["█▄▄ "],["  █ "],["▄▀▀▄"],["▀▄▄█"],["█▄▀█"],["██████"],["▀▀▀▀"] ,["█ █ █"],["  "],["  █  "]]
           ,[ ["▀  ▀"],["▀▀▀ "],["▀▀▀"],["▀▀▀ "],["▀▀▀"],["▀  "],["▀▀▀▀"],["▀  ▀"],["▀▀▀"],["█▄█"],["▀ ▀"],["▀▀▀"],["▀   ▀"],["▀  ▀"],["▀▀▀▀"],["█▀▀▀"],["▀▀▀█"],["▀ ▀▀"],["▀▀▀"],["  ▀  "],[" ▀▀▀"],["  ▀  "],[" ▀ ▀ "],["▀ ▀"],["▄▄▄█"],["▀▀▀"],["▀"],[" "],["▄█▄"],["█▄▄"],["█▄▄█"],["   █ "],["▄▄▀"],["▀▄▄▀"],[" ▐▌ "],["▀▄▄▀"],[" ▄▄▀"],["█▄▄█"],["  ██  "],["    "] ,["▀▀▀ █"],["██"],["▄█   "]]]

    if font == 0:
        font = font1.copy()
    elif font == 1:
        font = font2.copy()
    
    alpha = "abcdefghijklmnopqrstuvwxyz: 1234567890+-@./"
    
    img = []

    for i in range(len(font)):
        img.append([])
    
    
    for i in range(len(string)):
        for j in range(len(font)):
            img[j].extend((text_to_list(font[j][alpha.find(string[i])]))[0])
            img[j].extend([" "])


    return img
    



################################################################################
#makes a list for what everyone will see on the console which is a 100x40 character image
global screen
screen = []

#will add 50 rows to the screen to make it 100 by 40
for i in range(40):
    screen.append([])

screen[0].append("┏")
#adds the top of the list with a length of 100
for i in range(98):
    screen[0].append("━")
screen[0].append("┓")
    
#adds the sides and empty middle of the screen with a height of 40
for i in range(38):
    
    screen[i+1].append("┃")
    
    for p in range(98):
        screen[i+1].append(" ")
        
    screen[i+1].append("┃")


screen[39].append("┗")
#adds the bottem of the list with a length of 100
for i in range(98):
    screen[39].append("━")
screen[39].append("┛")



################################################################################

###
###

#file reading functions

#reads file
def read_records():
    try:
        # Opens the file and reads records
        file = open(file_text, 'r')
        return [line.strip().split(',') for line in file]
    # if the file is not found, it prints an error 
    except FileNotFoundError:
        print(color.RED + "File not found. Creating a new file." + color.END)
        return []
    
    # if there is error reading records, then there is this error statement
    except Exception as e:
        print(color.RED+ "Error reading records: " + str(e) + color.END)
        return []
# Function to sort records by ID
def extract_sort_key(record):
    """Extract the key for sorting from the record."""
    return int(record[0])

def sort_records(records):
    """Sort records based on the first field as an integer."""
    # Initialize a new list for valid records
    valid_records = []
    
    # Iterate over records and filter out invalid ones
    for record in records:
        if record[0].strip().isdigit():  # Check if the first element is a valid number
            valid_records.append(record)  # Add to valid_records if valid

    # Sort the valid records using the extract_sort_key function
    return sorted(valid_records, key=extract_sort_key)

def read_a_records():
    try:
        # Opens the file and reads records
        file = open("admin_records.txt", 'r')
        return [line.strip().split(',') for line in file]
    # if the file is not found, it prints an error 
    except FileNotFoundError:
        print(color.RED + "File not found. Creating a new file." + color.END)
        return []
    
    # if there is error reading records, then there is this error statement
    except Exception as e:
        print(color.RED+ "Error reading records: " + str(e) + color.END)
        return []
##
##

# Function to write records to the file
def write_records(records):
    try:
        #opens file
        file = open(file_text, 'w')
        # writes to the file 
        for record in records:
            file.write(','.join(record) + '\n')
        print(color.BOLD + "Records written to file successfully." + color.END)
    except Exception as e:
        print("Error writing records: " + str(e))


#customer functions

#function that will deposit money into the bank account
def deposit(records):
    clear_screen(screen)
    #images used in the code
    textboxTemp = [["┏━━━━━━━━━━━━━━━━━━━━━┓"],
                   ["┃                     ┃"],
                   ["┃                     ┃"],
                   ["┃                     ┃"],
                   ["┗━━━━━━━━━━━━━━━━━━━━━┛"]]
                   
    textbox1Temp = [["┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓"],
                    ["┃                              ┃"],
                    ["┃                              ┃"],
                    ["┃                              ┃"],
                    ["┃                              ┃"],
                    ["┃                              ┃"],
                    ["┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛"]]


    textbox_img = text_to_list(textboxTemp)
    bigtextbox_img = text_to_list(textbox1Temp)
    selectmon_img = mapping(1,"limit: 300")
    
    clear_screen(screen)
    
    edit_screen(textbox_img,8,22,screen)
    edit_screen(textbox_img,8,30,screen)
    edit_screen(textbox_img,38,22,screen)
    edit_screen(textbox_img,38,30,screen)
    edit_screen(textbox_img,69,22,screen)
    edit_screen(textbox_img,69,30,screen)
    
    edit_screen(bigtextbox_img,34,11,screen)
    edit_screen(selectmon_img,(100-len(selectmon_img[0]))//2,5,screen)
    
    one = mapping(1,"1")
    five = mapping(1,"5")
    ten = mapping(1,"10")
    twenty = mapping(1,"20")
    fifty = mapping(1,"50")
    hundred = mapping(1,"100")
    
    done_img = mapping(0,"done")
    
    plus_img = mapping(0,"+")
    minus_img = mapping(0,"-")
    
    edit_screen(one,(23-len(one[0]))//2+9,23,screen)
    edit_screen(twenty,(23-len(twenty[0]))//2+9,31,screen)
    edit_screen(five,(23-len(five[0]))//2+39,23,screen)
    edit_screen(fifty,(23-len(fifty[0]))//2+39,31,screen)
    edit_screen(ten,(23-len(ten[0]))//2+70,23,screen)
    edit_screen(hundred,(23-len(hundred[0]))//2+70,31,screen)
    edit_screen(done_img,(100-len(done_img[0]))//2,36,screen)
    
    edit_screen(plus_img,27,14,screen)
    edit_screen(minus_img,70,14,screen)
    
    print_screen(screen)
    
    #variable to store money numb with a limit of 300
    money = 0
    
    sign1 = True
    
    
    
    #will run until the user has decided the mon they want to deposit
    while True:
        moneystr = str(money)
        
        #adds extra zeros infront of the string depending if it is a one digit or two digit number
        if money < 10:
            moneystr = "00" + str(money)
        elif 100 > money > 9:
            moneystr = "0" + str(money)
        
        #will make the img out of the current mon of money
        money_imgtemp = mapping(1,"444")
        money_img = mapping(1,moneystr)
        
        
        clear_img(len(money_imgtemp),len(money_imgtemp[0]),(31-len(money_imgtemp[0]))//2+35,13,screen)
        
        #adds the img to the screen in the correct place
        edit_screen(money_img,(31-len(money_img[0]))//2+35,13,screen)
        
        print_screen(screen)
    
        amount = button([len(plus_img),5,5,5,5,5,5,len(done_img),len(minus_img)],[len(plus_img[0]),23,23,23,23,23,23,len(done_img[0]),len(minus_img[0])],[27,8,8,38,38,69,69,(100-len(done_img[0]))//2,70],[14,22,30,22,30,22,30,36,14],9,["1","2","3","4","5","6","7","8","9"],screen)
        
        #if statements depeendent the amouint of mooney they want to increase or decrease by
        if amount == "1":
            sign1 = True
            
        elif amount == "2":
            if sign1 == True and money + 1 <= 300:
                money = money + 1
            elif sign1 == False and money - 1 >= 0:
                money = money - 1
            
        elif amount == "3":
            if sign1 == True and money + 20 <= 300:
                money = money + 20
            elif sign1 == False and money - 20 >= 0:
                money = money - 20
        elif amount == "4":
            if sign1 == True and money + 5 <= 300:
                money = money + 5
            elif sign1 == False and money - 5 >= 0:
                money = money - 5
        elif amount == "5":
            if sign1 == True and money + 50 <= 300:
                money = money + 50
            elif sign1 == False and money - 50 >= 0:
                money = money - 50
        elif amount == "6":
            if sign1 == True and money + 10 <= 300:
                money = money + 10
            elif sign1 == False and money - 10 >= 0:
                money = money - 10
        elif amount == "7":
            if sign1 == True and money + 100 <= 300:
                money = money + 100
            elif sign1 == False and money - 100 >= 0:
                money = money - 100
            
        elif amount == "8":
            break
        
        elif amount == "9":
            sign1 = False
            

    if 0 < money:
        records[b][3] = str(money+int(records[b][3]))
        transfer = records[b][1] + " Deposited " + str(money)
        history.append(transfer)
    
    time.sleep(0.5)

#code to display the records of the user
def display_single_records(records,b):
    clear_screen(screen)

    #prints the customer records, all the values in the text file
    id1 = mapping(0,(records[b][0]).lower())
    name1 = mapping(0,(records[b][1]).lower())
    email1 = mapping(0,(records[b][2]).lower())
    bal1 = mapping(0,(records[b][3]).lower())
    
    id2 = mapping(0,"id:")
    name2 = mapping(0,"name:")
    email2 = mapping(0,"email:")
    bal2 = mapping(0,"balance:")
    
    
    edit_screen(id1,(100-len(id1[0]))//2,8,screen)
    edit_screen(id2,(100-len(id2[0]))//2,5,screen)
    edit_screen(name1,(100-len(name1[0]))//2,16,screen)
    edit_screen(name2,(100-len(name2[0]))//2,13,screen)
    edit_screen(email1,(100-len(email1[0]))//2,24,screen)
    edit_screen(email2,(100-len(email2[0]))//2,21,screen)
    edit_screen(bal1,(100-len(bal1[0]))//2,34,screen)
    edit_screen(bal2,(100-len(bal2[0]))//2,29,screen)
    
    print_screen(screen)
    time.sleep(5)
    
#code to withdrawl amount of money 
def withdrawal(records,b,screen):
    clear_screen(screen)
    #images used in the code
    
    textboxTemp = [["┏━━━━━━━━━━━━━━━━━━━━━┓"],
                   ["┃                     ┃"],
                   ["┃                     ┃"],
                   ["┃                     ┃"],
                   ["┗━━━━━━━━━━━━━━━━━━━━━┛"]]
                   
    textbox1Temp = [["┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓"],
                    ["┃                              ┃"],
                    ["┃                              ┃"],
                    ["┃                              ┃"],
                    ["┃                              ┃"],
                    ["┃                              ┃"],
                    ["┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛"]]


    textbox_img = text_to_list(textboxTemp)
    bigtextbox_img = text_to_list(textbox1Temp)
    selectmon_img = mapping(0,"limit: 999")
    currentbal = mapping(0,"current bal:")
    currentbalance = mapping(0,str(records[b][3]))
    
    
    
    clear_screen(screen)
    
    edit_screen(currentbal,(100-len(currentbal[0]))//2,5,screen)
    edit_screen(currentbalance,(100-len(currentbalance[0]))//2,8,screen)
    
    edit_screen(textbox_img,8,22,screen)
    edit_screen(textbox_img,8,30,screen)
    edit_screen(textbox_img,38,22,screen)
    edit_screen(textbox_img,38,30,screen)
    edit_screen(textbox_img,69,22,screen)
    edit_screen(textbox_img,69,30,screen)
    
    edit_screen(bigtextbox_img,34,11,screen)
    edit_screen(selectmon_img,(100-len(selectmon_img[0]))//2,2,screen)
    
    one = mapping(1,"1")
    five = mapping(1,"5")
    ten = mapping(1,"10")
    twenty = mapping(1,"20")
    fifty = mapping(1,"50")
    hundred = mapping(1,"100")
    
    done_img = mapping(0,"done")
    
    plus_img = mapping(0,"+")
    minus_img = mapping(0,"-")
    
    edit_screen(one,(23-len(one[0]))//2+9,23,screen)
    edit_screen(twenty,(23-len(twenty[0]))//2+9,31,screen)
    edit_screen(five,(23-len(five[0]))//2+39,23,screen)
    edit_screen(fifty,(23-len(fifty[0]))//2+39,31,screen)
    edit_screen(ten,(23-len(ten[0]))//2+70,23,screen)
    edit_screen(hundred,(23-len(hundred[0]))//2+70,31,screen)
    edit_screen(done_img,(100-len(done_img[0]))//2,36,screen)
    
    edit_screen(plus_img,27,14,screen)
    edit_screen(minus_img,70,14,screen)
    
    print_screen(screen)
    
    #variable to store money numb with a limit of 300
    money = 0
    
    sign1 = True
    
    
    
    #will run until the user has decided the mon they want to deposit
    while True:
        moneystr = str(money)
        
        #adds extra zeros infront of the string depending if it is a one digit or two digit number
        if money < 10:
            moneystr = "00" + str(money)
        elif 100 > money > 9:
            moneystr = "0" + str(money)
        
        #will make the img out of the current mon of money
        money_imgtemp = mapping(1,"444")
        money_img = mapping(1,moneystr)
        
        
        clear_img(len(money_imgtemp),len(money_imgtemp[0]),(31-len(money_imgtemp[0]))//2+35,13,screen)
        
        #adds the img to the screen in the correct place
        edit_screen(money_img,(31-len(money_img[0]))//2+35,13,screen)
        
        print_screen(screen)
        
        screentemp = screen.copy()

        
        amount = button([len(plus_img),5,5,5,5,5,5,len(done_img),len(minus_img)],[len(plus_img[0]),23,23,23,23,23,23,len(done_img[0]),len(minus_img[0])],[27,8,8,38,38,69,69,(100-len(done_img[0]))//2,70],[14,22,30,22,30,22,30,36,14],9,["1","2","3","4","5","6","7","8","9"],screen)
        
        #if statements depeendent the amouint of mooney they want to increase or decrease by
        if amount == "1":
            sign1 = True
            
        elif amount == "2":
            if sign1 == True and money + 1 <= 999:
                money = money + 1
            elif sign1 == False and money - 1 >= 0:
                money = money - 1
            
        elif amount == "3":
            if sign1 == True and money + 20 <= 999:
                money = money + 20
            elif sign1 == False and money - 20 >= 0:
                money = money - 20
        elif amount == "4":
            if sign1 == True and money + 5 <= 999:
                money = money + 5
            elif sign1 == False and money - 5 >= 0:
                money = money - 5
        elif amount == "5":
            if sign1 == True and money + 50 <= 999:
                money = money + 50
            elif sign1 == False and money - 50 >= 0:
                money = money - 50
        elif amount == "6":
            if sign1 == True and money + 10 <= 999:
                money = money + 10
            elif sign1 == False and money - 10 >= 0:
                money = money - 10
        elif amount == "7":
            if sign1 == True and money + 100 <= 999:
                money = money + 100
            elif sign1 == False and money - 100 >= 0:
                money = money - 100
            
        elif amount == "8":
            if money <= int(records[b][3]) and money != 0:
                records[b][3] = str(int(records[b][3])-money)
                transfer = records[b][1] + " Withdrew " + str(money)
                history.append(transfer)
                break
            if money == 0:
                break
                
            else:
                
                clear_screen(screen)
                
                toomuch = mapping(0,"withdrew too much")
                
                edit_screen(toomuch,(100-len(toomuch[0]))//2,19,screentemp)
                
                print_screen(screentemp)
                
                time.sleep(1.75)
                
                clear_screen(screen)
                
                edit_screen(currentbal,(100-len(currentbal[0]))//2,5,screen)
                edit_screen(currentbalance,(100-len(currentbalance[0]))//2,8,screen)
                
                edit_screen(textbox_img,8,22,screen)
                edit_screen(textbox_img,8,30,screen)
                edit_screen(textbox_img,38,22,screen)
                edit_screen(textbox_img,38,30,screen)
                edit_screen(textbox_img,69,22,screen)
                edit_screen(textbox_img,69,30,screen)
                
                edit_screen(bigtextbox_img,34,11,screen)
                edit_screen(selectmon_img,(100-len(selectmon_img[0]))//2,2,screen)
                
                edit_screen(one,(23-len(one[0]))//2+9,23,screen)
                edit_screen(twenty,(23-len(twenty[0]))//2+9,31,screen)
                edit_screen(five,(23-len(five[0]))//2+39,23,screen)
                edit_screen(fifty,(23-len(fifty[0]))//2+39,31,screen)
                edit_screen(ten,(23-len(ten[0]))//2+70,23,screen)
                edit_screen(hundred,(23-len(hundred[0]))//2+70,31,screen)
                edit_screen(done_img,(100-len(done_img[0]))//2,36,screen)
                
                edit_screen(plus_img,27,14,screen)
                edit_screen(minus_img,70,14,screen)
    

                continue
                
        elif amount == "9":
            sign1 = False



#function for transferring terms
def transfer_history(records,b,ids):
    pagenum = 0
    j3 = 0
    
    for i in range(len(records)):
        if str(ids) == str(records[i][0]):
            userNum = i
            break


    while True:
        clear_screen(screen)
        back = mapping(0,"back")
        j1 = 0 + j3
        j2 = 0
        userx =[]
        usery = []
        userheight = []
        userwidth = []
        value = 10
        
        while True:
            if ids != int(records[j1+pagenum*10][0]):
                edit_screen(mapping(0,(records[j1+pagenum*10][1]).lower()),(100-len((mapping(0,(records[j1+pagenum*10][1]).lower()))[0]))//2,3*(j2+1),screen)
                j2 = j2 + 1
                userx.append((100-len((mapping(0,(records[j1+pagenum*10][1]).lower()))[0]))//2)
                usery.append(3*j2)
                userheight.append(2)
                userwidth.append(len((mapping(0,(records[j1+pagenum*10][1]).lower()))[0]))
            elif ids == int(records[j1+pagenum*10][0]):
                j3 = 1
            #gets the amount of the peopele on the last page
            if (len(records)-1)-((pagenum+1)*10) < 0 and (len(records)-1)-((pagenum+1)*10) > -10:
                value = (len(records)-1) - ((len(records)-1)//10)*10
            
            if 3*(j2) == 3*(value):
                break
            
            j1 = j1 +1
                
        
        edit_screen(back,96-len(back[0]),36,screen)
        edit_screen(mapping(0,"next "+str(pagenum+1)+" / "+str(math.ceil((len(records)-1)/10))),4,36,screen)
        
        userx.append(4)
        userx.append(96-len(back[0]))
        usery.append(36)
        usery.append(36)
        
        userheight.append(2)
        userheight.append(2)
        userwidth.append(len(mapping(0,str(pagenum+1)+" / "+str(math.ceil((len(records)-1)/10)))[0]))
        userwidth.append(len(back[0]))
        
        templist = []
        for i in range(len(userx)):
            templist.append(str(i+1))
        
        choice2 = button(userheight,userwidth,userx,usery,len(userx),templist,screen)
        
        if choice2 == templist[-1] and pagenum > 0:
            pagenum = pagenum - 1
            continue
        
        elif choice2 == templist[-2] and pagenum+1 < math.ceil((len(records)-1)/10):
            pagenum = pagenum + 1
            continue
            
        elif choice2 in templist[:-2]:
            break
    
    
    clear_screen(screen)
    #images used in the code
    
    textboxTemp = [["┏━━━━━━━━━━━━━━━━━━━━━┓"],
                   ["┃                     ┃"],
                   ["┃                     ┃"],
                   ["┃                     ┃"],
                   ["┗━━━━━━━━━━━━━━━━━━━━━┛"]]
                   
    textbox1Temp = [["┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓"],
                    ["┃                              ┃"],
                    ["┃                              ┃"],
                    ["┃                              ┃"],
                    ["┃                              ┃"],
                    ["┃                              ┃"],
                    ["┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛"]]


    textbox_img = text_to_list(textboxTemp)
    bigtextbox_img = text_to_list(textbox1Temp)
    selectmon_img = mapping(0,"limit: 3500")
    currentbal = mapping(0,"current bal:")
    currentbalance = mapping(0,str(records[userNum][3]))
    
    
    
    clear_screen(screen)
    
    edit_screen(currentbal,(100-len(currentbal[0]))//2,5,screen)
    edit_screen(currentbalance,(100-len(currentbalance[0]))//2,8,screen)
    
    edit_screen(textbox_img,8,22,screen)
    edit_screen(textbox_img,8,30,screen)
    edit_screen(textbox_img,38,22,screen)
    edit_screen(textbox_img,38,30,screen)
    edit_screen(textbox_img,69,22,screen)
    edit_screen(textbox_img,69,30,screen)
    
    edit_screen(bigtextbox_img,34,11,screen)
    edit_screen(selectmon_img,(100-len(selectmon_img[0]))//2,2,screen)
    
    one = mapping(1,"1")
    five = mapping(1,"1000")
    ten = mapping(1,"10")
    twenty = mapping(1,"20")
    fifty = mapping(1,"50")
    hundred = mapping(1,"100")
    
    done_img = mapping(0,"done")
    
    plus_img = mapping(0,"+")
    minus_img = mapping(0,"-")
    
    edit_screen(one,(23-len(one[0]))//2+9,23,screen)
    edit_screen(twenty,(23-len(twenty[0]))//2+9,31,screen)
    edit_screen(five,(23-len(five[0]))//2+39,23,screen)
    edit_screen(fifty,(23-len(fifty[0]))//2+39,31,screen)
    edit_screen(ten,(23-len(ten[0]))//2+70,23,screen)
    edit_screen(hundred,(23-len(hundred[0]))//2+70,31,screen)
    edit_screen(done_img,(100-len(done_img[0]))//2,36,screen)
    
    edit_screen(plus_img,27,14,screen)
    edit_screen(minus_img,70,14,screen)
    
    print_screen(screen)
    
    #variable to store money numb with a limit of 300
    money = 0
    
    sign1 = True
    
    
    
    #will run until the user has decided the mon they want to deposit
    while True:
        moneystr = str(money)
        
        #adds extra zeros infront of the string depending if it is a one digit or two digit number
        if money < 10:
            moneystr = "000" + str(money)
        elif 100 > money > 9:
            moneystr = "00" + str(money)
        elif 1000 > money > 99:
            moneystr = "0" + str(money)
        
        #will make the img out of the current mon of money
        money_imgtemp = mapping(1,"4444")
        money_img = mapping(1,moneystr)
        
        
        clear_img(len(money_imgtemp),len(money_imgtemp[0]),(31-len(money_imgtemp[0]))//2+35,13,screen)
        
        #adds the img to the screen in the correct place
        edit_screen(money_img,(31-len(money_img[0]))//2+35,13,screen)
        
        print_screen(screen)
        
        screentemp = screen.copy()

        
        amount = button([len(plus_img),5,5,5,5,5,5,len(done_img),len(minus_img)],[len(plus_img[0]),23,23,23,23,23,23,len(done_img[0]),len(minus_img[0])],[27,8,8,38,38,69,69,(100-len(done_img[0]))//2,70],[14,22,30,22,30,22,30,36,14],9,["1","2","3","4","5","6","7","8","9"],screen)
        
        #if statements depeendent the amouint of mooney they want to increase or decrease by
        if amount == "1":
            sign1 = True
            
        elif amount == "2":
            if sign1 == True and money + 1 <= 3500:
                money = money + 1
            elif sign1 == False and money - 1 >= 0:
                money = money - 1
            
        elif amount == "3":
            if sign1 == True and money + 20 <= 3500:
                money = money + 20
            elif sign1 == False and money - 20 >= 0:
                money = money - 20
        elif amount == "4":
            if sign1 == True and money + 1000 <= 3500:
                money = money + 1000
            elif sign1 == False and money - 1000 >= 0:
                money = money - 1000
        elif amount == "5":
            if sign1 == True and money + 50 <= 3500:
                money = money + 50
            elif sign1 == False and money - 50 >= 0:
                money = money - 50
        elif amount == "6":
            if sign1 == True and money + 10 <= 3500:
                money = money + 10
            elif sign1 == False and money - 10 >= 0:
                money = money - 10
        elif amount == "7":
            if sign1 == True and money + 100 <= 3500:
                money = money + 100
            elif sign1 == False and money - 100 >= 0:
                money = money - 100
            
        elif amount == "8":
            if money <= int(records[userNum][3]) and money != 0:
                transfer = records[userNum][1] + " Transfered " + str(money) + " to " + records[pagenum*10+int(choice2)][1]
                records[userNum][3] = str(int(records[userNum][3])-money)
                records[pagenum*10+int(choice2)][3] = str(money+int(records[pagenum*10+int(choice2)][3]))
                history.append(transfer)
                break
            elif money == 0:
                break
            
            else:
                
                clear_screen(screen)
                
                toomuch = mapping(0,"transfered too much")
                
                edit_screen(toomuch,(100-len(toomuch[0]))//2,19,screentemp)
                
                print_screen(screentemp)
                
                time.sleep(1.75)
                
                clear_screen(screen)
                
                edit_screen(currentbal,(100-len(currentbal[0]))//2,5,screen)
                edit_screen(currentbalance,(100-len(currentbalance[0]))//2,8,screen)
                
                edit_screen(textbox_img,8,22,screen)
                edit_screen(textbox_img,8,30,screen)
                edit_screen(textbox_img,38,22,screen)
                edit_screen(textbox_img,38,30,screen)
                edit_screen(textbox_img,69,22,screen)
                edit_screen(textbox_img,69,30,screen)
                
                edit_screen(bigtextbox_img,34,11,screen)
                edit_screen(selectmon_img,(100-len(selectmon_img[0]))//2,2,screen)
                
                edit_screen(one,(23-len(one[0]))//2+9,23,screen)
                edit_screen(twenty,(23-len(twenty[0]))//2+9,31,screen)
                edit_screen(five,(23-len(five[0]))//2+39,23,screen)
                edit_screen(fifty,(23-len(fifty[0]))//2+39,31,screen)
                edit_screen(ten,(23-len(ten[0]))//2+70,23,screen)
                edit_screen(hundred,(23-len(hundred[0]))//2+70,31,screen)
                edit_screen(done_img,(100-len(done_img[0]))//2,36,screen)
                
                edit_screen(plus_img,27,14,screen)
                edit_screen(minus_img,70,14,screen)
                continue
                
        elif amount == "9":
            sign1 = False


#banker functions

#function to display records of each customer
def display_records(records):
    pagenum = 0
    
    #shows every customers details, and can change page with buttons on bottem
    while True:
        #puts every image on screen of current page, and button 
        clear_screen(screen)
        edit_screen(mapping(0,"back"),96-len((mapping(0,"back"))[0]),36,screen)
        edit_screen(mapping(0,"next"),4,36,screen)
        edit_screen(mapping(0,"done"),(100-len((mapping(0,"done"))[0]))//2,36,screen)
        edit_screen(mapping(0,str(pagenum+1)+" / "+str(len(records))),3,1,screen)
        
        #prints the customer records, all the values in the text file
        id1 = mapping(0,(records[pagenum][0]).lower())
        name1 = mapping(0,(records[pagenum][1]).lower())
        email1 = mapping(0,(records[pagenum][2]).lower())
        bal1 = mapping(0,(records[pagenum][3]).lower())
        
        id2 = mapping(0,"id:")
        name2 = mapping(0,"name:")
        email2 = mapping(0,"email:")
        bal2 = mapping(0,"balance:")
        
        
        edit_screen(id1,(100-len(id1[0]))//2,6,screen)
        edit_screen(id2,(100-len(id2[0]))//2,3,screen)
        edit_screen(name1,(100-len(name1[0]))//2,14,screen)
        edit_screen(name2,(100-len(name2[0]))//2,11,screen)
        edit_screen(email1,(100-len(email1[0]))//2,22,screen)
        edit_screen(email2,(100-len(email2[0]))//2,19,screen)
        edit_screen(bal1,(100-len(bal1[0]))//2,30,screen)
        edit_screen(bal2,(100-len(bal2[0]))//2,27,screen)
        
        print_screen(screen)
        
        #button to get what the user wants to, wether it is to get off the screen, go to next page or go back.
        choice3 = button([2,2,2],[len((mapping(0,"back")[0])),len((mapping(0,"next")[0])),len((mapping(0,"done")[0]))],[96-len((mapping(0,"back"))[0]),4,(100-len((mapping(0,"done"))[0]))//2],[36,36,36],3,["1","2","3"],screen)
        
        #will either go back a page forward a page, or go back to selection screen based on what the user choose
        
        if choice3 == "1" and pagenum > 0:
            pagenum = pagenum - 1
            continue
            
        elif choice3 == "2" and pagenum+1 < len(records):
            pagenum = pagenum + 1
            continue
                
        elif choice3 == "3":
            break

def update_balance(records):
    
    clear_screen(screen)
    #gets the id of the customer they wan to change the balance of
    #creates images used in the screen part of the code
    searchTemp = [["┏━━━━━━━━━━━━━━━━━━━━━━━┓"],
                  ["┃                       ┃"],
                  ["┃                       ┃"],
                  ["┃                       ┃"],
                  ["┃                       ┃"],
                  ["┃                       ┃"],
                  ["┗━━━━━━━━━━━━━━━━━━━━━━━┛"]]
    search_img = text_to_list(searchTemp)
    
    enterId_img1 = mapping(1,"enter id")
    enterId_img2 = mapping(1,"of customer")
    enterId_img3 = mapping(1,"to update")
    
    #gets user input for id
    while True:
        
        edit_screen(enterId_img1,(100-len((enterId_img1)[0]))//2,6,screen)
        edit_screen(enterId_img2,(100-len((enterId_img2)[0]))//2,12,screen)
        edit_screen(enterId_img3,(100-len((enterId_img3)[0]))//2,18,screen)
        edit_screen(search_img,(100-len((search_img)[0]))//2,25,screen)
        
        print_screen(screen)
        
        enter_id = input("Input Here: ")
        
        # variables used in the code 
        a=False
        b=0
        
        #checks each user in the record to see if there is one matching the id inputed
        for i in range(len(records)):
            if enter_id == records[i][0]:
                b=i
                a=True
        
        #if an id identical to the one was matched, that customer will be picked
        if a == True:
            #creates images used in the code and updates them
            idcode_img = mapping(1,enter_id)
            
            edit_screen(idcode_img,(100-len((idcode_img)[0]))//2,27,screen)
            print_screen(screen)
            
            time.sleep(1)
            break
        
        if a == False:
            error_screen(screen)
            clear_screen(screen)
            
    #gets the amount they want to change the balance by
    
    clear_screen(screen)
    #images used in the code
    
    textboxTemp = [["┏━━━━━━━━━━━━━━━━━━━━━┓"],
                   ["┃                     ┃"],
                   ["┃                     ┃"],
                   ["┃                     ┃"],
                   ["┗━━━━━━━━━━━━━━━━━━━━━┛"]]
                   
    textbox1Temp = [["┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓"],
                    ["┃                                                                                              ┃"],
                    ["┃                                                                                              ┃"],
                    ["┃                                                                                              ┃"],
                    ["┃                                                                                              ┃"],
                    ["┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛"]]


    textbox_img = text_to_list(textboxTemp)
    bigtextbox_img = text_to_list(textbox1Temp)
    
    for i in range(len(records)):
        if str(enter_id) == str(records[i][0]):
            customerNumb = i
            break
    
    selectmon_img = mapping(0,(records[customerNumb][1]).lower())
    currentbal = mapping(0,"current bal:")
    currentbalance = mapping(0,str(records[customerNumb][3]))
    
    
    
    clear_screen(screen)
    
    edit_screen(currentbal,(100-len(currentbal[0]))//2,5,screen)
    edit_screen(currentbalance,(100-len(currentbalance[0]))//2,8,screen)
    
    edit_screen(textbox_img,8,22,screen)
    edit_screen(textbox_img,8,30,screen)
    edit_screen(textbox_img,38,22,screen)
    edit_screen(textbox_img,38,30,screen)
    edit_screen(textbox_img,69,22,screen)
    edit_screen(textbox_img,69,30,screen)
    
    edit_screen(bigtextbox_img,2,11,screen)
    edit_screen(selectmon_img,(100-len(selectmon_img[0]))//2,2,screen)
    
    one = mapping(1,"1")
    five = mapping(1,"1000")
    ten = mapping(1,"10")
    twenty = mapping(1,"20")
    fifty = mapping(1,"9999")
    hundred = mapping(1,"100")
    
    done_img = mapping(0,"done")
    
    plus_img = mapping(0,"+")
    minus_img = mapping(0,"-")
    
    edit_screen(one,(23-len(one[0]))//2+9,23,screen)
    edit_screen(twenty,(23-len(twenty[0]))//2+9,31,screen)
    edit_screen(five,(23-len(five[0]))//2+39,23,screen)
    edit_screen(fifty,(23-len(fifty[0]))//2+39,31,screen)
    edit_screen(ten,(23-len(ten[0]))//2+70,23,screen)
    edit_screen(hundred,(23-len(hundred[0]))//2+70,31,screen)
    edit_screen(done_img,(100-len(done_img[0]))//2,36,screen)
    
    edit_screen(plus_img,27,19,screen)
    edit_screen(minus_img,70,19,screen)
    
    print_screen(screen)
    
    #variable to store money numb with a limit of 300
    money = 0
    
    sign1 = True
    
    
    
    #will run until the user has decided the mon they want to deposit
    while True:
        moneystr = str(money)
        
        #will make the img out of the current mon of money
        money_img = mapping(1,moneystr)
        
        
        clear_img(len(bigtextbox_img)-2,len(bigtextbox_img[0])-2,3,12,screen)
        
        #adds the img to the screen in the correct place
        edit_screen(money_img,(31-len(money_img[0]))//2+35,12,screen)
        
        print_screen(screen)
        
        screentemp = screen.copy()

        
        amount = button([len(plus_img),5,5,5,5,5,5,len(done_img),len(minus_img)],[len(plus_img[0]),23,23,23,23,23,23,len(done_img[0]),len(minus_img[0])],[27,8,8,38,38,69,69,(100-len(done_img[0]))//2,70],[19,22,30,22,30,22,30,36,19],9,["1","2","3","4","5","6","7","8","9"],screen)
        
        #if statements depeendent the amouint of mooney they want to increase or decrease by
        if amount == "1":
            sign1 = True
            
        elif amount == "2":
            if sign1 == True and money + 1 <= 10000000000000000:
                money = money + 1
            elif sign1 == False and money - 1 >= 0:
                money = money - 1
            
        elif amount == "3":
            if sign1 == True and money + 20 <= 10000000000000000:
                money = money + 20
            elif sign1 == False and money - 20 >= 0:
                money = money - 20
        elif amount == "4":
            if sign1 == True and money + 1000 <= 10000000000000000:
                money = money + 1000
            elif sign1 == False and money - 1000 >= 0:
                money = money - 1000
        elif amount == "5":
            if sign1 == True and money + 9999 <= 10000000000000000:
                money = money + 9999
            elif sign1 == False and money - 9999 >= 0:
                money = money - 9999
        elif amount == "6":
            if sign1 == True and money + 10 <= 10000000000000000:
                money = money + 10
            elif sign1 == False and money - 10 >= 0:
                money = money - 10
        elif amount == "7":
            if sign1 == True and money + 100 <= 10000000000000000:
                money = money + 100
            elif sign1 == False and money - 100 >= 0:
                money = money - 100
    
        #changes the balance of the user    
        elif amount == "8":
            records[customerNumb][3] = str(money)
            break
                
        elif amount == "9":
            sign1 = False
        
    
    clear_screen(screen)
    
    #tells the user balance changed
    
    toomuch1 = mapping(1,"balanced updated")
    toomuch2 = mapping(1,"successfully")
    
    edit_screen(toomuch1,(100-len(toomuch1[0]))//2,17,screen)
    edit_screen(toomuch2,(100-len(toomuch2[0]))//2,21,screen)
    print_screen(screen)
    
    time.sleep(3)

# Function to add a new customer record
def add_record(records):
    
    #gets the id of the new user
    
    clear_screen(screen)

    #creates images used in the screen part of the code
    searchTemp = [["┏━━━━━━━━━━━━━━━━━━━━━━━┓"],
                  ["┃                       ┃"],
                  ["┃                       ┃"],
                  ["┃                       ┃"],
                  ["┃                       ┃"],
                  ["┃                       ┃"],
                  ["┗━━━━━━━━━━━━━━━━━━━━━━━┛"]]
    
    searchTemp2 = [["┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓"],
                  ["                                                                                                "],
                  ["                                                                                                "],
                  ["                                                                                                "],
                  ["                                                                                                "],
                  ["                                                                                                "],
                  ["┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛"]]
    search_img = text_to_list(searchTemp)
    search2_img = text_to_list(searchTemp2)
    
    enterId_img1 = mapping(1,"enter id")
    enterId_img2 = mapping(1,"of new customer")
    
    entername_img1 = mapping(1,"enter first name")
    entername_img2 = mapping(1,"enter last name")
    
    entermail_img = mapping(1,"enter email")
    
    enterbal_img = mapping(1,"enter balance")
    
    or_img = mapping(1,"or")
    #gets user input for id
    while True:
        clear_screen(screen)
        edit_screen(enterId_img1,(100-len((enterId_img1)[0]))//2,12,screen)
        edit_screen(enterId_img2,(100-len((enterId_img2)[0]))//2,18,screen)
        edit_screen(search_img,(100-len((search_img)[0]))//2,25,screen)
        
        print_screen(screen)
        
        enter_id = input("Input Here: ")
        # variables used in the code 
        a=False
        
        templist = []
        #checks each user in the record to see if there is one matching the id inputed
        for i in range(len(records)):
            templist.append(records[i][0])
        
        if (enter_id not in templist) and (len(enter_id) == 4) and (enter_id.isdigit() == True):
                a=True
                
        if a == True:
            edit_screen(mapping(1,enter_id),(100-len((mapping(1,enter_id))[0]))//2,27,screen)
            print_screen(screen)
            break
        elif a == False:
            #clears screen
            clear_screen(screen)
            
            error_img1 = mapping(1,"is in use")
            error_img2 = mapping(1,"not 4 characters")
            error_img3 = mapping(1,"not all numbers")

            
            #prints error img
            edit_screen(error_img1,(100-len(error_img1[0]))//2,10,screen)
            edit_screen(or_img,(100-len(or_img[0]))//2,14,screen)
            edit_screen(error_img2,(100-len(error_img2[0]))//2,18,screen)
            edit_screen(or_img,(100-len(or_img[0]))//2,22,screen)
            edit_screen(error_img3,(100-len(error_img3[0]))//2,26,screen)
            print_screen(screen)
            
            time.sleep(3)
            
    time.sleep(2) 
    #gets the name of the new user
    
    #gets first name of user only useing characters of the english alphabet
    while True:
        clear_screen(screen)
        edit_screen(entername_img1,(100-len((entername_img1)[0]))//2,12,screen)
        edit_screen(enterId_img2,(100-len((enterId_img2)[0]))//2,18,screen)
        edit_screen(search2_img,(100-len((search2_img)[0]))//2,25,screen)
        
        print_screen(screen)
        firstname = input("Input Here: ").lower()
        
        firstname = firstname[0].upper() + firstname[1:]

        
        if firstname.isalpha() and 0 < len(firstname) <= 16:
            edit_screen(mapping(1,firstname.lower()),(100-len((mapping(1,firstname.lower()))[0]))//2,27,screen)
            print_screen(screen)
            break
        
        else:
             #clears screen
            clear_screen(screen)
            error_img4 = mapping(1,"not all letters")
            error_img5 = mapping(1,"more than 16 chars")
            error_img6 = mapping(1,"0 character name")

            
            #prints error img
            edit_screen(error_img4,(100-len(error_img4[0]))//2,10,screen)
            edit_screen(or_img,(100-len(or_img[0]))//2,14,screen)
            edit_screen(error_img5,(100-len(error_img5[0]))//2,18,screen)
            edit_screen(or_img,(100-len(or_img[0]))//2,22,screen)
            edit_screen(error_img6,(100-len(error_img6[0]))//2,26,screen)
            print_screen(screen)
            
            time.sleep(3)
            
    time.sleep(2)
    
    #gets last name of user only useing characters of the english alphabet
    while True:
        clear_screen(screen)
        
        edit_screen(entername_img2,(100-len((entername_img2)[0]))//2,12,screen)
        edit_screen(enterId_img2,(100-len((enterId_img2)[0]))//2,18,screen)
        edit_screen(search2_img,(100-len((search2_img)[0]))//2,25,screen)
        
        print_screen(screen)
        
        lastname = input("Input Here: ").lower()
        lastname = lastname[0].upper() + lastname[1:]
        
        if lastname.isalpha() and 0 < len(lastname) <= 16:
            edit_screen(mapping(1,lastname.lower()),(100-len((mapping(1,lastname.lower()))[0]))//2,27,screen)
            print_screen(screen)
            break
        
        else:
             #clears screen
            clear_screen(screen)
            error_img4 = mapping(1,"not all letters")
            error_img5 = mapping(1,"more than 16 chars")
            error_img6 = mapping(1,"0 character name")

            
            #prints error img
            edit_screen(error_img4,(100-len(error_img4[0]))//2,10,screen)
            edit_screen(or_img,(100-len(or_img[0]))//2,14,screen)
            edit_screen(error_img5,(100-len(error_img5[0]))//2,18,screen)
            edit_screen(or_img,(100-len(or_img[0]))//2,22,screen)
            edit_screen(error_img6,(100-len(error_img6[0]))//2,26,screen)
            print_screen(screen)
            
            time.sleep(3)
    
    time.sleep(2)
    
    #gets the email of the user with only english characters, with the person having @gmail.com
    while True:
        clear_screen(screen)
        
        edit_screen(entermail_img,(100-len((entermail_img)[0]))//2,12,screen)
        edit_screen(enterId_img2,(100-len((enterId_img2)[0]))//2,18,screen)
        edit_screen(search2_img,(100-len((search2_img)[0]))//2,25,screen)
        print_screen(screen)
        
        email = input("Input Here: (Include '@gmail.com')").lower()
        
        if email[-10:] == "@gmail.com" and email[:-10].isalpha() and 0 < len(email[:-10]) <= 16:
            edit_screen(mapping(1,email[:-10]),(100-len((mapping(1,email[:-10]))[0]))//2,27,screen)
            edit_screen(mapping(1,"@gmail.com"),(100-len((mapping(1,"@gmail.com"))[0]))//2,32,screen)
            print_screen(screen)
            break
        else:
             #clears screen
            clear_screen(screen)
            error_img4 = mapping(1,"not all letters")
            error_img7= mapping(0,"start more than 16 chars")
            error_img8 = mapping(1,"forgot @gmail.com")

            
            #prints error img
            edit_screen(error_img4,(100-len(error_img4[0]))//2,10,screen)
            edit_screen(or_img,(100-len(or_img[0]))//2,14,screen)
            edit_screen(error_img7,(100-len(error_img7[0]))//2,18,screen)
            edit_screen(or_img,(100-len(or_img[0]))//2,22,screen)
            edit_screen(error_img8,(100-len(error_img8[0]))//2,26,screen)
            print_screen(screen)
            
            time.sleep(3)
            
    time.sleep(2)
    
    #gets balance of the user
    while True:
        clear_screen(screen)
        
        edit_screen(enterbal_img,(100-len((enterbal_img)[0]))//2,12,screen)
        edit_screen(enterId_img2,(100-len((enterId_img2)[0]))//2,18,screen)
        edit_screen(search2_img,(100-len((search2_img)[0]))//2,25,screen)
        print_screen(screen)
        
        balance = input("Input Here: ")
        
        if balance.isdigit() and len(balance) <= 16 and "." not in balance.split():
            edit_screen(mapping(1,balance),(100-len((mapping(1,balance))[0]))//2,27,screen)
            print_screen(screen)
            break
        
        else:
            #clears screen
            clear_screen(screen)
            error_img9 = mapping(1,"not all postive numbs")
            error_img10 = mapping(1,"more than 16 digits")
            
            #prints error img
            edit_screen(error_img9,(100-len(error_img9[0]))//2,14,screen)
            edit_screen(or_img,(100-len(or_img[0]))//2,18,screen)
            edit_screen(error_img10,(100-len(error_img10[0]))//2,22,screen)

            print_screen(screen)
            
            time.sleep(3)
            
    time.sleep(2)
    
    records.append([enter_id, (firstname +" "+lastname), email, balance])
    
    #updates records succefully.
    toomuch1 = mapping(1,"new record")
    toomuch2 = mapping(1,"added successfully")
    clear_screen(screen)
    
    edit_screen(toomuch1,(100-len(toomuch1[0]))//2,17,screen)
    edit_screen(toomuch2,(100-len(toomuch2[0]))//2,21,screen)
    print_screen(screen)
    
    time.sleep(3)

def searchID(records):
    #gets the id of the new user
    clear_screen(screen)

    #creates images used in the screen part of the code
    searchTemp = [["┏━━━━━━━━━━━━━━━━━━━━━━━┓"],
                  ["┃                       ┃"],
                  ["┃                       ┃"],
                  ["┃                       ┃"],
                  ["┃                       ┃"],
                  ["┃                       ┃"],
                  ["┗━━━━━━━━━━━━━━━━━━━━━━━┛"]]
    
    search_img = text_to_list(searchTemp)

    
    enterId_img1 = mapping(1,"enter id")
    enterId_img2 = mapping(1,"of customer")

    
    or_img = mapping(1,"or")
    #gets user input for id
    while True:
        clear_screen(screen)
        edit_screen(enterId_img1,(100-len((enterId_img1)[0]))//2,12,screen)
        edit_screen(enterId_img2,(100-len((enterId_img2)[0]))//2,18,screen)
        edit_screen(search_img,(100-len((search_img)[0]))//2,25,screen)
        
        print_screen(screen)
        
        enter_id = input("Input Here: ")
        # variables used in the code 
        a=False
        
        templist = []
        #checks each user in the record to see if there is one matching the id inputed
        for i in range(len(records)):
            templist.append(records[i][0])
        
        if (enter_id in templist) and (len(enter_id) == 4) and (enter_id.isdigit() == True):
                a=True
                
        if a == True:
            edit_screen(mapping(1,enter_id),(100-len((mapping(1,enter_id))[0]))//2,27,screen)
            print_screen(screen)
            break
        elif a == False:
            #clears screen
            clear_screen(screen)
            
            error_img1 = mapping(1,"not in use")
            error_img2 = mapping(1,"not 4 characters")
            error_img3 = mapping(1,"not all numbers")

            
            #prints error img
            edit_screen(error_img1,(100-len(error_img1[0]))//2,10,screen)
            edit_screen(or_img,(100-len(or_img[0]))//2,14,screen)
            edit_screen(error_img2,(100-len(error_img2[0]))//2,18,screen)
            edit_screen(or_img,(100-len(or_img[0]))//2,22,screen)
            edit_screen(error_img3,(100-len(error_img3[0]))//2,26,screen)
            print_screen(screen)
            
            time.sleep(3)
            
    time.sleep(2) 
    
    #checks each user in the record to see if there is one matching the id inputed
    for i in range(len(records)):
        if records[i][0] == enter_id:
            customerNumb = i
        

    return customerNumb
    
def delete_record(records, target_id):
    
    #confirms the guy wants to delete
    clear_screen(screen)
    
    confirm = mapping(1,"confirm")
    yes = mapping(1,"yes")
    no = mapping(1,"no")
    
    edit_screen(confirm,(100-len(confirm[0]))//2,14,screen)
    edit_screen(yes,(46-len(yes[0])),20,screen)
    edit_screen(no,54,20,screen)
    
    print_screen(screen)
    
    choice3 = button([3,3],[len(yes[0]),len(no[0])],[(46-len(yes[0])),54],[20,20],2,["yes","no"],screen)
    
    if choice3 == "yes":
        
        for i in range(len(records)):
            if records[target_id][0] == records[i][0]:
                # removes record
                records.remove(records[i])
                break
        
        clear_screen(screen)
        edit_screen(mapping(1,"deleted successfully"),(100-len((mapping(1,"deleted successfully"))[0]))//2,18,screen)
        print_screen(screen)
        time.sleep(2)
        clear_screen(screen)

#shows the transaction history of each everyone
def transaction_history(records):
    #will show the history in the order it happened, everyone included, make it into pages, and have a certain amount per page
    
    pagenum = 0
    
    if len(history) > 0:
        
        while True:
            #puts every image on screen of current page, and button 
            clear_screen(screen)
            edit_screen(mapping(0,"back"),96-len((mapping(0,"back"))[0]),36,screen)
            edit_screen(mapping(0,"next"),4,36,screen)
            edit_screen(mapping(0,"done"),(100-len((mapping(0,"done"))[0]))//2,36,screen)
            edit_screen(mapping(0,str(pagenum+1)+" / "+str(len(history))),3,1,screen)
            
            
            for i in range(len((history[pagenum]).split())):
                edit_screen(mapping(0,(((history[pagenum]).split())[i]).lower()),(100-len((mapping(0,((history[pagenum]).split())[i]))[0]))//2,10+i*3,screen)
                
            print_screen(screen)
            
            #button to get what the user wants to, wether it is to get off the screen, go to next page or go back.
            choice3 = button([2,2,2],[len((mapping(0,"back")[0])),len((mapping(0,"next")[0])),len((mapping(0,"done")[0]))],[96-len((mapping(0,"back"))[0]),4,(100-len((mapping(0,"done"))[0]))//2],[36,36,36],3,["1","2","3"],screen)
            
            #will either go back a page forward a page, or go back to selection screen based on what the user choose
            
            if choice3 == "1" and pagenum > 0:
                pagenum = pagenum - 1
                continue
                
            elif choice3 == "2" and pagenum+1 < len(history):
                pagenum = pagenum + 1
                continue
                    
            elif choice3 == "3":
                break
    
    else:
        #say no transactions have made
        clear_screen(screen)
                
        toomuch1 = mapping(0,"no transactions have")
        toomuch2= mapping(0,"been made")
                
        edit_screen(toomuch1,(100-len(toomuch1[0]))//2,17,screen)
        edit_screen(toomuch2,(100-len(toomuch2[0]))//2,21,screen)
        
        print_screen(screen)
        
        time.sleep(3)

 
##
##

#screens
#prints an error screen using functions i made
def error_screen(screen):
    #clerars screen
    clear_screen(screen)
    
    #makes an error img
    errorTemp = [["███████╗██████╗ ██████╗  █████╗ ██████╗ "],
                 ["██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗"],
                 ["█████╗  ██████╔╝██████╔╝██║  ██║██████╔╝"],
                 ["██╔══╝  ██╔══██╗██╔══██╗██║  ██║██╔══██╗"],
                 ["███████╗██║  ██║██║  ██║╚█████╔╝██║  ██║"],
                 ["╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝ ╚════╝ ╚═╝  ╚═╝"],]
    
    error_img = text_to_list(errorTemp)
    
    #prints error img
    edit_screen(error_img,30,16,screen)
    print_screen(screen)
    
    time.sleep(1.5)

#makes opening screen
def bl_screen(screen):
    #creates the images used in the opening scene
    clear_screen(screen)
    
    blTemp = [["█████████████████████████████████████████████████████████▀█"],
              ["█▄─▄─▀█▄─▄█████▄─▄─▀██▀▄─██▄─▀█▄─▄█▄─█─▄█▄─▄█▄─▀█▄─▄█─▄▄▄▄█"],
              ["██─▄─▀██─██▀████─▄─▀██─▀─███─█▄▀─███─▄▀███─███─█▄▀─██─██▄─█"],
              ["▀▄▄▄▄▀▀▄▄▄▄▄▀▀▀▄▄▄▄▀▀▄▄▀▄▄▀▄▄▄▀▀▄▄▀▄▄▀▄▄▀▄▄▄▀▄▄▄▀▀▄▄▀▄▄▄▄▄▀"]]
    
    bl_img = text_to_list(blTemp)
    
    
    
    enterprisesTemp = [["███████████████████████████████████████████████████████████████████"],
                        ["█▄─▄▄─█▄─▀█▄─▄█─▄─▄─█▄─▄▄─█▄─▄▄▀█▄─▄▄─█▄─▄▄▀█▄─▄█─▄▄▄▄█▄─▄▄─█─▄▄▄▄█"],
                        ["██─▄█▀██─█▄▀─████─████─▄█▀██─▄─▄██─▄▄▄██─▄─▄██─██▄▄▄▄─██─▄█▀█▄▄▄▄─█"],
                        ["▀▄▄▄▄▄▀▄▄▄▀▀▄▄▀▀▄▄▄▀▀▄▄▄▄▄▀▄▄▀▄▄▀▄▄▄▀▀▀▄▄▀▄▄▀▄▄▄▀▄▄▄▄▄▀▄▄▄▄▄▀▄▄▄▄▄▀"]]

    
    enterprises_img = text_to_list(enterprisesTemp)
    
    #prints out the images on the screen
    print_screen(screen)
    time.sleep(0.6)
    edit_screen(bl_img,21,13,screen)
    print_screen(screen)
    
    time.sleep(0.6)
    
    edit_screen(enterprises_img,17,18,screen)
    print_screen(screen)
    
    
    #flashes the images to create an animation effect
    for i in range(2):
        time.sleep(0.4)
        clear_screen(screen)
        print_screen(screen)
        
        time.sleep(0.4)
        edit_screen(bl_img,21,13,screen)
        edit_screen(enterprises_img,17,18,screen)
        print_screen(screen)

#function used to create a screen for the login, either as a customer or banker
def login_screen(screen):
    
    while True:
        #creates imgs used on the screen
        clear_screen(screen)
        
        customerTemp = [["█▀▀█ █  █ █▀▀ ▀▀█▀▀ █▀▀█ █▀▄▀█ █▀▀ █▀▀█"],
                        ["█    █  █ ▀▀█   █   █  █ █ ▀ █ █▀▀ █▄▄▀"],
                        ["█▄▄█  ▀▀▀ ▀▀▀   ▀   ▀▀▀▀ ▀   ▀ ▀▀▀ ▀ ▀▀"]]
        
        bankerTemp = [["█▀▀█ █▀▀█ █▀▀▄ █ █ █▀▀ █▀▀█"],
                      ["█▀▀▄ █▄▄█ █  █ █▀▄ █▀▀ █▄▄▀"],
                      ["█▄▄█ ▀  ▀ ▀  ▀ ▀ ▀ ▀▀▀ ▀ ▀▀"]]
        
        loginTemp = [["██╗      █████╗  ██████╗ ██╗███╗  ██╗"],
                     ["██║     ██╔══██╗██╔════╝ ██║████╗ ██║"],
                     ["██║     ██║  ██║██║  ██╗ ██║██╔██╗██║"],
                     ["██║     ██║  ██║██║  ╚██╗██║██║╚████║"],
                     ["███████╗╚█████╔╝╚██████╔╝██║██║ ╚███║"],
                     ["╚══════╝ ╚════╝  ╚═════╝ ╚═╝╚═╝ ╚══╝ "]]
        
        
        login_img = text_to_list(loginTemp)
        customer_img = text_to_list(customerTemp)
        banker_img = text_to_list(bankerTemp)
        
        #displays the imgs on the screen
        clear_screen(screen)
        edit_screen(login_img,31,9,screen)
        edit_screen(customer_img,30,23,screen)
        edit_screen(banker_img,36,28,screen)
        print_screen(screen)
        
        print("\u001b[31;1mUse 'w'/'s' Or 'a'/'d' To Move The Buttons, And 'q' To Select\u001b[0m")
        print("\u001b[31;1mMake Sure To Click 'Enter' After Each Input\u001b[0m")
        time.sleep(5)
        
        #uses the button function to get whether the user is a customer or banker
        choice1 = button([3,3],[41,29],[29,35],[23,28],2,["customer","banker"],screen)
        
        return choice1
        
        
        
    

# Main menu function to run the program
records = read_records()
records = sort_records(records)

# displays all the options 
records_a = read_a_records()

#Login Part Of The Cod
bl_screen(screen)

#runs the code infinetly as the user could want to use anoither account
while True:
    choice1 = login_screen(screen)
    
    
    #Customer Code
    # creates images used in the screen part of the code
    searchTemp = [["┏━━━━━━━━━━━━━━━━━━━━━━━┓"],
                  ["┃                       ┃"],
                  ["┃                       ┃"],
                  ["┃                       ┃"],
                  ["┃                       ┃"],
                  ["┃                       ┃"],
                  ["┗━━━━━━━━━━━━━━━━━━━━━━━┛"]]
    search_img = text_to_list(searchTemp)
    
    loginTemp = [["██╗      █████╗  ██████╗ ██╗███╗  ██╗"],
                 ["██║     ██╔══██╗██╔════╝ ██║████╗ ██║"],
                 ["██║     ██║  ██║██║  ██╗ ██║██╔██╗██║"],
                 ["██║     ██║  ██║██║  ╚██╗██║██║╚████║"],
                 ["███████╗╚█████╔╝╚██████╔╝██║██║ ╚███║"],
                 ["╚══════╝ ╚════╝  ╚═════╝ ╚═╝╚═╝ ╚══╝ "]]
    login_img = text_to_list(loginTemp)
    
    customerid_img = mapping(0,"customer id: ")
    bankerid_img = mapping(0,"banker id: ")
    
    while True:
        if choice1 == "customer":
            
            #updates the screen to have login and id images
            clear_screen(screen)
            edit_screen(login_img,31,9,screen)
            print_screen(screen)
            time.sleep(0.5)
            
            edit_screen(customerid_img,15,25,screen)
            edit_screen(search_img,62,22,screen)
            print_screen(screen)
            
            #gets user input for id
            enter_id = input("Input Here: ")
            
            # variables used in the code 
            a=False
            b=0
            
            #checks each user in the record to see if there is one matching the id inputed
            for i in range(len(records)):
                if enter_id == records[i][0]:
                    b=i
                    a=True
            
            #if an id identical to the one was matched, that user will be logged in  
            if a == True:
                #creates images used in the code and updates them
                idcode_img = mapping(1,enter_id)
                
                edit_screen(idcode_img,64,24,screen)
                print_screen(screen)
                
                time.sleep(1)
                #while loop to run the code over and voer again
                while True:
                    
                    welcomeTemp = [["██╗       ██╗███████╗██╗      █████╗  █████╗ ███╗   ███╗███████╗"],
                                   ["██║  ██╗  ██║██╔════╝██║     ██╔══██╗██╔══██╗████╗ ████║██╔════╝"],
                                   ["╚██╗████╗██╔╝█████╗  ██║     ██║  ╚═╝██║  ██║██╔████╔██║█████╗  "],
                                   [" ████╔═████║ ██╔══╝  ██║     ██║  ██╗██║  ██║██║╚██╔╝██║██╔══╝  "],
                                   [" ╚██╔╝ ╚██╔╝ ███████╗███████╗╚█████╔╝╚█████╔╝██║ ╚═╝ ██║███████╗"],
                                   ["  ╚═╝   ╚═╝  ╚══════╝╚══════╝ ╚════╝  ╚════╝ ╚═╝     ╚═╝╚══════╝"],]
            
                    clear_screen(screen)
                    welcome_img = text_to_list(welcomeTemp)
                    
            
                    
                    firstName_img = mapping(0,(((records[b][1]).split())[0]).lower())
                    lastName_img = mapping(0,(((records[b][1]).split())[1]).lower())
                    
                    deposit_img = mapping(1,"deposit money")
                    display_img = mapping(1,"display information")
                    withdrawl_img = mapping(1,"withdraw money")
                    transfer_img = mapping(1,"transfer funds")
                    exit_img = mapping(1,"exit")
                    
               
                    
                    edit_screen(welcome_img,18,2,screen)
                    edit_screen(firstName_img,(100 - len(firstName_img[0]))//2,9,screen)
                    edit_screen(lastName_img,(100 - len(lastName_img[0]))//2,12,screen)
                    
                    print_screen(screen)
                    
                    time.sleep(0.5)
                    
                    #prints the options for what the user can do
                    edit_screen(deposit_img,(100 - len(deposit_img[0]))//2,16,screen)
                    edit_screen(display_img,(100 - len(display_img[0]))//2,21,screen)
                    edit_screen(withdrawl_img,(100 - len(withdrawl_img[0]))//2,26,screen)
                    edit_screen(transfer_img,(100 - len(transfer_img[0]))//2,31,screen)
                    edit_screen(exit_img,(100 - len(exit_img[0]))//2,35,screen)
                    
                    print_screen(screen)
                    
                    #user chooses what there choice is
                    choice2 = button([3,3,3,3,3],[60,88,73,63,18],[(100 - len(deposit_img[0]))//2,(100 - len(display_img[0]))//2,(100 - len(withdrawl_img[0]))//2,(100 - len(transfer_img[0]))//2,(100 - len(exit_img[0]))//2],[16,21,26,31,35],5,["1","2","3","4","5"],screen)
                    
                    # read record
                    if choice2 == "1":
                        deposit(records)
                        
                        
                    #displat record 
                    elif choice2 == "2":
                        display_single_records(records,b)
                        
                    
                    #update record
                    elif choice2 == "3":
                        withdrawal(records,b,screen)
                        
                        
                    #add record
                    elif choice2 == "4":
                        transfer_history(records,b,int(enter_id))
                        
                    
                    #exits
                    elif choice2 == "5":
                        break
                
                if choice2 == "5":
                    break
                
            
            elif a == False:
                error_screen(screen)
                
                
            
            
            
        
        elif choice1 == "banker":
            
            #updates the screen to have login and id images
            clear_screen(screen)
            edit_screen(login_img,31,9,screen)
            print_screen(screen)
            time.sleep(0.5)
            
            edit_screen(bankerid_img,15,25,screen)
            edit_screen(search_img,54,22,screen)
            print_screen(screen)
            
            #gets user input for id
            enter_id = input("Input Here: ")
            
            # variables used in the code 
            a=False
            b=0
            
            #checks each user in the record to see if there is one matching the id inputed
            for i in range(len(records_a)):
                if enter_id == records_a[i][1]:
                    b=i
                    a=True
            
            #if an id identical to the one was matched, that user will be logged in  
            if a == True:
                #creates images used in the code and updates them
                idcode_img = mapping(1,enter_id)
                
                edit_screen(idcode_img,56,24,screen)
                print_screen(screen)
                
                time.sleep(1)
                #while loop to run the code over and voer again
                while True:
                    #creates the images to display on the screen

                    clear_screen(screen)
                    welcome_img = mapping(1,"welcome")
                    
                    name_img = mapping(1,(records_a[b][0]).lower())
                    
                    
                    readRec = mapping(0,"read records")
                    displayRec = mapping(0,"display records")
                    updateRec = mapping(0,"update records")
                    addRec = mapping(0,"add record")
                    writeRec = mapping(0,"write records")
                    sortRec = mapping(0,"sort records")
                    searchRec = mapping(0,"search records")
                    deleteRec = mapping(0,"delete record")
                    transactionHis = mapping(0,"transaction history")
                    exit = mapping(0,"exit")
                    
                    #prints all the images on the screen
                    edit_screen(welcome_img,(100-len(welcome_img[0]))//2,1,screen)
                    edit_screen(name_img,(100 - len(name_img[0]))//2,5,screen)
                    
                    print_screen(screen)
                    time.sleep(0.5)
                    
                    edit_screen(readRec,(100 - len(readRec[0]))//2,9,screen)
                    edit_screen(displayRec,(100 - len(displayRec[0]))//2,12,screen)
                    edit_screen(updateRec,(100 - len(updateRec[0]))//2,15,screen)
                    edit_screen(addRec,(100 - len(addRec[0]))//2,18,screen)
                    edit_screen(writeRec,(100 - len(writeRec[0]))//2,21,screen)
                    edit_screen(sortRec,(100 - len(sortRec[0]))//2,24,screen)
                    edit_screen(searchRec,(100 - len(searchRec[0]))//2,27,screen)
                    edit_screen(deleteRec,(100 - len(deleteRec[0]))//2,30,screen)
                    edit_screen(transactionHis,(100 - len(transactionHis[0]))//2,33,screen)
                    edit_screen(exit,(100 - len(exit[0]))//2,36,screen)
                    print_screen(screen)
                    
                    #user chooses what there choice is
                    choice2 = button([2,2,2,2,2,2,2,2,2,2],[len(readRec[0]),len(displayRec[0]),len(updateRec[0]),len(addRec[0]),len(writeRec[0]),len(sortRec[0]),len(searchRec[0]),len(deleteRec[0]),len(transactionHis[0]),len(exit[0])], [(100-len(readRec[0]))//2,(100-len(displayRec[0]))//2,(100-len(updateRec[0]))//2,(100-len(addRec[0]))//2,(100-len(writeRec[0]))//2,(100-len(sortRec[0]))//2,(100-len(searchRec[0]))//2,(100-len(deleteRec[0]))//2,(100-len(transactionHis[0]))//2,(100-len(exit[0]))//2], [9,12,15,18,21,24,27,30,33,36],10,["1","2","3","4","5","6","7","8","9","10"],screen)
                    
                    #read record
                    if choice2 == '1':
                        records = read_records()
                        records = sort_records(records)  # Sort records after reading
                        clear_screen(screen)
                        edit_screen(mapping(1,"file read successfully"),(100-len((mapping(1,"file read successfully"))[0]))//2,18,screen)
                        print_screen(screen)
                        time.sleep(2)
                        clear_screen(screen)
                        continue
                        
                    #displat record 
                    elif choice2 == '2':
                        display_records(records)
                    
                    #update record
                    elif choice2 == '3':
                        update_balance(records)
                        records = sort_records(records)  # Sort records after updating
                        write_records(records)
                   
                    #add record
                    elif choice2 == '4':
                        add_record(records)
                        records = sort_records(records)  # Sort records after adding a new record
                        write_records(records)
                        
                    
                    #write record
                    elif choice2 == '5':
                        write_records(records)
                        clear_screen(screen)
                        edit_screen(mapping(1,"written successfully"),(100-len((mapping(1,"written successfully"))[0]))//2,18,screen)
                        print_screen(screen)
                        time.sleep(2)
                        clear_screen(screen)
                        continue
                    
                    #sort record 
                    elif choice2 == '6':
                        records = sort_records(records)
                        clear_screen(screen)
                        edit_screen(mapping(1,"sorted successfully"),(100-len((mapping(1,"sorted successfully"))[0]))//2,18,screen)
                        print_screen(screen)
                        time.sleep(2)
                        clear_screen(screen)
                        continue
                        
                    
                    #search record
                    elif choice2 == '7':
                        userId1 = searchID(records)
                        display_single_records(records,userId1)
                        
                    
                    #delete record
                    elif choice2 == '8':
                        userId2 = searchID(records)
                        delete_record(records, userId2)
                        records = sort_records(records)  # Sort records after deleting
                        write_records(records)
                    
                    #shows the transaction history of each person
                    elif choice2 == '9':
                        transaction_history(records)
                      
                    #if user presses 9, it breaks and exits
                    elif choice2 == '10':
                        break
                    
                    
                if choice2 == "10":
                    break
                
            
            elif a == False:
                error_screen(screen)