from Birthday import BirthdayReminderApp as bd
import datetime as dt

class driver:
    """ Driver class that uses th bIrthdayReminderApp class to fetch proper message for the user"""
    
    def get_todays_date(self):
        """Method used to fetch current date from the system"""
        
        date=str(dt.datetime.today())
        raw_date=date.split(" ")[0]
        Day=raw_date.split("-")[-1]
        Month=raw_date.split("-")[-2]
        Year=raw_date.split("-")[-3]
        todays_date=Day+"-"+Month+"-"+Year
        return todays_date
        

    def display(self,message):
        """Simple display function to display the results to the user"""
        
        print(message)

    def start(self,Date,dob):
        """Simple method that is used to implement the test_cases"""
        
        ob1=bd(Date,dob)
        diffdays=ob1.get_no_of_days()
        message=ob1.comparator(diffdays)
        return message
        
          

if(__name__=="__main__"):
    driv=driver()
    Date=input("Enter the current date in dd-mm-yyyy")
    dob=input("Enter the Date of birth  in dd-mm-yyyy")
    if(Date.split("-")[-1]==dob.split("-")[-1]):
        print("Year of birth cannot be same as current year")
    else:    
        ob1=bd(Date,dob)
        diffdays=ob1.get_no_of_days()
        message=ob1.comparator(diffdays)
        driv.display(message)
