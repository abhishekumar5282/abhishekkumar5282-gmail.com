import calendar
import datetime as dt


class BirthdayReminderApp:

    """Class which is responsible to provide appropriate message to the user about their Upcoming birthday"""
    
    def __init__(self,Date,dob):
        """Constructor to initliase all the instance variables """
                                        
        self.dob=dob
        self.Birth_year=int(self.dob.split("-")[-1])
        self.Birth_month=int(self.dob.split("-")[-2])
        self.Birth_day=int(self.dob.split("-")[-3])
        self.Current_year=int(Date.split("-")[-1])
        self.Current_month=int(Date.split("-")[-2])
        self.Current_day=int(Date.split("-")[-3])
        self.birthday=dt.datetime(self.Current_year,self.Birth_month,self.Birth_day)

        #List that stores the Names of the days in the week and returns the Name of the day when provided with the index
        self.weekdays=["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
        
    def get_no_of_days(self):
        """ Member function that returns the differnce in days between the Current date and the Birth date"""
        
        CurrentDate=dt.datetime(self.Current_year,self.Current_month,self.Current_day)
        BirthDate=dt.datetime(self.Current_year,self.Birth_month,self.Birth_day)

        #Intializing the difference in days to zero
        diffdays=0

        #Difference is to be calculated only if Current date and Birth date are unidentical
        
        if(CurrentDate!=BirthDate):
            difference=str(BirthDate-CurrentDate)
            diffdays=int(difference.split(" ")[0])
            
        return diffdays    
            

    def days_remaining(self,diffdays,birthweekday):
        """Member function that returns the number of days remaining when the Birthday is yet to come"""

        #Empty String
        
        message=" "

        #If birthday is on the present day
        if(diffdays==0):
            message="Today"
            
        elif(diffdays>=28):
    
            if(diffdays>=28 and diffdays<=30):
                if(self.Current_day==self.Birth_day):
                    message="Next month"
                else:    
                    message=str(diffdays)+" days from now"
                    
            #When difference is more than 30 days
            elif(diffdays>30):
                noofmonths=self.Birth_month-self.Current_month;
                if(noofmonths==1):
                    message="Next month"
                else:    
                    message=str(abs(noofmonths))+" months from now "

            
        elif(diffdays>=14 and diffdays<28):
            noofweeks=diffdays//7;
            if(diffdays>20):
                
                if(diffdays%7==0):
                    message=str(noofweeks)+" weeks from now "
                else:
                   message="After "+ str(noofweeks) +" weeks"

            elif(diffdays<=20):
                if(diffdays%7==0):
                    message=str(noofweeks)+" weeks from now "
                else:
                    message=str(diffdays)+" days from now "
                
        elif(diffdays>=7 and diffdays<=13):
            
            message="Next "+ birthweekday

        elif(diffdays<7):

            if(diffdays==2):
                message="Day after tomorrow"
            elif(diffdays==1):
               message="Tomorrow"
            else:
                message="Coming "+birthweekday
                
        return message       

    def days_passed(self,diffdays,birthweekday):
        """Member function that returns the number of days already passed when the Birthday is already passed"""

        message=" "

        #Getting the abs value of diffdays
        diffdays*=-1;

        
        if(diffdays>=28):
            
            if(diffdays>=28 and diffdays<=30):
                message=" Almost a month ago"

            #When difference is more than 30 days    
            elif(diffdays>30):
                noofmonths=self.Current_month-self.Birth_month;
                if(noofmonths==1):
                    message="Last month"
                else:    
                    message=str(noofmonths) +" months ago "
               
        elif(diffdays>=14 and diffdays<28):
            noofweeks=diffdays//7;
            message=str(noofweeks)+ " weeks ago"
                
        elif(diffdays>=7 and diffdays<=13):
            if(diffdays==7):
               message="Last "+birthweekday
            else:
               message="In the Last week"


        elif(diffdays<7):
            if(diffdays==2):
                message="Day before Yesterday"
            elif(diffdays==1):
                message="Yesterday"
            else:
                message=str(diffdays) +" days back"
                
        return message

         
    def comparator(self,diffdays):
        """Member function that compares difference in number of days and checks whether the Birthday is yet to come or has already passed ,and accordingly returns a message to the user """

        #Getting the day number in the week
        dayindex=self.birthday.weekday()
        birthweekday=self.weekdays[dayindex]

        #Forming the common part to be appended to the final message
        concatmessage=" on "+birthweekday+", "+str(self.Birth_day)+"th of March"
        message=" "
        if(diffdays>=0):
            message=self.days_remaining(diffdays,birthweekday)
            
        elif(diffdays<0):
            message=self.days_passed(diffdays,birthweekday)

        #appending the common part to the final message
        return message.strip()+concatmessage             
