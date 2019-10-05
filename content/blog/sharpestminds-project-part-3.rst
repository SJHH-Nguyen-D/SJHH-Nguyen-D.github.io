Ever wondered what your employee performance score would be? Part-3
###################################################################

:date: 20191004 23:06
:tags: sharpestminds-project, data science, projects, employee performance, EDA, exploratory-data-analysis
:category: projects, EDA, exploratory-data-analysis
:slug: sharpestminds-project-part-3
:authors: Nguyen-Do, Dennis;
:summary: Let's dig into the data even further with some EDA in Matplotlib and seaborn for the continuation this SharpestMinds project, in the third post of this series. Onward.

***********************************
SharpestMinds Project Series Part-3
***********************************

If you are new to this post and would like some context, I'd highly suggest you read through parts 1 and 2 of this project blogging series, as this is the third post of the series:

* `Part 1 - Introduction <{filename}./sharpestminds-project-part-1.rst>`_
* `Part 2 - Background, Loading, EDA <{filename}./sharpestminds-project-part-2.rst>`_

===================================
More Data Exploratory Data Analysis
===================================

One of the more interesting features available to us for exploration is the country which employees participated from - 'cntryid_e'. As a preliminary 

.. code-block:: python3

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


.. image:: /assets/data_visualizations/distribution_country_job_performance_CAN_ENG.png
    :width: 402px
    :height: 264px
    :alt: job performance by country CAN ENG
    :align: center

.. image:: /assets/data_visualizations/distribution_country_job_performance_CAN_FRA.png
    :width: 402px
    :height: 264px
    :alt: job performance by country CAN_FRA
    :align: center

.. image:: /assets/data_visualizations/distribution_country_job_performance_USA.png
    :width: 402px
    :height: 264px
    :alt: job performance by country USA
    :align: center

.. image:: /assets/data_visualizations/distribution_country_job_performance_NOR.png
    :width: 402px
    :height: 264px
    :alt: job performance by country NOR
    :align: center

.. image:: /assets/data_visualizations/distribution_country_job_performance_KOR.png
    :width: 402px
    :height: 264px
    :alt: job performance by country KOR
    :align: center

.. image:: /assets/data_visualizations/distribution_country_job_performance_GER.png
    :width: 402px
    :height: 264px
    :alt: job performance by country GER
    :align: center

.. image:: /assets/data_visualizations/distribution_country_job_performance_UK.png
    :width: 402px
    :height: 264px
    :alt: job performance by country UK
    :align: center

.. image:: /assets/data_visualizations/distribution_country_job_performance_SWE.png
    :width: 402px
    :height: 264px
    :alt: job performance by country SWE
    :align: center

.. image:: /assets/data_visualizations/distribution_country_job_performance_SING.png
    :width: 402px
    :height: 264px
    :alt: job performance by country SING
    :align: center

.. image:: /assets/data_visualizations/distribution_country_job_performance_JAP.png
    :width: 402px
    :height: 264px
    :alt: job performance by country JAP
    :align: center