from email.message import EmailMessage
from selenium.webdriver.common.by import By
from Chrome_Driver import *
import datetime
import re
import pandas as pd
import smtplib
import ssl

# compile data from flights in structured format
df = pd.DataFrame()

def compile_data():
    global df
    global departure_times_list
    global arrival_times_list
    global airline_names_list
    global flight_price_list
    global flight_duration_list
    global cheapest_departure_time
    global cheapest_arrival_time
    global cheapest_airline_name
    global cheapest_flight_duration
    global cheapest_flight_price

    departure_times = driver.find_elements(
        By.XPATH, '//div[@data-testid="flight_card_segment_departure_time_0"]')
    departure_times_list = [value.text for value in departure_times]

    arrival_times = driver.find_elements(
        By.XPATH, '//div[@data-testid="flight_card_segment_destination_time_0"]')
    arrival_times_list = [value.text for value in arrival_times]

    airline_names = driver.find_elements(
        By.XPATH, '//div[@data-testid="flight_card_carrier_0"]')
    airline_names_list = [value.text for value in airline_names]

    flight_price = driver.find_elements(By.XPATH, '//div[@class="css-vxcmzt"]')
    flight_price_list = [re.findall(
        r'[\d]+[ \d][.,\d]+', value.text) for value in flight_price]

    flight_duration = driver.find_elements(
        By.XPATH, '//div[@data-testid="flight_card_segment_duration_0"]')
    flight_duration_list = [value.text for value in flight_duration]

    current_year_month_day = datetime.datetime.today().strftime("%Y-%m-%d")
    current_hour_and_minute = datetime.datetime.today().strftime("%H:%M")
    current_price = 'Price_On_Date ' + \
        '(' + current_year_month_day + '---' + current_hour_and_minute + ')'

    for i in range(len(departure_times_list)):
        try:
            df.loc[i, 'Departure_Time'] = departure_times_list[i]
        except Exception:
            pass
        try:
            df.loc[i, 'Arrival_Time'] = arrival_times_list[i]
        except Exception:
            pass
        try:
            df.loc[i, 'Airline_Name'] = airline_names_list[i]
        except Exception:
            pass
        try:
            df.loc[i, 'Flight_Duration'] = flight_duration_list[i]
        except Exception:
            pass
        try:
            df.loc[i, str(current_price)] = flight_price_list[i][0]
        except Exception:
            pass
    print("Excel Sheet Created!")
    # values for email
    current_values = df.iloc[0]
    cheapest_departure_time = current_values[0]
    cheapest_arrival_time = current_values[1]
    cheapest_airline_name = current_values[2]
    cheapest_flight_duration = current_values[3]
    cheapest_flight_price = current_values[-1]


# send email
def send_email():
    port = 465
    smtp_server = "smtp.gmail.com"
    sender_email = "sender.email@gmail.com"
    receiver_email = "receiver.email@gmail.com"
    password = "16-digit passcode from App Password"
    body = "\nHello!\n\nI am honored to present you the cheapest flight of all time.\nYou won't find it cheaper anywhere!\nCurrent Cheapest flight:\n\nDeparture time: {}\nArrival time: {}\nAirline name: {}\nFlight duration: {}\nPrice: {}\n".format(cheapest_departure_time,
                                                                                                                                                                                                                                                        cheapest_arrival_time,
                                                                                                                                                                                                                                                        cheapest_airline_name,
                                                                                                                                                                                                                                                        cheapest_flight_duration,
                                                                                                                                                                                                                                                        cheapest_flight_price)

    msg = EmailMessage()
    msg.set_content(body)
    msg['Subject'] = 'Current Cheapest Flight'
    msg['From'] = sender_email
    msg['To'] = receiver_email

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        server.send_message(msg, from_addr=sender_email,
                            to_addrs=receiver_email)
    print('Email has been sent!')


# select where to save the file
def export_to_excel():
    writer = pd.ExcelWriter(r'C:\Users') # example localization
    df.to_excel(writer, sheet_name='Cheapest_Flights', index=False, na_rep='NaN')


    # dynamically adjust column width
    for column in df:
        column_width = max(df[column].astype(str).map(len).max(), len(column))
        col_idx = df.columns.get_loc(column)
        writer.sheets['Cheapest_Flights'].set_column(
            col_idx, col_idx, column_width)
    writer.save()

