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

===========================
Binary Categorical Features
===========================

The first of our categorical feature types we will cover in this post are binary features. They are the simplest type of categorical variable as there are only 2 available values in a binary variable domain. Examples of possible values for a binary variable include "Yes" and "No", "Up" and "Down", and "Employed" and "Unemployed". Unfortunately for our machine learning predictive model at the end of this blog series, it doesn't understand the concept of distances between string-values. Fortunately with binary variables, we can map the value of the two possible string values to either an integer of ``1`` or ``0``, with the former indicating the positive case, and the latter representing the negative case.

Our plan of attack would be to separate out our numeric and categorical features and from which we will create different mapping and encoding schemes for our binar, nominal and ordinal categorical variables. We will finally combine the numeric and categorical features back into a single final preprocessed dataset at the end.

.. code-block:: python3

    # separate out the numeric and categorical variables to see how much of each are missing
    def df_by_type_splitter(dataframe):
    """split a larger dataframe into numeric and object subsets"""
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
    
    # nans are included in the .unique() method
    binary_feature_names = [feature for feature in categorical_df.columns if len(categorical_df.unique()) <= 3]

    binary_feature_value_mapping = {
        "faet12": {'Did not participate in formal AET': 0, 'Participated in formal AET': 1},
        "v46" : {'One job or business': 0, 'More than one job or business': 1},
        "v53" : {'Employee': 0, 'Self-employed': 1},
        "nfe12" : {'Did not participate in NFE': 0, 'Participated in NFE': 1},
        "nativelang" : {'Did not participate in NFE': 0, 'Participated in NFE': 1},
        "nopaidworkever": {"Has not has paid work ever": 0, "Has had paid work": 1},
        "paidwork5" : {"Has not had paid work in past 5 years": 0, "Has had paid work in past 5 years": 1},
        "paidwork12" : {"Has not had paid work during the 12 months preceding the survey": 0, "Has had paid work during the 12 months preceding the survey": 1},
        "aetpop" : {"Excluded from AET population": 0, "AET population": 1},
        "edwork" : {"In work only": 0, "In education and work": 1},
        "v122" : {'Yes, unpaid work for family business': 0, 'Yes, paid work one job or business': 1, 'Yes, paid work more than one job or business or number of jobs/businesses missing': 2}
        }

    def binary_variable_mapping(dataframe, mapping_dict):

        # yes and no mappings
        yes_no_mapping = {'Yes': 1, 'No': 0}
        for feature in dataframe.columns:
            if "Yes" in dataframe.columns.unique():
                dataframe.feature = dataframe.feature.map(yes_no_mapping)

        # loop through dictionary with binary feature column with appropriate mappings
        for feature_name, mapping in mapping_dict.items():
            # loose tri-choice ordinal categorical variables
            if feature_name in ['v13', "v51", "v229"]:
                dataframe[feature_name] = dataframe[feature_name].replace({"Rarely or never": 0, "Less than once a week": 1, "At least once a week": 2})
            else:
                dataframe[feature_name] = dataframe[feature_name].replace(mapping)
    
    # we overwrite the values of the original categorical dataframe
    binary_variable_mapping(binary_df, binary_feature_value_mapping)

