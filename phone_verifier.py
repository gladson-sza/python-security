import phonenumbers

from phonenumbers import geocoder


if __name__ == '__main__':

    # Format +5588999999999
    phone_number = phonenumbers.parse('+16502230000')
    description = geocoder.description_for_number(phone_number, 'pt')
    print(description)