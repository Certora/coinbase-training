.. Certora training template master file.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Certora Coinbase training
=========================

Contents
--------

#. :doc:`lesson1/index` -- introduction to solidity *(optional)*, the basics of CVL, 
   running the Prover, ERC-20 *(optional)*,
   and various rule types: satisfy rules, relational rules and rules for reasoning about
   reverts.
#. :doc:`lesson2/index` -- introduces invariants, preserved blocks and parametric rules.
   Also deals with loops.
#. :doc:`lesson3/index` -- how to set up a multi-contract system, linking and dispatcher.
#. :doc:`lesson4/index` -- the different types of properties.
#. :doc:`lesson5/index` -- ghosts and hooks, sum pattern, re-entrancy, storage,
   quantifiers. 
#. :doc:`lesson6/index` -- different summary types (:cvl:`CONSTANT`, :cvl:`NONDET`, etc.),
   method entries, call resolution order, and dispatch list.
#. :doc:`lesson7/index` -- advanced sanity checking, mutation testing.


.. Root table of contents, possible options:
   :maxdepth: integer - determines how many nested levels to show in the table
   :numbered: integer - add numbering for parts, the number deterrmines how many
   nested levels will be numbered
   See https://www.sphinx-doc.org/en/master/usage/restructuredtext/directives.html#directive-toctree
.. Hidden table of contents, will appear on the side bar.

.. toctree::
   :maxdepth: 2
   :numbered: 2
   :hidden:

   lesson1/index
   lesson2/index
   lesson3/index
   lesson4/index
   lesson5/index
   lesson6/index
   lesson7/index


.. toctree::
   :hidden:

   genindex
   glossary

----

.. _lectures_recordings:

Lectures and office hours recordings
------------------------------------

.. todo:: Add recordings to :ref:`lectures_recordings`.

----

Useful links
------------
* `Prover installation instructions`_
* `Certora Prover documentation`_
* `Certora Prover tutorials`_


Indices and tables
==================

* :ref:`genindex`
* :ref:`search`


.. REPLACE paths in the tip below to the correct ones

.. tip::

   You can create a local version of these pages, with links to your local files.
   First, install the necessary Python dependencies, by running from the root folder of
   this repository *(use a virtual environment!)*: 

   .. code-block:: bash

      pip3 install -r requirements.txt
  
   Next, in :file:`docs/source/conf.py` change the value of ``link_to_github`` to
   ``False``. Finally, run:

   .. code-block:: bash

      sphinx-build -b html docs/source/ docs/build/html

   The html pages will be in :file:`docs/build/html/index.html`.


.. Links:
   ------

.. _Prover installation instructions:
   https://docs.certora.com/en/latest/docs/user-guide/getting-started/install.html

.. _Certora Prover documentation: https://docs.certora.com/

.. _Certora Prover tutorials: Prover installation instructions

.. _Certora Documents Infrastructure:
   https://certora-docs-infrastructure.readthedocs-hosted.com/en/latest/index.html

.. _Comments and TODOs:
   https://certora-docs-infrastructure.readthedocs-hosted.com/en/latest/showcase/comments_todos.html
