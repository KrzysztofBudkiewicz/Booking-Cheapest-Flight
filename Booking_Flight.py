from Variables import *
from Page_Navigation import MainPage
from Export_Data import *

MainPage.select_page()
MainPage.select_flights()
MainPage.select_ticket(one_way_ticket)
MainPage.select_cabin_class(first)
MainPage.select_adult_passengers(1)
MainPage.select_children_passengers(1, 6)
MainPage.select_only_direct_flights()
MainPage.select_departure_city('New York')
MainPage.select_arrival_city('Boston')
MainPage.select_departure_date(2)
MainPage.select_arrival_date(4)
MainPage.search_flights()
compile_data()
send_email()
export_to_excel()