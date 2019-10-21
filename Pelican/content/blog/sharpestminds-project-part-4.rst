Ever wondered what your employee performance score would be? Part 4: Preprocessing with Dropping
################################################################################################

:date: 20191007 16:27
:tags: sharpestminds-project, data science, projects, employee performance, dropping, preprocessing
:slug: sharpestminds-project-part-4
:authors: Nguyen-Do, Dennis;
:summary: In the 4th post of this series, we get into the first step of preprocessing our data which includes steps like feature selection and dropping. In the wise words of legendary hip-hop artist, Snoop Dogg, "drop it like it's [very poor quality data to work with]."

*****************************************************************
SharpestMinds Project Series Part 4: Preprocessing with Dropping
*****************************************************************

If you are new to this post and would like some context, I'd highly suggest you read through the previous posts of this project series, as this is the fourth post of this series:

* `Part 1 - Introduction <{filename}./sharpestminds-project-part-1.rst>`_
* `Part 2 - Background, Loading, EDA <{filename}./sharpestminds-project-part-2.rst>`_
* `Part 3 - More Exploratory Data Analysis <{filename}./sharpestminds-project-part-3.rst>`_

In the last post, we touched exploratory data analysis and some of the insights it provided for us in terms of which variables and data points we might want to exclude, due to their less-than-desired-influence on our predictive modeling later on in the chapter. In this post, we dip our toes into the first preprocessing step of our data science project pipeline and consider omitting features and values from our final dataset by dropping. So without further ado, let's get into it.

=================
Dropping Outliers
=================

From our previous post, I posted a method to fetch the outlier, extreme target variable values that will have an influence on our modeling step. We can observe theme with this snippet:

.. code-block:: python3

    from scipy.stats import iqr
    from numpy import percentile

    def get_outliers_and_extremes(df, num_attribute):
        
        IQR = iqr(df[num_attribute], axis=0, rng=(25, 75), scale='raw', nan_policy='propagate', interpolation='linear', keepdims=False)
        q1 = percentile(df[num_attribute], 0.25, axis=0, out=None, overwrite_input=False, interpolation='linear', keepdims=False)
        q3 = percentile(df[num_attribute], 0.75, axis=0, out=None, overwrite_input=False, interpolation='linear', keepdims=False)
        
        outliers = df[(df[num_attribute] <= (q1 - (IQR * 1.5))) | (df[num_attribute] <= (q3 + (IQR * 1.5)))]
        extremes = df[(df[num_attribute] <= (q1 - (IQR * 1.5))) | (df[num_attribute] <= (q3 + (IQR * 1.5)))]
        
        return outliers, extremes


    outliers, extremes = get_outliers_and_extremes(df, 'job_performance')
    
If you examine the shape of the extremes and outliers, you will notice that they are in fact the same for this dataset. In any case, we will drop them from the dataset with this:

.. code-block:: python3

    df.drop(index=outliers.index, inplace=True, axis=0)

=============================
Dropping Correlated Variables
=============================

If you have been following along with the `previous post <{filename}./sharpestminds-project-part-3.rst>`_ on data visualization, you got to see the wonderful and powerful abilities that the ``pandas-profiling`` module (a Python module that was built to extend the capabilities of the Pandas library) brought to the table in terms of preliminary data analysis and data visualization. The dataset profiling library was able to generate an HTML document which detailed, extensively (and I mean, quite extensively) which can be accessed through `this link <https://sjhh-nguyen-d.github.io/dataframe_profiling_report.html>`_.

Without having too do too much heavy lifting, we are able discover, courtesy of the mighty and powerful capabilities that the pandas-profiling API has to offer, the names of the features in our dataset which are highly correlated, which might dubiously influence the modeling process (in the way of introducing biases to our predictions of new employee examples.) We can identify them with this these few lines of code:
 
