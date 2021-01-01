"""Hi."""
rates_2019 = {
    100: 0,
    150: 15,
    200: 40,
}

rates = {
    2019 : {
        100: 0,
        150: 15,
        250: 25,
        350: 30,
        450: 45,
        1000: 55  
    }
}

hours = 200

def value_of_hours(hours):
    total = 0
    previous_threshold = 0

    for threshold, rate in rates[2019].items():
        hours_over_threshold = hours - threshold
        hours_over_previous_threshold = hours - previous_threshold

        if hours_over_threshold > 0:
            total += (threshold - previous_threshold) * rate
        elif hours_over_previous_threshold > 0:
            total += (hours - previous_threshold) * rate

        previous_threshold = threshold

    return total



print(value_of_hours(451))
