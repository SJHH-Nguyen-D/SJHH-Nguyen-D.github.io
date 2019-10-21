Ever wondered what your employee performance score would be? Part 2: Loading and Preliminary Analysis
#####################################################################################################

:date: 20191001 19:00
:tags: sharpestminds-project, data science, projects, employee performance, EDA, exploratory-data-analysis, loading, descriptive-statistics
:category: projects, EDA, exploratory-data-analysis
:slug: sharpestminds-project-part-2
:authors: Nguyen-Do, Dennis ;
:summary: The first part of diving into my SharpestMinds data science project. In this part, we get some more background information on the dataset, load in the dataset and look at some preliminary exploratory data analysis using Pandas and Matplotlib.

*********************************************************************
SharpestMinds Project Series Part 2: Loading and Preliminary Analysis
*********************************************************************

If you are new to this post and would like some context, I'd highly suggest you read through parts 1 this project blogging series, as this is the second post of the series. If you want to hop to the next post on further exploratory data analysis, the link to it will be listed here as well. Again, if you want to download the entire repo for the project and follow along yourself with the code, you can do so by cloning this `repo <https://github.com/SJHH-Nguyen-D/sharpestminds_project>`_.

* `Part 1 - Introduction <{filename}./sharpestminds-project-part-1.rst>`_
* `Part 3 - More Exploratory Data Analysis <{filename}./sharpestminds-project-part-3.rst>`_

===========
The Dataset
===========

Welcome to technically the first step of our project in which we will get to know the dataset a little bit and step through the some code to load, explore and visualize the data, and with each step, give our insight on what can be gleened.

If this all seems new to you, you can have a skim through the summary of the `introduction post <{filename}./sharpestminds-project-part-1.rst>`_ of this series for some background information on the premise of this project and the dataset. Unfortunately I can't actually disclose the dataset for reasons, but I can still discuss my processes, through documenting and journalling of this project.


.. image:: https://live.staticflickr.com/4258/35262249515_dc9c6165de_c_d.jpg
    :width: 800px
    :height: 640px
    :alt: mossy japanese sculpture
    :align: center

*Mossy Japanese sculpture* by `David Vuong <https://www.flickr.com/photos/dvpho_tos/35262249515>`_


===================
Loading the dataset
===================

Our entire tabular dataset, which is relatively small dataset by big data standards, is about 400Mbs of flat, tabular, comma-separated-values data.

First we load the data in with a function:

.. code-block:: python3

  # import dependencies
  import numpy as np
  import matplotlib.pyplot as plt
  import pandas as pd

    def load_dataset(filepath):
        try:
            preprocessing_dataset = pd.read_csv(filepath, header='infer')
        except IOError:
            print("The .csv file could not be read in as a dataframe")
        return preprocessing_dataset


    df = load_dataset("/path/to/data.csv", header="infer")


**SIDE-NOTE:** If the code block isn't showing up for you with proper syntax highlighting with the ``.. code-block`` directive, simply install Sphinx. According to Sphinx's documentation on its `website <https://www.sphinx-doc.org/en/master/>`_ :

    "Sphinx is a tool that makes it easy to create intelligent and beautiful documentation, written by Georg Brandl and licensed under the BSD license.
    It was originally created for the Python documentation, and it has excellent facilities for the documentation of software projects in a range of languages. Of course, this site is also created from reStructuredText sources using Sphinx! .... Code handling: automatic highlighting using the Pygments highlighter"

    -- Sphinx Documentation


You can install it through the terminal with this line of code if you are on Mac or Linux:

:: 

    sudo apt-get update
    sudo apt-get install python3-sphinx


=========================
Exploratory Data Analysis
=========================

Let's get right into it. So first off, we'd like to see the shape of the data - how many data points we have to work with, and how many variables we have in the dataset.

.. code-block:: python3

    print(df.shape)


``(20000, 380)``

We have a total of 380 variables, including the 'job performance' target variable and a total of 20,000 data points.

