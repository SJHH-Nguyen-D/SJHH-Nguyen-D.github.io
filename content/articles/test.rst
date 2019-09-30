Testing Testing 1, 2, 3
#######################

:date: 20180928 10:30
:tags: tutorial
:category: testing
:slug: testing
:author: Dennis Nguyen-Do
:summary: Does this even work

This is about post about testing testing whether this thing even works

https://www.flickr.com/photos/dvpho_tos/35222820026/
https://live.staticflickr.com/4271/35222820026_46cc483a34_c_d.jpg

.. image:: https://live.staticflickr.com/4278/34875474670_a97e36c750_c_d.jpg
    :height: 427px
    :width: 640px
    :alt: old lanterns
    :align: center
    :name: my picture

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

Python Visualization Code::

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


`
import matplotlib.pyplot as plt 
import seaborn as sns 
import pandas as pd 
from sklearn.datasets import *

iris = load_iris()
df = pd.DataFrame(iris.data, columns=iris.feature_names)
df.target = iris.target
`