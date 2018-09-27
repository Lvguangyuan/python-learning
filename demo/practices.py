

def find_min_max(data):
    min_value = max_value = data[0]
    for i, value in enumerate(data):
        if value > max_value:
            max_value = value
        elif value < min_value:
            min_value = value
    return max_value, min_value

