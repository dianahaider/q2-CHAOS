from setuptools import setup, find_packages
import versioneer

setup(
    name='q2_comp',
    version='use versioneer eventually',
    packages=find_packages(),
    author='Diana Haider',
    author_email='dianhaider@gmail.com',
    description='Compares feature tables',
    license='BSD-3-Clause',
    url='https://qiime2.org',
    entry_points={
        'qiime2.plugins':
        ['q2_comp=q2_comp.plugin_setup:plugin']
    },
    zip_safe=FALSE,
    package_data={'q2_comp': ['citations.bib']}
)
