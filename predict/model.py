import random
import sys
from joblib import load
import pickle
import numpy as np

# TODO: Implement this function to call the AI model
def predict(input, loaded_model):
    result = loaded_model.predict(input)
    result = float(result)
    result = np.exp(result) - 1
    return predict

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
    model_path, dict_path, lon_sc_path, lat_sc_path, pool, skyview, bedroom, bathroom, area, lat, lon, legal, feature, district, ward, project, balcony = sys.argv
    
    # Parse arguments
    area = parse_float(area)
    bathroom = parse_float(bathroom)
    bedroom = parse_float(bedroom)
    # Initialize input model
    input = np.zeros((1,450))
    # Load dictionary
    with open(dict_path, 'rb') as f:
        dictionary = pickle.load(f)
    # Convert attribute to input
    if (pool == 'Có' ):
        input[:,0] = 1
    if (skyview == 'Có' ):
        input[:,1] = 1
    input[:,2] = bedroom
    input[:,3] = bathroom
    input[:,4] = np.log1p(area)
    # Load standard scaler 
    input[:,5] = float(load(lat_sc_path).transform([[lat]]))
    input[:,6] = float(load(lon_sc_path).transform([[lon]]))

    for opt in legal:
        if (opt in dictionary):
            input[:,dictionary[opt]] = 1

    for opt in feature:
        if (opt in dictionary):
            input[:,dictionary[opt]] = 1

    district = 'district_' + district
    if (district in dictionary):
        input[:,dictionary[district]] = 1
    
    ward = 'ward_' + ward.lower()
    if (ward in dictionary):
        input[:,dictionary[ward]] = 1
    
    project = 'project_‘' + project + '’'
    if (project in dictionary):
        input[:,dictionary[project]] = 1

    for opt in balcony:
        if ((opt == 'Đông')|(opt == 'Đông Nam')|(opt == 'Nam')|(opt == 'Bắc')):
            input[:,dictionary['balcony.dong_tu_trach']] = 1
        if ((opt == 'Tây')|(opt == 'Đông Bắc')|(opt == 'Tây Nam')|(opt == 'Tây Bắc')):
            input[:,dictionary['balcony.tay_tu_trach']] = 1

    # Load model
    loaded_model = load(model_path)
    # Predict
    dataToSendBack = predict(input, loaded_model)
    
    # Send data
    print(dataToSendBack)
    sys.stdout.flush()