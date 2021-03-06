#tf_to_retinanet
#get data that was prepped for tf and change it to data that works for retinanet

import os
import csv

import pandas as pd

#function to convert to float type
def type_conversion(dataframe, list_of_cols_to_fix):
 
    for i in list_of_cols_to_fix:
        dataframe[i] = dataframe[i].astype(int)
        
    return dataframe

#read data from csv
data = pd.read_csv('data_from_tf_model/data/parkinglot_labels.csv')

#drop
data = data.drop(['width', 'height'], axis = 1)

#rename
data = data.rename(columns={"filename": "path", "class": "class_title", "xmin": "x_start", "xmax": "x_finish", "ymin": "y_start", "ymax": "y_finish"})

#change path
data['path'] = data['path'].apply(lambda text: os.getcwd() + '/data_from_tf_model/images/TrainingImages/' + text)

#get approp data
new_data = data[['path', 'x_start', 'y_start', 'x_finish', 'y_finish', 'class_title']]

#convert to float type
new_data = type_conversion(new_data, ['x_start', 'y_start', 'x_finish', 'y_finish'])

new_data['x_start'] = new_data['x_start'].apply(lambda row: int(row))
new_data['y_start'] = new_data['y_start'].apply(lambda row: int(row))
new_data['x_finish'] = new_data['x_finish'].apply(lambda row: int(row))
new_data['y_finish'] = new_data['y_finish'].apply(lambda row: int(row))

#export
new_data.to_csv(os.getcwd()+'/processed_JSON/retinanet_data_spacenet.csv', header=True, index=None, sep=',')


#merged
"""
def merge_csv (df1, df2):

	final_df = df1.append(df2)
	print(final_df)

	final_df.to_csv(os.getcwd()+'/processed_JSON/retinanet_data.csv', header=True, index=None, sep=',')

#df1 = pd.read_csv('/Users/neeliyer/Documents/SPOT/retinanet/retinanet/processed_JSON/retinanet_data_spacenet.csv')
#df2 = pd.read_csv('/Users/neeliyer/Documents/SPOT/retinanet/retinanet/processed_JSON/retinanet_data_supervisely.csv')
#merge_csv (df1, df2)


"""