import os

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

#def merge_df(filenames, metadata=None, var=None):
def adiv_pairwise(output_dir: str,
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
    return sns.pairplot(smpl)




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
def _frequencies(table1, axis):
    return pd.Series(data=table.sum(axis=axis), index=table.ids(axis=axis))




#add a print some text if no parameters are supplied & have errors if smtg goes wrong so u know how to fix it as user

#add an --help & --citations

#add version (github controlled or versioneer......)

#add smtg to print when --verbose & use sys.stderr for msgs&errors : NOT stdout

#don't hardcode PATHS

#check that all dependencies are installed

#index.html has to be written to output_dir by the function
#return type is none
