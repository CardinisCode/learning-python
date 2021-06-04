from datetime import datetime, date


def style_date_for_presentation(date_obj):
    date_string = ""
    months_list = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"] 

    year = date_obj.strftime("%Y")
    month = int(date_obj.strftime("%m"))
    month_string = months_list[month + 1]
    day = date_obj.strftime("%d")

    date_string += date_obj.strftime("%d") + " " + month_string + " " + date_obj.strftime("%Y")
    return date_string
