from q2_comp.plugin_setup import plugin_setup
from q2_dada2 import DADA2StatsFormat

import qiime2
import pandas as pd

def _read_dada2_denoising_stats(fh):
    df = pd.read_csv(fh, sep='\t', dtype=object)
    df.set_index(df.columns[0], drop= True, append=False, inplace=True)
    cols = df.columns
    df [cols] = df[cols].apply(pd.to_numeric, errors='ignore')
    return def

@plugin.register_transformer
def _1(ff: DADA2StatsFormat) -> pd.DataFrame:
    with ff.open() as fh:
        df = _read_dada2_denoising_stats(fh)
        dataframe = df.iloc
