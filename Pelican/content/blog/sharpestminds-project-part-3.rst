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

In the previous post, we loaded our CSV data set in as a Pandas dataframe object, and performed some very high level exploratory data analysis (EDA) using the ``.info(), .isnull().sum(), .unique(), .value_counts()`` dataframe and series object methods. This helped us understand the distribution of unique values, data types, and missing values across the various different features of our dataset. We were also able to see from the encoding scheme, that there was a high chance that many of the features might overlap in telling us about the same information (e.g., who different encoding schemes for occupational identification).

In this post, we go beyond this, and use data visualization techniques to look at variables of interest to further determine which features we can engineer/select/drop/encode and impute for missing values during our preprocessing step. Data visualization allows use to use space, color, direction to achieve a higher level understanding of many points of data simultaneously, allowing us to visually grok patterns among the fine details of each data point. There are a number of issues to consider when preparing and cleaning our data and this step is crucial to to this. This post assumes that you have loaded the dataset from the previous posts and have imported all the depenencies. If you want follow along again with the complete code (preferrably run in a Jupyter IPython Notebook), you can do so `here <https://github.com/SJHH-Nguyen-D/sharpestminds_project>`_. So without further ado, let's get into it.

===================================
More Data Exploratory Data Analysis
===================================

High Level Profiling
--------------------

Before we delve into specific statistical tests, one neat Pandas trick I recently learned allows one to quickly profile a dataframe without delving into it too much specifically. This method is available throught the ``pandas_profiling`` library and must be pip installed. With just a few lines of code, you can quickly spin up an HTML that does high level, powerful, stylish profiling of your dataset before anything is done!

.. code-block:: python3

    import pandas_profiling

    pandas_profiling.ProfileReport(df)


The output is quite extensive, given the depth and breadth of our dataset so I will not include the details, but more information on the module is located at its `PYPI page <https://pypi.org/project/pandas-profiling/>`_. And that's it! With just two powerful lines of code, we can get very insightful hints about our dataset!

Quick and Dirty
---------------

When we get into some of our data, we can posit some easy to answer hypotheses based on some immediately understandable demographic characteristics. We can come right out of the gate and ask if there is a significant difference between the performance scores of male and female employees with the ``gender_r`` variable. We can do this first by visually with box plots and secondly by the student t-test of significant means.

.. code-block:: python3

    import seaborn as sns
    from scipy.stats import ttest_ind
    import matplotlib.pyplot as plt
    %matplotlib inline

    df['age_r'].fillna(df.age_r.median(), inplace=True)

    sns.boxplot(x="gender_r", y="job_performance", data=df)
    plt.show()

    student_t_test = ttest_ind(df[df.gender_r=="Male"].job_performance.values, 
        df[df.gender_r=="Female"].job_performance.values, 
        axis=0, 
        equal_var=True, 
        nan_policy='propagate')

    print(student_t_test)

.. image:: /assets/data_visualizations/boxplot_gender_job_performance.png
    :width: 708px
    :height: 495px
    :alt:  gender vs job performance boxplot
    :align: center

Output: ``Ttest_indResult(statistic=23.333439202279298, pvalue=1.922195290614619e-118)``

Although there are some noteable outliers in this boxplot, we can reject the null hypothesis that there is not a significant difference in the job performance scores between the genders in this dataset, and that the mean job performance scores for males in this population have scored higher than the mean female job performance score.

Another simple question we could be able to look at off the bat would be to examine if there is a difference in ages of the employees between males and females in this dataset.

.. code-block:: python3

    sns.boxplot(x="gender_r", y="age_r", data=df)
    plt.show()

    student_t_test = ttest_ind(df[df.gender_r=="Male"].age_r.values, 
        df[df.gender_r=="Female"].age_r.values, 
        axis=0, 
        equal_var=True, 
        nan_policy='propagate')

    print(student_t_test)


.. image:: /assets/data_visualizations/boxplot_gender_age.png
    :width: 708px
    :height: 495px
    :alt:  gender vs age
    :align: center

