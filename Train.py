import os
import sys

'''Creating a dict for both train routes where staion codes are keys
   and their distance from hyderabad are values, negative indicates
   those stations are towards source'''
Train_A_route={'CHN': -1200,
 'SLM': -850,
 'BLR': -650,
 'KRN': -300,
 'HYB': 0,
 'NGP': 400,
 'ITJ': 700,
 'BPL': 800,
 'AGA': 1300,
 'NDL': 1500}

Train_B_route={'TVC': -2000,
 'SRR': -1700,
 'MAQ': -1400,
 'MAO': -1000,
 'PNE': -600,
 'HYB': 0,
 'NGP': 400,
 'ITJ': 700,
 'BPL': 800,
 'PTA': 1800,
 'NJP': 2200,
 'GHY': 2700}

'''compare_dist_hyd is a fuction which takes a station code as input and 
   returns its distance from hyderabad station'''
def compare_dist_hyd(x):
    return Train_A_route[x] if x in Train_A_route.keys() else Train_B_route[x]


'''Train_Boggies is a function which takes the actual input string as input 
   which has train name and bogies order at source and returns bogies ooder
   of that train at arrival of hyderabad'''
def Train_Bogies(Train):
    Train_bogies=Train[2:]
    Train_bogies_hyd=[]
    for bogie in Train_bogies:
        if compare_dist_hyd(bogie)>=0:
            Train_bogies_hyd.append(bogie)
    return(Train_bogies_hyd)


def main():
    path= sys.argv[1]
    Input_file=os.open(path,os.O_RDONLY)
    os.lseek(0,0,0)
    Input=os.read(Input_file,os.path.getsize(Input_file)).decode().split('\n')
    if Input[0][6]=='A':
        Train_A=Input[0].split(" ")
        Train_B=Input[1].split(" ")
    else:
        Train_A=Input[1].split(" ")
        Train_B=Input[0].split(" ")
    Train_A_bogies=Train_Bogies(Train_A)
    Train_B_bogies=Train_Bogies(Train_B)
    mixed_bogies=Train_A_bogies+Train_B_bogies
    mixed_bogies.sort(key=compare_dist_hyd,reverse=True)
    Train_AB_bogies=[]
    for i in mixed_bogies:
        if i!='HYB':
            Train_AB_bogies.append(i)
    if len(Train_A_bogies)!=0 and len(Train_B_bogies)!=0:        
        print('ARRIVAL TRAIN_A ENGINE '+" ".join(Train_A_bogies))
        print('ARRIVAL TRAIN_B ENGINE '+" ".join(Train_B_bogies))
        print('DEPARTURE TRAIN_AB ENGINE ENGINE '+" ".join(Train_AB_bogies))
    elif len(Train_A_bogies)!=0 and len(Train_B_bogies)==0:
        print('ARRIVAL TRAIN_A ENGINE '+" ".join(Train_A_bogies))
        print('JOURNEY_ENDED')
        print('DEPARTURE TRAIN_AB ENGINE ENGINE '+" ".join(Train_AB_bogies))
    elif len(Train_A_bogies)==0 and len(Train_B_bogies)!=0:
        print('JOURNEY_ENDED')
        print('ARRIVAL TRAIN_B ENGINE '+" ".join(Train_B_bogies))
        print('DEPARTURE TRAIN_AB ENGINE ENGINE '+" ".join(Train_AB_bogies))
    else:
        print('JOURNEY_ENDED')
        print('JOURNEY_ENDED')
        print('JOURNEY_ENDED')
    
if __name__=='__main__':
    main()