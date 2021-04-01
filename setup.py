import setuptools

# get current version from keras_dgl._version
with open('keras_dgl/_version.py', 'r') as fid:
    exec(fid.read())

# use README as long description
with open('README.md', 'r') as readme:
    # ignore images
    description = ''.join([i for i in readme.readlines()
                           if not i.startswith('![')])

setuptools.setup(name='keras_dgl',
                 version=__version__,
                 author='vermaMachineLearning',
                 url='https://github.com/vermaMachineLearning/keras-deep-graph-learning',
                 description="Deep Graph Learning Layers for Keras",
                 long_description=description,
                 long_description_content_type='text/markdown',
                 packages=setuptools.find_packages(),
                 python_requires='>=3')