.. code-block:: python3

    print(df.info(memory_usage='deep))

::

    <class 'pandas.core.frame.DataFrame'>
    RangeIndex: 20000 entries, 0 to 19999
    Columns: 380 entries, cntryid to uni
    dtypes: float64(80), int64(5), object(295)
    memory usage: 357.9 MB

From this we can see that the filesize is approximately 360MBs. We see that we only have a handful of numerical variables to work with, while the large majority of the dataset include values that have string values - indicated by the object-datatype.

The 380 variables in the data set consists of questionnaire questions collected on demographic characteristics of the respondents. The questions probe participants on socioeconomic factors, skills, literacy, language and several numeric indices of competency.

.. code-block:: python3

    print(df.keys()

.. code-block:: python3

    Index(['cntryid', 'cntryid_e', 'age_r', 'gender_r', 'computerexperience',
       'nativespeaker', 'edlevel3', 'monthlyincpr', 'yearlyincpr', 'lng_home',
       'cnt_h', 'cnt_brth', 'reg_tl2', 'lng_bq', 'lng_ci', 'yrsqual',
       'yrsqual_t', 'yrsget', 'vet', 'ctryqual', 'birthrgn', 'nativelang',
       'ctryrgn', 'imyrs', 'imyrs_c', 'imyrcat', 'ageg5lfs', 'ageg10lfs',
       'ageg10lfs_t', 'edcat8', 'edcat7', 'edcat6', 'leaver1624', 'leavedu',
       'fe12', 'aetpop', 'faet12', 'faet12jr', 'faet12njr', 'nfe12',
       'fnfaet12', 'edwork', 'neet', 'nfehrsnjr', 'nfehrsjr', 'nfehrs',
       'nopaidworkever', 'paidwork12', 'iscoskil4', 'isic1l', 'isic2l',
       'isic1c', 'isic2c', 'isco1c', 'isco2c', 'isco1l', 'isco2l', 'earnhr',
       'earnhrppp', 'earnhrbonus', 'earnhrbonusppp', 'earnmth', 'earnmthppp',
       'earnmthselfppp', 'earnmthbonus', 'earnmthall', 'earnmthallppp',
       'earnmthbonusppp', 'nfe12jr', 'nfe12njr', 'fnfe12jr', 'fnfaet12jr',
       'fnfaet12njr', 'paidwork5', 'earnhrdcl', 'earnhrbonusdcl',
       'earnmthalldcl', 'earnflag', 'learnatwork', 'learnatwork_wle_ca',
       'readytolearn', 'readytolearn_wle_ca', 'icthome', 'icthome_wle_ca',
       'ictwork', 'ictwork_wle_ca', 'influence', 'influence_wle_ca',
       'planning', 'planning_wle_ca', 'readhome', 'readhome_wle_ca',
       'readwork', 'readwork_wle_ca', 'taskdisc', 'taskdisc_wle_ca',
       'writhome', 'writhome_wle_ca', 'writwork', 'writwork_wle_ca',
       'job_performance', 'v59', 'v200', 'v266', 'v83', 'v31', 'v202', 'v151',
       'v231', 'v272', 'v32', 'v78', 'v138', 'v90', 'v157', 'v74', 'v56',
       'v107', 'v245', 'v153', 'v230', 'v243', 'v196', 'v58', 'v61', 'v38',
       'v129', 'v117', 'v256', 'v268', 'v252', 'v290', 'v16', 'v72', 'v9',
       'v4', 'v126', 'v274', 'v265', 'v102', 'v101', 'v206', 'v60', 'v207',
       'v133', 'v285', 'v136', 'v187', 'v17', 'v194', 'v154', 'v94', 'v137',
       'v222', 'v234', 'v223', 'v91', 'v269', 'v236', 'v47', 'v283', 'v145',
       'v41', 'v291', 'v227', 'v225', 'v203', 'v201', 'v36', 'v209', 'v185',
       'v238', 'v159', 'v35', 'v183', 'v5', 'v273', 'v259', 'v286', 'v95',
       'v67', 'v217', 'v174', 'v45', 'v20', 'v98', 'v11', 'v226', 'v161',
       'v213', 'v125', 'v232', 'v68', 'v264', 'v79', 'v64', 'v205', 'v46',
       'v122', 'v92', 'v88', 'v179', 'v281', 'v110', 'v211', 'v160', 'v75',
       'v52', 'v97', 'v84', 'v270', 'v33', 'v242', 'v140', 'v53', 'v82', 'v70',
       'v184', 'v19', 'v104', 'v182', 'v22', 'v168', 'v241', 'v147', 'v48',
       'v8', 'v115', 'v257', 'v37', 'v55', 'v251', 'v29', 'v3', 'v135', 'v235',
       'v1', 'v261', 'v263', 'v158', 'v244', 'v198', 'v212', 'v62', 'v221',
       'v214', 'v276', 'v246', 'v181', 'v96', 'v100', 'v63', 'v87', 'v262',
       'v12', 'v76', 'v144', 'v199', 'v44', 'v39', 'v109', 'v255', 'v210',
       'v6', 'v118', 'v169', 'v289', 'v150', 'v172', 'v287', 'v121', 'v30',
       'v113', 'v119', 'v130', 'v215', 'v254', 'v163', 'v112', 'v220', 'v10',
       'v93', 'v81', 'v156', 'v192', 'v77', 'v123', 'v141', 'v24', 'v193',
       'v275', 'v204', 'v108', 'v164', 'v166', 'v197', 'v34', 'v42', 'v292',
       'v131', 'v142', 'v188', 'v139', 'v247', 'v99', 'v180', 'v124', 'v51',
       'v190', 'v248', 'v229', 'v189', 'v165', 'v173', 'v134', 'v2', 'v25',
       'v18', 'v216', 'v178', 'v282', 'v13', 'v233', 'v278', 'v103', 'v155',
       'v152', 'v258', 'v277', 'v40', 'v146', 'v195', 'v73', 'v23', 'v106',
       'v271', 'v250', 'v176', 'v111', 'v218', 'v253', 'v132', 'v284', 'v267',
       'v260', 'v26', 'v171', 'v14', 'v7', 'v240', 'v186', 'v162', 'v149',
       'v228', 'v28', 'v237', 'v280', 'v175', 'v288', 'v15', 'v208', 'v43',
       'v27', 'v114', 'v191', 'v170', 'v65', 'v57', 'v177', 'v69', 'v85',
       'v50', 'v89', 'v127', 'v239', 'v224', 'v71', 'v105', 'row', 'uni'],
      dtype='object')
      
It is apparent by some of the variable names, that there are several overlapping encodings for the same variable such as "isco1c" and "isco2c" which ultimately provide the same information. This introduces issues of multicollinearity and correlation among the variables, which gives redundant information. This is something we will have to quantify and address during the preprocessing step to ensure we limit as much of this redundancy before we can build our predictive model.

We can look at the numeric frequency counts for unique value for each feature with the following lines of code:

.. code-block:: python3

    for column in df.columns:
        print("#### {} ###".format(column))
        print(df[column].value_counts().sort_values(ascending=False))
        print("\n")


.. code-block:: python3

    #### cntryid ###
    United States         4061
    Germany               2061
    Japan                 1711
    Canada                1274
    Russian Federation    1210
    United Kingdom        1169
    Korea                 1169
    France                1130
    Spain                  891
    Italy                  806
    Poland                 768
    Turkey                 537
    Netherlands            411
    Czech Republic         389
    Chile                  344
    Greece                 208
    Finland                207
    Austria                186
    Slovak Republic        184
    Israel                 178
    Singapore              156
    Sweden                 148
    New Zealand            144
    Belgium                143
    Denmark                134
    Ireland                112
    Norway                  89
    Lithuania               70
    Slovenia                67
    Estonia                 43
    Name: cntryid, dtype: int64


    #### gender_r ###
    Male      12495
    Female     7505
    Name: gender_r, dtype: int64


    #### computerexperience ###
    Yes    19789
    No       196
    Name: computerexperience, dtype: int64


    #### nativespeaker ###
    Yes    18203
    No      1596
    Name: nativespeaker, dtype: int64


    #### edlevel3 ###
    High      11894
    Medium     6951
    Low         969
    Name: edlevel3, dtype: int64


    #### yearlyincpr ###
    50 to less than 75    4221
    75 to less than 90    3967
    90 or more            3903
    25 to less than 50    2747
    10 to less than 25    1111
    Less than 10           812
    Name: yearlyincpr, dtype: int64


    #### birthrgn ###
    North America and Western Europe                5439
    Central and Eastern Europe                      3324
    East Asia and the Pacific (richer countries)    3072
    Latin America and the Caribbean                  409
    East Asia and the Pacific (poorer countries)      85
    Arab States                                       60
    South and West Asia                               59
    Sub-Saharan Africa                                53
    Central Asia                                      16
    Name: birthrgn, dtype: int64


    #### nativelang ###
    Test language same as native language        17384
    Test language not same as native language     1386
    Name: nativelang, dtype: int64


    #### ctryrgn ###
    North America and Western Europe                13208
    Central and Eastern Europe                       3268
    East Asia and the Pacific (richer countries)     3036
    Latin America and the Caribbean                   344
    Name: ctryrgn, dtype: int64


We can see that the majority of respondents were able to answer the test in their native langage; they are predominantly from North America and Western Europe, with high to medium levels of education, and males with experience working with computers. 

Let's take a look at the top 10 features with the most missing values, to get an idea of the completeness of our dataset, at a high level.

.. code-block:: python3

    print(df.isnull().sum().sort_values(ascending=False))[:10]

::

    v262    20000
    v44     19997
    v76     19993
    v144    19992
    v199    19991
    v159    19985
    v10     19981
    v172    19977
    v110    19956
    v160    19955
    dtype: int64


Already we can see that, from a higher level, some features have virtually all their values missing and therefore a candidate to be discarded later in the preprocessing step of the pipeline. There are many other features with a large proportion of their data missing that we will have to consider whether or not we can impute for missing values or just drop the column entirely.

We can examine the types of values that are recorded for each feature. The below code will print out all of the values for all feature, however, I will only include snippets within this post for brevity sake.


.. code-block:: python3

    for feature in df.columns:
        print("####{}###".format(feature))
        print(f"{df[feature].unique()}")
        print("Number of unique values: {}\n".format(len(df[feature].unique())))


.. code-block:: python3

    ####reg_tl2###
    ['99999' 'UKJ' 'UKI' nan 'RU40' 'SE11' 'KR01' 'IE02' 'SG00' 'PL22' 'UKD'
    'RU28' 'FR71' 'JPH' 'UKH' 'NL3' 'FR10' 'CL09' 'JPD' 'KR03' 'KR05' 'ES12'
    'KR04' 'RU74' 'FR22' 'KR02' 'FR81' 'SI01' 'FR43' 'DK04' 'PL11' 'UKG'
    'UKF' 'ES13' 'BE2' 'RU64' 'SK02' 'PL12' 'RU37' 'IL04' 'UKN' 'ES22' 'FR21'
    'JPG' 'CZ05' 'PL43' 'ES30' 'ES61' 'RU45' 'JPC' 'JPF' 'RU50' 'CL05' 'JPE'
    'UKC' 'EE00' 'CZ08' 'GR3' 'FR51' 'JPJ' 'FR30' 'SK01' 'PL32' 'CL13' 'SE33'
    'ES51' 'FR24' 'ES70' 'RU01' 'FR52' 'RU19' 'NL4' 'RU27' 'KR06' 'JPI'
    'RU54' 'PL63' 'UKE' 'NZ01' 'PL41' 'RU41' 'PL21' 'RU22' 'DK01' 'CZ01'
    'PL61' 'RU39' 'CZ04' 'JPB' 'NL2' 'FR82' 'PL52' 'ES52' 'FR23' 'CZ07'
    'SE22' 'ES21' 'FR61' 'FR62' 'RU65' 'PL51' 'CL08' 'SK03' 'PL33' 'RU08'
    'SE31' 'IL07' 'NZ02' 'IL02' 'PL31' 'RU58' 'PL42' 'ES42' 'GR2' 'ES53'
    'SE12' 'UKK' 'IL05' 'RU56' 'CZ06' 'ES23' 'ES62' 'ES41' 'RU67' 'LT08'
    'CZ03' 'GR1' 'ES24' 'IE01' 'PL34' 'JPA' 'LT04' 'CL14' 'FR42' 'FR53'
    'FR41' 'NL1' 'SE21' 'RU44' 'SI02' 'PL62' 'LT05' 'ES11' 'LT09' 'CZ02'
    'RU15' 'FR83' 'DK02' 'FR25' 'ES43' 'CL02' 'IL01' 'ES63' 'CL06' 'IL06'
    'DK05' 'RU16' 'SK04' 'DK03' 'CL07' 'LT07' 'IL03' 'LT02' 'FR72' 'LT06'
    'SE23' 'CL10' 'CL01' 'LT03' 'GR4' 'LT01' 'LT10' 'FR26' 'KR07' 'FR63'
    'SE32']
    Number of unique values: 176

    ####lng_bq###
    ['eng' 'rus' 'tur' 'swe' 'deu' 'kor' 'ita' 'pol' 'fra' 'jpn' 'nld' 'spa'
    'slv' 'dan' 'slk' 'heb' 'ces' 'est' 'ell' 'fin' 'nor' 'ara' 'cat' 'lit'
    '999' 'glg' 'hun']
    Number of unique values: 27

    ####lng_ci###
    ['eng' 'nor' 'rus' 'tur' 'swe' 'deu' 'kor' 'ita' 'pol' 'fra' 'jpn' 'nld'
    'spa' 'slv' 'dan' 'slk' 'heb' 'ces' 'est' 'ell' 'fin' 'cat' 'ara' 'lit'
    '999' 'glg' 'eus' nan 'hun']
    Number of unique values: 29

    ####yrsqual###
    [12.  15.  16.  18.  11.  14.   nan 19.  17.  22.  13.  20.   8.   9.
    21.  10.   6.   5.  14.5  7.  13.5]
    Number of unique values: 21

    ####yrsqual_t###
    [12.  15.  16.  18.  11.  14.   nan 19.  17.  22.  13.  20.   8.   9.
    21.  10.   6.   5.  14.5  7.  13.5]
    Number of unique values: 21


Here, we see specific values used to encode missing, unavailable, or other values. The common values that are used to encode such meanings are integers/strings of 9995, 9996, 9997, 9998, and 9999. This gives us an idea of how many additional missing values there are in the data set on top of the NaN values detected by the ``.isnull()`` method, and thusly, how to deal with these values as missing values. Again, we will address this later on during the preprocessing step of our pipeline.


Conclusion
----------

In summation, we were able to gleen at a higher level, some of the characteristics of our tabular dataset by loading it into a Pandas dataframe. We say that many of the feautures were predominantly object columns that contained string values, and many of our values for our data set were missing of many of those columns. We also saw the potential for multicollinearity among our 380 features, which introduces the problem of redundancy in our data. This can also be gleened visually from the naming scheme of our feature names. All of this provides us a better idea of some of the problematic issues we have with our data set and how we might address them later down the line. As with most real-world data sets, the majority of the work in a data scientists workflow comes down to preprocessing the data. In our next post, we will continue further with a more indepth exploration with our data using graphic visualizations and statistics. Until next time - ``print("Onward")``.