.. code-block:: python3

    import pandas_profiling
    
    profile = df.profile_report()
    rejected_variables = profile.get_rejected_variables(threshold=0.9)
    print(f"There were {len(rejected_variables} highly correlated variables that were detected")
    print(rejected_variables)


Output: 

::

    ['earnhrbonus',
    'earnhrbonusppp',
    'earnmthall',
    'earnmthallppp',
    'earnmthbonus',
    'earnmthbonusppp',
    'earnmthppp',
    'isco2l',
    'v1',
    'v100',
    'v110',
    'v145',
    'v156',
    'v160',
    'v163',
    'v169',
    'v231',
    'v235',
    'v283',
    'v41',
    'v45',
    'v52',
    'v63',
    'v81',
    'v87',
    'v97',
    'yrsqual_t']
    There were 36 highly correlated variables that were detected

As we can see, there were quite a lot of variables that were detected by the profiling engine as being very highly correlated. As part of the initial preprocessing and feature selection step, we can choose to drop these variables based on these suggestions from the engine or keep them for other options for preprocessing but we're just going to drop them based on the suggestions. We will do just this:

.. code-block:: python3

    df.drop(labels=rejected_variables, axis=1, inplace=True)
    print(df.shape)

Output: ``(20000, 353)``

=============================
Dropping Correlated Variables
=============================

We now see that we've reduced the number of features that are in our dataframe to 353. But that's still a large number of features in our data set. How would we know if the quality of the data in the remaining data points is of a lesser quality (i.e., lacking)? And if so, how much of it can we omit from our dataset based on poor quality?

Dropping Data Column-Wise
*************************

One way we can approach this is to set a column-wise threshold fraction by which a column must meet in terms of completeness, in order to be considered elligible for retainment. Python uses ``nan`` to indicate that a value is missing from the dataset, which is equivalent to numpy's ``numpy.nan`` value. However, in the real world, sometimes the value that is used to indicate a missing value is something other than a blank space such as "unavailable", "NA", "9999", or anything else. It is therefore important to reencode these in or dataset so that we can get a better estimate as to the true proportion of the data that is unavailable to us. 

.. code-block:: python3

    considered_missing_values = [
    '999', 9995, '9995', 9996, 
    '9996' ,9997, "9997", 9998,
    '9998', 9999, '9999', '99999']

    df = df.replace(to_replace=considered_missing_values, value=np.nan)


After the missing values have been encoded, we can use the following code to print out a series containing the features along with the proprotion of missing values, by feature:

.. code-block:: python3

    print(f"{((df.isnull().sum().sort_values(ascending=False)[df.isnull().sum() > 1000]/df.shape[0]) * 100)[:10]}")

Output: 

::

    v262    100.000
    v44      99.985
    v76      99.965
    v144     99.960
    v199     99.955
    v159     99.925
    v10      99.905
    v172     99.885
    v110     99.780
    v160     99.775
    dtype: float64%

As we can see from just from this pandas series of sorted missing value proportions - there are quite a large number of columns with missing values. What we can do is set a threshold of 60%, and any column that meets the threshold of having greater or equal to 60% of its values missing will be added to the list of features to be dropped.

..code-block:: python3

    col_drop_threshold = 0.6
    more_than_60_missing = [feature for feature in df.columns if (df[feature].isnull().sum() / df.shape[0]) >= col_drop_threshold]
    pp.pprint(sorted(more_than_60_missing)[:10])
    print(f"There are {len(more_than_60_missing)} features that have more than or equal to 60% of it's data missing.")

Output:

::

    [   'earnmthselfppp',
        'imyrs',
        'imyrs_c',
        'leaver1624',
        'v10',
        'v100',
        'v107',
        'v109',
        'v11',
        'v110']
    There are 114 features that have more than or equal to 60% of it's data missing.

That is a considerable number of variables that have been dropped due to insufficient data. Dropping these variables would equate to dropping about a quarter of the number of features we originally started with, and do this we will.


