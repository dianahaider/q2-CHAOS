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
    input_read_num = new_df['read_number'].max() #to normalize your data with input (input is the highest read_number)
    new_df['% of Reads Remaining'] = new_df['read_number'] / input_read_num * 100
    step_order = {'input':0, 'filtered':1, 'denoised':2, 'merged':3, 'non-chimeric':4}
    new_df['order'] = new_df['step'].apply(lambda x: step_order[x])
    new_df = new_df.reset_index()

    sns.set_style('whitegrid')
    sns.set_context('talk')

    sns.lineplot(data = df, y='% of Reads Remaining', x='order', hue='Run Number')
    plt.ylim(0,100)
    plt.xlim(0,4)
    plt.xticks([x/2 for x in range (0,9)], ['Input', '', 'Filtered', '', 'Denoised', '', 'Merged', '', 'Non-Chimeric'])
    plt.xlabel('Processing Steps')
    plt.title('Parameter Settings')


    plt.savefig(os.path.join(output_dir, 'linegraph_denoise.png'))
    plt.savefig(os.path.join(output_dir, 'linegraph_denoise.pdf'))
    plt.gcf().clear()

    index = os.path.join(TEMPLATES, 'denoise_assets', 'index.html')
    q2templates.render(index, output_dir)
