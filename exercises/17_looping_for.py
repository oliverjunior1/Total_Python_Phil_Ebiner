# Given the following list of numbers, perform the sum of all even and
# odd* numbers separately in the variables sum_even and sum_odd
# respectively:*Recall from previous days: the modulus (or remainder) of
# a number divided by 2 is zero when said value is even, and 1 when it is
# odd
#
# num % 2 == 0 (even values)
#
# num % 2 == 1 (odd values)

list_numbers = [1,5,8,7,6,8,2,5,2,6,4,8,5,9,8,3,5,4,2,5,6,4]

sum_even = 0

sum_odd = 0

for num in list_numbers:
    if num % 2 ==0:
        sum_even += num
    else:
        sum_odd += num

print(sum_odd)
print(sum_even)