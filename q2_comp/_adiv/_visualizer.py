import os
import json
import pkg_resources
import shutil

import qiime2
import q2templates

from q2_types.feature_table import FeatureTable, Frequency

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib
import matplotlib.pyplot as plt
import ptitprince as pt
import biom #need biom bcs import table.qza (FeatureTable[Frequency] format is biomtable
import skbio

TEMPLATES = pkg_resources.resource_filename('q2_comp', '_adiv')

#def merge_df(filenames, metadata=None, var=None):
def adiv_pairwise(output_dir: str,
                table1: biom.Table,
                table2: biom.Table,
                sample_metadata: qiime2.CategoricalMetadataColumn) -> None:
    number_of_features1, number_of_samples1 = table1.shape
    number_of_features2, number_of_samples2 = table2.shape
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
    sample_frequencies_df1.index.name = "sample-id"
    sample_frequencies_df1.reset_index(inplace=True)
    sample_frequencies_df2.index.name = "sample-id"
    sample_frequencies_df2.reset_index(inplace=True)
    smpl = pd.merge(sample_frequencies_df1, sample_frequencies_df2, on = "sample-id")
    niceplot = sns.pairplot(smpl)
    niceplot.savefig(os.path.join(output_dir, 'pleasework.png'))
    plt.gcf().clear()

    #niceplot.get_figure().savefig(os.path.join(output_dir, 'pleasework.png'))

    index = os.path.join(TEMPLATES, 'assets', 'index.html')
    q2templates.render(index, output_dir)

    #table_preview = smpl.to_html()
    #print(table_preview)


def adiv_raincloud(output_dir: str,
                    table1: biom.Table,
                    table2: biom.Table,
                    sample_metadata: qiime2.CategoricalMetadataColumn) -> None:
    sample_frequencies1 = _frequencies(
    table1, axis='sample')
    sample_frequencies1.sort_values(inplace=True, ascending=False)
    sample_frequencies1.to_csv(
                os.path.join(output_dir, 'sample-frequency-detail1.csv'))
    sample_frequencies2 = _frequencies(
        table2, axis='sample')
    sample_frequencies2.sort_values(inplace=True, ascending=False)
    sample_frequencies2.to_csv(
                os.path.join(output_dir, 'sample-frequency-detail2.csv'))
    smpl = pd.merge(sample_frequencies1, sample_frequencies2, on = 'sample')
    smpl = pd.melt(smpl, id_vars = 'sample-id')
    return pt.RainCloud(x = 'variable', y = 'value', data = smpl, orient = 'h',
                        hue = sample_metadata)


def adiv_stats(output_dir: str,
                    table1: biom.Table,
                    table2: biom.Table,
                    sample_metadata: qiime2.CategoricalMetadataColumn) -> None:
    sample_frequencies1 = _frequencies(
    table1, axis='sample')
    sample_frequencies1.sort_values(inplace=True, ascending=False)
    sample_frequencies1.to_csv(
                os.path.join(output_dir, 'sample-frequency-detail1.csv'))
    sample_frequencies2 = _frequencies(
        table2, axis='sample')
    sample_frequencies2.sort_values(inplace=True, ascending=False)
    sample_frequencies2.to_csv(
                os.path.join(output_dir, 'sample-frequency-detail2.csv'))
    smpl = pd.merge(sample_frequencies1, sample_frequencies2, on = 'sample')
    smpl = pd.melt(smpl, id_vars = 'sample-id')
    return pt.RainCloud(x = 'variable', y = 'value', data = smpl, orient = 'h',
                        hue = sample_metadata)


#taken from q2-feature-table/_visualizer
def _frequencies(table, axis):
    return pd.Series(data=table.sum(axis=axis), index=table.ids(axis=axis))




#add a print some text if no parameters are supplied & have errors if smtg goes wrong so u know how to fix it as user

#add an --help & --citations

#add version (github controlled or versioneer......)

#add smtg to print when --verbose & use sys.stderr for msgs&errors : NOT stdout

#don't hardcode PATHS

#check that all dependencies are installed

#index.html has to be written to output_dir by the function
#return type is none
