import os

import qiime2
import q2templates
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib
import matplotlib.pyplot as plt
import biom #need biom bcs import table.qza (FeatureTable[Frequency] format is biomtable

#import qiime2 q2 types
from q2_types.feature_table import FeatureTable, Frequency

#def merge_df(filenames, metadata=None, var=None):
def comp_pairwise(outputdir: str,
                table1: biom.Table,
                table2: biom.Table,
                sample_metadata: qiime2.CategoricalMetadataColumn) -> None:
            number_of_features, number_of_samples = table.shape

    # stolen from q2_diversity._alpha._visualizer.py to filter metadata by categorical column
    pre_filtered_cols = set(metadata.columns)
    metadata = metadata.filter_columns(column_type='categorical')
    non_categorical_columns = pre_filtered_cols - set(metadata.columns)
        pre_filtered_cols = set(metadata.columns)
    metadata = metadata.filter_columns(
        drop_all_unique=True, drop_zero_variance=True, drop_all_missing=True)
    filtered_columns = pre_filtered_cols - set(metadata.columns)

    if len(metadata.columns) == 0:
        raise ValueError(
            "Metadata does not contain any columns that satisfy this "
            "visualizer's requirements. There must be at least one metadata "
            "column that contains categorical data, isn't empty, doesn't "
            "consist of unique values, and doesn't consist of exactly one "
            "value.")

    #before running the comp pairwise, need the summary functions
    #code taken from q2-feature-table/q2_feature_table/_summarize/_visualizer.py from the summarize function
     sample_frequency_template = os.path.join(
        TEMPLATES, 'summarize_assets', 'sample-frequency-detail.html')
    sample_summary_table = q2templates.df_to_html(
        sample_summary.apply('{:,}'.format).to_frame('Frequency'))

    # run comp_pairwise
    smpl = pd.merge(table1, table2, on = 'sample')




    smpl = pd.merge(pd.read_csv(filenames[1]), pd.read_csv(filenames[2]), on = 'sample')
    for i in range(len(filenames)-1):
        smpl = pd.merge(smpl, pd.read_csv(filenames[i+2]), on = 'sample')
        if metadata:
            smpl.rename(columns={'sample':'sample-id'}, inplace=True)
            smpl = pd.merge(smpl,pd.read_csv(metadata), on = 'sample-id')
            if var:
                sns.pairplot(smpl, hue = 'var')
            else: return 'Variable must be provided if metadata'
        else: return sns.pairplot(smpl)
    return

def pairplt (filenames, metadata=None):
    smpl = pd.merge(pd.read_csv(filenames[1]), pd.read_csv(filenames[2]), on = 'sample')
    for i in range(len(filenames)-1):
        smpl = pd.merge(smpl, pd.read_csv(filenames[i+2]), on = 'sample')
        if metadata:
            smpl.rename(columns={'sample':'sample-id'}, inplace=True)
            smpl = pd.merge(smpl,pd.read_csv(metadata), on = 'sample-id')
            sns.pairplot(smpl, hue = 'depth_code', vars = ['f2','f27','f97-2'])
    else: return sns.pairplot(smpl, vars = ['f2','f27','f97-2'])
    return

#add a print some text if no parameters are supplied & have errors if smtg goes wrong so u know how to fix it as user

#add an --help & --citations

#add version (github controlled or versioneer......)

#add smtg to print when --verbose & use sys.stderr for msgs&errors : NOT stdout

#don't hardcode PATHS

#check that all dependencies are installed

#index.html has to be written to output_dir by the function
#return type is none