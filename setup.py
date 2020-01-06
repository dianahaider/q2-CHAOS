from setuptools import setup, find_packages

import versioneer

setup(
    name='q2_comp',
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
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
    package_data={ 'q2_comp._alpha': [
                        'frequency_assets/index.html',
                        'diversity_assets/index.html'
                    ],
                    'q2_comp': ['citations.bib'],
                    'q2_comp._denoise': [
                        'denoise_assets/index.html'
                    ]
                    },

)
