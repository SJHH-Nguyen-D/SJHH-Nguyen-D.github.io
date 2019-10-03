Ever wondered what your employee performance score would be? Part-2
###################################################################

:date: 20191001 19:00
:tags: sharpestminds-project, data science, projects, employee performance
:category: projects
:slug: sharpestminds-project-part-2
:authors: Nguyen-Do, Dennis 
:summary: The first part of diving into my SharpestMinds data

***********************************
SharpestMinds Project Series Part-2
***********************************

===========
The Dataset
===========

Welcome to technically the first step of our project in which we will get to know the dataset a little bit and step through the some code to load, explore and visualize the data, and with each step, give our insight on what can be gleened.

If this all seems new to you, please have skim through the summary of the `introduction post <https://SJHH-Nguyen-D.github.io/2019/09/firstpost.html>`_ of this series for some background information on the premise of this project and the dataset.


.. image:: https://live.staticflickr.com/4258/35262249515_dc9c6165de_c_d.jpg
    :width: 800px
    :height: 640px
    :alt: mossy japanese sculpture
    :align: center

*Mossy Japanese sculpture* by `David Vuong <https://www.flickr.com/photos/dvpho_tos/35262249515>`_

``Onward``

===================
Loading the dataset
===================

Our entire dataset, which is relatively small dataset by big data standards, is about 93Mbs, consisting of 20,000 data points and 380 features, one of which is the target we are trying to predict - an abitrary job performance score.

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


.. image:: /assets/data_visualizations/distribtuion_country_job_performance.png
    :width: 402px
    :height: 264px
    :alt: job performance by country
    :align: center

