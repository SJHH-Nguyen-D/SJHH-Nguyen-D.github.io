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

In the previous post, we completed the necessary preprocessing methods that were required of dealing a variety of categorical data types (nominal, binary, and ordinal) and developed an encompassing transformation at the end to encode the mappings for our data points that remained after the initial preprocessing steps. During the previous post, we separated the numeric data from our categorical data to first work with the categorical features. This is the sixth post of my SharpestMinds project series talk about missing data values and how to come up with a smarter way to go about dealing with them. If you want to follow along with the full codebase in the Jupyter IPython Notebook, you can do so at the `link to the repo <https://github.com/SJHH-Nguyen-D/sharpestminds-project>`_). This is going to be a brief but insightful one, so let's get into it. 

============================
Imputation of Missing Values
============================

If you've been following allow since the last post, you will know that a large part of our numeric feature values still contain NaN values. Typically in blogs and tutorials which detail handling missings values, use a measure of centrality such as mean, median or mode to fill in for missing numeric values. We'd like to take this one step further in our problem and use a powerful API called ``missingpy`` to used 'informed imputation', which you can read the documentation for `here <https://pypi.org/project/missingpy/>`_).


First let's get our data in order:


.. code-block:: python3

    df = pd.concat([numeric_df, categorical_df], axis=1)

Before you can use the ``missingpy`` imputation package, you have to install it with: ``pip install missingpy`` in terminal. 

::

    $ pip install missingpy


.. image:: /assets/connect_the_dots.jpg
    :width: 600px
    :height: 380px
    :alt: connect the dots
    :align: center

*Imputing data: You might as well draw something up that makes sense.*


Now we can simply call the ``.fit_transform()`` method, just like any ol' machine learning model in the ``scikit-learn`` library to generate the imputed missing data points. There are different approaches available in the ``missingpy`` library for which we can use to to impute values. For our pipeline, I chose to use the K-Nearest Neighbors (KNN) imputer object to predict what the missing values for both the numeric and categorical values are. There is some caution to be had about using this type of imputation method for categorical variables, as they will be using numeric encoding schemes to represent the real-world string values - i.e., those values that are predicted my contain point-values for discrete valued categorical numeric encodings and thus have to be rounded to the nearest integer. There is a fallacy in using imputation of values as such is that discrete real world categories can somehow be adjusted to be another through numeric rounding, which isn't the case. This is something we ought of be aware of when using such a method. 

As opposed to using the arithmetic mean (sensitive to outlier values) or mode to impute for missing values,  our basis of imputation uses a notion of 'distance' or 'similarity' between samples using the nearest neighbours algorithm. With a fairly large dataset and many features to impute for, it is oft the case that running this on a single CPU will take a considerable amount of time (though definitely less than 1 day, with todays modern CPUs). We won't go through hyperparameter optimization of the imputer in this example, as this will take an obscene amount of time that I am not willing to wait for with my hardware, however this is something someone with the right resources could attempt to do. We will just be running the KNN Imputer object using 5 nearest neighbours and uniform weighting for our sample neighbor weights.

.. code-block:: python3

    def impute_missing_for_dataframe(dataframe, target='job_performance'):
        """ The imputer function should be used on a dataframe that has already been numerically encoded """
        from missingpy import KNNImputer #, MissForest
        
        X = dataframe.loc[:, dataframe.columns != target].values
        y = dataframe[target].values

        # imputer object
        knn = KNNImputer(n_neighbors=5, 
                        weights="uniform",
                        metric="masked_euclidean",
                        row_max_missing=0.8,
                        col_max_missing=0.8, 
                        copy=True)
        
        knn_missing_imputation = knn.fit_transform(X)
        imputed_dataframe = pd.DataFrame(knn_missing_imputation, 
                                         columns = dataframe.columns[dataframe.columns != target])
        imputed_dataframe[target] = pd.Series(y)

        return imputed_dataframe

    imputed_df = impute_missing_for_dataframe(df, target="job_performance")

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
    print(df.writhome.agg(['median', 'var', 'std', 'kurt', 'skew']))
    print(df.writhome.describe())
    missing_writhome = list(numeric_df[numeric_df.writhome.isnull()].index)
    print("\nThe top 5 generated values for writhome")
    df.loc[missing_writhome, "writhome"].head()

Output:

.. code-block:: bash

    writhome attribute has: 0 missing values
    median    2.446716
    var       0.811755
    std       0.900975
    kurt      2.503343
    skew     -0.358559
    Name: writhome, dtype: float64
    count    14424.000000
    mean         2.340815
    std          0.900975
    min         -0.296028
    25%          1.766668
    50%          2.446716
    75%          2.823340
    max          6.104219
    Name: writhome, dtype: float64

    The top 5 generated values for writhome
    9      2.438870
    55     2.438870
    148    2.787867
    173    2.918247
    187    2.787867
    Name: writhome, dtype: float64

As you can see, the missing values for the writhome attribute were realistic enough with the ones at indices [9, 55] falling around the median and [148, 173, 187] falling around the 75% percentile.

Let's take examine another feature such as v8, which is an ordinal variable. Notice how point values were imputed for these supposedly discrete ordinal numeric mappings.

.. code-block:: python

    imputed_df.v8.unique()

Ouput:

.. code-block:: python3

    array([1.2, 1.4, 1. , 2. , 0. , 0.8, 0.6, 0.4, 1.6, 1.8, 0.2])

We can correct for this issue with the rounding function below:

.. code-block:: python3

    def round_selected_attributes_imputed(dataframe_to_round, dataframe_not_round):
        rounded_dataframe = dataframe_to_round.apply(lambda x: x.round())
        dataframe = pd.concat([rounded_dataframe, dataframe_not_round], axis=1)
        dataframe.drop("index", axis=1, inplace=True)
        return dataframe

    imputed_df = round_selected_attributes_imputed(imputed_df[categorical_df.columns], 
        imputed_df[list(set(imputed_df.columns)-set(categorical_df.columns))]
        )


Using the ``.head()`` method on our dataframe yields a beautifully, cleaned and imputed dataframe with no NaN values and the values are valid.

.. image:: /assets/data_visualizations/dataframe_head_after_imputation.jpg
    :width: 881px
    :height: 174px
    :alt: dataframe head after imputation with imputer
    :align: center 


Conclusion
**********

Although it was brief, the amount of work and effort that went into sorting out the kinks in my code could not be understated but that goes without saying. What can I say. It was a learning experience and the best way to learn is through failure and trial. 

In any case, in this post, we covered the preparation for imputation and the actual imputation of missing values for our dataset with the missingpy.KNNImputer doing the heavy lifting for us. In the `next post <{filename}./sharpestminds-project-part-7.rst>`_, we will cover the feature selection step, which will also be a relatively brief post. Stay tuned! Until next time!

Bonus picture of my cat!

.. image:: /assets/cocos_bizarre_adventure.jpg
    :width: 518px
    :height: 691px
    :alt: CoCo the cat
    :align: center
