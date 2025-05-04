Exercises
=========

.. _set_elements_are_unique_ex:

Set exercises
-------------
* This exercise is for the :clink:`Set library<@evc/Set.sol>` from
  `Euler's Ethereum Vault Connector`_.
* To expose the library's functions, we created the
  :clink:`SetHarness<@set/certora/harness/SetHarness.sol>` contract, see below.
* Note that the :solidity:`get(uint8)` function actually returns the element at
  :solidity:`index - 1`.
* The goal is to prove the following properties:

  #. :cvl:`invariant uniqueElements` -- The elements in :solidity:`SetStorage` are unique.
  #. :cvl:`rule setLengthChangedByOne` --
     The length of the set can change by at most 1 when calling a function.
  #. :cvl:`rule setLengthIncreaseDecrease` --
     Only :cvl:`insert` increases the set's length, and only :cvl:`remove` decreases it.

#. Complete the spec file
   :clink:`SetExercise.spec<@set/certora/specs/SetExercise.spec>`
   according to the properties.
#. Complete the config file
   :clink:`SetExercise.conf<@set/certora/confs/SetExercise.conf>`.

   * Note the working directory for running
     :clink:`SetExercise.conf<@set/certora/confs/SetExercise.conf>`
     is: :clink:`training-examples/set/<@set>`.

#. Run the config file and check all properties are verified.

.. tip::

   It is best to use the same number of iterations as :solidity:`SET_MAX_ELEMENTS`.

.. dropdown:: SetHarness code

   .. cvlinclude:: @set/certora/harness/SetHarness.sol
      :lines: 8-
      :emphasize-lines: 18-21
      :caption:

.. dropdown:: SetExercise.spec and SetExercise.conf

   .. cvlinclude:: @set/certora/specs/SetExercise.spec
      :lines: 11-
      :emphasize-lines: 3, 8, 17
      :caption:
   
   .. cvlinclude:: @set/certora/confs/SetExercise.conf
      :emphasize-lines: 7-8 
      :caption:

.. dropdown:: Solution

   .. cvlinclude:: @set/certora/specs/Set.spec
      :caption:

   .. cvlinclude:: @set/certora/confs/Set.conf
      :emphasize-lines: 8
      :caption:

   Report: `Set solution report`_.


----

Voting exercises
----------------
Exercises regarding the :clink:`Voting contract<@lesson1/voting/Voting.sol>`.

#. Write a parametric rule saying ``votesInFavor``, ``votesAgainst`` and ``totalVotes``
   are all non-decreasing.
#. Write an invariant saying the sum of votes in favor and against equals the total votes.

----

.. _lesson2_erc20_exercises:

ERC20 exercises
---------------
Exercises regarding the :clink:`ERC20 contract<@ERC20/contracts/ERC20.sol>`.

#. Prove that the balance of address zero is always zero.
#. Prove that the :solidity:`_owner` is immutable.
#. Prove that only the owner can change :solidity:`totalSupply`.
#. The only methods that can decrease allowance are:
   :solidity:`approve`, :solidity:`decreaseAllowance` and :solidity:`transferFrom`.
   Who can be the message sender in each case?
#. Prove that :solidity:`totalSupply`:

   * Can only be increased by :solidity:`mint`.
   * Can only be decreased by :solidity:`burn`.

#. Try proving that the balance of any account is at most :solidity:`totalSupply` using
   an invariant. Is this even possible?

----

Funds managers exercises
------------------------
Exercises regarding the :clink:`Manager contract<@lesson2/manager/Manager.sol>` (see
:ref:`funds-managers` for details).

#. Complete the invariants in :clink:`Manager.spec<@lesson2/manager/Manager.spec>` --
   ensure they verify :clink:`Manager.sol<@lesson2/manager/Manager.sol>`.
#. Use the spec to find and fix the bugs in:

   #. :clink:`ManagerBug1.sol<@lesson2/manager/ManagerBug1.sol>`
   #. :clink:`ManagerBug2.sol<@lesson2/manager/ManagerBug2.sol>`


.. only:: is_dev_build

   Solution
   ^^^^^^^^
   #. :clink:`ManagerBug1.sol<@lesson2/manager/ManagerBug1.sol>`:
      does not check if manager is available before creating new one,
      `ManagerBug1.sol report <https://prover.certora.com/output/98279/2c6d919755824dfe807319a38650cd82/?anonymousKey=96b3e6cdf675498c18336f0e83dca7191a057679>`_.
   #. :clink:`ManagerBug2.sol<@lesson2/manager/ManagerBug2.sol>`:
      in `claimManagement` does not mark new manager as active,
      `ManagerBug2.sol report <https://prover.certora.com/output/98279/db7b52e3de70434398335a8fceb11ec0?anonymousKey=a1bb9a02b4d91262e4b0f138f42e37149d954409>`_.


.. Links
   -----

.. _Euler's Ethereum Vault Connector:
   https://github.com/euler-xyz/ethereum-vault-connector

.. _Set solution report:
   https://prover.certora.com/output/98279/cba7e7a297c14572b2cfcb46ec79ed53?anonymousKey=a63340f61e5e1546e1e09308e396a996ae381a96

