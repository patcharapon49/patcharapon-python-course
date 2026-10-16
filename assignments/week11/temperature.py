"""
Write a program that analyzes daily temperatures for a week:

Create a function get_temperatures() that:

- Uses a local list to store 7 temperature values (use input or predefined values)
- Returns the list

Create a function analyze_temps(temp_list) that:

- Calculates and returns the average temperature (local variable)
- Finds and returns the highest temperature
- Finds and returns the lowest temperature
- Returns all three values as a tuple

Create a function display_analysis(avg, high, low) that prints the results nicely formatted

Example Output:
Temperature Analysis for the Week:
Average: 23.5 C
Highest: 28 C
Lowest: 19 C

"""
<<<<<<< HEAD

def get_temperature():

    temps = [30, 20, 32, 33, 31, 30]
    return temps

def analyze_temps(temp_list):

    average = sum(temp_list) / 2
    high = max(temp_list)
    low = min(temp_list)

    return (average ,high ,low)

def display_temperature(average,high,low):

    print("Temperature Analysis for the Week :")
    print("Average: " % average)
    print("Highest: " % high)
    print("Lowest: " % low)

temp = get_temperature()
result = analyze_temps(temps)
display_analysis(result[0], result[1], result[2])
=======
    
>>>>>>> upstream/main
