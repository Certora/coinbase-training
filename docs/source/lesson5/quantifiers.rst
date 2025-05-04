.. index::
   single: quantifiers
   single: forall
   single: exists
   :name: quantifiers_section


Quantifiers
===========
* Quantifiers provide a very powerful way to state certain properties should apply
  *for all* values. Equivalently that *there exists* some value satisfying a property.
* With great power comes great limitations.

Basics
------

Syntax
^^^^^^
* The following states that for every possible value of :cvl:`type` the
  :cvl:`boolean-expression` holds.

  .. code-block:: cvl

     forall <type> <id> . <boolean-expression>

* For example:
  
  .. code-block:: cvl

     require forall uint8 x. (2 * x) % 2 == 0;

Limitations
^^^^^^^^^^^
* Calls to solidity or CVL functions are not allowed inside quantified expressions.
* `Quantifier Grounding`_ may result in spurious counter-examples. To turn off
  quantifier grounding add the following to your config:

  .. code-block:: json

     "prover_args": ["-smt_groundQuantifiers false"]


Example
-------
* The example is for the :clink:`Set library<@evc/Set.sol>`,
  using the :clink:`SetHarness<@set/certora/harness/SetHarness.sol>`.
* We encountered these in :ref:`set_elements_are_unique_ex`.
* Due to the limitations of using quantifiers we add two definitions:

  #. :cvl:`definition numElements` -- replaces calls to :solidity:`length()`.
  #. :cvl:`definition getElement` -- replaces calls to :solidity:`get(uint8)`.

* Report link: `quantifier example report`_.


Spec and config
^^^^^^^^^^^^^^^
.. cvlinclude:: @set/certora/specs/SetQuantifiers.spec
   :caption:

.. cvlinclude:: @set/certora/confs/SetQuantifiers.conf
   :emphasize-lines: 11
   :caption:


.. Links
   -----

.. _Quantifier Grounding:
   https://docs.certora.com/en/latest/docs/prover/approx/grounding.html

.. _quantifier example report:
   https://prover.certora.com/output/98279/2f598ed15bd9441da510279f6aa3d886?anonymousKey=216eedfa51561faf1f6013bf1f07ab2a08951ba6
