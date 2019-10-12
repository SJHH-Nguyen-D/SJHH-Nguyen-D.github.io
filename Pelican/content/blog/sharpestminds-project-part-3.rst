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

In the previous post, loaded our CSV data set in as a Pandas dataframe object, and performed some very high level exploratory data analysis (EDA) using the ``.info(), .isnull().sum(), .unique(), .value_counts()`` dataframe and series object methods. This helped us understand the distribution of unique values, data types, and missing values across the various different features of our dataset. We were also able to see from the encoding scheme, that there was a high chance that many of the features might overlap in telling us about the same information (e.g., who different encoding schemes for occupational identification).

In this post, we go beyond this, and use data visualization techniques to look at variables of interest to further determine which features we can engineer/select/drop/encode and impute for missing values during our preprocessing step. There are a number of issues to consider when preparing and cleaning our data and this step is crucial to to this. If you want follow along again with the complete code, you can do so `here <https://github.com/SJHH-Nguyen-D/sharpestminds_project>`_. So without further ado, let's get into it.

===================================
More Data Exploratory Data Analysis
===================================

Let's assume that we already have our data loaded in as a dataframe from the previous post. We have some intuition in the real world as to socioeconomic and demographic characteristic variables might a correlation to some of our target variable. Additional numeric features of interest include evaluated indices on work place competencies (i.e., usage of information technnology in line of employment, workplace influence, potential for workplace facilitated education, etc).

We can plot histograms of the distribution of job performance scores by the country of the respondent:

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

I've presented only a handful of plots of job performance score distributions against countries, however, this gives us a general understanding of how these scores vary between countries. To see whether these performance scores are truly statistically different between countries, we would have perform a statistical analyses, namely, the ANOVA test.

.. code-block:: python3

    from scipy.stats import statistical test
    print(test score)
        
The conclusion of the test is....


If we want to roll-up and filter by an even larger geographic aggregation, we can do so by applying the same logic to the 'ctryrgn' variable:

.. code-block:: python3

    for region in df['ctryrgn'].unique()[pd.Series(df['ctryrgn'].unique()).isnull() == False]:
        
        region_grouped_df = df[df['ctryrgn'] == region]
        
        h = sorted(region_grouped_df['job_performance'].values)

        fit = stats.norm.pdf(h, np.mean(h), np.std(h))  #this is a fitting indeed

        pl.plot(h,fit,'--')

        pl.hist(h,normed=True)  #use this to draw histogram of your data
        
        pl.title(f"Distribution of Job Performance Scores by {region}")
                
        pl.show()


The measured index scores are features which measure ones ability in the work environment and home, in a variety of domains (reading, technological competency, etc). These measures are ordinally binned into 5 buckets - each constituting 20% of the score for that measure. We have to do a little bit of preprocessing before we can start doing any vizualization, otherwise some of the methods would not work.

.. code-block:: python3

    performance_index_values = ["writhome_wle_ca", "writwork_wle_ca","planning_wle_ca", "readhome_wle_ca", "readwork_wle_ca", 
                            "readytolearn_wle_ca", "taskdisc_wle_ca", "learnatwork_wle_ca",  "icthome_wle_ca", "ictwork_wle_ca"]
    
    # temporarily fill the missing values for each index feature with the most frequent value
    for col in performance_index_values:
        index_df[col].fillna(value=index_df[col].value_counts().sort_values(ascending=False).index[0], inplace=True)

    # set the ordinality of each of the values in this order
    categories = ['All zero response', 'Lowest to 20%', 'More than 20% to 40%', 'More than 40% to 60%', 'More than 60% to 80%', 'More than 80%']
    for i in index_df.columns[index_df.columns != 'job_performance']:
        ordered_categorical_object = pd.Categorical(i, categories=categories, ordered=True)
        index_df[i] = index_df[i].astype(ordered_categorical_object)

    

Now that we have done some preparation with the data, we can examine these ordinal features and their central tendency with some data visualization in the form of boxplots:

.. code-block:: python3

    import seaborn as sns
    %matplotlib inline
    import matplotlib.pyplot as plt

    fig, ax = plt.subplots()
    for feature in performance_index_values:
        fig = plt.figure()
        plt.title("Job Performance by {}".format(feature))
        sns.boxplot(x=feature, y="job_performance", data=index_df, linewidth=2.5, order=categories)
    

