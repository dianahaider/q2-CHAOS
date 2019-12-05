# q2-comp

QIIME2 plugin for comparison of results <br>
For descriptions on how to install and run this plugin, see  <a href="https://github.com/dianahaider/q2-comp/wiki">here</a>.

## CHAOS! Clustering Helper: ASVs and OTUs Scrutinized

<p>Clustering, or denoising of high-throughput sequencing can get confusing because of the diversity of parameters, and methods! &#128549; &#129327; CHAOS both quantifies differences between methods and is a visual exploration tool for your post-clustering or post-denoising data.</p>
<br>
CHAOS conducts pairwise comparisons of alpha diversity or frequency tables, and comparisons of denoising statistics.
<br>
All visualizations can be tweaked by preferences for color palette, style and context.

![tutorial_V1](https://github.com/dianahaider/q2-comp/blob/master/tutorial/tutorial_v1.png)


## Alpha

Feature tables of frequency or alpha diversity indices artifacts can be compared through three visualizations and one table. The pairwise plot shows the correlation between each pair of samples between each method, and the density plot of each method is displaned in the diagonale. The raincloud plot shows both the density plot and a box plot for each method.

Cool trick: it can also produce simpler visualizations such as box plots or violin plots if that's your preference. All plots can be colored by categorical metadata colummns.

```
qiime comp alpha-frequency \
  --i-tables table1.qza table2.qza table3.qza \
  --m-metadata METADATA.txt \
  --p-metadata-col depth \
  --o-visualization visualization_frequency.qzv
```
<b>Output artifacts:</b>
<p>
  <ul>
    <li> visualization_frequency.qzv <a href="https://github.com/dianahaider/q2-comp/wiki">view</a> | <a href="https://github.com/dianahaider/q2-comp/wiki">download</a>
    </li>
  </ul>
</p>





```
qiime comp alpha-index \
  --i-alpha-diversity-index shannon1.qza shannon2.qza shannon3.qza \
  --m-metadata METADATA.txt \
  --p-metadata-col depth \
  --o-visualization visualization_index.qzv
```
<b>Output artifacts:</b>
<ul>
  <li>visualization_index.qzv <a href="https://github.com/dianahaider/q2-comp/wiki">view</a> | <a href="https://github.com/dianahaider/q2-comp/wiki">download</a>
</ul>

And just def

```
qiime comp alpha-core \
  --i-tables table1.qza table2.qza table3.qza \
  --i-alpha-diversity shannon1.qza shannon2.qza shannon3.qza \
  --m-metadata METADATA.txt \
  --p-metadata-col depth \
  --o-visualization visualization_index.qzv
  --o-visualization visualization_frequency.qzv
  --o-visualization visualization_merged.qzv

```

<b>Output artifacts:</b>
<ul>
  <li> <span style="background-color:#00FEFE">visualization_index.qzv</span> <a href="https://github.com/dianahaider/q2-comp/wiki">view</a> | <a href="https://github.com/dianahaider/q2-comp/wiki">download</a> </li>
  <li><span style="background-color:#00FEFE">visualization_frequency.qzv</span> <a href="https://github.com/dianahaider/q2-comp/wiki">view</a> | <a href="https://github.com/dianahaider/q2-comp/wiki">download</a></li>
  <li><span style="background-color:#00FEFE">visualization_merged.qzv</span> <a href="https://github.com/dianahaider/q2-comp/wiki">view</a> | <a href="https://github.com/dianahaider/q2-comp/wiki">download</a></li>
</ul>

### Denoise

This functions xyz

```
qiime comp denoise \
  --i-stats stats1.qza stats.qza stats.qza \
  --p-labels Method1 Method2 Method3
  --o-visualization visualization.qzv
```
<b>Output artifacts:</b>
<ul>
  <li> <span style="background-color:#00FEFE">visualization.qzv</span> <a href="https://github.com/dianahaider/q2-comp/wiki">view</a> | <a href="https://github.com/dianahaider/q2-comp/wiki">download</a> </li>
</ul>
