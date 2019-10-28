#add license

from qiime2.plugin import (Str, Citations, Plugin, Visualization, MetadataColumn, Categorical)
#import versioneer

#import types
from q2_types.feature_table import FeatureTable, Frequency

#import my functions
import q2_comp
from q2_comp import _adiv
import _adiv


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


#function4: alternative to mantel test.... or combination of 2 plots
plugin.visualizers.register_function(
    function=q2_comp.comp_beta,
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
