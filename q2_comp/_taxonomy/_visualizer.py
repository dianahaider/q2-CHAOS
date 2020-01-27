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
from sklearn import preprocessing



TEMPLATES = pkg_resources.resource_filename('q2_comp', '_taxonomy')

def taxo_variability(output_dir: str,
                taxonomy: pd.Series,
                tables: pd.DataFrame,
                metadata_column: str = None,
                metadata: qiime2.Metadata = None,
                palette: str = 'husl',
                style: str = 'white',
                context: str = 'paper',
                quantile: float = 0.8,
#                plot_type: str = 'all',
                labels : str = None) -> None:

#first 2 tables
    #tables is a list of pd.DataFrames of rows = samples and columns = feature_data
    #sum outputs a list of the sums of each column (aka frequency of a specific feature ID accross all samples)
    sum1 = tables[0].sum()
    sum1.sort_values(inplace = True, ascending = False)
    sum1_df = sum1.to_frame()
    #sum1_df is a dataframe with index= feature-ID and column2= frequency across all samples
    #give the index a name
    sum1_df.index.name = 'Feature-ID'
    #prepare to merge taxonomy
    #taxonomy is a list of pd.series with the corresponding feature-id to taxonomy
    #so first transform to a frame
    taxo_df1 = taxonomy[0].to_frame()
    #Feature-ID is the index
    taxo_df1.index.name = 'Feature-ID'
    #now merge the 2 dataframes to get one dataframe of Taxon, Feature ID, and frequency for method1
    merged_1 = pd.merge(sum1_df, taxo_df1, on = "Feature-ID")
    #Taxon is a column, and Feature-ID is the index_name
    #get rid of feature-id for this analysis by setting the taxon as the index id
    merged_1.set_index('Taxon', inplace = True)
    merged_1.reset_index(inplace = True)
    #because the frequency didn't ahve a column name, rename it 1 or by the label given
    merged_1 = merged_1.rename(columns = {0:1})

    #repeat the same method but for table/taxo2
    sum2 = tables[1].sum()
    sum2.sort_values(inplace = True, ascending = False)
    sum2_df = sum2.to_frame()
    sum2_df.index.name = 'Feature-ID'
    taxo_df2 = taxonomy[1].to_frame()
    taxo_df2.index.name = 'Feature-ID'
    merged_2 = pd.merge(sum2_df, taxo_df2, on = "Feature-ID")
    merged_2 = merged_2.rename(columns = {0:2})

    #now merge the two dataframes on their taxonomy
    merged_1_2 = pd.merge(merged_1, merged_2, on = "Taxon")
    #merged_1_2 is index=taxon name & each column is one method

    #group by taxon because we don't care for per sample
    merged_grouped_taxons = merged_1_2.groupby(['Taxon']).sum()
    #transform index to colum for melting
    #merged_grouped_taxons['Taxon'] = merged_grouped_taxons.index
    #merged_grouped_taxons.reset_index

    print (merged_grouped_taxons)

    variances = []
    for i in range(len(merged_grouped_taxons.index)):
        var_temp = np.var(merged_grouped_taxons.iloc[i,:])
        variances.append(var_temp)

    merged_grouped_taxons['variance'] = variances
    new_df = merged_grouped_taxons.loc[merged_grouped_taxons['variance'] >= merged_grouped_taxons.variance.quantile(quantile)]
    new_df = new_df.sort_values(by=['variance'])
    df_to_plot = new_df.drop(columns = ['variance'])
    print (df_to_plot)


#    merged_1_2['variance'] = variances

    heatmap = sns.heatmap(df_to_plot, linewidths= .2, cmap="YlGnBu")

    heatmap.figure.savefig(os.path.join(output_dir, 'heatmap.png'), bbox_inches = 'tight')
    heatmap.figure.savefig(os.path.join(output_dir, 'heatmap.pdf'), bbox_inches = 'tight')
    plt.gcf().clear()


    index = os.path.join(TEMPLATES, 'taxonomy_assets', 'index.html')
    q2templates.render(index, output_dir)


"""
    temp_values = merged_grouped_taxons.values
    min_max_scaler = preprocessing.MinMaxScaler()
    temp_values_scaled = min_max_scaler.fit_transform(temp_values)
    norm_data = pd.DataFrame(temp_values_scaled)

    print(temp_values_scaled)
"""


"""
    #sort the dataframe by highest values for variances
    sorted_by_var = merged_without_sample_id.sort.values('variance')
    #return top n rows with highest variance
    # create a new dataframe with only the most variable taxonomies
    mostVar = sorted_by_var
"""
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
