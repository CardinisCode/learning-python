# Printing the hash value for a float:
float_value = 545.4
print(float_value.hex())
# Note this approach (using dot notation) doesn't work with integer values

# To get the hex values for integers, you can use this approach:
int_value = 643
print("Int:", int_value, "Hex value:", hex(int_value))
# Output: Ox283

# But if you use this approach with a float: 
# float_2 = 64.22 
# print("Float:", float_2, "Hex:", hex(float_2))
# You get the error: 
# TypeError: 'float' object cannot be interpreted as an integer

# You can use this same approach on negative integers:
negative_int = -643
print("Integer:", negative_int, "Hex:", hex(negative_int))
# Output: -Ox283
