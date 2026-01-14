# To do the coding exercise below, you can choose different paths.
# While the correct path in programming is the one that returns the
# correct result, I encourage you to try applying list comprehension
# concepts to begin to assimilate them for the future. They can be very
# useful in your professional practice!
#
# For the following list of temperatures in degrees Fahrenheit, express
# these same values in a new list of temperature values in degrees
# Celsius. The conversion between type of units is as follows:
#
# °C = (°F - 32) * (5/9)
#
# or expressed in another way:
#
# (degrees_fahrenheit-32)*(5/9)

temperature_fahrenheit = [32, 212, 275]

degrees_celsius = [(f-32)*(5/9) for f in temperature_fahrenheit]

print(degrees_celsius)
