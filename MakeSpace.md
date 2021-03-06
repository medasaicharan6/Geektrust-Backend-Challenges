## How to run the script
python -m MakeSpace <absolute_path_to_input_file> \
Here, <absolute_path_to_input_file> is the path of Input file 

## [Make Space](https://www.geektrust.in/coding-problem/backend/make-space)

Make Space Ltd. is a startup offering a co-working space to individuals, freelancers and startups. They provide a common workspace where anyone can come and work. Along with it, they have dedicated meeting rooms that their customers can book for private discussions.

They are looking for a scheduling system to effectively schedule meetings. Can you build such a system for Make Space Ltd.?

Make Space Ltd. currently has 3 meeting rooms with varying capacity


C-Cave - 3 People \
D-Tower - 7 People \
G-Mansion - 20 People 

Person Capacity - Maximum number of people the meeting room can accommodate.
Buffer Time - Buffer time is the time used to clean up the meeting room. It happens at fixed times from 09:00 - 09:15, 13:15 - 13:45 and 18:45 - 19:00. During this time, no meeting rooms will be available to book.


## Rules

1. Bookings can be made only in a single day from 00:00 to night 23:45. It cannot overlap across days. So you cannot book from 23:00 to 01:00, but can from 23:00 to 23:45.

2. A booking can be started and ended only in 15 minute intervals, i.e. XX:00, XX:15, XX:30, XX:45. This means a booking can be made at 01:15 or 16:00 but not 15:35 or 16:03.

3. The rooms will be allocated only to those who book them, on a first come first serve basis.

4. The most optimal room which can accommodate the number of people will be allocated. For eg., if you asked for a 4 person capacity requirement then the D-Tower (7 person capacity) will be allocated, provided it is available.

5. In case if the room of desired capacity is not available, the next available capacity room will be allocated. For eg., If you asked for the 4 person capacity room between 12:00 to 13:00 and the D-Tower is not available then the G-Mansion will be allocated, provided it is available.

6. No meetings can be scheduled during the buffer time. If the booking time overlaps with the buffer time NO_VACANT_ROOM should be printed.

7. Bookings can be only made for 2 or more people and upto a maximum of 20 people. If the person capacity for booking is outside of 2-20 range NO_VACANT_ROOM should be printed.

8. Time input should follow HH:MM format (24 hours format). If an incorrect time input is provided then INCORRECT_INPUT should be printed.


# Input Details

The system will take two types of inputs:

## 1. Book Meeting Room

As a co-working space customer, I shall schedule a meeting by giving a time period and capacity requirement. \
Format - BOOK <start_time(inclusive)> <end_time(exclusive)> <person_capacity> \
Example - BOOK 14:15 16:00 12 \
Possible Output: \
???<Meeting_Room_Name>??? - If the booking is successful \
???NO_VACANT_ROOM??? - If no room is vacant during the requested time period.

## 2. View available meeting rooms

As a co-working space customer, I would like to view a list of available meeting rooms by giving a time period. This should print the rooms in the ascending order of the room capacity. The rooms printed should be separated by a single space character. \

Format - VACANCY <start_time(inclusive)> <end_time(exclusive)> \
Example - VACANCY 14:30 15:00 \
Output: C-Cave G-Mansion


## Input Constraints

1. Time will be in HH:MM (24 hours) format
2. Time input should always consider the 15 minute time interval
3. For all the time inputs end_time > start_time


## SAMPLE INPUT 1

VACANCY 10:00 12:00 \
BOOK 11:00 11:45 2	\
BOOK 11:30 13:00 35	\
BOOK 11:30 13:00 15	\
VACANCY 11:30 12:00	\
BOOK 14:00 15:30 3	\
BOOK 15:00 16:30 2	\
BOOK 15:15 12:15 12	\
VACANCY 15:30 16:00	\
BOOK 15:30 16:30 2	\
VACANCY 15:45 16:00	\
BOOK 16:00 17:00 5	\
VACANCY 18:00 19:00

## SAMPLE OUTPUT 1

C-Cave D-Tower G-Mansion \
C-Cave\
NO_VACANT_ROOM \
G-Mansion \
D-Tower \
C-Cave \
D-Tower \
INCORRECT_INPUT \
C-Cave G-Mansion \
C-Cave \
G-Mansion \
G-Mansion \
NO_VACANT_ROOM


## SAMPLE INPUT 2

BOOK 09:30 13:15 2 \
BOOK 13:45 18:45 2 \
BOOK 12:55 14:00 3 \
BOOK 13:45 17:15 6 \
VACANCY 13:45 15:00	\
BOOK 14:00 15:00 2	\
BOOK 17:00 18:30 12 \
VACANCY 17:00 18:00	\
VACANCY 17:30 18:00 \
BOOK 17:00 18:30 12 \
BOOK 15:35 16:35 12

## SAMPLE OUTPUT 2

C-Cave \
C-Cave \
INCORRECT_INPUT \
D-Tower \
VG-Mansion \
G-Mansion \
G-Mansion \
NO_VACANT_ROOM \
D-Tower \
NO_VACANT_ROOM \
INCORRECT_INPUT
