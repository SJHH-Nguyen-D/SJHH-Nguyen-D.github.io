Ever wondered what your employee performance score would be? Part-4
###################################################################

:date: 20191007 16:27
:tags: sharpestminds-project, data science, projects, employee performance, dropping, preprocessing
:slug: sharpestminds-project-part-4
:authors: Nguyen-Do, Dennis;
:summary: Let's dig into the data even further with some EDA in Matplotlib and seaborn for the continuation this SharpestMinds project, in the third post of this series. Onward.

***************************************************
SharpestMinds Project Series Part-4 - Preprocessing
***************************************************

If you are new to this post and would like some context, I'd highly suggest you read through the previous posts of this project series, as this is the fourth post of this series:

* `Part 1 - Introduction <{filename}./sharpestminds-project-part-1.rst>`_
* `Part 2 - Background, Loading, EDA <{filename}./sharpestminds-project-part-2.rst>`_
* `Part 3 - More Exploratory Data Analysis <{filename}./sharpestminds-project-part-3.rst>`_

=============
Dropping Data
=============

Dropping Correlated Variables
-----------------------------

One of the more interesting features available to us for exploration is the country which employees participated from - 'cntryid_e'. As a preliminary 

.. code-block:: python3

    import pandas_profiling
    
    profile = df.profile_report()
    rejected_variables = profile.get_rejected_variables(threshold=0.9)
    print(f"There were {len(rejected_variables} highly correlated variables that were detected")

Output: ``There were 36 highly correlated variables that were detected``.

As we can see, there were quite a lot of variables that were detected by the profiling engine as being very highly correlated. As part of the initial preprocessing and feature selection step, we can choose to drop these variables based on these suggestions from the engine. We will do just this:

.. code-block:: python3

    df.drop(labels=rejected_variables, axis=1, inplace=True)


Dropping Insufficient Data
--------------------------

Dropping Data Column-Wise
*************************

Dropping Data Row-Wise
**********************

Conclusion
----------

To sum it up, what remains of the data after the initial preprocessing step of dropping some variables for feature selection and due to insufficient data is a dataframe of shape ``(df.shape)``. ... In the next post on  `data dropping <{filename}./sharpestminds-project-part-4.rst>`_, we will begin the next preprocessing step of our pipeline.

.. todo:
    things to do
    conclusory paragraph about what the next step of the project isEver wondered what your employee performance score would be? Part-3
