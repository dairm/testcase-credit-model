import pandas as pd
import pickle
import argparse

def load_model(pathmodel):
    with open(pathmodel, "rb") as fin:
        return pickle.load(fin)

def scoring(path_data, path_model):
    data = pd.read_csv(path_data)
    test_set = data.drop("client_id", axis=1)
    
    model = load_model(path_model)
    print(model)
    try:
        prediction = model.predict_proba(test_set)[:,1]
    except:
        prediction = model.predict_proba(data)
    print(prediction)
    data["prediction"] = prediction
    
    data[["client_id", "prediction"]].to_csv("output/prediction.csv", index=False)
    
def main():
    # Initialize parser
    parser = argparse.ArgumentParser()

    # Adding optional argument
    parser.add_argument("-d", "--path_data")
    parser.add_argument("-m", "--path_model")

    # Read arguments from command line
    args = parser.parse_args()
    scoring(args.path_data, args.path_model)
    
main()