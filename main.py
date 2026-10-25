import math_utils
import string_utils
import shop_package.discount as disc
from shop_package.billing import calculate_total


print(math_utils.add(10,20));
print(math_utils.subtract(20,10))
print(math_utils.square(10))

print(string_utils.capitalize_word("hello"))
print(string_utils.reverse_string("hello"))
print(string_utils.word_count("hello world"))

print(disc.apply_discount(100, 10))
print(disc.flat_discount(100))
print(calculate_total([100, 200, 300]))