Using our defined function, we provide the binary mappings for our binary categorical variables inplace (meaning that we overwrite the original string representations for the values in our binary feature set.

=================================
Nominal Categorical Data Encoding
=================================

The nominal type data is a type of categorical data in which we can either use string or numeric values to indicate discrete and mutually exclusive groupings of a variable. In order for a machine learning model to "understand" a notion of differences and distances between different types of groupings, we would need to convert these string representations of these groupings into a numeric representations. There are a few approaches that we can take with this:

* Domain Specific Encoding
* Integer Encoding
* Onehot Encoding

Often in the real world, there are already defined encoding schemes for a specific representations of a grouping. Examples of this encoding scheme are the Saffir-Simpson hurricane wind scale, SNOMED CT classification of medicine, WHMIS symbology, or character encoding schemes (e.g., UTF-8, US-ASCII, etc.). These encoding schemes represent distinct individual groupings of phenomena using human-readable string and numeric character values. One important distinction between this type of encoding type and other types of encoding types is that there is a standardized, *domain-specific encoding* that is understood by those anyone who has access to mapping.

.. image:: /assets/saffir-simpson-windscale.jpeg
    :width: 1140px
    :height: 681px
    :alt: The Saffir-Simpson hurricane wind scale
    :align: center 

*Saffir-Simpson Hurricane Wind Scale*

*Integer encoding* is a type of numeric encoding scheme by which we typically assign a numeric value for k number of groupings, and each grouping value is represented by k+0-k (or k+1-k if you are starting from 1 instead) to k groupings. This type of numeric encoding scheme is reserved for ordinal type data as there are magnitudes of difference between each different integer encoding value, however this type of encoding scheme diminishes in precision unless there are clear linear distances between sequential values.

*Onehot encoding* is another type of numeric encoding scheme by which we can use binary switches to represent each *group within a single categorical variable* for each categorical variable. Onehot encoding schemes are the choice of scheme when we choose to encode nominal categorical variables with no notion of ordering or magnitude.

The task of determining which categorical variables are either nominal or ordinal in nature is not obvious at a glance. This task becomes much more tedious and time consuming when working with a large number of categorical features with a variety of different grouping domains, in which case, we would have manually select out each of the categorical features and classify them as either nominal or ordinal. Furthermore, determining the ordering of ordinal variables may not be immediately apparent. This part will require consultation from a data dictionary or domain experts to complete. Fortunately in this case, a data dictionary with an explanation of each variable and its domain values was provided for us with this dataset. 


.. code-block:: python3

   from sklearn.preprocessing import LabelEncoder, OneHotEncoder

    nominal_multicategorical_feats = ["v3", 'ctryrgn', 'v91', 'lng_home', 'cnt_brth', 'v31', 'v96', "isic1c", "v92", "v88", "v140", "v137"]
    nominal_df = categorical_df[nominal_multicategorical_feats]
    nominal_categorical_encoding_manifest = {}

    def nominal_feature_mapping(dataframe):
        """transform mapping for nominal features"""
        from sklearn.preprocessing import LabelEncoder
        nominal_categorical_encoding_manifest = {}
        
        # temp fill of NaN values with a string
        dataframe.fillna('Null', inplace=True)
        
        for col in dataframe.columns:
            le = LabelEncoder()
            le.fit(dataframe[col].values.ravel())
            dataframe[col] = le.transform(dataframe[col].values.ravel())
            nominal_categorical_encoding_manifest[col] = list(le.classes_)
            if dataframe[col].isnull().sum() > 0:
                # fill back missing value index with actual null values
                dataframe[col].replace(to_replace=list(le.classes_).index('Null'), value=np.nan, inplace=True)
                null_index = list(le.classes_).index('Null')
            le = None
    
    nominal_feature_mapping(nominal_df)

With our custom function, we perform the one hot encoding procedure inplace to overwrite the previous string representations of the group values.

=================================
Ordinal Categorical Data Encoding
=================================

Ordinal categorical data is another type categorical data. Ordinal type data is like a cross between numeric data and nominal categorical data - they are often represented in terms of a string-value however, there is a magnitude or ordering to each group value is assigned. The distance between assigned values is often assumed to be linear, however, in reality, this is not always the case, and therefore, we must be cognizant of the method used to encode these variables and the assumptions thus made. 

For ordinal data encoding, we determine what unique group names are within the allowed domains and then specify the order of magnitude (e.g., from lowest quality to highest quality) of each value for our mapping. We can then apply integer encoding scheme, using either 0 or 1 to indicate the lowest quality value to k representing the highest quality value. We can also make use of the ``CategoricalDType`` data type from the ``Pandas`` object data type.

It is convenient to apply this type of encoding scheme when there are many ordinal categorical features that share the same domain of categorical groupings and ordering, however this task becomes more tedious and time consuming when working with a large number of categorical features (many of which could be nominal features), in which case, we would have manually select out each of the ordinal features and specify the appropriate ordinality for each of their domain values. I'm sure there is a more eloquent and more performant method of performing this mapping but this is what I've mangled together, but hey, it works specifically for this dataset.

.. code-block:: python3

    def ordinal_variable_mapping(dataframe, mapping_dict):
    from pandas.api.types import CategoricalDtype
    
    for feature in dataframe.columns:
        if feature in ["v233", "v280", "v103", "v15", "v24", "v108", "v218", "v171", "v189", \
                         "v204", "v166", "v267", "v292", "v155", "v165", "v190", "v288", \
                         "v276","v43", "v197", "v214", "v7", "v175", "v139", "v123", "v14", "v178",\
                        "v34", "v106", "v246", "v131", "v111", "v173", "v260", "v164", "v186", "v240", "v208",\
                        "v275", "v132", "v141", "v25", "v177", "v149", "v23", "v193", "v237", "v162", "v146",\
                        "v277", "v40", "v73", "v195"]:

            categories = ['Never','Less than once a month','Less than once a week but at least once a month','At least once a week but not every day','Every day']
            ordered_categorical_object = CategoricalDtype(categories=categories, ordered=True)
            dataframe[feature] = dataframe[feature].astype(ordered_categorical_object)

        elif feature in ['v244', "v65", "v263", "v158", "v57", "v170", "v198", "v278", "v25", "v191", "v114", "v27"]:
            categories = ['Not at all','Very little', 'To some extent', 'To a high extent','To a very high extent']
            ordered_categorical_object = CategoricalDtype(categories=categories, ordered=True)
            dataframe[feature] = dataframe[feature].astype(ordered_categorical_object)


        elif feature in ["v247", "v134", "v13", "v18", "v26", "v124", "v99", "v282", "v51", "v2", "v248"]:
            categories = ['Never','Rarely','Less than once a week' ,'At least once a week']
            ordered_categorical_object = CategoricalDtype(categories=categories, ordered=True)
            dataframe[feature] = dataframe[feature].astype(ordered_categorical_object)

        elif feature in ["v291", "v77"]:
            categories = ['None of the time', 'Up to a quarter of the time','Up to half of the time','More than half of the time','All of the time']
            ordered_categorical_object = CategoricalDtype(categories=categories, ordered=True)
            dataframe[feature] = dataframe[feature].astype(ordered_categorical_object)

        elif feature in ["v216", "v124"]:
            categories = ['Rarely or never','Less than once a week', 'At least once a week']
            ordered_categorical_object = CategoricalDtype(categories=categories, ordered=True)
            dataframe[feature] = dataframe[feature].astype(ordered_categorical_object)


        elif feature in ["v253", "v284"]:
            categories = ['Never', 'Rarely', 'Less than once a week but at least once a month', 'At least once a week']
            ordered_categorical_object = CategoricalDtype(categories=categories, ordered=True)
            dataframe[feature] = dataframe[feature].astype(ordered_categorical_object)

        elif feature in ["v85", "v50", "v69"]:
            categories = ['Strongly disagree', 'Disagree', 'Neither agree nor disagree', 'Agree', 'Strongly agree']
            ordered_categorical_object = CategoricalDtype(categories=categories, ordered=True)
            dataframe[feature] = dataframe[feature].astype(ordered_categorical_object)

        elif feature in ["v82", "v70"]:
            categories = ['Employee, not supervisor', 'Self-employed, not supervisor','Employee, supervising fewer than 5 people', 'Employee, supervising more than 5 people', 'Self-employed, supervisor']
            ordered_categorical_object = CategoricalDtype(categories=categories, ordered=True)
            dataframe[feature] = dataframe[feature].astype(ordered_categorical_object)

        else:
            for feature, categories in mapping_dict.items():
                ordered_categorical_object = CategoricalDtype(categories=categories, ordered=True)
                dataframe[feature] = dataframe[feature].astype(ordered_categorical_object)


    ordinal_variable_mapping(ordinal_df, ordinal_feature_mapping)

We see that all the values for the variables have not changed on the surface level, but if we look at the data types with a ``print(oridinal_df.dtypes)``, we can see that the datatypes of those variables are now cast to 'category'. 

=======================
Putting it all together
=======================

Now that we define all our functions separately for each of the categorical data types that needed encoding, we can slap it all together under one function and call it to perform the necessary transformation on our entire categorical dataframe.

.. code-block:: python3

    def transform_all(dataframe, binary_mapping, ordinal_mapping):
        """all transformations into one function"""
        # binary mappings
        binary_feature_names = [col for col in categorical_df.columns if len(categorical_df[col].unique()) <= 3]
        binary_df = dataframe[binary_feature_names]
        binary_variable_mapping(binary_df, binary_mapping)
        
        # ordinal mappings
        ordinal_feature_names = ["v233", "v280", "v103", "v15", "v24", "v108", "v218", "v171", "v189",
        "v204", "v166", "v267", "v292", "v155", "v165", "v190", "v288", "v276","v43", "v197", "v214", 
        "v7", "v175", "v139", "v123", "v14", "v178", "v34", "v106", "v246", "v131", "v111", "v173", 
        "v260", "v164", "v186", "v240", "v208", "v275", "v132", "v141", "v25", "v177", "v149", "v23", 
        "v193", "v237", "v162", "v146", "v277", "v40", "v73", "v195", 'v244', "v65", "v263", "v158", 
        "v57", "v170", "v198", "v278", "v25", "v191", "v114", "v27", "v151","v181", "v271", "v122", 
        "v247", "v134", "v13", "v18", "v26", "v124", "v99", "v282", "v51", "v2", "v248","v291", 
        "v77","v269","v216", "v124","v253", "v284", "ageg5lfs", "v289","v261", "v221", "v85","v50",
        "v69", "v82", "v70", "v200", "v62", "v236","v19", "imyrcat","v48","v47","iscoskil4","v94",
        "v8",'edcat6',]

        ordinal_df = dataframe[ordinal_feature_names]
        ordinal_variable_mapping(ordinal_df, ordinal_mapping)
        
        # nominal encoding
        nominal_feature_names = ["cntryid", 
                                "lng_home", 
                                "cnt_h", 
                                "cnt_brth", 
                                "ctryqual", 
                                "birthrgn", 
                                "ctryrgn", "isic1c", 
                                "v31", 
                                "v137", 
                                "v234", 
                                "v91",
                                "v92",
                                "v88", 
                                "v140", 
                                "v3",]
        
        nominal_df = dataframe[nominal_feature_names]
        nominal_feature_mapping(nominal_df)
        
        # combine all
        transformed_dataframe = pd.concat([binary_df, ordinal_df, nominal_df], axis=1)
        
        return transformed_dataframe

    encoded_df = transform_all(df, binary_feature_value_mapping, ordinal_feature_mapping)


Conclusion
**********

In this post, we covered the prerequisite encoding that was required for our categorical variable types (nominal, categorical, binary). This process was probably one of the more tedious parts of preprocessing our data. Thank goodness that is over with. As you might recall, we also also split our dataset into a numeric dataframe subset. In the next `post <{filename}./sharpestminds-project-part-6.rst>`_, we will cover how we deal with missing value imputation for the numeric dataframe, as well as that of the categorical dataframe and combine them. Until then, ciao!
