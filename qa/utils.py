import plotly.graph_objects as go
import pandas as pd
import numpy as np


def create_chart(data):
    df = construct_df(data)
    print(df)



def construct_df(sessions):
    sessions_names = [session["session"].sample_name + "_" + str(session["session"].measurement_date)  for session in sessions]
    rois_data = []
    sessions_data = []
    for j, session in enumerate(sessions):
        for i, roi in enumerate(session['rois']):
            rois_data.append({roi["name"]: roi["decay_corr"]})

        sessions_data.append({sessions_names[j]: rois_data})
        rois_data = []

    df_data = []
    for item in sessions_data:
        for key, value in item.items():
            row = {}
            for element in value:
                for element_key, element_value in element.items():
                    row[element_key] = element_value
            df_data.append([key, row['Cs-137'], row['Am-241'], row['Co-60']])

    df = pd.DataFrame(df_data, columns=np.array(['Refname', 'Cs-137', 'Am-241', 'Co-60']))
    df = df.set_index('Refname')

    return df


