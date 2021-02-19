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
import re
import matplotlib.pyplot as plt
import matplotlib.pylab
#import ptitprince as pt
from scipy.spatial.distance import pdist, squareform
from sklearn import preprocessing
import sklearn
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mutual_info_score
from sklearn.feature_selection import mutual_info_classif
from sklearn.feature_selection import mutual_info_regression
from sklearn.linear_model import LassoCV



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
    merged_1 = merged_1.groupby(['Taxon']).sum()

    print('merged first table ...')

    #repeat the same method but for table/taxo2
    sum2 = tables[1].sum()
    sum2.sort_values(inplace = True, ascending = False)
    sum2_df = sum2.to_frame()
    sum2_df.index.name = 'Feature-ID'
    taxo_df2 = taxonomy[1].to_frame()
    taxo_df2.index.name = 'Feature-ID'
    merged_2 = pd.merge(sum2_df, taxo_df2, on = "Feature-ID")
    merged_2 = merged_2.rename(columns = {0:2})
    merged_2 = merged_2.groupby(['Taxon']).sum()
    print('merged second table ...')

    #now merge the two dataframes on their taxonomy
    merged = pd.merge(merged_1, merged_2, on = "Taxon", how='outer')
    #merged_1_2 is index=taxon name & each column is one method
    print (merged)

    if len(taxonomy)>2:
        if len(tables) != len(taxonomy):
            raise ValueError("The number of tables is different than the number of taxonomies")

        for i in range((len(tables))-2) :
            sum = tables[i+2].sum()
            sum.sort_values(inplace = True, ascending = False)
            sum_df = sum.to_frame()
            sum_df.index.name = 'Feature-ID'
            taxo_df = taxonomy[i+2].to_frame()
            taxo_df.index.name = 'Feature-ID'
            merged_t = pd.merge(sum_df, taxo_df, on = "Feature-ID")
            merged_t = merged_t.rename(columns = {0:(i+3)})
            merged_t = merged_t.groupby(['Taxon']).sum()
            merged = pd.merge(merged, merged_t, on = "Taxon", how='outer')

    print (merged)
    print ('merged all tables ...')
    print (merged)
    #group by taxon because we don't care for per sample
    taxons = merged.groupby(['Taxon']).sum()
    #transform index to colum for melting
    #merged_grouped_taxons['Taxon'] = merged_grouped_taxons.index
    #merged_grouped_taxons.reset_index

    print ('merged_grouped_taxons')

    variances = []
    for i in range(len(taxons.index)):
        var_temp = np.var(taxons.iloc[i,:])
        variances.append(var_temp)

    taxons['variance'] = variances

    table_preview = taxons.to_csv()
    with open('alltaxons.csv', 'w') as file:
        file.write(table_preview)

    df_most_var = taxons.loc[taxons['variance'] >= taxons.variance.quantile(quantile)]
    df_most_var = df_most_var.sort_values(by=['variance'])
    df_most_var_plot = df_most_var.drop(columns = ['variance'])
    df_most_var_plot = (np.log(df_most_var_plot)).replace(-np.inf, 0)
    print (df_most_var_plot)

    df_less_var = taxons.loc[taxons['variance'] <= taxons.variance.quantile(quantile)]
    df_less_var = df_less_var.sort_values(by=['variance'], ascending=False)
    df_less_var_plot = df_less_var.drop(columns = ['variance'])
    df_less_var_plot = (np.log(df_less_var_plot)).replace(-np.inf, 0)
    print (df_less_var_plot)

    table_preview = df_less_var_plot.to_csv()
    with open('mostvar_table.csv', 'w') as file:
        file.write(table_preview)

    table_preview = df_less_var_plot.to_csv()
    with open('lessvar_table.csv', 'w') as file:
        file.write(table_preview)

    table1_html = q2templates.df_to_html(df_most_var_plot)
    df_most_var_plot.to_csv(os.path.join(output_dir, 'table.csv'))

    table2_html = q2templates.df_to_html(df_less_var_plot)
    df_less_var_plot.to_csv(os.path.join(output_dir, 'table.csv'))

    #add pca plot
    pca_plot = taxons.drop(columns = ['variance'])
    print ('pca dataframe')
    pca_plot = pca_plot.reset_index()
    pca_plot = pca_plot.drop(columns=['index'])
    print ('drop dataframe index')

    y = pca_plot.loc[:,['id']].values
    x = feature_tables.values
    x = StandardScaler().fit_transform(x)
    df = pd.DataFrame(data = x, columns = df_x.columns)

    pca = PCA(n_components=2)
    principalComponents = pca.fit_transform(x)
    principalDf = pd.DataFrame(data = principalComponents
             , columns = ['principal component 1', 'principal component 2'])
    principalDf.head(5)
    feature_tables['id'] =['DADA_2', 'DADA_3', 'DADA_4','DADA_1','Deblur_3','Deblur_4','Deblur_1','Deblur_2']
    col_one_list = finalDf['id'].tolist()
    len(col_one_list)
    finalDf = pd.concat([principalDf, feature_tables[['id']]], axis = 1)
    finalDf.head(5)

    fig = plt.figure(figsize = (8,8))
    ax = fig.add_subplot(1,1,1)
    ax.set_xlabel('Principal Component 1', fontsize = 15)
    ax.set_ylabel('Principal Component 2', fontsize = 15)
    ax.set_title('PCA of taxonomy assignment', fontsize = 20)

    targets =['DADA_1', 'DADA_2', 'DADA_3','DADA_4','Deblur_3', 'Deblur_2','Deblur_1','Deblur_4']
    colors = ['#E5FCC2','#9DE0AD','#45ADA8','#547980','#F26B38', '#EC2049','#A7226E','#F7DB4F']
    for target, color in zip(targets, colors):
        indicesToKeep = finalDf['id'] == target
        ax.scatter(finalDf.loc[indicesToKeep, 'principal component 1']
                , finalDf.loc[indicesToKeep, 'principal component 2']
                , c = color
                , s = 50)
    ax.legend(targets)
    ax.grid()


