Ever wondered what your employee performance score would be? Part 6: Imputation of Missing Data
###############################################################################################

:date: 20191028 18:45
:tags: sharpestminds-project, data science, projects, employee performance, preprocessing, missing data, imputation, impute, missingpy
:slug: sharpestminds-project-part-6
:authors: Nguyen-Do, Dennis;
:summary: This is the sixth post of my SharpestMinds project series talk about missing data values and how to come up with a smarter way to go about dealing with them. This is going to be a brief but insightful one, so let's get into it.

***************************************************************
SharpestMinds Project Series Part 6: Imputation of Missing Data
***************************************************************

If you are new to this post and would like some context, I'd highly suggest you read through the previous posts of this project series, as this is the sixth post of this series:

* `Part 1 - Introduction <{filename}./sharpestminds-project-part-1.rst>`_
* `Part 2 - Background, Loading, EDA <{filename}./sharpestminds-project-part-2.rst>`_
* `Part 3 - More Exploratory Data Analysis <{filename}./sharpestminds-project-part-3.rst>`_
* `Part 4 - Dropping Data <{filename}./sharpestminds-project-part-4.rst>`_
* `Part 5 - Categorical Data Encoding <{filename}./sharpestminds-project-part-5.rst>`_

In the previous post, we completed the necessary preprocessing methods that were required of dealing a variety of categorical data types (nominal, binary, and ordinal) and developed an encompassing transformation at the end to encode the mappings for our data points that remained after the initial preprocessing steps. During the previous post, we separated the numeric data from our categorical data to first work with the categorical features. This is the sixth post of my SharpestMinds project series talk about missing data values and how to come up with a smarter way to go about dealing with them. If you want to follow along with the full codebase, you can do so at the `link to the repo <https://github.com/SJHH-Nguyen-D/sharpestminds-project>`_). This is going to be a brief but insightful one, so let's get into it. 

============================
Imputation of Missing Values
============================

If you've been following allow since the last post, you will know that a large part of our numeric feature values still contain NaN values. Typically in blogs and tutorials which detail handling missings values, use a measure of centrality such as mean, median or mode to fill in for missing numeric values. We'd like to take this one step further in our problem and use a powerful API called ``missingpy`` to used 'informed imputation', which you can read the documentation for `here <https://pypi.org/project/missingpy/>`_).


First let's get our data in order:


.. code-block:: python3

    df = pd.concat([numeric_df, categorical_df], axis=1)
    X = df.loc[:, df.columns != 'job_performance'].values
    y = df['job_performance'].values

Before you can use the ``missingpy`` imputation package, you have to install it with: ``pip install missingpy`` in terminal. 

::

    $ pip install missingpy


.. image:: /assets/connect_the_dots.jpg
    :width: 600px
    :height: 380px
    :alt: connect the dots
    :align: center

*Can you connect the dots to find out what the missing values are?*


Now we can simply call the ``.fit_transform()`` method, just like any ol' machine learning model in the ``scikit-learn`` library to generate the imputed missing data points. There are different approaches available in the ``missingpy`` library for which we can use to to impute values. For our pipeline, I chose to use the K-Nearest Neighbors (KNN) imputer object to predict what the missing values for both the numeric and categorical values are. There is some caution to be had about using this type of imputation method for categorical variables, as they will be using numeric encoding schemes to represent the real-world string values - i.e., those values that are predicted my contain point-values for discrete valued categorical numeric encodings and thus have to be rounded to the nearest integer. There is a fallacy in using imputation of values as such is that discrete real world categories can somehow be adjusted to be another through numeric rounding, which isn't the case. This is something we ought of be aware of when using such a method. 

As opposed to using the arithmetic mean (sensitive to outlier values) or mode to impute for missing values,  our basis of imputation uses a notion of 'distance' or 'similarity' between samples using the nearest neighbours algorithm. With a fairly large dataset and many features to impute for, it is oft the case that running this on a single CPU will take a considerable amount of time (though definitely less than 1 day, with todays modern CPUs). We won't go through hyperparameter optimization of the imputer in this example, as this will take an obscene amount of time that I am not willing to wait for with my hardware, however this is something someone with the right resources could attempt to do. We will just be running the KNN Imputer object using 5 nearest neighbours and uniform weighting for our sample neighbor weights.

.. code-block:: python3

    from missingpy import KNNImputer

    knn = KNNImputer(n_neighbors=5, weights="uniform",
                    metric="masked_euclidean", row_max_missing=0.8,
                    col_max_missing=0.8, copy=True)

    knn_missing_imputation = knn.fit_transform(X)

    # combine the series containing the newly imputed values back in with the target attribute
    imputed_df = pd.DataFrame(knn_missing_imputation, columns = df.columns[df.columns != 'job_performance'])
    imputed_df['job_performance'] = pd.Series(y)


As a check, we can examine number of remaining missing values in each of the features as such:

.. code-block:: python3

    def missing_values_checker(dataframe):
    """ prints a statement if the dataframe contains any missing values """
        contains_missing_list = []
        for col in dataframe.columns:
            if dataframe[col].isnull().sum() > 0:
                contains_missing_list.append(dataframe[col].isnull().sum())
        if sum(contains_missing_list) == 0:
            print("There were no missing values remaining after imputation")
        else:
            print("There were still NaN values remaining in the dataframe")

    missing_values_checker(imputed_df)

Output:

.. code-block:: python3

    There were no missing values remaining after imputation

We can also take a look at some of the attributes that had their missing values imputed for. We can also have a look at median and mean values for each attribute and compare them to some of the ones that were generated.

.. code-block:: python3

    print(f"writhome attribute has: {df.writhome.isnull().sum()} missing values")
    print(df.writhome.agg(['count', 'min', 'max', 'median', 'mean', 'var', 'std', 'kurt', 'skew']))
    print(imputed_df.writhome.head())

Output:

.. code-block:: bash

    writhome attribute has: 486 missing values
    count     13938.000000
    min          -0.296028
    max           6.104219
    median        2.446716
    mean          2.339455
    var           0.834437
    std           0.913475
    kurt          2.382859
    skew         -0.352368
    Name: writhome, dtype: float64



Conclusion
**********

In this post, we covered the ... Until then, ciao!
