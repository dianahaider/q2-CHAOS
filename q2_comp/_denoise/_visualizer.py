import os
import json
import pkg_resources
import shutil

import qiime2
import q2templates

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib
import matplotlib.pyplot as plt
import skbio

TEMPLATES = pkg_resources.resource_filename('q2_comp', '_denoise')

#def merge_df(filenames, metadata=None, var=None):

def denoise_vis(output_dir: str,
                stats1: qiime2.Metadata, #stats type is not a metadata but this is the transformer used by DADA2 plugin to make DADA2Stats into pd.dataframe
                stats2: qiime2.Metadata,
                plot_type: 'line',
                label1: str = 'Stats 1',
                label2: str = 'Stats 2') -> None:
    df1 = stats1.to_dataframe()
    df2 = stats2.to_dataframe()
    df1['id'] = label1
    df2['id'] = label2

    inputs = [df1, df2] #change it to list input for n stats file
    df = []
    for i in inputs:
        df.append(i)

    df = pd.concat(df, sort = True)

    df = df.groupby('id').sum()
    new_df = pd.melt(df.reset_index(), id_vars = 'id', var_name = 'step', value_name = 'read_number')
    input_read_num = new_df['read_number'].max() #to normalize your data
    df['% of Reads Remaining'] = df['read_number'] / input_read_num * 100
    step_order = {'input':0, 'filtered':1, 'denoised':2, 'merged':3, 'non-chimeric':4}




    table_preview=new_df.to_html()
    with open('outfile.html','w') as file:
        file.write(table_preview)

"""


    input = [stats1, stats2]
    labels = [label1, label2]
    stats_df = []
    for i in input:
        df = i.to_dataframe()
        for j in labels
        df['id'] =
        stats_df.append(df)

    stats_df = pd.concat(stats_df)
    stats_df = stats_df[list(stats_df.columns[-7:])]

    numeric = ['input','denoised','filtered','merged','non-chimeric']
    df[numeric] = df[numeric].apply(pd.to_numeric)
    sums = pd.DataFrame(data=None, columns=['Input','Filtered','Denoised','Merged','Non-chimeric'])
    sums = sums.append(df.iloc[:,1:6].sum(), ignore_index=True)

    denoise_barplot = plt.bar( )
    niceplot.savefig(os.path.join(output_dir, 'pleasework.png'))
    niceplot.savefig(os.path.join(output_dir, 'pleasework.pdf'))
    plt.gcf().clear()

    index = os.path.join(TEMPLATES, 'denoise_assets', 'index.html')
    q2templates.render(index, output_dir)
"""
