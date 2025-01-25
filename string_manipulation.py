orig_str = "   Hello, World!   "
print(f"Original string: '{orig_str}'")

# lstrip() - Remove leading whitespace
lstripped_str = orig_str.lstrip()
print(f"After lstrip(): '{lstripped_str}'")

# rstrip() - Remove trailing whitespace
rstripped_str = orig_str.rstrip()
print(f"After rstrip(): '{rstripped_str}'")

# strip() - Remove leading and trailing whitespace
stripped_str = orig_str.strip()
print(f"After strip(): '{stripped_str}'")

# upper() - Convert to uppercase
upper_str = orig_str.upper()
print(f"After upper(): '{upper_str}'")

# lower() - Convert to lowercase
lower_str = orig_str.lower()
print(f"After lower(): '{lower_str}'")

# replace() - Replace a substring with another substring
replaced_str = orig_str.replace("World", "Python")
print(f"After replace(): '{replaced_str}'")

# split() - Split the string into a list of substrings
split_str = orig_str.split()
print(f"After split(): {split_str}")

# join() - Join a list of strings into a single string
joined_str = " ".join(split_str)
print(f"After join(): '{joined_str}'")

# find() - Find the first occurrence of a substring
find_index = orig_str.find("World")
print(f"Index of 'World' in original string: {find_index}")

# count() - Count the occurrences of a substring
count_world = orig_str.count("World")
print(f"Count of 'World' in original string: {count_world}")

# capitalize() - Capitalize the first character
capitalized_str = orig_str.capitalize()
print(f"After capitalize(): '{capitalized_str}'")

# title() - Capitalize the first character of each word
title_str = orig_str.title()
print(f"After title(): '{title_str}'")

# swapcase() - Swap the case of each character
swapcase_str = orig_str.swapcase()
print(f"After swapcase(): '{swapcase_str}'")

# ljust() - Left justify the string
ljust_str = orig_str.ljust(20, '-')
print(f"After ljust(): '{ljust_str}'")

# rjust() - Right justify the string
rjust_str = orig_str.rjust(20, '-')
print(f"After rjust(): '{rjust_str}'")

# center() - Center the string
center_str = orig_str.center(20, '-')
print(f"After center(): '{center_str}'")

# zfill() - Pad the string with zeros
zfill_str = orig_str.strip().zfill(20)
print(f"After zfill(): '{zfill_str}'")

# startswith() - Check if the string starts with a substring
starts_with = orig_str.startswith("   Hello")
print(f"Starts with '   Hello': {starts_with}")

# endswith() - Check if the string ends with a substring
ends_with = orig_str.endswith("World!   ")
print(f"Ends with 'World!   ': {ends_with}")

# isdigit() - Check if all characters in the string are digits
is_digit = orig_str.isdigit()
print(f"Is digit: {is_digit}")

# isnumeric() - Check if all characters in the string are numeric
is_numeric = orig_str.isnumeric()
print(f"Is numeric: {is_numeric}")

# isdecimal() - Check if all characters in the string are decimal
is_decimal = orig_str.isdecimal()
print(f"Is decimal: {is_decimal}")

# isalpha() - Check if all characters in the string are alphabetic
is_alpha = orig_str.isalpha()
print(f"Is alpha: {is_alpha}")

# isalnum() - Check if all characters in the string are alphanumeric
is_alnum = orig_str.isalnum()
print(f"Is alnum: {is_alnum}")

# islower() - Check if all characters in the string are lowercase
is_lower = orig_str.islower()
print(f"Is lower: {is_lower}")

# isupper() - Check if all characters in the string are uppercase
is_upper = orig_str.isupper()
print(f"Is upper: {is_upper}")

# isspace() - Check if all characters in the string are whitespace
is_space = orig_str.isspace()
print(f"Is space: {is_space}")

# index() - Find the first occurrence of a substring
index_world = orig_str.index("World")
print(f"Index of 'World': {index_world}")

# str() - Convert an object to a string
num = 123
str_num = str(num)
print(f"String representation of number: '{str_num}'")

# len() - Get the length of the string
length = len(orig_str)
print(f"Length of original string: {length}")

# max() - Get the maximum character in the string
max_char = max(orig_str)
print(f"Maximum character in original string: '{max_char}'")

# min() - Get the minimum character in the string
min_char = min(orig_str)
print(f"Minimum character in original string: '{min_char}'")

# ord() - Get the Unicode code point of a character
ord_char = ord('A')
print(f"Unicode code point of 'A': {ord_char}")

# chr() - Get the character from a Unicode code point
chr_code = chr(65)
print(f"Character for Unicode code point 65: '{chr_code}'")