Ever wondered what your employee performance score would be? Part 8: Modeling (training, testing, validation)
#############################################################################################################

:date: 20191105 14:18
:tags: sharpestminds-project, data science, projects, employee performance, preprocessing, model selection, training, testing, fitting, validation
:slug: sharpestminds-project-part-8
:authors: Nguyen-Do, Dennis;
:summary: In this brief seventh post of the SharpestMinds project series we will go through the feature selection for our dataset and figure out which attributes in this thing are worth keeping. Without further ado, let's ``SELECT+START+A+B``!.

*****************************************************************************
SharpestMinds Project Series Part 8: Modeling (training, testing, validation)
*****************************************************************************

If you are new to this post and would like some context, I'd highly suggest you read through the previous posts of this project series, as this is the seventh post of this series:

* `Part 1 - Introduction <{filename}./sharpestminds-project-part-1.rst>`_
* `Part 2 - Background, Loading, EDA <{filename}./sharpestminds-project-part-2.rst>`_
* `Part 3 - More Exploratory Data Analysis <{filename}./sharpestminds-project-part-3.rst>`_
* `Part 4 - Dropping Data <{filename}./sharpestminds-project-part-4.rst>`_
* `Part 5 - Categorical Data Encoding <{filename}./sharpestminds-project-part-5.rst>`_
* `Part 6 - Imputing Missing Values <{filename}./sharpestminds-project-part-6.rst>`_
* `Part 7 - Feature Selection <{filename}./sharpestminds-project-part-7.rst>`_

In the previous post, we explored some of the various tooling and approaches to feature selection available in the ``sklearn`` and ``mlxtend`` libraries and ultimately decided on using a simple approach that was available to use (e.g., univariate feature elimination). This is the eighth post where we will be doing the meat and potatoes of any data science project, and probably the one that garners the most attention, despite taking proportionally less time compared to the other steps. As is typical for the modeling step, we go into aspects of training, testing, validating, model selection, and saving of learned model parameter and weights. If you want to follow along with the full codebase in the Jupyter IPython Notebook, you can do so at the `link to the repo <https://github.com/SJHH-Nguyen-D/sharpestminds-project>`_) at the ``sharpestminds_project.ipynb`` file or the ``main.py`` file. So without further ado, let's step into it!


Conclusion
**********