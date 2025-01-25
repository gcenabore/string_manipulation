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