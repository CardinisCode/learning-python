
def print_pyramid(pyramid_size):
    pyramid = ""
    for i in range(1, pyramid_size + 1):
        space_count = pyramid_size - i
        left_side = (" " * space_count) + ("#" * i)
        right_side = "#" * i
        pyramid += left_side + "  " + right_side + "\n"
    pyramid = pyramid.rstrip()
    return pyramid




    # if pyramid_size == 1:
    #     return "#  #"
    # if pyramid_size == 2:
    #     return " #  #\n##  ##"
    # return "  #  #\n ##  ##\n###  ###"
