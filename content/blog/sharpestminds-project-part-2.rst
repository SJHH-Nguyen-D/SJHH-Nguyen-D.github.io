Ever wondered what your employee performance score would be? Part-2
###################################################################

:date: 20191001 19:00
:tags: sharpestminds-project, data science, projects, employee performance, EDA, exploratory-data-analysis, loading, descriptive-statistics
:category: projects, EDA, exploratory-data-analysis
:slug: sharpestminds-project-part-2
:authors: Nguyen-Do, Dennis ;
:summary: The first part of diving into my SharpestMinds data science project. In this part, we get some more background informatoin on the dataset, load in the dataset and look at some preliminary exploratory data analysis using Pandas and Matplotlib.

***********************************
SharpestMinds Project Series Part-2
***********************************

If you are new to this post and would like some context, I'd highly suggest you read through parts 1 this project blogging series, as this is the second post of the series. If you want to hop to the next post on further exploratory data analysis, the link to it will be listed here as well. Again, if you want to download the entire repo for the project and follow along yourself with the code, you can do so by cloning this `repo <https://github.com/SJHH-Nguyen-D/sharpestminds_project>`_.

* `Part 1 - Introduction <{filename}./sharpestminds-project-part-1.rst>`_
* `Part 3 - More Exploratory Data Analysis <{filename}./sharpestminds-project-part-3.rst>`_

===========
The Dataset
===========

Welcome to technically the first step of our project in which we will get to know the dataset a little bit and step through the some code to load, explore and visualize the data, and with each step, give our insight on what can be gleened.

If this all seems new to you, you can have a skim through the summary of the `introduction post <{filename}./sharpestminds-project-part-1.rst>`_ of this series for some background information on the premise of this project and the dataset. Unfortunately I can't actually disclose the dataset for reasons, but I can still discuss my processes, through documenting and journalling of this project.


.. image:: https://live.staticflickr.com/4258/35262249515_dc9c6165de_c_d.jpg
    :width: 800px
    :height: 640px
    :alt: mossy japanese sculpture
    :align: center

*Mossy Japanese sculpture* by `David Vuong <https://www.flickr.com/photos/dvpho_tos/35262249515>`_


===================
Loading the dataset
===================

Our entire tabular dataset, which is relatively small dataset by big data standards, is about 400Mbs of flat, tabular, comma-separated-values data.

First we load the data in with a function:

.. code-block:: python3

  # import dependencies
  import numpy as np
  import matplotlib.pyplot as plt
  import pandas as pd

    def load_dataset(filepath):
        try:
            preprocessing_dataset = pd.read_csv(filepath, header='infer')
        except IOError:
            print("The .csv file could not be read in as a dataframe")
        return preprocessing_dataset


    df = load_dataset("/path/to/data.csv", header="infer")


**SIDE-NOTE:** If the code block isn't showing up for you with proper syntax highlighting with the ``.. code-block`` directive, simply install Sphinx. According to Sphinx's documentation on its `website <https://www.sphinx-doc.org/en/master/>`_ :

    "Sphinx is a tool that makes it easy to create intelligent and beautiful documentation, written by Georg Brandl and licensed under the BSD license.
    It was originally created for the Python documentation, and it has excellent facilities for the documentation of software projects in a range of languages. Of course, this site is also created from reStructuredText sources using Sphinx! .... Code handling: automatic highlighting using the Pygments highlighter"

    -- Sphinx Documentation


You can install it through the terminal with this line of code if you are on Mac or Linux:

:: 

    sudo apt-get update
    sudo apt-get install python3-sphinx


=========================
Exploratory Data Analysis
=========================

Let's get right into it. So first off, we'd like to see the shape of the data - how many data points we have to work with, and how many features 

.. code-block:: python3

    print(df.shape)

``(20000, 380)``



.. code-block:: python3

    print(df.info(memory_usage='deep))



.. code-block:: python3

    print(df.keys())Nguyen-Do, Dennis;



.. code-block:: python3

    print(df.describe())



.. code-block:: python3

    print(df.isnull().sum())



.. code-block:: python3

    for feature in df.columns():
        print(f"####{feature}###")
        print(f"####{df[feature].unique()}###\n")
        print(f"Number of unique values: {len(df[feature].unique()}###\n")



.. todo:
    comment on datatypes
    talk about the features that are in this dataset
    talk about how some of the features are duplicates and how we might want to deal with those later on through the dropping step
    comment on encoding for missing values; what features might have to be encoded as nan and dropped
    maybe talk about strategies on what to do next by the end of the post that will be carried onto the next post (impressions)
    maybe talk about what kind of further analysis we can do outside of just the higher level descriptive statistics. we want to be able to look at more data visualizations using matplotlib
    