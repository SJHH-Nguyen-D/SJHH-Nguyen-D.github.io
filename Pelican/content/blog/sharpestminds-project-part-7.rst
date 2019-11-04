Ever wondered what your employee performance score would be? Part 7: Feature Selection
######################################################################################

:date: 20191030 18:26
:tags: sharpestminds-project, data science, projects, employee performance, preprocessing, feature selection, feature engineering
:slug: sharpestminds-project-part-7
:authors: Nguyen-Do, Dennis;
:summary: In this brief seventh post of the SharpestMinds project series we will go through the feature selection for our dataset and figure out which attributes in this thing are worth keeping. Without further ado, let's ``SELECT+START+A+B``!.

******************************************************
SharpestMinds Project Series Part 7: Feature Selection
******************************************************

If you are new to this post and would like some context, I'd highly suggest you read through the previous posts of this project series, as this is the seventh post of this series:

* `Part 1 - Introduction <{filename}./sharpestminds-project-part-1.rst>`_
* `Part 2 - Background, Loading, EDA <{filename}./sharpestminds-project-part-2.rst>`_
* `Part 3 - More Exploratory Data Analysis <{filename}./sharpestminds-project-part-3.rst>`_
* `Part 4 - Dropping Data <{filename}./sharpestminds-project-part-4.rst>`_
* `Part 5 - Categorical Data Encoding <{filename}./sharpestminds-project-part-5.rst>`_
* `Part 6 - Imputing Missing Values <{filename}./sharpestminds-project-part-6.rst>`_

In the previous post, we approached the problem of missing values with the use of very useful package in the PYPI library called ``missingpy`` and used its ``KNNImputer`` class to help better impute for the missings values in our dataset. After the imputation of missing values, which were preivously encoded with numeric values, we had to perform rounding for the categorical discrete values of our dataset to make sure that . This is the seventh post of my SharpestMinds project series go into process of selecting the features to be included to be used for the modeling step of our pipeline. We make use some computationally intensive, but powerful tooling provided for us through the ``mlxtend`` python library from PYPI as well as the ``sklearn.feature_selection`` submodule. If you want to follow along with the full codebase in the Jupyter IPython Notebook, you can do so at the `link to the repo <https://github.com/SJHH-Nguyen-D/sharpestminds-project>`_) at the ``sharpestminds_project.ipynb`` file or the ``main.py`` file. Let's get into it!

=================
Feature Selection
=================

In the data science pipeline, the process of 'feature selection' refers to selecting a subset of the features or attributes of our dataset to include in the final modeling process. This step could be one of the most intensive steps alongside feature engineering, and is a means to produce the most signal to our model during the training and prediction step. The reason we perform feature selection is to remove to the chaff from the wheat - that is, to remove the useless features from the truly useful ones, which would not only improve the predictive ability of our model but also improve the training times for the training of our model. This process often requires in-depth technical domain knowledge (which can be very resource expensive) or an algorithmic search strategy by which we can approach feature selection. We will go over this latter part with the ``scikit-learn`` library's ``feature_selection`` classes, which include meta-transformative estimators. In addition, we will go over the powerful and mighty 'automatic' approach to feature selection with the ``mlxtend`` library. Each one of these approaches has their specific nuances for use and we will go over high level as to how they work.


Univariate Feature Elimination
******************************

Using the univariate feature elimination strategy, we use univariate statistics (e.g., chi-squared test of independence for categorical data, f-test for regression, mutual information for regression) and specify a number of features to be included in the final dataset that have quantified a specified level of statistical significance (typically alpha=0.05 or alpha=0.01). The ``sklearn`` library also provides the convenience of selecting the top user-specified percentile of features to be included.


Removing Features with Low Variance
***********************************

Numeric features that contain little to no variance do no provide more noise to signal ratio by being included in the modeling processes. Setting a cut-off value to this variance (i.e., the square of the standard deviation), allows us to eliminate noisy variables below this cut-off. By default, a variable containing only one value would be eliminated using this approach (cutoff=0.0).


Selecting Features Using a Meta-Model
*************************************

The task of selecting a subset of features for final inclusion in a predictive model can also be tasked to another model (e.g., tree-based, regression or other). Similar to the low-variance feature removal procedure, a cutoff value is set and using the ``coef_`` and ``feature_importances_`` attributes, any feature that does not score above this set parameter is eliminated from the contest. Additionally, there are meta-heuristic that can be specified in order to find the optimal threshold for elimination. There details are available through the documentation for the ``sklearn.feature_selection.SelectFromModel`` module.


.. image:: /assets/wheat-317021_640.jpg
    :width: 640px
    :height: 406px
    :alt: thresher
    :align: center

`Image by Karen Arnold <https://pixabay.com/users/Kaz-19203/?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=image&amp;utm_content=317021>`_


Recursive Feature Elimination
*****************************

The RFE approach employs a user-specified estimator to assign *weights* for the importance of features (their contribution in a subset of features) and recursively removes a number of features which fail the weight contribution requirement until a user-specified limit of inclusive features is met. Initially starting with the entire dataset, features are assigned a numeric coefficient of their importance in predicting the response variable. The features can be viewed using the ``coef_`` or ``feature_importances`` attribute. This method also offers the option of performing RFE with cross-validation. 


Sequential Forward Feature Selection
************************************

*Sequential forward feature selection*  (SFFS) is a strategy to feature selection which starts the predictive modeling process with a single feature at a time, and *sequentially* combining combinations of features together to select the 'best' subset of features to provide the most predictive value to your model (which you also select before hand). This SFFS process is typically also performed alongside a predictive model with k-fold cross-validation and therefore can be quite time-consuming running on a single CPU. 

Sequential Backward Feature Selection
*************************************

*Sequential Backward Feature Selection* (SBFS), in contrast with SFFS, does the reverse in that it starts off with performing the predictive modeling task on the entire dataset first, and then removing a feature(s) each time, and selecting the best subset of features that gives the best predictive scores (either training set score or validation test scores), with cross-fold validation. Again, a fairly computationally intensive and time-consuming approach on a single CPU.

Exhaustive Feature Selection
****************************

*Exhaustive Feature Selection* (EFS) 


The code
********

Now, having gone through that, we are going to opt to use the SFS approach alongside a tree-based random forest regressor algorithm

.. code-block:: python3

    def select_n_features(X, Y, n_features=10):
    """ uses the mlxtend module to select a number of features to keep in the dataframe """
        from mlxtend.feature_selection import SequentialFeatureSelector as SFS
        from sklearn.ensemble import RandomForestRegressor

        # # Build RF regressor to use in feature selection
        rfr = RandomForestRegressor(n_estimators=100, n_jobs=-1)

        sfs = SFS(rfr, 
                k_features=n_features, 
                forward=True, 
                floating=False, 
                scoring='r2',
                n_jobs=-1,
                cv=10)

        sfs = sfs.fit(X, Y)

        feature_indices = sfs.k_feature_idx_
        feature_names = sfs.k_feature_names_

        return feature_indices, feature_names

    # We select only about a third of the features arbitrarily
    selected_feature_indices, selected_feature_names = select_n_features(X_train, y_train, n_features=round(0.33*len(df.columns)-1))
    df = imputed_df[feature_names]


.. image:: /assets/cocos_bizarre_adventure.jpg
    :width: 518px
    :height: 691px
    :alt: CoCo the cat
    :align: center


Conclusion
**********

This is some words about the conclusion. There! Conclusion!