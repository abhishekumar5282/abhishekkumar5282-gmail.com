import pytest
from Driver import driver as d

#Empty List
test_data=list()

#Fetching the Test cases from the file
with open('test_cases.txt') as FH:
    counter=0
    for line in FH:
        counter+=1;
        if(counter>=3):
            Date=(line.split("|")[0]);
            message=(line.split("|")[1]);
            test_data.append((Date.strip(),message.strip()))


#Creating instance of the driver class
ob=d()

def message(Curdate,dob):
    """simple function that returns the message fetched from the BirthdayReminderApp class"""
    
    return ob.start(Curdate,dob).strip()


@pytest.mark.parametrize('Curdate,Res',test_data)
def test_one(Curdate,Res):
    """Function that passes all the test cases to the Start method of the Driver class"""
    
    act=message(Curdate,"15-03-1995")
    assert act==Res

    
    
    