Output: ``Ttest_indResult(statistic=23.333439202279298, pvalue=1.922195290614619e-118)``

From this, we can also see that the mean ages of the participants in this dataset among the male and female groups also differ to a statistically significant extent (p-value=0.05). 

We can also extend this intuitive exploration and hypothesis testing and visualization to employee education. First we will visualize the distribution of the job performance scores grouped by the three marked tiers of education (i.e., low, medium, and high), and then perform a non-parametric statistical test of significance of grouped median job performance scores:

.. code-block:: python

    # impute small number of missing values with the most frequent value
    df.edlevel3.fillna(value=df.edlevel3.value_counts().nlargest(1).index[0], inplace=True)

    categories = ['Low', 'Medium', 'High']

    for i in df.columns[df.columns != 'job_performance']:
        ordered_categorical_object = pd.Categorical(i, categories=categories, ordered=True) # create categorical object
        df[i] = df[i].astype(ordered_categorical_object) # use .astype to columns to categorical feature

    sns.boxplot(x="edlevel3", y="job_performance", data=df, order=["Low", "Medium", "High"])
    plt.show()

    from scipy.stats.mstats import kruskalwallis

    kruskal_table = kruskalwallis(df[df.edlevel3 == "Low"].job_performance.values, 
                                df[df.edlevel3 == "Medium"].job_performance.values, 
                                df[df.edlevel3 == "High"].job_performance.values)
    print(kruskal_table)

.. image:: /assets/data_visualizations/boxplot_education_job_performance.png
    :width: 708px
    :height: 495px
    :alt:  education level vs job performance boxplot
    :align: center

Output: ``KruskalResult(statistic=846.3836603432501, pvalue=1.6222708699914698e-184)``

If the boxplot wasn't obvious enough, the Kruskal-Wallis H-test says it all with that p-value. We reject the null hypothesis and conclude that the median job performance scores between the different education levels are significantly different, and we might be able to go further than that and conclude that the higher an employee's education, the higher they scored on their job performance score evaluation.

That being said, we can probably conclude that these features should be tentatively kept the dataset until the preprocessing step, where we will decide what to do with this further.

Outliers and Extremes
---------------------

Outlier and extreme cases are fringe cases with measurement values that have an effect the overall central tendency of our dataset values, and thus make it more difficult to make accurate inferences about our data. Outlier and extreme values are determined in relation to the interquartile range (IQR) of values, in that they are greater or lower than the interquartile range by 1.5x or 3.0x, respectively. We can examine which data points are outside this range using the ``iqr`` method from ``scipy.stats``.

.. code-block:: python3

    from scipy.stats import iqr
    from numpy import percentile

    def get_outliers_and_extremes(df, num_attribute):
        
        IQR = iqr(df[num_attribute], axis=0, rng=(25, 75), scale='raw', nan_policy='propagate', interpolation='linear', keepdims=False)
        q1 = percentile(df[num_attribute], 0.25, axis=0, out=None, overwrite_input=False, interpolation='linear', keepdims=False)
        q3 = percentile(df[num_attribute], 0.75, axis=0, out=None, overwrite_input=False, interpolation='linear', keepdims=False)
        
        outliers = index_df[(df[num_attribute] <= (q1 - (IQR * 1.5))) | (df[num_attribute] <= (q3 + (IQR * 1.5)))]
        extremes = index_df[(df[num_attribute] <= (q1 - (IQR * 1.5))) | (df[num_attribute] <= (q3 + (IQR * 1.5)))]
        
        return outliers, extremes

    interquartile_range = iqr(df['job_performance'], axis=0, rng=(25, 75), scale='raw', nan_policy='propagate', interpolation='linear', keepdims=False)
    print(f"The interquartile range of the job performance scores is: {interquartile_range}")


Output: ``The interquartile range of the job performance scores is: 562.7908287543005``. 

With our ``get_outliers_and_extremes`` function, we can look at the data points that quantify as outliers.

.. code-block:: python3

    outliers, extremes = get_outliers_and_extremes(index_df, 'job_performance')
    print(f"{outliers.shape[0]} outlier values and {extremes.shape[0]} extreme values")


