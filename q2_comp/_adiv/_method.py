import qiime2
import biom
import
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

#def merge_df(filenames, metadata=None, var=None):
def seq_count_pairwise(output_dir: str)
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