.. code-block:: python3

    df.drop(more_than_60_missing, inplace=True, axis=1)
    print(df.shape)


Output: ``(15985, 239)``

This leaves us left with a little less than 2/3's of our original number of columns. Data points with an extensive proportion of their values can, in rare cases,provide us information as to the underlying nature of our data and how the data itself was collected. In most cases, however, having the majority of our data missing is a bad thing, and we want to do like Marie Kondo and because they don't spark any joy in our lives anymore.

Dropping Data Row-Wise
**********************

We can drop data row-wise by the same measure we chose to drop data column-wise, that is, using a threshold approach, and we can do that with these lines of code:

.. code-block:: python3 

    # Data points with percentage of data missing and greater will be dropped from the dataset
    dropthreshold = 20

    # get the data points in the dataframe that have >= 30% of their data missing
    more_than_20_missing_rows = df.loc[(df.isnull().sum(axis=1)/df.shape[1]*100) >= dropthreshold].columns
    df = df.loc[(
        df.isnull().sum(axis=1) / df.shape[1]*100 < dropthreshold
    )]

    print(df.shape)

Output: ``(14566, 239)``


Dropping Redundant Information
******************************

At this point, we've whittled down the proportion of missing values by quite a bit. Some features we can identify algorithmically, or by some criterion, as elligible for dropping. Sometimes, this cannot be done without having the coding scheme or domain knowledge of how you retrieved your data. Luckily, if you've been provided a code book or have consulted your local, registered dataset provider, you will have even further insight as to what can or cannot be dropped for redundancy. One example of such redundancy can be seen in different versions of coding for the same information (e.g., the 2007 encoding for a value vs. the 2018 encoding scheme of a value). This case, we used our domain knowledge we received from other experts in our department, and will rule out which columns can be dropped from this dataset. In a way this step is similar to the feature selection step, but we will choose to include it in this section.

Our strategy then is to simply hand pick the feature sets that represent the same information, select the one that has the most complete information and discard the remaining one.

.. code-block:: python3 

    redundant_features = ["readytolearn_wle_ca", "icthome_wle_ca", "ictwork_wle_ca", 
                      "influence_wle_ca", "planning_wle_ca", "readhome_wle_ca", 
                      "readwork_wle_ca", "taskdisc_wle_ca", "writhome_wle_ca", 
                      "writwork_wle_ca", "ageg10lfs", "ageg10lfs_t", "edcat7", 
                      "edcat8", "isco2c", "isic2c", "earnflag", "reg_tl2", "lng_bq", 
                      "lng_ci", "edlevel3", "nfehrsnjr", "nfehrsjr", "fnfe12jr", 
                      "fnfaet12jr", "faet12jr", "faet12njr", "fe12", "monthlyincpr",
                      "earnhrdcl", "earnhrbonusdcl", "row", "uni", "cntryid_e"
                     ]
    df.drop(redundant_features, inplace=True, axis=1)
    print(df.shape)

Output: ``(14424, 206)``

The naming convention of these variables also gives hiint as to what is encoded in the values of these variables such as different encoding schemes, a more granular measurement of information, or an ordinalized organization of a numeric variable. Each of these offer different levels of signal to our model, however, for simplicity sake, we remove the versions of the features that have the largest proportions of their data missing.


Conclusion
----------

In summation, what remains of the data after the initial preprocessing step of dropping some variables for due to insufficient data, redudant and highly correlated features is a dataframe of shape ``(14424, 206)``. We covered a a few methods to identify such data as well as the dropping operation for row-wise and column-wise data from the Pandas library. In the `next post <{filename}./sharpestminds-project-part-5.rst>`_, we will begin the next preprocessing step of our pipeline, in which we prepare our data for further processing of by manipulating and encoding our data so that we can perform operations on the data later down the road. Until then...ciao!

.. todo:
    things to do
    conclusory paragraph about what the next step of the project isEver wondered what your employee performance score would be? Part-3
