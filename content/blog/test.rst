Testing Testing 1, 2, 3
#######################

:date: 20180928 10:30
:tags: tutorial
:category: testing
:slug: testing
:author: Dennis Nguyen-Do
:summary: Does this even work

.. todo:
  0. Get the content and writing skeleton down first
  05. Get the images that you need in the right directory
  1. Navigation
  2. Social Media Links
  3. Image Formatting in-line
  4. Output Plots for EDA
  5. Finish Entry Blog post
  6. Get cover banner to properly read
  7. Deploy it to github pages

This is about post about testing testing whether this thing even works

.. image:: https://live.staticflickr.com/4364/35630875744_5cff0b53b6_c_d.jpg
    :height: 427px
    :width: 640px
    :alt: moss on a log
    :align: center
    :name: my picture

*Moss on a Log* by `dvpho_tos <https://www.flickr.com/photos/dvpho_tos/35630875744/>`_

`` for i in range(0, 4): print('Hello World!)``


`python <www.google.com>`_ as a link

*python* in Italics

**python** bolded

This is an ordinary paragraph, introducing a block quote.

    "It is my business to know things.  That is my trade."

    -- Sherlock Holmes

what
  Definition lists associate a term with a definition.

*how*
  The term is a one-line phrase, and the definition is one or more
  paragraphs or body elements, indented relative to the term.
  Blank lines are not allowed between term and definition.

**when**
  The term is a one-line phrase, and the definition is one or more
  paragraphs or body elements, indented relative to the term.
  Blank lines are not allowed between term and definition.

.. code-block:: python

  import numpy as np
  import scipy.stats as stats
  import pylab as pl

  for country in df['cntryid_e'].unique()[pd.Series(df['cntryid_e'].unique()).isnull() == False]:
      
      country_grouped_df = df[df['cntryid_e'] == country]
      
      h = sorted(country_grouped_df['job_performance'].values)

      fit = stats.norm.pdf(h, np.mean(h), np.std(h))  #this is a fitting indeed

      pl.plot(h,fit,'--')

      pl.hist(h,normed=True)  #use this to draw histogram of your data
      
      pl.title(f"Distribution of Job Performance Scores by {country}")
                
      pl.show()     

The regular expression ``[+-]?(\d+(\.\d*)?|\.\d+)`` matches
floating-point numbers (without exponents).

:code:`a = b + c`

.. role: python(code)
  :language: python


  import matplotlib.pyplot as plt 
  import seaborn as sns 
  import pandas as pd 
  from sklearn.datasets import *

  iris = load_iris()
  df = pd.DataFrame(iris.data, columns=iris.feature_names)
  df.target = iris.target

How to publish a User Page with GitHub Pages::

.. code-block:: python

    pelican content -o output -s pelicanconf.py
    ghp-import output
    git push git@github.com:SJHH-Nguyen-D/SJHH-Nguyen-D.github.io.git gh-pages:master

.. image:: https://live.staticflickr.com/4345/36465727015_3a918829bc_k_d.jpg
    :height: 427px
    :width: 640px
    :alt: moss on a log
    :align: center
    :name: log

