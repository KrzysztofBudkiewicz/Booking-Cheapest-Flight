# Booking Cheapest Flight
Script written in Python with Selenium framework to find the cheapest flight. All data is exported to an Excel sheet and an additional Email is sent with the cheapest flight details.

UI test case for Booking.com:
Search for the cheapest flight for specific data.

## Steps to reproduce:
1. Go to the website [http://booking.com](http://booking.com)
2. Search flights.
3. Select flight details.

* Ticket type (Multi-city ticket is still in progress :)): **One-way**
* Cabin class: **First**
* Adults passengers (if you choose nothing then 1 is the default): **2**
* Number of children: **1**
* Total number of passengers must not exceed 9
* Age for each child: **6 years**
* Choose if you want a direct flight: **Yes**
* Choose departure city: **New York**
* Choose arrival city: **Boston**
* Choose departure date from today (in days): **2** 
* Choose arrival date from today (in days): **4** 

4. Press the "search" button.
5. Specify the location in the **Export_Data.py** file, where to save the found data in xlsx format.
6. If you would like to receive an Email with the best score, please enter your Gmail details in the **Export_Data.py** file.
7. To complete the above steps, run **Booking_Flight.py** file

## Expected results:

1. The file with the results of the cheapest flights was saved on the disk.
2. The best flight result has been sent to the email address.

## Actual results:

1. As expected.
2. As expected.



