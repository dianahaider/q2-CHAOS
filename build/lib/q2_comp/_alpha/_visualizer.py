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
import biom
import skbio
import sys

TEMPLATES = pkg_resources.resource_filename('q2_comp', '_alpha')

def alpha_frequency(output_dir: str,
                tables: biom.Table,
                metadata_column: str = None,
                metadata: qiime2.Metadata = None,
                palette: str = 'husl',
                style: str = 'white',
                context: str = 'paper',
                plot_type: str = 'all',
                labels : str = None) -> None:

#first 2 tables

    sample_frequencies1 = _frequencies(tables[0], axis='sample')
    sample_frequencies2 = _frequencies(tables[1], axis='sample')
    sample_frequencies1.sort_values(inplace=True, ascending=False)
    sample_frequencies2.sort_values(inplace=True, ascending=False)
    sample_frequencies_df1 = sample_frequencies1.to_frame()
    sample_frequencies_df2 = sample_frequencies2.to_frame()
    sample_frequencies_df1.index.name = "sample-id"
    sample_frequencies_df1.reset_index(inplace=True)
    sample_frequencies_df2.index.name = "sample-id"
    sample_frequencies_df2.reset_index(inplace=True)

    #if not metadata & labels:
    #    raise ValueError("Metadata file was not provided")

#if no labels are given, label the inputs as numbers
    if not labels:

        merged = pd.merge(sample_frequencies_df1, sample_frequencies_df2, on = "sample-id")
        merged = merged.rename(columns = {'0_x':'1', '0_y':'2'})
        vars_to_plot = ['1','2']


        if len(tables)>2:
            for i in range((len(tables))-2) :
                sample_frequencies = _frequencies(tables[i+2], axis='sample')
                sample_frequencies.sort_values(inplace=True, ascending=False)
                sample_frequencies_df = sample_frequencies.to_frame()
                sample_frequencies_df.index.name = "sample-id"
                sample_frequencies_df.reset_index(inplace=True)
                merged = pd.merge(merged, sample_frequencies_df, on = "sample-id")
                merged = merged.rename(columns = {0:(i+3)})
            vars_to_plot = list(merged.loc[:, merged.columns !='sample-id'])

    else:
        if len(labels) != len(tables):
            raise ValueError("The number of labels is different than the number of tables")
        sample_frequencies_df1.rename(columns = {"0":labels[0]})
        sample_frequencies_df2.rename(columns = {"0":labels[1]})
        vars_to_plot = list(merged.loc[:, merged.columns !='sample-id'])

        merged = pd.merge(sample_frequencies_df1, sample_frequencies_df2, on = "sample-id")

        if len(tables)>2:
            for i in range((len(tables))-2) :
                sample_frequencies = _frequencies(tables[i+2], axis='sample')
                sample_frequencies.sort_values(inplace=True, ascending=False)
                sample_frequencies_df = sample_frequencies.to_frame()
                sample_frequencies_df.index.name = "sample-id"
                sample_frequencies_df.reset_index(inplace=True)
                sample_frequencies_df.rename(columns = {"0":labels[i+2]})
                merged = pd.merge(merged, sample_frequencies_df, on = "sample-id")
            vars_to_plot = list(merged.loc[:, merged.columns !='sample-id'])

    melted_merged = pd.melt(merged, id_vars = 'sample-id')


    if not metadata:

        pairplot_frequency = sns.pairplot(merged, vars = vars_to_plot, palette = palette)

        raincloud_plot = pt.RainCloud( x = 'Table', y = 'Sequencing Depth', data = melted_merged,
                    orient = 'h', alpha = 0.65, palette = palette )

        boxplot = sns.boxplot(data=melted_merged,x='Table',y='Sequencing Depth', palette = palette, saturation = 1)

    else:

        metadata = metadata.to_dataframe()
        metadata.index.name = "sample-id"
        metadata.reset_index(inplace = True)
        merged_metadata = pd.merge(merged,metadata, on = "sample-id")

        melted_merged_metadata = pd.merge(melted_merged, metadata, on = "sample-id")
        melted_merged_metadata = melted_merged_metadata.rename(columns = {'variable':'Table', 'value':'Sequencing Depth'})

        pairplot_frequency = sns.pairplot(merged_metadata, hue = metadata_column, vars = vars_to_plot, palette = palette)

        raincloud_plot = pt.RainCloud( x = 'Table', y = 'Sequencing Depth', data = melted_merged_metadata,
                    orient = 'h', hue = metadata_column, alpha = 0.65, palette = palette )

        boxplot = sns.boxplot(data=melted_merged_metadata,x='Table',y='Sequencing Depth',hue=metadata_column, palette = palette, saturation = 1)

    sns.set_style(style)
    sns.set_context(context)

    pairplot_frequency.savefig(os.path.join(output_dir, 'pairplot_frequency.png'))
    pairplot_frequency.savefig(os.path.join(output_dir, 'pairplot_frequency.pdf'))
    plt.gcf().clear()

    raincloud_plot.figure.savefig(os.path.join(output_dir, 'raincloud.png'), bbox_inches = 'tight')
    raincloud_plot.figure.savefig(os.path.join(output_dir, 'raincloud.pdf'), bbox_inches = 'tight')
    plt.gcf().clear()

    sns.set_style(style)
    sns.set_context(context)

    boxplot = sns.boxplot(data=melted_merged_metadata,x='Table',y='Sequencing Depth',hue=metadata_column, palette = palette, saturation = 1)
    boxplot.figure.savefig(os.path.join(output_dir, 'boxplot.png'), bbox_inches = 'tight')
    boxplot.figure.savefig(os.path.join(output_dir, 'boxplot.pdf'), bbox_inches = 'tight')
    plt.gcf().clear()

    index = os.path.join(TEMPLATES, 'frequency_assets', 'index.html')
    q2templates.render(index, output_dir)


