from setuptools import setup, find_packages

setup(
    name='pyture-remo',
    version='0.2.2',
    description='nature-remo library for Python',
    url='https://github.com/suzutan/pyture-remo',
    author='Suzuka Asagiri',
    author_email='admin@suzutan.jp',
    license='MIT',
    keywords='nature-remo',
    packages=find_packages(),
    install_requires=[
        "requests>=2.22.0"
    ],
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Programming Language :: Python :: 3.6',
        'License :: OSI Approved :: MIT License',
        'Intended Audience :: Developers',
    ],
    project_urls={
        'Bug Reports': 'https://github.com/suzutan/pyture-remo/issues',
        'Source': 'https://github.com/suzutan/pyture-remo/',
    },
)
