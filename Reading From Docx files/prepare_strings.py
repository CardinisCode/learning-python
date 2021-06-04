from datetime import datetime, date
from style_date_value import style_date_for_presentation


def create_recipient_string(recipients_name, recipients_address, recipients_job_description):
    updated_string = ""
    current_date = datetime.now().date()
    todays_date_str = style_date_for_presentation(current_date)

    updated_string += recipients_name + "\n"
    updated_string += recipients_job_description.lstrip(" ") + "\n"
    address_list = recipients_address.split(",")
    for address in address_list:
        updated_string += address.lstrip(" ") + "\n"
    updated_string += todays_date_str

    return updated_string


def create_personal_info_string():
    my_name = "Andrea Folgado"
    my_email = "ac.folgado@gmail.com"
    my_contact_number = "073 7756 1277"

    return my_name + "\n" + my_email + " | " + my_contact_number + "\n"