def adiv_raincloud(output_dir: str,
                tables: biom.Table,
                metadata_col: str,
                metadata: qiime2.Metadata,
                palette: str = 'husl',
                style: str = 'ticks',
                context: str = 'paper') -> None:
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
    metadata = metadata.to_dataframe()
    metadata.index.name = "sample-id"
    metadata.reset_index(inplace = True)
    sample_frequencies_df1.index.name = "sample-id"
    sample_frequencies_df1.reset_index(inplace=True)
    sample_frequencies_df2.index.name = "sample-id"
    sample_frequencies_df2.reset_index(inplace=True)
    smpl = pd.merge(sample_frequencies_df1, sample_frequencies_df2, on = "sample-id")
    smpl = smpl.rename(columns = {'0_x':'Table 1', '0_y':'Table 2'})
    melted_smpl = pd.melt(smpl, id_vars = 'sample-id')
    melted_smpl_metadata = pd.merge(melted_smpl, metadata, on = "sample-id")
    melted_smpl_metadata = melted_smpl_metadata.rename(columns = {'variable':'Table', 'value':'Sequencing Depth'})

    sns.set_style(style)
    sns.set_context(context)


    niceplot = pt.RainCloud( x = 'Table', y = 'Sequencing Depth', data = melted_smpl_metadata,
                orient = 'h', hue = metadata_col, alpha = 0.65, palette = (sns.set_palette(palette)) )
    niceplot.figure.savefig(os.path.join(output_dir, 'raincloud.png'), bbox_inches = 'tight')
    niceplot.figure.savefig(os.path.join(output_dir, 'raincloud.pdf'), bbox_inches = 'tight')
    plt.gcf().clear()

    index = os.path.join(TEMPLATES, 'raincloud_assets', 'index.html')
    q2templates.render(index, output_dir)

def adiv_raincloud_vector(output_dir: str,
                alpha_diversity: pd.Series,
                metadata_col: str,
                metadata: qiime2.Metadata) -> None:

    alpha_div1 = alpha_diversity1.to_frame()
    alpha_div2 = alpha_diversity2.to_frame()
    metadata = metadata.to_dataframe()
    metadata.index.name = "sample-id"
    metadata.reset_index(inplace = True)
    alpha_div1.index.name = "sample-id"
    alpha_div1.reset_index(inplace=True)
    alpha_div2.index.name = "sample-id"
    alpha_div2.reset_index(inplace=True)
    smpl = pd.merge(alpha_div1, alpha_div2, on = "sample-id")
    smpl = smpl.rename(columns = {'0_x':'Vector 1', '0_y':'Vector 2'})
    melted_smpl = pd.melt(smpl, id_vars = 'sample-id')
    melted_smpl_metadata = pd.merge(melted_smpl, metadata, on = "sample-id")
    melted_smpl_metadata = melted_smpl_metadata.rename(columns = {'variable':'Vectors', 'value':'A diversity'})

    niceplot = pt.RainCloud( x = 'Vectors', y = 'A diversity', data = melted_smpl_metadata, orient = 'h', hue = metadata_col, alpha = 0.65, palette = 'husl' )
    niceplot.figure.savefig(os.path.join(output_dir, 'rainclouda.png'), bbox_inches = 'tight')
    niceplot.figure.savefig(os.path.join(output_dir, 'rainclouda.pdf'), bbox_inches = 'tight')
    plt.gcf().clear()

    index = os.path.join(TEMPLATES, 'rainclouda_assets', 'index.html')
    q2templates.render(index, output_dir)

"""
    table_preview = melted_smpl_metadata.to_html()
    with open('outfile.html', 'w') as file:
        file.write(table_preview)
"""

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
