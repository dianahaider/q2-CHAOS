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

def plot_types():
    return {'line', 'bar'}

def denoise_vis(output_dir: str,
                stats1: qiime2.Metadata, #stats type is not a metadata but this is the transformer used by DADA2 plugin to make DADA2Stats into pd.dataframe
                stats2: qiime2.Metadata,
                plot_type: str = 'line',
                label1: str = 'Stats 1',
                label2: str = 'Stats 2',
                style: str = 'whitegrid',
                context: str = 'talk') -> None:
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
    new_df['order'] = new_df['order'].apply(pd.to_numeric)

    hue_order = new_df.query('step == "non-chimeric"').sort_values('% of Reads Remaining', ascending = False)

    sns.lineplot(data = new_df, y='% of Reads Remaining', x='order', hue='id')
    plt.ylim(0,100)
    plt.xlim(0,4)
    plt.xticks([x/2 for x in range (0,9)], ['Input', '', 'Filtered', '', 'Denoised', '', 'Merged', '', 'Non-Chimeric'])
    plt.xlabel('Processing Steps')
    plt.title('Parameter Settings')

    sns.set_style(style)
    sns.set_context(context)

    plt.savefig(os.path.join(output_dir, 'linegraph_denoise.png'), bbox_inches = 'tight')
    plt.savefig(os.path.join(output_dir, 'linegraph_denoise.pdf'), bbox_inches = 'tight')
    plt.gcf().clear()

    index = os.path.join(TEMPLATES, 'denoise_assets', 'index.html')
    q2templates.render(index, output_dir)


    table_preview = new_df.to_html()
    with open('outfile.html', 'w') as file:
        file.write(table_preview)

default_labels_for_denoise_list = []
for i in range(1,100):
    i = str(i)
    default_labels_for_denoise_list.append(i)

def denoise_list(output_dir: str,
                input_stats: qiime2.Metadata, #stats type is not a metadata but this is the transformer used by DADA2 plugin to make DADA2Stats into pd.dataframe
                labels: str = default_labels_for_denoise_list,
                plot_type: str = 'line',
                style: str = 'whitegrid',
                context: str = 'talk') -> None:

#problem is if i dont put a default value labels becomes required and i cant call variable within functiosn

    df = []

    for i in range(len(input_stats)):
        temp_df = input_stats[i].to_dataframe()
        temp_df['id'] = labels[i]
        df.append(temp_df)

    df = pd.concat(df, sort = True)

    table_preview = df.to_html()
    with open('outfile.html', 'w') as file:
        file.write(table_preview)

"""
    df = df.groupby('id').sum()
    new_df = pd.melt(df.reset_index(), id_vars = 'id', var_name = 'step', value_name = 'read_number')
    input_read_num = new_df['read_number'].max() #to normalize your data with input (input is the highest read_number)
    new_df['% of Reads Remaining'] = new_df['read_number'] / input_read_num * 100
    step_order = {'input':0, 'filtered':1, 'denoised':2, 'merged':3, 'non-chimeric':4}
    new_df['order'] = new_df['step'].apply(lambda x: step_order[x])
    new_df['order'] = new_df['order'].apply(pd.to_numeric)
    new_df['id'] = new_df['id'].apply(pd.to_numeric)

    new_df = new_df.reset_index()

    hue_order = new_df.query('step == "non-chimeric"').sort_values('% of Reads Remaining', ascending = False)

    sns.lineplot(data = new_df, y='% of Reads Remaining', x='order', hue='id')
    plt.ylim(0,100)
    plt.xlim(0,4)
    plt.xticks([x/2 for x in range (0,9)], ['Input', '', 'Filtered', '', 'Denoised', '', 'Merged', '', 'Non-Chimeric'])
    plt.xlabel('Processing Steps')
    plt.title('Parameter Settings')

    sns.set_style(style)
    sns.set_context(context)

    plt.savefig(os.path.join(output_dir, 'linegraph_denoise.png'), bbox_inches = 'tight')
    plt.savefig(os.path.join(output_dir, 'linegraph_denoise.pdf'), bbox_inches = 'tight')
    plt.gcf().clear()

    index = os.path.join(TEMPLATES, 'denoise_assets', 'index.html')
    q2templates.render(index, output_dir)

    table_preview = new_df.to_html()
    with open('outfile.html', 'w') as file:
        file.write(table_preview)
"""
