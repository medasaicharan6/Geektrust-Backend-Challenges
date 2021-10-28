## How to run the script
python -m Train <absolute_path_to_input_file> \
Here, <absolute_path_to_input_file> is the path of Input file 

## [Train](https://www.geektrust.in/coding-problem/backend/train)

Train A and Train B are two limited stop super fast trains that travel from Chennai to New Delhi and Trivandrum to Guwahati.

The uniqueness of these trains are that for some part of the journey they follow the same route and travel as one train - Train AB. Also passengers can board this train only at the source stations, but they can get down at any station enroute.

There are only reserved bogies and each bogie will only have passengers to a specific station. When the train arrives in the station enroute, instead of waiting for the passengers to get down, the entire bogie is removed from the train, and the train continues its journey.

These train’s reservation systems are designed in a unique way where Train A can have passengers in the route for Train B and vice versa. For e.g. people can board from Chennai in Train A and travel to Guwahati.

Trains start from their respective source stations and meet at Hyderabad on Wednesdays every week at exactly the same time and travel till Bhopal as a single train, from where it again travels as two independent trains.

At Hyderabad both trains are merged as single train, Train AB. However the merging is done based on the distance each remaining bogie in both the trains has to travel. First both the engines are attached and then the bogies are attached in the descending order of distances they have to travel further from Hyderabad. This is done so that the last bogie can be immediately detached at the respective stations and the train can continue its journey quickly.

The routes and distances of each train are as given. Station codes can be used for ease of inputs and outputs. The distances are also given.


# Train A	
## STATION (CODE) - DISTANCE

CHENNAI (CHN) - 0

SALEM (SLM) - 350 

BANGALORE (BLR) - 550 

KURNOOL (KRN) - 900 

HYDERABAD (HYB) - 1200 

NAGPUR (NGP) - 1600 

ITARSI (ITJ) - 1900 

BHOPAL (BPL) - 2000

AGRA (AGA) - 2500 

NEW DELHI (NDL) - 2700

# Train B

## STATION (CODE) - DISTANCE

TRIVANDRUM (TVC) -0 

SHORANUR (SRR) - 300 

MANGALORE (MAQ) - 600 

MADGAON (MAO) - 1000 

PUNE (PNE) - 1400 

HYDERABAD (HYB) - 2000 

NAGPUR (NGP) - 2400 

ITARSI (ITJ) - 2700 

BHOPAL (BPL) - 2800 

PATNA (PTA) - 3800 

NEW JALPAIGURI (NJP) - 4200 

GUWAHATI (GHY) - 4700 


Given initial bogie order of both trains your program should print the bogie order of arrival of each train at Hyderabad, Train AB’s departure bogie order from Hyderabad.


## Your program should take as input:

1. The order of bogies for train A while departing from Chennai.
2. The order of bogies for train B while departing from Trivandrum.

## The output should be:

1. The order of bogies for train A while arriving at Hyderabad.
2. The order of bogies for train B while arriving at Hyderabad.
3. The order of bogies for train AB (merged train) while departing from Hyderabad.


# Input Commands

There are 2 input commands defined to separate out the actions. Your input format will start with either of these commands i.e TRAIN_A, TRAIN_B

## TRAIN_A

The TRAIN_A command receives the initial order of bogies (seperated by space) for train A while departing from Chennai. \

Format - TRAIN_A ENGINE BOGIE_1 BOGIE_2 BOGIE_3 ... BOGIE_N \
Example- TRAIN_A ENGINE NDL NDL KRN GHY SLM NJP NGP BLR

## TRAIN_B

The TRAIN_B command receives the initial order of bogies (seperated by space) for train B while departing from Trivandrum. \

Format - TRAIN_B ENGINE BOGIE_1 BOGIE_2 BOGIE_3 ... BOGIE_N \
Example- TRAIN_B ENGINE NJP GHY AGA PNE MAO BPL PTA


## Assumptions

1. The passengers board only from the source station.

2. If there are no passenger bogies to travel from Hyderabad station, then train should stop there. In such a case it should print JOURNEY_ENDED

3. The distances are in kilometers.

4. If there are multiple bogies with same station as its destination, then they can be arranged next to each other when the Train AB leaves Hyderabad.


## SAMPLE INPUT-OUTPUT 1

## INPUT:
TRAIN_A ENGINE NDL NDL KRN GHY SLM NJP NGP BLR \
TRAIN_B ENGINE NJP GHY AGA PNE MAO BPL PTA 


## OUTPUT:
ARRIVAL TRAIN_A ENGINE NDL NDL GHY NJP NGP \
ARRIVAL TRAIN_B ENGINE NJP GHY AGA BPL PTA \
DEPARTURE TRAIN_AB ENGINE ENGINE GHY GHY NJP NJP PTA NDL NDL AGA BPL NGP \


## SAMPLE INPUT-OUTPUT 2

## INPUT:
TRAIN_A ENGINE SLM BLR KRN HYB SLM NGP ITJ \
TRAIN_B ENGINE SRR MAO NJP PNE PTA


## OUTPUT:
ARRIVAL TRAIN_A ENGINE HYB NGP ITJ \
ARRIVAL TRAIN_B ENGINE NJP PTA \
DEPARTURE TRAIN_AB ENGINE ENGINE NJP PTA ITJ NGP
