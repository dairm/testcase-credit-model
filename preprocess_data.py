import pandas as pd
import argparse
from utils import * 
categorical_features = ["gender", "marital_status", "job_position", "education"]
cols_label = ["living_region"]
cols_zero_fill = ["overdue_credit_count", "credit_count", "monthly_income"]

def main():
    # Initialize parser
    parser = argparse.ArgumentParser()

    # Adding optional argument
    parser.add_argument("-d", "--main_data")
    parser.add_argument("-t", "--transactions_data")
    parser.add_argument("-g", "--geo_data")

    # Read arguments from command line
    args = parser.parse_args()
    print(args)
    main_data = pd.read_csv(args.main_data, encoding="WINDOWS-1252", sep=";")
    main_data["score_shk"]=main_data["score_shk"].apply(lambda x: float(x.replace(",",".")))
    main_data["credit_sum"]=main_data["credit_sum"].apply(lambda x: float(x.replace(",",".")))
    
    main_data = data_prep(main_data, categorical_features, cols_label, cols_zero_fill)
    
    trans_data_agg = trans_func_agg(args.transactions_data)
    print(trans_data_agg.columns)
    main_data = main_data.merge(trans_data_agg, on="client_id", how="left")
    
    merchant_geo = pd.read_csv(args.geo_data, sep=";")
    merchant_geo = merchant_geo.rename({'merchant_id': 'client_id'}, axis="columns")
    
    main_data = main_data.merge(merchant_geo, on="client_id", how="left")
    postfix = args.main_data.split("/")[-1]
    main_data.fillna(0).to_csv("dataset_{}".format(postfix), index = False)

main()