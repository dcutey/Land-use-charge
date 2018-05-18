# Name: Oladeinde Kuti
# Project Title: Lagos State Land Use Charge Calculator
# This program aims to calculate the Land Use Charge
# Welcome user to the Lagos State Land Use Charge Calculator
print("Welcome to the Lagos State Land Use Charge Calculator")
# Ask user to enter the value of the property
propertyvalue=float(input("\n Please type the value of your property and press enter: ₦"))
# Apply the 40% general relief on property value and calculate the relief value
reliefvalue=propertyvalue*0.6
# Ask user to enter the type of the property
propertytype=int(input("\n What type of property do you have (Please type the number option and press enter):\n\n(1)owner occupied only residential\n\n(2)residential without owner in residence,\n commercial (used by occupier for business purposes),\n vacant property and open empty land \n\n(3)owner occupied and third party; industrial and manufacturing purposes:"))
# Apply the 15% discount and calculate the Land Use Charge for owner occupied only residential category
luc1=reliefvalue*0.076*0.85/100
# Apply the 50% discount and calculate the Land Use Charge for residential without owner in residence, commercial (used by occupier for business purposes, vacant property and open empty land category
luc2=reliefvalue*0.76*0.5/100
# Apply the 25% discount and calculate the Land Use Charge for owner occupied and third party; and industrial and manufacturing purposes category
luc3=reliefvalue*0.256*.75/100
# Apply the condition for owner occupied only residential category and print the land use charge
if (propertytype==1) and (luc1>5000):
    print ("\n Your Land Use Charge for the year is ₦{0}".format(round(luc1,2)))
# Apply the minimum amount payable condition
elif (luc1<=5000):
    print("\n Your Land Use Charge for the year is ₦5000")
# Apply the condition for residential without owner in residence, commercial (used by occupier for business purposes, vacant property and open empty land category and print the land use charge
elif (propertytype==2) and (luc2>5000):
    print ("\n Your Land Use Charge for the year is ₦{0}".format(round(luc2,2)))
# Apply the minimum amount payable condition
elif (luc2<=5000):
    print("\n Your Land Use Charge for the year is ₦5000") 
# Apply the condition for Owner Occupied and third party; and industrial and manufacturing purposes category and print the land use charge
elif (propertytype==3) and (luc3>5000):
    print ("\n Your Land Use Charge for the year is ₦{0}".format(round(luc3,2)))
# Apply the minimum amount payable condition           
else:
    print("\n Your Land Use Charge for the year is ₦5000")

print("\n Thank you for being a law abiding citizen! Itesiwaju Ipinle Eko lo je wa l'ogun")
