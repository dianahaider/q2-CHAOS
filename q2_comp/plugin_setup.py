#add license

from qiime2.plugin import   (Str, Citations, Plugin, Visualization, MetadataColumn,
                            Categorical, Metadata, Set, Numeric, Choices, List)
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
        'metadata': Metadata, #can seaborn support numerical metadata?
        'metadata_col': Str
    },
    input_descriptions={
        'table1': 'Frequency feature table containing the samples to be compared.',
        'table2': 'Frequency feature table containing the samples to be compared'
    },
    parameter_descriptions={
        'metadata': 'Sample metadata containing metadata_column which will be used to map color the plot.',
        'metadata_col': 'Sample metadata column to use to map color the plot.'
    },
    name= 'Frequency count pairwise plot',
    description= "Visually compare the frequency tables obtained by different clustering methods with pairwise plots of samples ranked by frequency and colored by metadata." ,

)
#maybe can add parameters for labels
#second function: raincloud plot for a diversity or feature table (both boxplot and density plot)
plugin.visualizers.register_function(
    function=q2_comp.adiv_raincloud,
    inputs={
        'table1': FeatureTable[Frequency],
        'table2': FeatureTable[Frequency]
    },
    parameters={
        'metadata': Metadata,
        'metadata_col': Str,
        'palette': Str,
        'style': Str,
        'context': Str
    },
    input_descriptions={
        'table1': 'Frequency feature table containing the samples to be compared.',
        'table2': 'Frequency feature table containing the samples to be compared'
    },
    parameter_descriptions={
        'metadata': 'Sample metadata',
        'metadata_col': 'Categorical metadata column to map plot to different colors.',
        'palette': 'Palette to be chosen from seaborn color palette. Existing color palettes are available through seaborn website.',
        'style': 'Set a figure style according to personal preferences amongst: darkgrid, whitegrid, dark, white, and ticks.',
        'context': 'Set a figure context according to plot use. Contexts are: paper, notebook, talk and poster.'
    },
    name='Frequency count boxplot',
    description= "Visually compare the frequency tables obtained by different clustering methods with probablity curves and boxplots of samples ranked by frequency and colored by metadata.",
)

#test function here for a_div vectors
plugin.visualizers.register_function(
    function=q2_comp.adiv_raincloud_vector,
    inputs={
        'alpha_diversity1': SampleData[AlphaDiversity],
        'alpha_diversity2': SampleData[AlphaDiversity]
    },
    parameters={
        'metadata': Metadata,
        'metadata_col': Str
    },
    input_descriptions={
        'alpha_diversity1': 'Frequency feature table containing the samples to be compared.',
        'alpha_diversity2': 'Frequency feature table containing the samples to be compared'
    },
    parameter_descriptions={
        'metadata': 'Sample metadata',
        'metadata_col': 'Categorical metadata column to map plot to different colors.'
    },
    name='Frequency count boxplot',
    description= "Visually compare the frequency tables obtained by different clustering methods with probablity curves and boxplots of samples ranked by frequency and colored by metadata.",
)

"""
#third function; statistical significance of adiv comparison
plugin.visualizers.register_function(
    function=q2_comp.adiv_stats,
    inputs={
        'table1': FeatureTable[Frequency],
        'table2': FeatureTable[Frequency]
    },
    parameters={
        'sample_metadata': MetadataColumn[Categorical] #can seaborn support numerical metadata
    },from q2_types.feature_table import DADA2Stats

    input_descriptions={
        'table1': 'Frequency feature table containing the samples to be compared.',
        'table2': 'Frequency feature table containing the samples to be compared'
    },
    parameter_descriptions={
        'sample_metadata': 'Categorical metadata column.'
    },
    name='Frequency count statistics',
    description="Statistically compare the frequency tables obtained by different clustering methods.",
)

#add pipeline function for all a_div

plugin.pipelines.register_function(
    functin=q2_comp.all_alpha_comparison,
    inputs={
        'table': List[Frequency],
        'alpha_diveristy': List[AlphaDiversity]
    },
    parameters={
        'metadata': Metadata,
        'metadata_col': Str
    },
    outputs=[
        ('pairwise', Visualization),
        ('raincloud', Visualization),
        ('violin', Visualization),
    ],
    input_descriptions={
        'table': 'List of all feature tables to be compared',
        'alpha_diversty': 'List of alpha diversity vectors to be compared'
    },
    paremeter_descriptions={
        'metadata': 'Sample metadata to use in the visualizations.',
        'metadata_col': 'Sample metadata column to use to color plots in visualization.'
    },
    output_descriptions={
        'pairwise': 'Pairwise plot.',
        'raincloud': 'Raincloud plot.',
        'violin': 'Violin plot.'
    },
    name='All alpha diversity visual comparisons',
    description='Compute multiple visualizations for the comparison of '
                'resulting diversity when using different parameters.'
)



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
"""

#function5: denoise bar diagram take as input stats from qiime2 can only do dada2 for now!
plugin.visualizers.register_function(
    function=q2_comp.denoise_vis,
    inputs={
        'stats1': SampleData[DADA2Stats],
        'stats2': SampleData[DADA2Stats],
    },
    parameters={
        'plot_type': Str % Choices (['line', 'bar']),
        'label1' : Str, #add default stats1, stats2, etc.
        'label2' : Str,
        'style' : Str,
        'context' : Str
    },
    #no metadata here! UNLESS think of complex figure able to show per md categorical column
    input_descriptions={
        'stats1': 'Denoising statistics from DADA2.',
        'stats2': 'Denoising statistics from DADA2.'
    },
    parameter_descriptions={
        'plot_type': 'Type of plot visualization.',
        'label1': 'Label for stats1 in the visualization.',
        'label2': 'Label for stats2 in the visualization.',
        'style': 'Set a figure style according to personal preferences amongst: darkgrid, whitegrid, dark, white, and ticks.',
        'context': 'Set a figure context according to plot use. Contexts are: paper, notebook, talk and poster.'
    },
    name= 'Denoising statistics comparison',
    description= "Visually compare the denoising statistics from DADA2 using two different sets of parameters to assess which denoising steps are more stringent.",
)

plugin.visualizers.register_function(
    function=q2_comp.denoise_list,
    inputs={
        'input_stats': List[SampleData[DADA2Stats]],
    },
    parameters={
        'plot_type': Str % Choices (['line', 'bar']),
        'labels' : List[Str], #add default stats1, stats2, etc.
        'style' : Str,
        'context' : Str
    },
    #no metadata here! UNLESS think of complex figure able to show per md categorical column
    input_descriptions={
        'input_stats': 'List of denoising statistics from DADA2. All paths to file should be separated by a space only.',
    },
    parameter_descriptions={
        'plot_type': 'Type of plot visualization.',
        'labels': 'Label for stats1 in the visualization.',
        'style': 'Set a figure style according to personal preferences amongst: darkgrid, whitegrid, dark, white, and ticks.',
        'context': 'Set a figure context according to plot use. Contexts are: paper, notebook, talk and poster.'
    },
    name= 'Denoising statistics comparison',
    description= "Visually compare the denoising statistics from DADA2 when different sets of parameters to assess which denoising steps are more stringent to your dataset.",
)



"""
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
