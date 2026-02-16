def leap_year(year):
    isDivisibleBy400 = year % 400 == 0
    isDivisibleBy100 = year % 100 == 0
    isDivisibleBy4 = year % 4 == 0
    return (isDivisibleBy4 and not isDivisibleBy100 or
           isDivisibleBy100 and isDivisibleBy400)
