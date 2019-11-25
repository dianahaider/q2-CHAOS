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
import ptitprince as pt
import skbio

TEMPLATES = pkg_resources.resource_filename('q2_comp', '_denoise')

#def merge_df(filenames, metadata=None, var=None):
def denoise_vis(output_dir: str,
                stats1: pd.DataFrame,
                stats2: pd.DataFrame,
                plot_type: 'line',
                label1: str = 'Stats 1',
                label2: str = 'Stats 2') -> None:
    numeric = ['denoised','filtered','input','merged','non-chimeric']
    stats1[numeric] = stats[numeric].apply(pd.to_numeric)

    table_preview = stats1.to_html()
    print(table_preview)

"""

    sample_frequencies1 = _frequencies(
    table1, axis = 'sample')
    sample_frequencies1.sort_values(inplace=True, ascending=False)
    sample_frequencies1.to_csv(
                os.path.join(output_dir, 'sample-frequency-detail1.csv'))
    sample_frequencies2 = _frequencies(
        table2, axis = 'sample')
    sample_frequencies2.sort_values(inplace=True, ascending=False)
    sample_frequencies2.to_csv(
                os.path.join(output_dir, 'sample-frequency-detail2.csv'))
    sample_frequencies_df1 = sample_frequencies1.to_frame()
    sample_frequencies_df2 = sample_frequencies2.to_frame()
    metadata = metadata.to_dataframe()
    metadata.index.name = "sample-id"
    metadata.reset_index(inplace = True)
    sample_frequencies_df1.index.name = "sample-id"
    sample_frequencies_df1.reset_index(inplace=True)
    sample_frequencies_df2.index.name = "sample-id"
    sample_frequencies_df2.reset_index(inplace=True)
    smpl = pd.merge(sample_frequencies_df1, sample_frequencies_df2, on = "sample-id")
    smpl = smpl.rename(columns = {'0_x':'Table 1', '0_y':'Table 2'})
    smpl_metadata = pd.merge(smpl,metadata, on = "sample-id")

    niceplot = sns.pairplot(smpl_metadata, hue = metadata_col, vars = ['Table 1','Table 2'])
    niceplot.savefig(os.path.join(output_dir, 'pleasework.png'))
    niceplot.savefig(os.path.join(output_dir, 'pleasework.pdf'))
    plt.gcf().clear()

    index = os.path.join(TEMPLATES, 'pairwise_assets', 'index.html')
    q2templates.render(index, output_dir)
"""
#    table_preview = metadata.to_html()
#    print(table_preview)
