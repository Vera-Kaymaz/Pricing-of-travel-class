# -*- coding: utf-8 -*-
"""Pricing of travel class.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1KhgfEebIqMCemsI4woC4eLHs8eFiox97
"""

class_of_travel = ("Economy Class Flights")
transfers_in_the_flight = 3

fligth_price = 0
final_price = 0
currency = "$"

if class_of_travel == ("First Class Flights"):
  flight_price = (f"{currency}1,300")
elif class_of_travel == ("Economy Class Flights"):
  flight_price =(f"{currency}300")
else:
  flight_price = (f"{currency}700")

print("Flight price:")
print(flight_price)

if transfers_in_the_flight > 1:
  flight_price == (f"{currency}300")
  flight_price = 300
  final_price = flight_price * transfers_in_the_flight

print("Final price:")
print(f"{currency}{final_price}")