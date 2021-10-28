import sys
import os
########################
'''created a class pd for using date-time operations'''
class pd(object):
    def __init__(self,time):
        self.time=list(map(int,time.split(':')))
        self.time_tuple=tuple(map(int,time.split(':')))
    def get_time(self):
        return(self.time)
    def set_time(self,new_time):
        self.time=new_time
    def __eq__(self, other):
        if self.get_time()==other.get_time():
            return True
        else:
            return False
    def __ne__(self, other):
        return(not(self.__eq__(other)))
    def __le__(self,other):
        self_time_in_min=(self.get_time()[0])*60+self.get_time()[1]
        other_time_in_min=(other.get_time()[0])*60+other.get_time()[1]
        if self_time_in_min<=other_time_in_min:
            return True
        else:
            return False
    def minute(self):
        return(self.get_time()[1])
    def __add__(self,other):       ###### adds only 15min irrespective of given value-"other"
        time=self.get_time().copy()
        if time[1]+15<60:
            time[1]=time[1]+15
        else:
            time[1]=time[1]+15
            time[0]=time[0]+time[1]//60
            time[1]=time[1]%60
        new_time=str(time[0])+":"+str(time[1])
        return(pd(new_time))
    def __hash__(self):
        return hash(self.time_tuple)
    
########################
'''creating a dict for each meeting_room where keys are time-intervals
   in a day and value is 1 if occupied or 0 if unoccupies, here default
   value for last 15min of the day is 1'''
   
def stack():
    start=pd("00:00")
    change=pd('00:15')
    d={}
    for i in range(96):
        d[(start,start+change)]=0
        start=start+change
    d[-1]=1
    return(d)

d=stack()

   
########################
'''creating a class meeting_room to create instances for each type
   of meting room with name,capacity and slot(avaliability 1/0) at
   all 15min timeIntervals of the day'''

class meeting_room(object):
    def __init__(self, Name, person_Capacity):
        self.name = Name
        self.capacity = person_Capacity
        self.slot = d.copy()
        
    def get_name(self):
        return(self.name)

    def get_capacity(self):
        return(self.capacity)
    
    def get_slot(self):
        return(self.slot)
    
    def isvacant(self,start,end):
        change=pd('00:15')
        is_vacant=True
        slot=self.get_slot()
        while start!=end:
            temp=start+change
            if slot[(start,temp)]==1:
                is_vacant=False
                break
            start=temp
        return(is_vacant)
                
    def update(self,start,end):
        change=pd('00:15')
        slot=self.get_slot()
        while start!=end:
            temp=start+change
            slot[(start,temp)]=1
            start=temp
                
########################
'''Creating instances for each meeting room and every room slot values
   to 1(occupied) for buffer timeIntervals'''

Buffertime=['09:00-09:15', '13:15-13:45', '18:45-19:00']
C_Cave=meeting_room('C-Cave', 3)
D_Tower=meeting_room('D-Tower', 7)
G_Mansion=meeting_room('G-Mansion', 20)
for timeInterval in Buffertime:
    start,end=timeInterval.split("-")
    start,end=pd(start),pd(end)
    for room in (C_Cave,D_Tower,G_Mansion):
        room.update(start,end)


########################
'''input_validation function is created for middleware helper
   whch returns validation of input either True or False along
   with passed input'''
      
def input_validation(Input): # input_details : Either BOOK/VACANCY input string
    input_details_list=Input.split(" ")
    start=pd(input_details_list[1])
    end=pd(input_details_list[2])
    input_details_list[1],input_details_list[2]=start,end
    if (end<=start or (end.minute())%15!=0 or (start.minute())%15!=0):
            return(False,input_details_list)
    else:
        return(True,input_details_list)
    

########################
'''output_for_singleInput function returns output for single user command'''

def output_for_singleInput(Input):
    validation,input_details_list=input_validation(Input)
    if validation==True:
        start,end=input_details_list[1],input_details_list[2]
        output,vacant_rooms=[],[]
        for room in (C_Cave,D_Tower,G_Mansion):
            if room.isvacant(start,end)==True:
                output.append(room.get_name())
                vacant_rooms.append(room)
        if input_details_list[0]=='VACANCY':
            if len(output)!=0:
                return(" ".join(output))
            else:
                return('NO_VACANT_ROOM')
        elif input_details_list[0]=='BOOK' and int(input_details_list[-1])<=20:
            for room in vacant_rooms:
                if room.get_capacity()>=int(input_details_list[-1]):
                    room.update(start, end)
                    return(room.get_name())
            return('NO_VACANT_ROOM')
        elif input_details_list[0]=='BOOK' and int(input_details_list[-1])>20:
            return('NO_VACANT_ROOM')
    else:
        return('INCORRECT_INPUT')
        

########################
'''output fuction takes input requests from text file and prints
   output of each input'''


def output():
    input_file = sys.argv[1]
    file=os.open(input_file,os.O_RDONLY)
    os.lseek(file,0,0)
    ALL_Inputs_list=os.read(file,os.path.getsize(file)).decode().split('\n')
    for Input in ALL_Inputs_list:
        print(output_for_singleInput(Input))

    
if __name__=="__main__":
    output()