# Created by: James Lee
# Created on: Dec 2017
# Created for: ICS3U
# This program displays an example of a structure with a list

from enum import Enum

# an enumerated type of streets
Street_types = Enum('Street', 'Boulevard', 'Road', 'Avenue', 'Crescent')

# an enumerated type of provinces and territories
Provinces_and_territories = Enum('AB', 'BC', 'MB', 'NB', 'NL', 'NT', 'NS', 'NU', 'ON', 'PE', 'QC', 'SK', 'YT')

address = []
address.append([])
counter = 0

class MailingAddress():
    def __init__(self, name, street_number, street_name, street_type, city, province_or_territory, postal_code):
        self.name = name
        address[counter].append(self.name)
        self.street_number = street_number
        address[counter].append(self.street_number)
        self.street_name = street_name 
        address[counter].append(self.street_name)                  
        self.street_type = street_type
        address[counter].append(self.street_type)
        self.city = city  
        address[counter].append(self.city)        
        self.province_or_territory = province_or_territory
        address[counter].append(self.province_or_territory)
        self.postal_code = postal_code
        address[counter].append(self.postal_code)                              

while True:
    name = raw_input("Enter your name: ")  
    street_number = raw_input("Enter your street number: ")
    street_name = raw_input("Enter your street name: ")
    print("Choose your street type: Street, Boulevard, Road, Avenue, Crescent") 
    street_type = raw_input("Enter your street type: ")   
    while street_type not in Street_types:
        street_type = raw_input("Please enter a valid street type. (ex: Street) ")
    city = raw_input("Enter your city: ")
    print("Enter the abbreviation of the province or territory in this list: AB (Alberta), BC (British Columbia), MB (Manitoba), NB (New Brunswick), NL (Newfoundland and Labrador), NT (Northwest Territories), NS (Nova Scotia), NU (Nunavut), ON (Ontario), PE (Prince Edward Island), QC (Quebec), SK (Saskatchewan)")
    province_or_territory = raw_input("Enter your province or territory: ")     
    while province_or_territory not in Provinces_and_territories:
        province_or_territory = raw_input("Please enter a valid province or territory. (ex: ON) ")
        province_or_territory = province.upper()
    province_or_territory = province_or_territory
    province_or_territory = province_or_territory.upper()          
    postal_code = raw_input("Enter your postal code: ")

    mailing_address = MailingAddress(name, street_number, street_name, street_type, city, province_or_territory, postal_code)

    address.append([])
    counter = counter + 1
    print(address)
    print(mailing_address.name + '\n' + mailing_address.street_number + ' ' + mailing_address.street_name + ' ' + mailing_address.street_type + '\n' + mailing_address.city + ' ' + mailing_address.province_or_territory + ' ' + mailing_address.postal_code)          