Output: ``4015 outlier values and 4015 extreme values``.

We examine the histograms built from the outlier values:

.. code-block:: python3

    h = sorted(outliers['job_performance'].values)

    fit = stats.norm.pdf(h, np.mean(h), np.std(h))

    pl.plot(h,fit,'--')

    pl.hist(h,normed=True) 

    pl.title(f"Distribution of Job Performance Scores in Outlier values")

    pl.show()

.. image:: /assets/data_visualizations/hist_dist_outliers.png
    :width: 402px
    :height: 264px
    :alt: job performance outliers
    :align: center

Note that the outlier data are right skewed and not normally distributed, with a higher density towards the higher most values.

Taking a look at ``outliers.head()`` and ``extremes.head()`` yields the same data points, meaning that, by definition, we have 4015 fringe values for the target variable 'job performance'. In some cases, we would like to further investigate this group of data points to for further insight into extreme variants in performance, but in this case, we will drop them.


.. code-block:: python3

    df.drop(outliers.index, inplace=True, axis=0)
    print(f"New dataframe shape: {df.shape}")


Output: ``New dataframe shape: (15985, 11)``.


Plotting
--------
Let's assume that we already have our data loaded in as a dataframe from the previous post. We have some intuition in the real world as to socioeconomic and demographic characteristic variables might correlate to some of our target variable. Additional numeric features of interest include evaluated indices on work place competencies (i.e., usage of information technnology in line of employment, workplace influence, potential for workplace facilitated education, etc).

We can plot histograms of the distribution of job performance scores by the country of the respondent:

.. code-block:: python3

    import numpy as np
    import scipy.stats as stats
    import pylab as pl

    for country in df['cntryid_e'].unique()[pd.Series(df['cntryid_e'].unique()).isnull() == False]:
        
        country_grouped_df = df[df['cntryid_e'] == country]
        
        h = sorted(country_grouped_df['job_performance'].values)

        fit = stats.norm.pdf(h, np.mean(h), np.std(h))

        pl.plot(h,fit,'--')

        pl.hist(h,normed=True)
        
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

If we want to roll-up and filter by an even larger geographic aggregation, we can do so by applying the same logic to the 'ctryrgn' variable, which has a total of 4  categories (NA and Central Europe; Central and Eastern Europe; East Asian and Pacific; and Latin America and the Carribean):

.. code-block:: python3

    # There are 144 nan values for the region feature...a relatively small number.
    print(df['ctryrgn'].isnull().sum())

    # impute small number of nan values with the most frequent category so that we can work with it temporarily
    df['ctryrgn'].fillna(value=df['ctryrgn'].value_counts().sort_values(ascending=False).index[0], inplace=True)

    for region in df['ctryrgn'].unique()[pd.Series(df['ctryrgn'].unique()).isnull() == False]:
        
    import numpy as np
    import scipy.stats as stats
    import pylab as pl

    for region in df['ctryrgn'].unique()[pd.Series(df['ctryrgn'].unique()).isnull() == False]:
        region_grouped_df = df[df['ctryrgn'] == region]
        h = sorted(region_grouped_df['job_performance'].values)
        fit = stats.norm.pdf(h, np.mean(h), np.std(h))  #this is a fitting indeed
        pl.plot(h,fit,'--')
        pl.hist(h,normed=True)  #use this to draw histogram of your data
        pl.legend(df['ctryrgn'].unique())
        pl.title(f"Distribution of Job Performance Scores by Region")
        pl.show()

.. image:: /assets/data_visualizations/hist_jps_region_ALL.png
    :width: 402px
    :height: 264px
    :alt: histogram job performance by all regions
    :align: center


Here we can see an overarching trend. That is, visually, the distribution of the East Asia and Pacific regions typically have higher mean job performance scores. We can also see that there is more variability in the job performance scores of those in the Latin and Carribean regions, than the rest of the other regions, which approximately exemplify a normal distribution. 

