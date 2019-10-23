Ever wondered what your employee performance score would be? Part 5: Labelling and Encoding for Categorical Data
################################################################################################################

:date: 20191021 18:00
:tags: sharpestminds-project, data science, projects, employee performance, preprocessing, labeling, encoding, categorical, nominal, ordinal
:slug: sharpestminds-project-part-5
:authors: Nguyen-Do, Dennis;
:summary: This is the fifth post of the SharpestMinds project in which we cover methods for the processing of nominal categorical variables and nominal categorical variables. 

*********************************************************************************
SharpestMinds Project Series Part 5: Labelling and Encoding Categorical Variables
*********************************************************************************

If you are new to this post and would like some context, I'd highly suggest you read through the previous posts of this project series, as this is the fifth post of this series:

* `Part 1 - Introduction <{filename}./sharpestminds-project-part-1.rst>`_
* `Part 2 - Background, Loading, EDA <{filename}./sharpestminds-project-part-2.rst>`_
* `Part 3 - More Exploratory Data Analysis <{filename}./sharpestminds-project-part-3.rst>`_
* `Part 4 - Dropping Data <{filename}./sharpestminds-project-part-4.rst>`_

Up until this point in the series, we covered loading, EDA and began the some of the tasks that are required of dealing with high dimensional, messy data by dropping these insufficient data points. In this post, we cover the necessary preprocessing steps required when dealing with categorical data - both nominal and ordinal types through methods such as integer encoding and onehot-encoding. Assuming we've been following along and have all the dependencies from the previous posts loaded (even if you don't you can get follow along with the full codebase at the accompanying `repo <https://github.com/SJHH-Nguyen-D/sharpestminds-project>`_), we can dive right into discussing all of the terms and processes necessary to work with these categorical type data.

The types of categorical features we will cover in post will include:
* Binary features
* Nominal features
* Ordinal features

Binary Categorical Features
===========================
Often in the real world, there are already defined encoding schemes for a specific representations of a grouping. Examples of this encoding scheme are the Saffir-Simpson hurricane wind scale, SNOMED CT classification of medicine, WHMIS symbology, or character encoding schemes (e.g., UTF-8, US-ASCII, etc.). These encoding schemes represent distinct individual groupings of phenomena using human-readable string and numeric character values. One important distinction between this type of encoding type and other types of encoding types is that there is a standardized, domain-specific representation that is understood by those anyone who has access to mapping.

.. image:: /assets/saffir-simpson-windscale.jpeg
    :width: 1140px
    :height: 641px
    :alt: saffir-simpson-hurricane-scale
    :align: center

*Saffir-Simpson Hurricane Wind Scale*


In contrast, integer encoding is a type of numeric encoding scheme by which we typically assign a numeric value for k number of groupings, and each grouping value is represented by k+0-k (or k+1-k if you are starting from 1 instead) to k groupings. This type of numeric encoding scheme is reserved for ordinal type data as there are magnitudes of difference between each different integer encoding value, however this type of encoding scheme diminishes in precision unless there are clear linear distances between sequential values.

The first of our categorical feature types we will cover in this post are binary features. They are the simplest type of categorical variable as there are only 2 available values in a binary variable domain. Examples of possible values for a binary variable include "Yes" and "No", "Up" and "Down", and "Employed" and "Unemployed". Unfortunately for our machine learning predictive model at the end of this blog series, it doesn't understand the concept of distances between string-values. Fortunately with binary variables, we can map the value of the two possible string values to either an integer of ``1`` or ``0``, with the former indicating the positive case, and the latter representing the negative case.

Our plan of attack would be to separate out our numeric and categorical features and from which we will create different mapping and encoding schemes for our binar, nominal and ordinal categorical variables. We will finally combine the numeric and categorical features back into a single final preprocessed dataset at the end.

.. code-block:: python3

    # separate out the numeric and categorical variables to see how much of each are missing
    def df_by_type_splitter(dataframe):
    """a larger dataframe into immediately identifiable numeric and other type dataframes"""
    num_df = dataframe._get_numeric_data().copy()
    cat_df = dataframe.select_dtypes(exclude = [int, float]).copy()

    return num_df, cat_df


    numeric_df, categorical_df = df_by_type_splitter(df)

    print("Number of Numeric Features: {}".format(numeric_df.shape[1]))
    print("Number of Categorical Features: {}".format(categorical_df.shape[1]))
    

Output: 

::

    Number of Numeric Features: 31
    Number of Categorical Features: 168


We can then identify and sort out the binary features with this block of code. From there we can hand-pick the features and determine the specific types of discrete numeric mappings each binary string-value is assigned. I wished it was as easy as plugging in these Pandas series into the ``scikit-learn`` API and have it do all the heavy lifting for me, in the real world, it isn't always as easy as that, unfortunately. However, there were only a handful of features that we'd have to manually assign the mapping here for.

