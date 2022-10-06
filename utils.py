from sklearn import preprocessing
import pandas as pd
from tqdm import tqdm 
tqdm.pandas(desc="my bar!")
from datetime import datetime

def data_prep(data, cols_categ_dummy, cols_categ_label, cols_zero_fill):
    '''Preprocess dataset

    Keyword arguments:
    data -- raw data
    cols_categ -- list of category features
    '''
    
    #dataset = data.drop(cols_categ_dummy, axis=1)
    dataset = pd.get_dummies(data, columns=cols_categ_dummy, dummy_na=True)
    
    le = preprocessing.LabelEncoder()
    for col in cols_categ_label:
        dataset[col] = le.fit_transform(data[col])
    print(dataset.shape)
    dataset.fillna(0, inplace=True)
    return dataset

def trans_func_agg(path_to_trans):
    '''Create aggregate features from trasactions

    Keyword arguments:
    path_to_trans -- path to transactions data
    '''
    trans_data = pd.read_csv(path_to_trans)
    
    trans_data["durat_ttime"] = trans_data.progress_apply(lambda x: 
                                                      abs(datetime.strptime(x["real_transaction_dttm"], "%H:%M:%S")
                                                          -datetime.strptime(x["record_date"], "%H:%M:%S")).total_seconds(),
                                                          axis=1)

    trans_data_agg = trans_data\
                            .groupby("merchant_id")\
                            .agg({
                                "latitude":"mean",
                                "longitude":"mean",
                                "durat_ttime":["max", "min", "count", "mean"],
                                })

    flat_cols = []

    for i in trans_data_agg.columns:
        flat_cols.append(i[0]+'_'+i[1])

    trans_data_agg.columns = flat_cols
    trans_data_agg = trans_data_agg.reset_index().rename({'merchant_id': 'client_id'}, axis="columns")
    return trans_data_agg