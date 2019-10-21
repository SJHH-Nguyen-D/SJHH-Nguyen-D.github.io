Ever wondered what your employee performance score would be? Part 5: Labelling and Encoding for Categorical Data
###############################################################################################

:date: 20191021 18:00
:tags: sharpestminds-project, data science, projects, employee performance, preprocessing, labeling, encoding
:slug: sharpestminds-project-part-5
:authors: Nguyen-Do, Dennis;
:summary: This is the fifth post of the SharpestMinds project in which we cover processing of nominal categorical variables and nominal categorical variables. 

*********************************************************************************
SharpestMinds Project Series Part 5: Labelling and Encoding Categorical Variables
*********************************************************************************

If you are new to this post and would like some context, I'd highly suggest you read through the previous posts of this project series, as this is the fifth post of this series:

* `Part 1 - Introduction <{filename}./sharpestminds-project-part-1.rst>`_
* `Part 2 - Background, Loading, EDA <{filename}./sharpestminds-project-part-2.rst>`_
* `Part 3 - More Exploratory Data Analysis <{filename}./sharpestminds-project-part-3.rst>`_
* `Part 4 - Dropping Data <{filename}./sharpestminds-project-part-4.rst>`_

Up until this point in the series, we covered loading, EDA and began the some of the tasks that are required of dealing with high dimensional, messy data by dropping these insufficient data points. In this post, we cover the necessary preprocessing steps required when dealing with categorical data - both nominal and ordinal types through methods such as integer encoding and onehot-encoding. Assuming we've been following along and have all the dependencies from the previous posts loaded (even if you don't you can get follow along with the full codebase at the accompanying `repo <https://github.com/SJHH-Nguyen-D/sharpestminds-project>`_), we can dive right into discussing all of the terms and processes necessary to work with these categorical type data.

=================================
Nominal Categorical Data Encoding
=================================

Nominal categorical data is a type of categorical data in which we can either use string or numeric values to indicate discrete and mutually exclusive groupings of a variable. In order for a machine learning model to "understand" a notion of differences and distances between different types of groupings, we would need to convert these string representations of these groupings into a numeric representations. There are a few approaches that we can take with this:

* Domain Specific Encoding
* Integer Encoding
* Onehot Encoding

Often in the real world, there are already defined encoding schemes for a specific representations of a grouping. These encoding schemes are 

... (go through all the types of categorical data to be able to get to the below code)

Our plan of attack would be to separate out our numeric and categorical features and deal with each of these data at separate steps. We will ultimately combine the numeric and categorical features into our final preprocessed dataset for the modeling step.

.. code-block:: python3

    # separate out the numeric and categorical variables to see how much of each are missing
    def df_by_type_splitter(dataframe):
    """ a larger dataframe into immediately identifiable numeric and other type dataframes"""
    num_df = dataframe._get_numeric_data().copy()
    cat_df = dataframe.select_dtypes(exclude = [int, float]).copy()

    return num_df, cat_df


    numeric_df, categorical_df = df_by_type_splitter(df)

    print("Number of Numeric Features: {}".format(numeric_df.shape[1]))
    print("Number of Categorical Features: {}".format(categorical_df.shape[1]))
    

Output: 

::

    Number of Numeric Features: 31
    Number of Categorical Features: 175



.. image:: /assets/data_visualizations/countplot_occupation_sector.png
    :width: 561px
    :height: 281px
    :alt: countplot of occupational sector
    :align: center 


=================================
Ordinal Categorical Data Encoding
=================================

Ordinal categorical data is another type categorical data. Ordinal type data is like a cross between numeric data and nominal categorical data - they are often represented in terms of a string-value however, there is a magnitude or ordering to each group value.

Conclusion
----------


.. todo:
    things to do
    conclusory paragraph about what the next step of the project isEver wondered what your employee performance score would be? Part-3