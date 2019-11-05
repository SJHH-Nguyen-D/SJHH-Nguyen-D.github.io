Ever wondered what your employee performance score would be? Part 1: Introduction
#################################################################################

:date: 20190927 10:35
:tags: sharpestminds-project, data science, projects, employee performance
:category: projects
:slug: sharpestminds-project-part-1
:authors: Nguyen-Do, Dennis;
:summary: My first project with my SharpestMinds mentorship program does just this in my first multi-step blog series. Curious? Well, come on in!

*************************************************
SharpestMinds Project Series Part 1: Introduction
*************************************************

==========
Background
==========

As part of the `SharpestMinds mentorship program <https://www.sharpestminds.com/>`_, each mentee is assigned a mentor based on interests and compatibility. Our mentorship spanned 4 months, for which we select a topic of our data science project, and along side the mentor, devote the majority of the time building an end-to-end data science project. The language chosen for this project was chosen to be Python 3.6 and up, using many of the popular modules and libraries commonly used for data science problems (i.e., Pandas, Matplotlib, Seaborn, Numpy, Scikit-Learn, etc...)

I had been fortunate enough to be provided the opportunity to work along side `mentor Charlie Liu <https://www.sharpestminds.com/>`_. We'd had some time to to discuss each others interests and what projects might be suitable for the program and ultimately decided the project for which this series of blog post seeks to showcase and document.

.. image:: https://cdn.pixabay.com/photo/2017/07/25/22/54/office-2539844_960_720.jpg
    :width: 784px
    :height: 447px
    :alt: Who's ready for their performance evaluation?!
    :align: center

`Image Credit: Pixabay <https://pixabay.com/photos/office-people-accused-accusing-2539844/>`_

Employee Performance Scoring
****************************

After several iterations of ideas for a project, including several based on agriculture, food-sustainability, non-profit organizations, NLP, and webscraping, we decided to settle with a very different, but equally interesting idea of building a project around predicting employee scoring based on a number of employee education, economic and demographic characteristics. The project was suggested due to its novelty in relation to my current knoweldge domains and because I thought it was neat!

**DISCLAIMER:** This project has no intention of discrimination and makes causal claims about an individual's socioeconomic and demographic characteristics and their ability to perform work, based on an arbitrary, fabricated performance index.

The blog will sequentially follow the table below and for each step of the project, a blog post will detail my methods and serve to archive my progress through my project.

=============  ===========================================================================================
  Step               Process
=============  ===========================================================================================
Introduction    `Rationale <{filename}./sharpestminds-project-part-1.rst>`_
The Data        `Background, Loading, EDA <{filename}./sharpestminds-project-part-2.rst>`_
The Data        `Some more EDA <{filename}./sharpestminds-project-part-3.rst>`_
Preprocessing   `Dropping Insufficient Data <{filename}./sharpestminds-project-part-4.rst>`_
Preprocessing   `Encoding, Labeling Categorical Variables <{filename}./sharpestminds-project-part-5.rst>`_
Preprocessing   `Imputation of Missing Values <{filename}./sharpestminds-project-part-6.rst>`_
Selection       `Feature Selection <{filename}./sharpestminds-project-part-7.rst>`_
Modeling        `Training, Testing, Validation <{filename}./sharpestminds-project-part-8.rst>`_
Deployment      Web Application Endpoint
Write-Up        Blog about it - which is what this is all about!
=============  ===========================================================================================

A link to the complete code for the project can be found `here <https://github.com/SJHH-Nguyen-D/sharpestminds_project/>`_ for you to follow along.

And in the words of the wise philosopher, Dr. Mario:

    "He-ah we go!"
    
    --  Mario of the Mario Bros.

.. todo:
    make links connecting internal blog post html links to this one, when the project is complete