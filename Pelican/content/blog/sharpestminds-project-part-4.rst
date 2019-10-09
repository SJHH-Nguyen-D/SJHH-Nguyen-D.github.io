Ever wondered what your employee performance score would be? Part-4
###################################################################

:date: 20191007 16:27
:tags: sharpestminds-project, data science, projects, employee performance, dropping, preprocessing
:slug: sharpestminds-project-part-4
:authors: Nguyen-Do, Dennis;
:summary: Let's dig into the data even further with some EDA in Matplotlib and seaborn for the continuation this SharpestMinds project, in the third post of this series. Onward.

***************************************************
SharpestMinds Project Series Part-4 - Preprocessing
***************************************************

If you are new to this post and would like some context, I'd highly suggest you read through the previous posts of this project series, as this is the fourth post of this series:

* `Part 1 - Introduction <{filename}./sharpestminds-project-part-1.rst>`_
* `Part 2 - Background, Loading, EDA <{filename}./sharpestminds-project-part-2.rst>`_
* `Part 3 - More Exploratory Data Analysis <{filename}./sharpestminds-project-part-3.rst>`_

==========================
Dropping Insufficient Data
==========================

One of the more interesting features available to us for exploration is the country which employees participated from - 'cntryid_e'. As a preliminary 

.. code-block:: python3

    import numpy as np
    import scipy.stats as stats
    import pylab as pl


.. image:: /assets/data_visualizations/distribution_country_job_performance_CAN_ENG.png
    :width: 402px
    :height: 264px
    :alt: job performance by country CAN ENG
    :align: center


Conclusion
----------

To sum it up, ... In the next post on  `data dropping <{filename}./sharpestminds-project-part-4.rst>`_, we will begin the preprocessing step of our data science pipeline

.. todo:
    things to do
    conclusory paragraph about what the next step of the project isEver wondered what your employee performance score would be? Part-3
