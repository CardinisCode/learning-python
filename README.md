# learning-python
 All these code challenges are part of the edX course I'm working through: 
 "Computing in Python: Data Structures - Starting from 
        Section: Dictionaries. 
This includes the code challenges I complete as I complete my python learning as well as random tests and playing with code. 


For MartaBreezeCardTaps & Marta_updated.py:
- stations.txt and marta_sample.txt are the data files provided to solve this challenge. 
- stations_small.txt and small_marta.csv are just smaller versions of stations.txt and marta_sample.txt for testing purposes
- In the code challenge, the hashed text is the additional data, which I wanted to have on hand when solving the challenge. 
- Here is some more information provided in the code challenge: 

This problem is different from the others that you've done. Instead of writing a program to solve a general problem, we want you to write a program that will come to a specific answer.

First, read a little about the data in the box below.

Then, use the coding resource to explore the data. Your goal is to answer some questions about the data set.

When you've got your answers, enter them into the boxes below the coding window.

MARTA (Metropolitan Atlanta Rapid Transit Authority)

MARTA is the principal public transportation agency in the Atlanta metropolitan area. Since opening in 1979, MARTA has made over 5 billion trips carrying passengers by bus and rail. We will take a look at the rail traffic on Martin Luther King Jr. Day (January 18, 2016). By doing so, we will gain some understanding of the rail system.

Get to know the data

MARTA is mainly using Breeze cards for its "tap-and-go" fare collection. All of these taps are recorded in the following format:

transit_day and transit time: show when the Breeze card was tapped
device_id: unique identifier of the gate at which the card was tapped
station_id: MARTA Rail Station identifier
use_type: indicates the transaction type (entry/exit/transfer/etc.)
serial_number: serial number of the Breeze Card

Using this data, we want you to answer these questions:

What is the average number of Breeze Card taps per station?
Which station has traffic closest to the average?
Which station has the least traffic?