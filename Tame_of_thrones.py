import sys
import os
import string
alphabets_list=list(string.ascii_uppercase)
'''Creating a dict with kingdom name as keys and its emblem as values'''

Name_emblem_dict={'SPACE':'Gorilla','LAND':'Panda','WATER':'octopus',
                  'ICE':'Mammoth','AIR':'Owl','FIRE':'Dragon'}


'''Defining a function decipher which takes a Encoded_string(using Seasar cipher)
   and key as input and returns decoded string'''

def decipher(Encoded_string,key):
    decoded_string=""
    Encoded_string_list=list(Encoded_string)
    for i in Encoded_string_list:
        if i.upper() in alphabets_list:
            i_index=alphabets_list.index(i.upper())
            decoded_string+=alphabets_list[i_index-key]
        else:
            decoded_string+=i
    return(decoded_string)


'''Defining a function count which takes a string and a char as input and return
   no. of occurences of that char in that string(lowercase and upper case are treated
   as same)'''
def count(string,char):
    count=0
    for i in string:
        if i.upper()==char.upper():
            count+=1
    return count
    

'''Defining a function does_support which takes a string as input which 
  contains kindom_name and secret message from space kingdom and 
  returns true if that kingdom supports SPACE or else returns false and also 
  name of the kingdom which received message'''
  
def does_support(Input):
    Input=Input.split(" ",1)
    Input_emblem=Name_emblem_dict[Input[0]]
    decoded_message=decipher(Input[-1],len(Input_emblem))
    flag=True
    for i in Input_emblem:
        if count(Input_emblem,i)>count(decoded_message,i):
            flag=False
            break
    return (flag,Input[0])

def main():
    Input_file_path= sys.argv[1]
    Input_file=os.open(Input_file_path,os.O_RDONLY)
    os.lseek(0,0,0)
    Input_list=os.read(Input_file,os.path.getsize(Input_file)).decode().split('\n')
    output='SPACE'
    allies_status={'LAND':0,'WATER':0,'ICE':0,'AIR':0,'FIRE':0}
    for Input in Input_list:
        response=does_support(Input)
        if response[0]==True:
            if allies_status[response[-1]]==0:
                output+=' '+response[-1]
                allies_status[response[-1]]=1
    if sum(allies_status.values())<3:
        output='NONE'
    print(output)

if __name__=='__main__':
    main()
    