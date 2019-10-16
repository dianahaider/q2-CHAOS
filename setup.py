from setuptools import setup, find_packages

setup(
    name='q2_comp',
    version='2019.7.1',
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
    zip_safe=False,
    #include non .py files such as txt html bib
    package_data={'q2_comp._adiv': [
                    'assets/index.html'],
                    'q2_comp':['citations.bib']
                    #eventually add the other ones too
                    },

)
