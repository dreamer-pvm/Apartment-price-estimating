import random
import sys

# TODO: Implement this function to call the AI model
def predict(geoloc, area, project, bedroom, bathroom,floor,direction,legalPaper,feature):
    return (random.randint(50, 100)) * area + bathroom * 50 + bedroom * 50; 

# Help function
def parse_int(x):
    if (x == ''):
        return 0
    else:
        return int(x)

def parse_float(x):
    if (x == ''):
        return 0
    else:
         return float(x)

if __name__ == "__main__":
    # Get arguments
    filename, geoloc, area, project, bedroom, bathroom, floor, direction, legalPaper, feature = sys.argv
    
    # Parse arguments
    area = parse_float(area)
    bathroom = parse_int(bathroom)
    bedroom = parse_int(bedroom)
    floor = parse_int(floor)

    # Predict
    dataToSendBack = predict(geoloc, area, project, bedroom, bathroom,floor,direction,legalPaper,feature)
    
    # Send data
    print(dataToSendBack)
    sys.stdout.flush()