from setuptools import setup, find_packages

setup(
    name='pyture-remo',
    version='0.2.3',
    description='nature-remo library for Python',
    url='https://github.com/suzutan/pyture-remo',
    author='suzuka',
    author_email='6679870+suzutan@users.noreply.github.com',
    license='MIT',
    keywords='nature-remo',
    packages=find_packages(),
    install_requires=[
        "requests>=2.28.0"
    ],
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Programming Language :: Python :: 3.11',
        'License :: OSI Approved :: MIT License',
        'Intended Audience :: Developers',
    ],
    project_urls={
        'Bug Reports': 'https://github.com/suzutan/pyture-remo/issues',
        'Source': 'https://github.com/suzutan/pyture-remo/',
    },
)
