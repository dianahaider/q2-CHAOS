# q2-comp

QIIME2 plugin for comparison of results <br>
For descriptions on how to install and run this plugin, see  <a href="https://github.com/dianahaider/q2-comp/wiki">here</a>.

## Getting started

For all vis has the option to change palette, style and context of visualizations.

## Alpha

This function xyz

```
qiime comp alpha-frequency \
  --i-tables table1.qza table2.qza table3.qza \
  --m-metadata METADATA.txt \
  --p-metadata-col depth \
  --o-visualization visualization_frequency.qzv
```
<b>Output artifacts:</b>
<ul>
  <li> <span style="background-color:#00FEFE">visualization_frequency.qzv</span> <a href="https://github.com/dianahaider/q2-comp/wiki">view</a> | <a href="https://github.com/dianahaider/q2-comp/wiki">download</a> </li>
</ul>

Can also abc <p>&#128520;</p>

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
