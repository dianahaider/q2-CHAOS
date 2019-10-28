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

    # run comp_pairwise
    t1=table.transpose(table1.to_dataframe())
    t2=table.transpose(table2.to_dataframe())
    smpl = pd.merge(t1, t2, on = 'sample-id')





def comp_raincloud(outputdir: str,
                table1: biom.Table,
                table2: biom.Table,
                sample_metadata: qiime2.CategoricalMetadataColumn) -> None:

#add a print some text if no parameters are supplied & have errors if smtg goes wrong so u know how to fix it as user

#add an --help & --citations
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

    # run comp_pairwise
    t1=table.transpose(table1.to_dataframe())
    t2=table.transpose(table2.to_dataframe())
    smpl = pd.merge(t1, t2, on = 'sample-id')





def comp_raincloud(outputdir: str,
                table1: biom.Table,
                table2: biom.Table,
                sample_metadata: qiime2.CategoricalMetadataColumn) -> None:

#add a print some text if no parameters are supplied & have errors if smtg goes wrong so u know how to fix it as user

#add an --help & --citations

#add version (github controlled or versioneer......)

#add smtg to print when --verbose & use sys.stderr for msgs&errors : NOT stdout

#don't hardcode PATHS

#check that all dependencies are installed

#index.html has to be written to output_dir by the function
#return type is none
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

    # run comp_pairwise
    t1=table.transpose(table1.to_dataframe())
    t2=table.transpose(table2.to_dataframe())
    smpl = pd.merge(t1, t2, on = 'sample-id')





def comp_raincloud(outputdir: str,
                table1: biom.Table,
                table2: biom.Table,
                sample_metadata: qiime2.CategoricalMetadataColumn) -> None:

#add a print some text if no parameters are supplied & have errors if smtg goes wrong so u know how to fix it as user

#add an --help & --citations

#add version (github controlled or versioneer......)

#add smtg to print when --verbose & use sys.stderr for msgs&errors : NOT stdout

#don't hardcode PATHS

#check that all dependencies are installed

#index.html has to be written to output_dir by the function
#return type is none

#add version (github controlled or versioneer......)
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

    # run comp_pairwise
    t1=table.transpose(table1.to_dataframe())
    t2=table.transpose(table2.to_dataframe())
    smpl = pd.merge(t1, t2, on = 'sample-id')





def comp_raincloud(outputdir: str,
                table1: biom.Table,
                table2: biom.Table,
                sample_metadata: qiime2.CategoricalMetadataColumn) -> None:

#add a print some text if no parameters are supplied & have errors if smtg goes wrong so u know how to fix it as user

#add an --help & --citations

#add version (github controlled or versioneer......)

#add smtg to print when --verbose & use sys.stderr for msgs&errors : NOT stdout

#don't hardcode PATHS

#check that all dependencies are installed

#index.html has to be written to output_dir by the function
#return type is none

#add smtg to print when --verbose & use sys.stderr for msgs&errors : NOT stdout

#don't hardcode PATHSimport os

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

    # run comp_pairwise
    t1=table.transpose(table1.to_dataframe())
    t2=table.transpose(table2.to_dataframe())
    smpl = pd.merge(t1, t2, on = 'sample-id')





def comp_raincloud(outputdir: str,
                table1: biom.Table,
                table2: biom.Table,
                sample_metadata: qiime2.CategoricalMetadataColumn) -> None:

#add a print some text if no parameters are supplied & have errors if smtg goes wrong so u know how to fix it as user

#add an --help & --citations

#add version (github controlled or versioneer......)

#add smtg to print when --verbose & use sys.stderr for msgs&errors : NOT stdout

#don't hardcode PATHS

#check that all dependencies are installed

#index.html has to be written to output_dir by the function
#return type is none


#check that all dependencies are installeimport os

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

    # run comp_pairwise
    t1=table.transpose(table1.to_dataframe())
    t2=table.transpose(table2.to_dataframe())
    smpl = pd.merge(t1, t2, on = 'sample-id')





def comp_raincloud(outputdir: str,
                table1: biom.Table,
                table2: biom.Table,
                sample_metadata: qiime2.CategoricalMetadataColumn) -> None:

#add a print some text if no parameters are supplied & have errors if smtg goes wrong so u know how to fix it as user

#add an --help & --citations

#add version (github controlled or versioneer......)

#add smtg to print when --verbose & use sys.stderr for msgs&errors : NOT stdout

#don't hardcode PATHS

#check that all dependencies are installed

#index.html has to be written to output_dir by the function
#return type is none


#index.html has to be written to output_dir by the function
#return type is none
