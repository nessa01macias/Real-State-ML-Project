import json
import pickle
import warnings
warnings.filterwarnings('ignore')

def load_pickle():
    with open(r'./model/banglore_home_prices_model.pickle', 'rb') as f:
        model = pickle.load(f)
        return model

def load_columns():
    with open(r'./model/columns.json', 'r') as f:
        data = json.load(f)
        locations = list(data.values())
        return locations

def get_location_names():
    locations = load_columns()
    return locations[0][3:]

def get_estimation(total_sqft, bath, BHK, location):
    model = load_pickle()
    columns = load_columns()[0]
    house = [0] * len(columns)
    try:
        location_index = columns.index(location.lower())
        # print(f"house[{location_index}] = 1")
        house[location_index] =1
    except:
        print("...something went wrong.")
        location_index = -1
    
    house[0] = total_sqft
    house[1] = bath
    house[2] = BHK

    model.predict([house]) 

    # the prediction is an array so we select the first element
    return model.predict([house])[0]

if __name__ == "__main__":
    #print(get_location_names())
    print(get_estimation(2000,4,4,"1st Block Jayanagar"))
    print(get_estimation(1000,2,3,"1st Block Jayanagar"))
