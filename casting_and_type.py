"""
python is not typed. OMG
"""
# casting

num_str = "3"
num_int = 3
num_to_float = 3

num_str_to_int = int(num_str)
num_int_to_str = str(num_int)
num_int_to_float = float(num_to_float)

print(f"Before: string {type(num_str)}, int {type(num_int)}, int to float {type(num_to_float)}")
print(f'\nAfter: string to int {type(num_str_to_int)}, int to string {type(num_int_to_str)}, int to float {type(num_int_to_float)}')
