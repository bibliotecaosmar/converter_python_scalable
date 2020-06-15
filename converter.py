import sys

VELOCITY_SCALE = ['m/s', 'km/h', 'mile/h']

TIME_SCALE = ['ms', 'cs', 's', 'min', 'h', 'day', 'mouth', 'year']

SPACE_SCALE = ['nm', 'mm', 'cm', 'm', 'km', 'mile']


UPWARD_METRICS = [
        {
            'm/s': 0.36,
            'km/h': 3.6,
            'mile/h': 0.621371,
        },
        {
            'ms': 0,
            'cs': 0,
            's': 0,
            'min': 0,
            'h': 0,
            'day': 0,
            'mouth': 0,
            'year': 0,
        },
        {
            'nm': 0,
            'mm': 0,
            'cm': 0,
            'm': 0,
            'km': 0,
            'mile': 0
         }
    ]

DOWNWARD_METRICS = [
    {
        'm/s': 3.6,
        'km/h': 0.36,
        'mile/h': 1.60934,
     },
     {
        'ms': 0,
        'cs': 0,
        's': 0,
        'min': 0,
        'h': 0,
        'day': 0,
        'mouth': 0,
        'year': 0,
    },
    {
        'nm': 0,
        'mm': 0,
        'cm': 0,
        'm': 0,
        'km': 0,
        'mile': 0
    }
]

def integral_valor(var):
    count = 0
    for v in var:
        try:
            int(v)
            count = count + 1
        except:
            return int(var[:count])

def scale(var):
    count = 0
    for v in var:
        try:
            int(v)
            count = count + 1
        except:
            return var[count:]

def greatness(scale):
    if scale in VELOCITY_SCALE:
        return VELOCITY_SCALE
    if scale in TIME_SCALE:
        return TIME_SCALE
    if scale in SPACE_SCALE:
        return SPACE_SCALE
    print("Error: It isn't a scale accepted.")

def greatness_code(scale):
    if scale in UPWARD_METRICS[0]:
        return 0
    if scale in UPWARD_METRICS[1]:
        return 1
    if scale in UPWARD_METRICS[2]:
        return 2
    print("Error: It isn't a scale accepted.")

def fly(dimension, scale, acceleration):
    if not False in dimension: 
        dimension.insert(0, False)
        dimension.append(False)
    if dimension[dimension.index(scale) + acceleration]:
        return ['up', acceleration]
    if dimension[dimension.index(scale) - acceleration]:
        return ['down', acceleration]

def convert(var, greatness, greatness_code, direct, scale):
    if direct[0] == 'up':
        converted_var = var * UPWARD_METRICS[greatness_code][greatness[greatness.index(scale) + direct[1]]]
        return str(converted_var) + greatness[greatness.index(scale) + direct[1]]
    if direct[0] == 'down':
        converted_var = var * DOWNWARD_METRICS[greatness_code][greatness[greatness.index(scale) - direct[1]]]
        return str(converted_var) + greatness[greatness.index(scale) - direct[1]]

def add_to_valors(var, direct, valors):
    if var in valors:
        return valors
    if direct[0] == 'up':
        valors.append(var)
        return valors
    if direct[0] == 'down':
        valors.insert(0, var)
        return valors

def map_valors(var, greatness, scale, how_many_types):
    valors          = [var]
    acceleration    = 1
    direct          = fly(greatness, scale, acceleration)
    
    while len(valors) != how_many_types:
        initial_valors  = valors

        valors = add_to_valors(
                   convert(
                       integral_valor(var),
                       greatness,
                       greatness_code(scale),
                       direct,
                       scale
                       ),
                   direct,
                   valors)
        if valors == initial_valors:
            direct = fly(greatness, scale, -1)
        else:
            direct = fly(greatness, scale, acceleration + 1)
    return valors

def show_valors(valors):
    for valor in valors:
        print('<' + valor + '>')

#
# Main Application
#===================================================

def main():
    PARAMETER   = sys.argv[1]
    SCALE       = scale(PARAMETER)
    GREATNESS   = greatness(SCALE)
    
    show_valors(map_valors(PARAMETER,
                           GREATNESS,
                           SCALE,
                           len(GREATNESS)))

main()
