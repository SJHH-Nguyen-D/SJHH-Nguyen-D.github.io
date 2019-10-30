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

In the previous post, we completed the necessary preprocessing methods that were required of dealing a variety of categorical data types (nominal, binary, and ordinal) and developed an encompassing transformation at the end to encode the mappings for our data points that remained after the initial preprocessing steps. During the previous post, we separated the numeric data from our categorical data to first work with the categorical features. This is the sixth post of my SharpestMinds project series talk about missing data values and how to come up with a smarter way to go about dealing with them. If you want to follow along with the full codebase in the Jupyter IPython Notebook, you can do so at the `link to the repo <https://github.com/SJHH-Nguyen-D/sharpestminds-project>`_). This is going to be a brief but insightful one, so let's get into it. 

=================
Feature Selection
=================

.. image:: /assets/cocos_bizarred_adventure.jpg
    :width: 600px
    :height: 380px
    :alt: placeholder image for page
    :align: center


Conclusion
**********

This is some words about the conclusion. There! Conclusion!