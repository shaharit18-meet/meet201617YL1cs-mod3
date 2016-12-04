
#This script performs some simple tests on the UserAccount class.

import UserAccount

#Three things are missing from the line below - fill them in
my_user=UserAccount("shaharit18- meet", "meetyear18" , "my secret")

#Call the print_secret method (function) - it takes one input - a guess for the password.

my_user.print_secret("meetyear18")


#Use the wrong password as input here
my_user.password("meetyear17")
#Use the right password here
my_user.password("meetyear18")