I've presented only a handful of plots of job performance score distributions against regions, however, this gives us a general understanding of how these scores vary between regions. To see whether these performance scores are truly statistically different between regions, we would have perform a statistical analyses, eitherthe Kruskal-Wallis H-test(Non-parametric version of ANOVA), or ANOVA. The ANOVA test makes some assumptions and is sensitive to the effects of homoscedasticity (same variance among groups). Therefore, we test the assumptions first before we pick a statistical method to select.

We test homoscedasticity (pip install the pingouin statistical library in python if you haven't already):

.. code-block:: python3

    from pingouin import homoscedasticity

    levene_test = homoscedasticity(data=df, dv='job_performance', group='ctryrgn')
    bartlett_test = homoscedasticity(data=df, dv='job_performance', method='bartlett', group='ctryrgn')

    print(levene_test)
    print(bartlett_test)


::

                W          pval  equal_var
    levene  18.237  8.274316e-12      False
                T          pval  equal_var
    bartlett  53.207  1.656381e-11      False
    

We see that we do not meet the criteria for homoscedasticity, and therefore we must use a more robust test like the Kruskal-Wallis H-test.

We can take a look at the medians visually first to have an idea of centrality of job performance scores between region groups.


.. code-block:: python3

    df.groupby('ctryrgn').job_performance.median()
    df.groupby('ctryrgn').job_performance.median().plot(kind='bar')


::

    ctryrgn
    Central and Eastern Europe                      2958.906281
    East Asia and the Pacific (richer countries)    3099.385517
    Latin America and the Caribbean                 2938.909632
    North America and Western Europe                3058.351212
    Name: job_performance, dtype: float64


.. image:: /assets/data_visualizations/median_hist_by_region.png
    :width: 384px
    :height: 468px
    :alt: barplot of median job performance by region
    :align: center


Therefore, we compute the Kruskal-Wallis H-test, which tests whether the population measurements for job performance are equal between groups of regions:

.. code-block:: python3

    kruskal_table = kruskalwallis(df[df.ctryrgn == "North America and Western Europe"].job_performance.values, 
                                df[df.ctryrgn == "Central and Eastern Europe"].job_performance.values, 
                                df[df.ctryrgn == "East Asia and the Pacific (richer countries)"].job_performance.values,
                                df[df.ctryrgn == "Latin America and the Caribbean"].job_performance.values)
    print(kruskal_table)

Output: ``KruskalResult(statistic=249.06502880278276, pvalue=1.0424276756331046e-53)``

Given a p-value=0.05, we can reject the null-hypothesis that there is no difference between the medians of the job performance scores between the different regions of the world, and conclude that the median job performance scores among the regions are different. This means that the 'ctryrgn' region variable groups show a difference in their median job performance scores. Best to keep this feature in the dataset for now.

Correlation Matrix
------------------

Another set of interesting features are the measured competency indices. The measured index scores are features which measure ones ability in the work environment and home, in a variety of domains (reading, technological competency, etc). These measures are ordinally binned into 5 buckets - each constituting 20% of the score for that measure. We have to do a little bit of preprocessing before we can start doing any vizualization, otherwise some of the methods would not work.


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


The same features are also available in the data set as numeric features, with some missing values.

.. code-block:: python3

    import seaborn as sns
    %matplotlib inline
    import matplotlib.pyplot as plt

    indices_of_performance = ["readytolearn", "icthome", "ictwork", "influence", "planning", "readhome", "readwork", "taskdisc", "writhome", "writwork"]

    for i in indices_of_performance:
        df[i].fillna(df[i].median(), inplace=True)
        
    frame = df[indices_of_performance + ["job_performance"]]
    corr = frame.corr()
    sns.heatmap(corr, annot=True)
    plt.show()
    

.. image:: /assets/data_visualizations/heatmap_performance_indices.png
    :width: 721px
    :height: 568px
    :alt: heatmap of of job performance vs all indices of performance
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
    Note that there are a small number of actual numeric features outside of the job performance metric.... you might wnat to visualize this this in terms of bar charts or a pie to indicate the proprotion of numeric data to the number of categorical discrete features...which will further infrom us what types of transformations might be necessary to analyse and work with this data.