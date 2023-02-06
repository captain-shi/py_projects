''' ###########################################
#####################################@Captain######################
####################################################################
################################################################ '''

'''  
    BMI calculator
The program calculates the body-mass index of a person
'''
Name = input('Enter your name')    #Getting the user's name

Height = float(input('Enter height in meters'))    #User's height in meters

Weight = int(input('Enter weight in Kilogrammes'))       #User's weight

def bmi_calc(Name,Height,Weight):       #Function with three arguments;name, height, weight

    BMI = Weight / (Height ** 2)
    
    print('client'+ Name + ":",'BMI is ', BMI, end='\n')
  
#Conclusion section
    if BMI < 25:
        print('client' + Name + ' is not overweight')
    else:
        print('client'+ Name +' is overweight', end='\n')
        
        print('client'+ Name +' needs to reduce weight')
        
Result = bmi_calc(Name, Height, Weight)
 
