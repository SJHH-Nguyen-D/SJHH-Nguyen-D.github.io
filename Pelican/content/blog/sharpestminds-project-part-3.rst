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

In this post, we go beyond this, and use data visualization techniques to look at variables of interest to further determine which features we can engineer/select/drop/encode and impute for missing values during our preprocessing step. Data visualization allows use to use space, color, direction to achieve a higher level understanding of many points of data simultaneously, allowing us to visually grok patterns among the fine details of each data point. There are a number of issues to consider when preparing and cleaning our data and this step is crucial to to this. This post assumes that you have loaded the dataset from the previous posts and have imported all the dependencies. If you want follow along again with the complete code (preferrably run in a Jupyter IPython Notebook), you can do `so <https://github.com/SJHH-Nguyen-D/sharpestminds_project>`_. So without further ado, let's get into it.

===================================
More Data Exploratory Data Analysis
===================================

High Level Profiling
--------------------

Before we delve into specific statistical tests, one neat Pandas trick I recently learned allows one to quickly profile a dataframe without delving into it too much specifically. This method is available through the ``pandas_profiling`` library and must be pip installed with ``pip install pandas-profiling && pip install --upgrade pandas-profiling``. With just a few lines of code, you can quickly spin up an HTML that does high level, powerful, stylish profiling of your dataset before anything is done!

.. code-block:: python3

    import pandas_profiling

    pandas_profiling.ProfileReport(df)

A link to the generate report can generated report can be viewed at the generated HTML link.

The output is quite extensive and very detailed, given the depth and breadth of our dataset so I will not include the details within the body of this post, but more information on the module is located at its `PYPI page <https://pypi.org/project/pandas-profiling/>`_. And that's it! With just two powerful lines of code, we can get very insightful hints about our dataset!


Quick and Dirty - Numeric Variables
-----------------------------------


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
    :alt:  gender vs age boxplot
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

Quick and Dirty - Categorical Variables
---------------------------------------

We've had a look at some relationships between numeric features through visualizations and hypothesis testing using statistical methods. We can do the same for some of our categorical features of interest, albeit with statistically appropriate tests.

We can ask the question, "Is there an association between education level and employment sector type?". We can first visualize the plots of these two variables and then use the chi-square test of independence to determine whether or not the association is statistically significant.

.. code-block:: python3

    import matplotlib.pyplot as plt
    import seaborn as sns
    %matplotlib inline

    # quickly impute the most frequent values for the few missing values in the occupation sector feature
    df.edlevel3.fillna(value=df.edlevel3.value_counts().nlargest(1).index[0], inplace=True)
    df.v140.fillna(df.v140.value_counts().nlargest(1).index[0], inplace=True)

    sns.countplot(x = 'edlevel3', data = df, palette = 'magma', order=["Low", "Medium", "High"])
    plt.title('Count plot of Education Level')
    plt.show()

    
    sns.countplot(x = 'v140', data = df, palette = "Blues")
    plt.title('Count plot of Occupational Sector')
    plt.show()


.. image:: /assets/data_visualizations/countplot_educationlevel.png
    :width: 405px
    :height: 281px
    :alt: countplot of edlevel3 feature
    :align: center

.. image:: /assets/data_visualizations/countplot_occupation_sector.png
    :width: 561px
    :height: 281px
    :alt: countplot of occupational sector
    :align: center 

Based on these two count plots, one might think it reasonable to assume that education level has some bearing on the occupational sector that an employee might work in. In the form of a statistical question, we might posit a null hypothesis stating that there is no correlation between education level and occupational sector. We can perform a chi-squared test of independence with an alpha value of 0.05 and run this code:

.. code-block:: python3

    from pingouin import chi2_independence
    import pprint
    pp = pprint.PrettyPrinter(indent=4)

    chi2_test = chi2_independence(data=df, x="edlevel3", y="v140", correction=True)
    pp.pprint(chi2_test)

