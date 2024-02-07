'''any 7'''
def any7(nums):
    """Are any of these numbers a 7? (True/False)"""
    return any(num == 7 for num in nums)

print("should be true:", any7([1, 2, 7, 4, 5]))
print("should be false:", any7([1, 2, 4, 5]))

'''convert temp'''
def convert_temp(unit_in, unit_out, temp):
    """Convert farenheit <-> celsius and return results.

    - unit_in: either "f" or "c" 
    - unit_out: either "f" or "c"
    - temp: temperature (in f or c, depending on unit_in)

    Return results of conversion, if any.

    If unit_in or unit_out are invalid, return "Invalid unit [UNIT_IN]".

    For example:

      convert_temp("c", "f", 0)  =>  32.0
      convert_temp("f", "c", 212) => 100.0
    """
    if unit_in not in ['c', 'f'] or unit_out not in ['c', 'f']:
        return f"Invalid unit {unit_in if unit_in not in ['c', 'f'] else unit_out}"

    if unit_in == 'c' and unit_out == 'f':
        return (temp * 9/5) + 32
    elif unit_in == 'f' and unit_out == 'c':
        return (temp - 32) * 5/9
    else:
        return temp

print("c", "f", 0, convert_temp("c", "f", 0), "should be 32.0")
print("f", "c", 212, convert_temp("f", "c", 212), "should be 100.0")
print("z", "f", 32, convert_temp("z", "f", 32), "should be Invalid unit z")
print("c", "z", 32, convert_temp("c", "z", 32), "should be Invalid unit z")
print("f", "f", 75.5, convert_temp("f", "f", 75.5), "should be 75.5")

'''count up'''
def count_up(start, stop):
    """Print all numbers from start up to and including stop."""
    for num in range(start, stop+1):
        print(num)

count_up(5, 7)

'''in range'''
def in_range(nums, lowest, highest):
    """Print numbers inside the range."""
    for num in nums:
        if lowest <= num <= highest:
            print(f"{num} fits")

in_range([10, 20, 30, 40, 50], 15, 30)

'''sum nums'''
def sum_nums(nums):
    """Given list of numbers, return sum of those numbers."""
    total = 0
    for num in nums:
        total += num
    return total

# Test the function
result = sum_nums([1, 2, 3, 4])
print("sum_nums returned:", result)


