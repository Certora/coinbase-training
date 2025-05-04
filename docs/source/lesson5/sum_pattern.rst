.. index::
   single: sum
   :name: sum_pattern_example

Sum pattern
===========
This pattern is commonly used to prove in ERC-20 that the :solidity:`totalSupply` is the
sum of all balances. We'll use the :clink:`ERC20<@ERC20/contracts/ERC20.sol>` contract
for this example.


Spec
----
* Below is the ghost, hook and invariant.
* Report: `Sum pattern report`_.

.. cvlinclude:: @ERC20/certora/specs/SumExample.spec
   :lines: 6-
   :caption:


Using consequences
------------------
* Once this sum invariant is proved, we can require its consequences as needed.

Example
^^^^^^^
* For example, consider the :cvl:`sumOfTwo` invariant below.

   .. cvlinclude:: @ERC20/certora/specs/SumOfTwo.spec
      :cvlobject: sumOfTwo
      :caption: :clink:`sumOfTwo<@ERC20/certora/specs/SumOfTwo.spec>`

* The :cvl:`sumOfTwo` invariant is violated on several functions
  (see `Sum of two report`_):

  #. :solidity:`burn(address,uint256)`
  #. :solidity:`withdraw(uint256)`
  #. :solidity:`transfer(address,uint256)`
  #. :solidity:`transferFrom(address,address,uint256)`

* Even adding several more preserved blocks does not help,
  see `Sum of two with preserved blocks report`_.
* Instead, use:

  .. code-block:: cvl

     require balanceOf(user1) + balanceOf(user2) <= sumOfBalances;

  where needed.

.. caution::

   Recall that :cvl:`require` statements can be :term:`unsound`. Use them sparingly
   and ensure they are indeed consequences of the invariant you proved.


.. Links
   -----

.. _Sum pattern report:
   https://prover.certora.com/output/98279/dc1a1cba8ed94a35862c4caca07fa723?anonymousKey=bc21dd661bfcde8c1e7d2edb11b082ddc9628f25

.. _Sum of two report:
   https://prover.certora.com/output/98279/75a7cc2365e54493b19b41222bec443f?anonymousKey=5424570e41b478c98769d1661243dacc828eb801

.. _Sum of two with preserved blocks report:
   https://prover.certora.com/output/98279/97bb0a2610174103b74cec660a23dc66?anonymousKey=e6584b4e13f5fa7063c977903912ec090a16a845