.. code-block:: python3
    
    # note that I'm using 3 here, because the .unique() series method includes nan values as a unique value
    binary_feature_names = [ feature for feature in categorical_df.columns if len(categorical_df[feature].unique()) <=3 ]
    binary_df = categorical_df[binary_feature_names]

    binary_df = binary_df.replace(to_replace={'Yes': 1, 'No': 0})
    binary_df = binary_df.replace(to_replace={'Male': 1, 'Female': 0})
    binary_df['faet12'] = binary_df['faet12'].map({'Did not participate in formal AET': 0, 'Participated in formal AET': 1})
    binary_df['v46'] = binary_df['v46'].map({'One job or business': 0, 'More than one job or business': 1})
    binary_df['v53'] = binary_df['v53'].map({'Employee': 0, 'Self-employed': 1})
    binary_df['nfe12'] = binary_df['nfe12'].map({'Did not participate in NFE': 0, 'Participated in NFE': 1})
    binary_df['nativelang'] = binary_df['nativelang'].map({'Test language not same as native language': 0, 'Test language same as native language': 1})
    binary_df['nopaidworkever'] = binary_df['nopaidworkever'].replace({"Has not has paid work ever": 0, "Has had paid work": 1})
    binary_df['paidwork5'] = binary_df['paidwork5'].replace({"Has not had paid work in past 5 years": 0, "Has had paid work in past 5 years": 1})
    binary_df['paidwork12'] = binary_df['paidwork12'].replace({"Has not had paid work during the 12 months preceding the survey": 0, "Has had paid work during the 12 months preceding the survey": 1})
    binary_df['aetpop'] = binary_df['aetpop'].replace({"Excluded from AET population": 0, "AET population": 1})
    binary_df['edwork'] = binary_df["edwork"].replace({"In work only": 0, "In education and work": 1})
    binary_df[['v13', "v51", "v229"]] = binary_df[['v13', "v51", "v229"]].replace({"Rarely or never": 0, "Less than once a week": 1, "At least once a week": 2}
    binary_df["v122"] = binary_df["v122"].replace({'Yes, unpaid work for family business': 0, 'Yes, paid work one job or business': 1, 'Yes, paid work more than one job or business or number of jobs/businesses missing': 2})
    


=================================
Nominal Categorical Data Encoding
=================================

Nominal categorical data is a type of categorical data in which we can either use string or numeric values to indicate discrete and mutually exclusive groupings of a variable. In order for a machine learning model to "understand" a notion of differences and distances between different types of groupings, we would need to convert these string representations of these groupings into a numeric representations. There are a few approaches that we can take with this:

* Domain Specific Encoding
* Integer Encoding
* Onehot Encoding

Often in the real world, there are already defined encoding schemes for a specific representations of a grouping. Examples of this encoding scheme are the Saffir-Simpson hurricane wind scale, SNOMED CT classification of medicine, WHMIS symbology, or character encoding schemes (e.g., UTF-8, US-ASCII, etc.). These encoding schemes represent distinct individual groupings of phenomena using human-readable string and numeric character values. One important distinction between this type of encoding type and other types of encoding types is that there is a standardized, domain-specific representation that is understood by those anyone who has access to mapping.

.. image:: /assets/saffir_simpson_wind_scale.jpeg
    :width: 1140px
    :height: 681px
    :alt: The Saffir-Simpson hurricane wind scale
    :align: center 

*Saffir-Simpson Hurricane Wind Scale*

In contrast, integer encoding is a type of numeric encoding scheme by which we typically assign a numeric value for k number of groupings, and each grouping value is represented by k+0-k (or k+1-k if you are starting from 1 instead) to k groupings. This type of numeric encoding scheme is reserved for ordinal type data as there are magnitudes of difference between each different integer encoding value, however this type of encoding scheme diminishes in precision unless there are clear linear distances between sequential values.

Onehot encoding is another type of numeric encoding scheme by which we can use binary switches to represent each *group within a single categorical variable* for each categorical variable. Onehot encoding schemes are the choice of scheme when we choose to encode nominal categorical variables with no notion of ordering or magnitude.

The task of determining which categorical variables are either nominal or ordinal in nature is not obvious at a glance. This task becomes much more tedious and time consuming when working with a large number of categorical features with a variety of different grouping domains, in which case, we would have manually select out each of the categorical features and classify them as either nominal or ordinal. Furthermore, determining the ordering of ordinal variables may not be immediately apparent. This part will require consultation from a data dictionary or domain experts to complete. Fortunately in this case, a data dictionary with an explanation of each variable and its domain values was provided for us with this dataset. 


=================================
Ordinal Categorical Data Encoding
=================================

Ordinal categorical data is another type categorical data. Ordinal type data is like a cross between numeric data and nominal categorical data - they are often represented in terms of a string-value however, there is a magnitude or ordering to each group value is assigned. The distance between assigned values is often assumed to be linear, however, in reality, this is not always the case, and therefore, we must be cognizant of the method used to encode these variables and the assumptions thus made. 

For ordinal data encoding, we determine what unique group names are within the allowed domains and then specify the order of magnitude (e.g., from lowest quality to highest quality) of each value for our mapping. We can then apply integer encoding scheme, using either 0 or 1 to indicate the lowest quality value to k representing the highest quality value.

It is convenient to apply this type of encoding scheme when there are many ordinal categorical features that share the same domain of categorical groupings and ordering. However this task becomes more tedious and time consuming when working with a large number of categorical features (many of which could be nominal features), in which case, we would have manually select out each of the categorical features and 


Conclusion
**********


.. todo:
    things to do
    conclusory paragraph about what the next step of the project isEver wondered what your employee performance score would be? Part-3
