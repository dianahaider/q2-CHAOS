#add license

from qiime2.plugin import (Str, Citations, Plugin, Visualization, MetadataColumn, Categorical)
#import versioneer


#import my functions
import q2_comp
from q2_comp import _adiv as adiv
from q2_comp import _betadiv as betadiv
from q2_comp import _denoise as denoise
from q2_comp import _ml as ml
from q2_comp import _taxo as taxo


#import types
from q2_types.feature_table import FeatureTable, Frequency
from q2_types.distance_matrix import DistanceMatrix
from q2_types.sample_data import AlphaDiversity, SampleData
import q2_dada2
from q2_dada2 import DADA2Stats, DADA2StatsFormat, DADA2StatsDirFmt

#(add png downloadable format for all figures)

plugin = Plugin (
    name='comp',
    version='q2_comp.__version__',
    website='https://github.com/dianahaider/q2-comp',
    package='q2-comp',
    description=('This QIIME2 plugin compares two or more feature tables'
    '(generated) by different clustering methods from a single dataset'
    'through statistics and visualizations.'),
    short_description='Plugin to compare feature tables.',
)

#register the functions
#first function: pairwise comparison of either a diversity index (shannon) or feature table
#maybe combine fun1 and fun2 and add an input 'method: str = {pairwise, raincloud}'
plugin.visualizers.register_function(
    function=q2_comp.adiv_pairwise,
    inputs={
        'table1': FeatureTable[Frequency],
        'table2': FeatureTable[Frequency]
    },
    parameters={
        'sample_metadata': MetadataColumn[Categorical] #can seaborn support numerical metadata
    },
    input_descriptions={
        'table1': 'Frequency feature table containing the samples to be compared.',
        'table2': 'Frequency feature table containing the samples to be compared'
    },
    parameter_descriptions={
        'sample_metadata': 'Categorical metadata column to map plot to different colors.'
    },
    name= 'Frequency count pairwise plot',
    description= "Visually compare the frequency tables obtained by different clustering methods with pairwise plots of samples ranked by frequency and colored by metadata." ,

)

#second function: raincloud plot for a diversity or feature table (both boxplot and density plot)
plugin.visualizers.register_function(
    function=q2_comp.adiv_raincloud,
    inputs={
        'table1': FeatureTable[Frequency],
        'table2': FeatureTable[Frequency]
    },
    parameters={
        'sample_metadata': MetadataColumn[Categorical] #can seaborn support numerical metadata
    },
    input_descriptions={
        'table1': 'Frequency feature table containing the samples to be compared.',
        'table2': 'Frequency feature table containing the samples to be compared'
    },
    parameter_descriptions={
        'sample_metadata': 'Categorical metadata column to map plot to different colors.'
    },
    name='Frequency count boxplot',
    description= "Visually compare the frequency tables obtained by different clustering methods with probablity curves and boxplots of samples ranked by frequency and colored by metadata.",
)

#third function; statistical significance of adiv comparison
plugin.visualizers.register_function(
    function=q2_comp.adiv_stats,
    inputs={
        'table1': FeatureTable[Frequency],
        'table2': FeatureTable[Frequency]
    },
    parameters={
        'sample_metadata': MetadataColumn[Categorical] #can seaborn support numerical metadata
    },
    input_descriptions={
        'table1': 'Frequency feature table containing the samples to be compared.',
        'table2': 'Frequency feature table containing the samples to be compared'
    },
    parameter_descriptions={
        'sample_metadata': 'Categorical metadata column to map plot to different colors.'
    },
    name='Frequency count statistics',
    description="Statistically compare the frequency tables obtained by different clustering methods.",
)

#add pipeline function for all a_div

"""
#function4: alternative to mantel test.... or combination of 2 plots
#take as input distance matrices
plugin.visualizers.register_function(
    function=q2_comp.comp_beta,
    inputs={
        'dm1': skbio.DistanceMatrix,
        'dm2': skbio.DistanceMatrix
    },
    parameters={
        'metadata': MetadataColumn[Categorical]
    },
    outputs=[
        ('notsureyet', Visualization)
        #('merged_tables', also add csv of the merged tables)
    ],
    input_description={
        'dm1': 'Distance matrix between pairs of samples obtained from one method.',
        'dm2': 'Distance matrix between pairs of samples obtained from a different method.'
    },
    parameter_description={
        'metadata': 'Categorical metadata column to map plot to different colors.'
    },
    name={
        'Distance matrix comparison'
    },
    description={
        'Visually compare two distance matrices to identify the correlation between'
        'methods for assessment of beta diversity.'
    },
    citations=[]

)


#function5: denoise bar diagram take as input stats from qiime2 can only do dada2 for now!
plugin.visualizers.register_function(
    function=q2_comp._denoise,
    inputs={
        'stats1': SampleData[DADA2Stats],
        'stats2': SampleData[DADA2Stats]
    },
    #no metadata here! UNLESS think of complex figure able to show per md categorical column
    input_descriptions={
        'stats1': 'Denoising statistics from DADA2',
        'stats2': 'Denoising statistics from DADA2 with different parameters.'
    },
    parameters={

    }
    name= 'Denoising statistics comparison',
    description= "Visually compare the denoising statistics from DADA2 using two different sets of parameters to assess which denoising steps are more stringent.",
)


#function6: machine learning for prediction of sample metadata
#in qiime2 you can do -classify samples (nested cross validation)
                    # -fit supervised learning
                    # -random forest

plugin.visualizers.register_function(
    function=q2_comp.comp_ml,
    inputs={
        'model-summary1': something,
        'model-summary2': something something
    },
    #no metadata here! UNLESS think of complex figure able to show per md categorical column
    outputs=[
        ('#####', Visualization)
    ],
    input_description={
        'model-summary1': 'Table with model accuracy, and ####',
        'model-summary2': 'Table from same method but different clustering'
    },
    parameter_description={
        'metadata': 'Categorical metadata column to map plot to different colors.'
    },
    name={
        'Model accuracy comparison'
    },
    description={
        'Visually compare one machine learning model from two different'
        'clustering methods to assess which clustering model predicts the data'
        'best.'
    },
    citations=[]

)

#function7: taxonomic comparison (how well does it assign taxonomy from these repseqs)
#sklearn classifier or VSEARCH or naivebayes
plugin.visualizers.register_function(
    function=q2_comp.comp_taxo,
    inputs={
        'taxo1': something,
        'taxo2': something something
    },
    outputs=[
        ('barplot', Visualization)
    ],
    input_description={
        'taxo1': 'Taxonomic classification from one feature table',
        'taxo2': 'Taxonomic classification from a different feature table'
    },
    parameter_description={
        'metadata': 'Categorical metadata column to map plot to different colors.'
    },
    name={
        'Taxonomic classification comparison'
    },
    description={
        'Visually compare the assignment of taxonomy from the same dataset using'
        'two different clustering methods.'
    },
    citations=[]

)
"""
