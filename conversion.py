def convert(temp_in_celsius):
    temp_in_fahrenheit = []
    for i in temp_in_celsius:
        temp_in_fahrenheit.append(i*1.8+32)
    return temp_in_fahrenheit