.. image:: /assets/data_visualizations/boxplot_icthome.png
    :width: 402px
    :height: 264px
    :alt: box plot job performance by icthome
    :align: center

.. image:: /assets/data_visualizations/boxplot_ictwork.png
    :width: 402px
    :height: 264px
    :alt: box plot job performance by ictwork
    :align: center

.. image:: /assets/data_visualizations/boxplot_icthome.png
    :width: 402px
    :height: 264px
    :alt: box plot job performance by icthome
    :align: center

.. image:: /assets/data_visualizations/boxplot_icthome.png
    :width: 402px
    :height: 264px
    :alt: box plot job performance by icthome
    :align: center

.. image:: /assets/data_visualizations/boxplot_learnatwork.png
    :width: 402px
    :height: 264px
    :alt: box plot job performance by learnatwork
    :align: center

.. image:: /assets/data_visualizations/boxplot_planning.png
    :width: 402px
    :height: 264px
    :alt: box plot job performance by planning
    :align: center

.. image:: /assets/data_visualizations/boxplot_readtolearn.png
    :width: 402px
    :height: 264px
    :alt: box plot job performance by readtolearn
    :align: center

.. image:: /assets/data_visualizations/boxplot_readhome.png
    :width: 402px
    :height: 264px
    :alt: box plot job performance by readhome
    :align: center

.. image:: /assets/data_visualizations/boxplot_taskdisc.png
    :width: 402px
    :height: 264px
    :alt: box plot job performance by taskdisc
    :align: center

.. image:: /assets/data_visualizations/boxplot_writhome.png
    :width: 402px
    :height: 264px
    :alt: box plot job performance by writhome
    :align: center

.. image:: /assets/data_visualizations/boxplot_writwork.png
    :width: 402px
    :height: 264px
    :alt: box plot job performance by writwork
    :align: center


What we can gleen from this is ...


Conclusion
----------

To sum it up, ... In the next post on  `data dropping <{filename}./sharpestminds-project-part-4.rst>`_, we will begin the preprocessing step of our data science pipeline

.. todo:
    statistical tests
    conclusory paragraph about what the next step of the project isEver wondered what your employee performance score would be? Part-3
    Ordinal/Categorical data/discrete:
        - Frequencies, percentages, proportions
        - central tendency: mean, median, mode, interquartile range (which discribes variability between points)
        - visualize: barchart, pie chart (not that in bar charts, the bars are disjoint to indicate that they are discrete quanitities of counts)
        - the relatiionship between two categorical variables could be reduced to a single statitic such as a Phi coefficient or Cramer's V and tested for statistical significance using the chi squared test....but for the purpose of EDA, a contingency table is fine (counts or precentages). 
    Continuous/numeric data:
        - create an array of all the index variables; examine the missing values, impute or drop with them; correlation plots for each and job performance score. 
        - percentiles, median, interquartile range
        - mean, median, mode, 
        - standard deviation, variance, range, IQR
        - visualization: histogram, boxplot (histogram is a good way to visualize the central tendency, variablity and shape of a disiribution)
        - skew, kurtosis
        - note, a histogram is not good way to identify outliers...a box plot is a good way. 
        - choose the plot that tells the best story. If you have a bimodal distribution, use a histogram (which is good for telling how many modes you have)
        - make both plots but only choose one for your report
    We ask our selves, how do values of one variable change as another variable changes
    Common questions:
        - How do you know when to use the median instead of the mean?
        - Should I use IQR instead of standard deviation?
        - When should I use a boxplot instead of a bar chart?
        - the answers to these depends on what you can learn from your data using graphs
    Outliers:
        - values smaller than lower inner fence of a boxpot (i.e., Q1 - 1.5IQR)
        - values larger than upper inner fence of boxplot (i.e., Q3 - 1.5IQR)
    Extreme values:
        - values smaller than lower outer fence, of a boxpot (i.e., Q1 - 3.0IQR) 
        - values larger than upper outer fence of boxplot (i.e., Q3 - 3.0IQR)
    Apply to continuous data
        - if the values are indeed real outliers and extreme values, you can use median and IQR instead of mean and standard deviation because it is more robust to these types of values than range. 
        - median and IQR are a more robust way to describe central tendency in the presence of outliers and extreme values. 
        - you can use a scattter plot also to see outliers between two numeric variables quite easily. Bivariate outliers can have adverse impact on the Pearson correlation coefficient. If you notice a bivariate outlier, you might want to use a spearman ranked order correlation instead of a pearson correlation. 