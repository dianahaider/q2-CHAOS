import os
import json
import pkg_resources
import shutil

import qiime2
import q2templates

from q2_types.feature_table import FeatureTable, Frequency
from q2_types.feature_data import FeatureData, Taxonomy, Sequence

import pandas as pd
import numpy as np
import seaborn as sns
import scipy.stats
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.pylab
import ptitprince as pt
from scipy.spatial.distance import pdist, squareform



TEMPLATES = pkg_resources.resource_filename('q2_comp', '_alpha')

def taxo_variability(output_dir: str,
                taxonomy: pd.Series,
                tables: pd.DataFrame,
                metadata_column: str = None,
                metadata: qiime2.Metadata = None,
                palette: str = 'husl',
                style: str = 'white',
                context: str = 'paper',
#                plot_type: str = 'all',
                labels : str = None) -> None:

#first 2 tables
    sum1 = tables[0].sum()
    sum1.sort_values(inplace = True, ascending = False)
    sum1_df = sum1.to_frame()
    sum1_df.index.name = "Feature-ID"
    print("indexed 1")
#prepare to merge taxonomy
    taxo_df1 = taxonomy[0].to_frame()
    taxo_df1.index.name = "Feature-ID"
    merged_1 = pd.merge(sum1_df, taxo_df1, on = "Feature-ID")
    merged_1.set_index('Taxon', inplace = True)
    merged_1.reset_index(inplace=True)
    print("merged 1")

    table_preview = merged_1.to_html()
    with open('merged_1.html', 'w') as file:
        file.write(table_preview)
    print("to html 1")

    sum2 = tables[1].sum()
    sum2.sort_values(inplace = True, ascending = False)
    sum2_df = sum2.to_frame()
    sum2_df.index.name = "Feature-ID"
    taxo_df2 = taxonomy[1].to_frame()
    taxo_df2.index.name = "Feature-ID"
    merged_2 = pd.merge(sum2_df, taxo_df2, on = "Feature-ID")
    merged_2.set_index('Taxon', inplace = True)
    merged_2.reset_index(inplace=True)
    print("same to 2")

    merged_1_2 = pd.merge(merged_1, merged_2, on = "Taxon")
    print("merged 1 and 2")

    table_preview = merged_1_2.to_html()
    with open('mergedtaxo.html', 'w') as file:
        file.write(table_preview)

"""


    merged_1 = pd.merge(sum1_df, taxo_df, on = "Feature-ID")

    if not labels:
        merged = pd.merge(sum1_df, sum2_df, on = "Feature-ID")
        merged = merged.rename(columns = {'0_x' : '1', '0_y' : '2'})
        vars_to_plot = ['1', '2']

        taxo_df = taxonomy[0].to_frame()
        merged_taxo = pd.merge(merged, taxo_df, on = "Feature-ID")

    table_preview = merged_1.to_html()
    with open('mergedtaxo.html', 'w') as file:
        file.write(table_preview)


    for i in range(len(tables)):
        new_sum = tables[i].sum()
        new_sum.to_frame()
        new_sum.index_name = "Feature-ID"
"""

"""
    di = tables[0]
    table_preview = di.to_html()
    with open('preview2.html', 'w') as file:
        file.write(table_preview)
"""



#add a print some text if no parameters are supplied & have errors if smtg goes wrong so u know how to fix it as user

#add an --help & --citations

#add version (github controlled or versioneer......)

#add smtg to print when --verbose & use sys.stderr for msgs&errors : NOT stdout

#don't hardcode PATHS

#check that all dependencies are installed

#index.html has to be written to output_dir by the function
#return type is none
