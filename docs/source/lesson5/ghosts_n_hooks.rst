Ghosts and hooks
================

Links:

* `Ghosts and hooks (from Tutorials)`_
* `Ghosts (from Documentation)`_
* `Hooks (from Documentation)`_

.. index::
   single: hook; storage

Storage hooks
-------------
A *storage hook* is a CVL function that will be executed whenever a particular storage
is loaded or stored (modified).

Example
^^^^^^^
We have an example of the Voting contract with a bug in
:clink:`VotingBug4.sol<@lesson1/buggy_voting/VotingBug4.sol>`.
The bug enables voters in favor to vote many times.

.. dropdown:: VotingBug4.sol

   .. cvlinclude:: @lesson1/buggy_voting/VotingBug4.sol
      :lines: 4-

Here is a basic spec that catches this bug.

.. cvlinclude:: @lesson1/voting/SimpleHook.spec
   :lines: 3-
   :caption:

The report: `Simple Hook report`_.


.. index::
   single: ghost

Ghost variables
---------------
* *Ghost* variables are "global" variables defined in CVL and accessible from
  CVL rules, invariants, hooks and functions.
* There are two types of ghost variables:

  #. Ordinary ghost variables behave like storage variables. In particular they revert
     when the transaction reverts, and they are "havoc'd" when the storage is.
  #. In contrast, *persistent* ghosts do not revert and are not havoc'd.

* Like storage variables, the value of ghost variables at the start of a rule is
  arbitrary, i.e. it can be anything.
* To set the value of a ghost variable for the base of an invariant (in other words the
  state after the constructor) use the :cvl:`init_state axiom` like so:

  .. cvlinclude:: @ERC20/certora/specs/SumExample.spec
     :cvlobject: sumOfBalances
     :caption: :clink:`Setting init state<@ERC20/certora/specs/SumExample.spec>`

* See also `Initial state axioms`_.

Example
^^^^^^^
* In :clink:`SimpleHook.spec<@lesson1/voting/SimpleHook.spec>` (see below)
  is a basic ghost example for the :clink:`Voting<@lesson1/voting/Voting.sol>`
  contract.
* The ghost records whether a store operation was performed.
* The rule :cvl:`someoneVotesUsingVote` states that if :cvl:`_hasVoted` had a store
  operation, then the total votes increased and the function called was :cvl:`vote`.
* This rule catches the bug in
  :clink:`VotingBug6.sol<@lesson1/buggy_voting/VotingBug6.sol>`, see
  `Simple Ghost report`. 

.. cvlinclude:: @lesson1/voting/SimpleGhost.spec
   :language: cvl
   :lines: 6-
   :caption:


.. Links
   -----

.. _Ghosts and hooks (from Tutorials):
   https://docs.certora.com/projects/tutorials/en/latest/lesson4_invariants/ghosts/basics.html

.. _Ghosts (from Documentation): https://docs.certora.com/en/latest/docs/cvl/ghosts.html
.. _Hooks (from Documentation): https://docs.certora.com/en/latest/docs/cvl/hooks.html

.. _Initial state axioms:
   https://docs.certora.com/en/latest/docs/cvl/ghosts.html#initial-state-axioms

.. _Simple Hook report:
   https://prover.certora.com/output/98279/a2de6a57ab844bff86a6554971bd923a?anonymousKey=f28ca571f41ceec8f68d484046cf3dd97d407978

.. _Simple Ghost report:
   https://prover.certora.com/output/98279/30faad7d0b034c4db97a03e644a892dc?anonymousKey=63a6cec01b4b77ed5b23a9bf74492656f173af91
