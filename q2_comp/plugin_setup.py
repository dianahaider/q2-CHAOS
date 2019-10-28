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

#(add png downloadable format for all figures)

plugin = Plugin (
    name='comp',
    version='q2_comp.__version__',
    website='https://github.com/dianahaider/q2-comp',
    package='q2-comp',
    citations='',
    description=('This QIIME2 plugin compares two or more feature tables'
    '(generated) by different clustering methods from a single dataset'
    'through statistics and visualizations.'),
    short_description='Plugin to compare feature tables.',
)

#register the functions
#first function: pairwise comparison of either a diversity index (shannon) or feature table
#maybe combine fun1 and fun2 and add an input 'method: str = {pairwise, raincloud}'
plugin.visualizers.register_function(
    function=q2_comp.comp_pairwise,
    inputs={
        'table1': FeatureTable[Frequency],
        'table2': FeatureTable[Frequency]
    },
    parameters={
        'metadata': MetadataColumn[Categorical] #can seaborn support numerical metadata
    },
    outputs=[
        ('pairplot', Visualization)
        #('merged_tables', also add csv of the merged tables)
    ],
    input_description={
        'table1': 'Frequency feature table containing the samples to be compared.',
        'table2': 'Frequency feature table containing the samples to be compared'
    },
    parameter_description={
        'metadata': 'Categorical metadata column to map plot to different colors.'
    },
    name={
        'Frequency count pairwise plot'
    },
    description={
        'Visually compare the frequency tables obtained by different clustering',
        'methods with pairwise plots of samples ranked by frequency and colored',
        'by metadata.'
    },
    citations=[]
)

#second function: raincloud plot for a diversity or feature table (both boxplot and density plot)
plugin.visualizers.register_function(
    function=q2_comp.comp_raincloud,
    inputs={
        'table1': FeatureTable[Frequency],
        'table2': FeatureTable[Frequency]
    },
    parameters={
        'metadata': MetadataColumn[Categorical] #can seaborn support numerical metadata
    },
    outputs=[
        ('raincloudplot', Visualization)
        #('merged_tables', also add csv of the merged tables)
    ],
    input_description={
        'table1': 'Frequency feature table containing the samples to be compared.',
        'table2': 'Frequency feature table containing the samples to be compared'
    },
    parameter_description={
        'metadata': 'Categorical metadata column to map plot to different colors.'
    },
    name={
        'Frequency count boxplot'
    },
    description={
        'Visually compare the frequency tables obtained by different clustering',
        'methods with probablity and box plots of samples ranked by frequency and',
        'colored by metadata.'
    },
    citations=[]
)

#third function; statistical significance of adiv comparison
plugin.visualizers.register_function(
    function=q2_comp.comp_stats,
    inputs={
        'table1': FeatureTable[Frequency],
        'table2': FeatureTable[Frequency]
    },
    parameters={
        'metadata': MetadataColumn[Categorical] #can seaborn support numerical metadata
    },
    outputs=[
        ('markdown', Visualization)
        #('merged_tables', also add csv of the merged tables)
    ],
    input_description={
        'table1': 'Frequency feature table containing the samples to be compared.',
        'table2': 'Frequency feature table containing the samples to be compared'
    },
    parameter_description={
        'metadata': 'Categorical metadata column to map plot to different colors.'
    },
    name={
        'Frequency count statistics'
    },
    description={
        'Statistically compare the frequency tables obtained by different clustering',
        'methods.'
    },
    citations=[]

)

#add pipeline function for all a_div


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
    function=q2_comp.comp_denoise,
    inputs={
        'stats1': SampleData[DADA2Stats],
        'stats2': SampleData[DADA2Stats]
    },
    #no metadata here! UNLESS think of complex figure able to show per md categorical column
    outputs=[
        ('barplot', Visualization)
    ],
    input_description={
        'stats1': 'Denoising statistics from DADA2',
        'stats2': 'Denoising statistics from DADA2 with different parameters.'
    },
    #parameter_description={
    #    'metadata': 'Categorical metadata column to map plot to different colors.'
    #},
    name={
        'Denoising statistics comparison'
    },
    description={
        'Visually compare the denoising statistics from DADA2 using two different'
        'sets of parameters to assess which denoising steps are more stringent.'
    },
    citations=[]

)

#function6: machine learning for prediction of sample metadata
#in qiime2 you can do -classify samples (nested cross validation)
                    # -fit supervised learning
                    # -random forest
plugin.visualizers.register_function(
    function=q2_comp.comp_ml,
    inputs={
        'model-summary1': SampleData[DADA2Stats],
        'model-summary2': SampleData[DADA2Stats]
    },
    #no metadata here! UNLESS think of complex figure able to show per md categorical column
    outputs=[
        ('barplot', Visualization)
    ],
    input_description={
        'stats1': 'Denoising statistics from DADA2.',
        'stats2': 'Denoising statistics from DADA2 with different parameters.'
    },
    #parameter_description={
    #    'metadata': 'Categorical metadata column to map plot to different colors.'
    #},
    name={
        'Distance matrix comparison'
    },
    description={
        'Visually compare two distance matrices to identify the correlation.'
    },
    citations=[]

)

#function5: denoise bar diagram
#take as input stats from qiime2 can only do dada2 for now!
plugin.visualizers.register_function(
    function=q2_comp.comp_denoise,
    inputs={
        'stats1': SampleData[DADA2Stats],
        'stats2': SampleData[DADA2Stats]
    },
    #no metadata here! UNLESS think of complex figure able to show per md categorical column
    outputs=[
        ('barplot', Visualization)
    ],
    input_description={
        'stats1': 'Denoising statistics qza.',
        'stats2': 'Distance matrix between pairs of samples obtained from a different method.'
    },
    parameter_description={
        'metadata': 'Categorical metadata column to map plot to different colors.'
    },
    name={
        'Distance matrix comparison'
    },
    description={
        'Visually compare two distance matrices to identify the correlation.'
    },
    citations=[]

)