#    merged_1_2['variance'] = variances

    heatmap_most = sns.heatmap(df_most_var_plot, linewidths= .2, cmap="YlGnBu")
    heatmap_less = sns.heatmap(df_less_var_plot, linewidths= .2, cmap="YlGnBu")


    heatmap_most.figure.savefig(os.path.join(output_dir, 'heatmap_most.png'), bbox_inches = 'tight')
    heatmap_most.figure.savefig(os.path.join(output_dir, 'heatmap_most.pdf'), bbox_inches = 'tight')
    plt.gcf().clear()

    heatmap_less.figure.savefig(os.path.join(output_dir, 'heatmap_less.png'), bbox_inches = 'tight')
    heatmap_less.figure.savefig(os.path.join(output_dir, 'heatmap_less.pdf'), bbox_inches = 'tight')
    plt.gcf().clear()

    ax.figure.savefig(os.path.join(output_dir, 'pca_all.pdf'), bbox_inches = 'tight')
    ax.figure.savefig(os.path.join(output_dir, 'pca_all.pdf'), bbox_inches = 'tight')


    index = os.path.join(TEMPLATES, 'taxonomy_assets', 'index.html')
    q2templates.render(index, output_dir)



"""
    x = merged_grouped_taxons.values
    min_max_scaler = preprocessing.MinMaxScaler()
    x_scaled = min_max_scaler.fit_transform(x)
    scaled_taxons = pd.DataFrame(x_scaled, columns = merged_grouped_taxons.columns)
"""




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





"""
################### june 10
#tempted to print the tables
def _build_seq_len_table(qscores: pd.DataFrame) -> str:
    sequence_lengths = qscores.notnull().sum(axis=1).copy()
    stats = _compute_stats_of_df(sequence_lengths)

    stats[stats.index != 'count'] = \
        stats[stats.index != 'count'].astype(int).apply('{} nts'.format)

    stats.rename(index={'50%': '50% (Median)',
                        'count': 'Total Sequences Sampled'},
                 inplace=True)
    frame = stats.to_frame(name="")
    return q2templates.df_to_html(frame)


        html_df = result.to_frame()
        context['result'] = context['result'].join(html_df, how='outer')

   context['result_data'] = \
        q2templates.df_to_html(context['result_data'].transpose())

    # Create a TSV before turning into HTML table
    result_fn = 'per-sample-fastq-counts.tsv'
    result_path = os.path.join(output_dir, result_fn)
    context['result'].to_csv(result_path, header=True, index=True, sep='\t')

    context['result'] = q2templates.df_to_html(context['result'])

    q2templates.render(templates, output_dir, context=context)

    shutil.copytree(os.path.join(TEMPLATES, 'assets', 'dist'),
                    os.path.join(output_dir, 'dist'))

    with open(os.path.join(output_dir, 'data.jsonp'), 'w') as fh:
        fh.write("app.init(")
        json.dump({'subsampleSize': subsample_size,
                   'totalSeqCount': sequence_count,
                   'minSeqLen': min_seq_len}, fh)
        fh.write(', ')
        if qual_stats['forward'] is not None and not \
                qual_stats['forward'].empty:
            qual_stats['forward'].to_json(fh)
        else:
            fh.write('undefined')
        fh.write(', ')
        if qual_stats['reverse'] is not None and not \
                qual_stats['reverse'].empty:
            qual_stats['reverse'].to_json(fh)
        else:
            fh.write('undefined')
        fh.write(');')

################## june 10
"""








#add a print some text if no parameters are supplied & have errors if smtg goes wrong so u know how to fix it as user

#add an --help & --citations

#add version (github controlled or versioneer......)

#add smtg to print when --verbose & use sys.stderr for msgs&errors : NOT stdout

#don't hardcode PATHS

#check that all dependencies are installed

#index.html has to be written to output_dir by the function
#return type is none
