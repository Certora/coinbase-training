.. index::
   single: parametric
   single: rule; parametric

Parametric rules
================

* Parametric rules are used for *state transitions*, e.g. "The number of people voted
  cannot decrease".
* See `Parametric rules (from Documentation)`_ and
  `Parametric rules (from Tutorials)`_.


Examples
--------
These examples are for the :clink:`ERC20.sol<@ERC20/contracts/ERC20.sol>` contract.

Only account holder can increase allowance
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. cvlinclude:: @ERC20/certora/specs/Parametric.spec
   :cvlobject: allowanceIncreaseAlwaysCalledByHolder
   :caption: :clink:`from Parametric.spec <@ERC20/certora/specs/Parametric.spec>`

----

.. _functions_increasing_allowance:

Which functions can increase allowance
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
* The rule below asserts that only certain functions will increase allowance.
* To identify a function we use :cvl:`sig:function_signature().selector`,
  see :ref:`detour_identify_function` below.

.. cvlinclude:: @ERC20/certora/specs/Parametric.spec
   :cvlobject: allowanceIncreaseConditions
   :caption: :clink:`from Parametric.spec <@ERC20/certora/specs/Parametric.spec>`

----

.. index::
   single: sig
   single: selector
   single: function
   :name: detour_identify_function

Detour -- function properties
"""""""""""""""""""""""""""""
In :ref:`functions_increasing_allowance` above we used the following syntax to
identify a function:

.. cvlinclude:: @ERC20/certora/specs/Parametric.spec
   :lines: 46-47

Additional data about :cvl:`method f` we have in CVL:

* :cvl:`bool f.isView` -- if :cvl:`f` is a :solidity:`view` function
  (see `View Functions`_).
* :cvl:`bool f.isPure` -- if it is a :solidity:`pure` function
  (see `Pure Functions`_).
* :cvl:`address f.contract` -- the contract of :cvl:`f`.


.. Links
   -----

.. _Parametric rules (from Tutorials):
   https://docs.certora.com/projects/tutorials/en/latest/lesson2_started/parametric.html

.. _Parametric rules (from Documentation):
   https://docs.certora.com/en/latest/docs/cvl/rules.html#parametric-rules

.. _View Functions: https://docs.soliditylang.org/en/latest/contracts.html#view-functions
.. _Pure Functions: https://docs.soliditylang.org/en/latest/contracts.html#pure-functions