.. code-block:: bash

    (   v140      A non-profit organisation (for example a charity, professional association or religious organisation)  ...  The public sector (for example the local government or a state school)
    edlevel3                                                                                                         ...                                                                        
    High                                             272.544510                                                      ...                                        1815.627401                     
    Low                                               13.527682                                                      ...                                          90.118236                     
    Medium                                           121.927807                                                      ...                                         812.254363                     

    [3 rows x 3 columns],
        v140      A non-profit organisation (for example a charity, professional association or religious organisation)  ...  The public sector (for example the local government or a state school)
    edlevel3                                                                                                         ...                                                                        
    High                                                    278                                                      ...                                               2166                     
    Low                                                       0                                                      ...                                                 33                     
    Medium                                                  130                                                      ...                                                519                     

    [3 rows x 3 columns],
                        test  lambda     chi2  dof             p    cramer  power
    0             pearson   1.000  271.473  4.0  1.535794e-57  0.092149    1.0
    1        cressie-read   0.667  280.714  4.0  1.563492e-59  0.093705    1.0
    2      log-likelihood   0.000  307.553  4.0  2.543601e-65  0.098082    1.0
    3       freeman-tukey  -0.500      NaN  4.0           NaN       NaN    NaN
    4  mod-log-likelihood  -1.000      inf  4.0  0.000000e+00       inf    1.0
    5              neyman  -2.000      NaN  4.0           NaN       NaN    NaN)


With an alpha of 0.05, and the plot of the 

That being said, we can probably conclude that these features should be tentatively kept in the dataset until the preprocessing step, where we will decide what to do with this further.


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
    print(f"The IQR of the job performance scores is: {interquartile_range}")


Output: ``The IQR of the job performance scores is: 562.7908287543005``. 

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


Here we can see the distribution of the East Asia and Pacific regions typically have higher mean job performance scores. We can also see that there is more variability in the job performance scores of those in the Latin and Carribean region (a bimodal distribution), than the rest of the other regions, which approximately exemplify a normal distribution. 

I've presented only a handful of plots of job performance score distributions against regions, however, this gives us a general understanding of how these scores vary between regions. To see whether these performance scores are truly statistically different between regions, we would have perform a statistical analyses, either the Kruskal-Wallis H-test or ANOVA. The ANOVA test makes some assumptions and is sensitive to the effects of homoscedasticity (same variance among groups). Therefore, we test the assumptions first before we pick a statistical method to select.

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
    

We see that we do not meet the criteria for homoscedasticity, and therefore we must default to a more robust test like the Kruskal-Wallis H-test.

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

Given an alpha value of 0.05, we can reject the null-hypothesis that there is no difference between the medians of the job performance scores between the different regions of the world, and conclude that the median job performance scores among the regions are different. This means that the 'ctryrgn' region variable groups show a difference in their median job performance scores. Best to keep this feature in the dataset for now.

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


What we can gleen from this heatmap of the correlation scores is that (much of it is intuitive):
* One's index of planning and influence are highly correlated
* Use of information, communication and technology at home is also highly correlated to one's writing and reading capabilities in a domestic setting
* Intuitively, proficiency of use of information, communication and technology at home is also correlated and transferred to ICT use at work.
* Literacy in reading at home is correlated to being able to write at home and at work.


Conclusion
----------

To sum it up, we've been able to use data visualization to understand our categorical and numeric data on a higher level through visual pattern representations (histograms, bar graphs, boxplots). In addition to this, we've also been able to use hypothesis testing using data appropriate statistical tests (student t-test, ANOVA, Levene and Bartlett test, Kruskal-Wallis test) to determine whether or not that some of measurement differences we observe in our visualizations are statistically significant. Using the handy ``pandas-profiling`` module that was featured, which gave a detailed profile account of our dataset, we can further use it to help us make decisions to feature selection and preprocessing. In the next post on  `data dropping <{filename}./sharpestminds-project-part-4.rst>`_, we will begin the preprocessing step of our data science pipeline. Until then, ciao!

.. todo: 
    `here <{filename}../dataframe_profiling_report.html>`_ -> download pandas profiling html and link to generated html in browser