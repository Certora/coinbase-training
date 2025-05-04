Invariant vs. Parametric
========================

Writing an invariant as a rule
------------------------------
* We show how to write an invariant as a rule.
* The examples here use the :clink:`Voting<@lesson1/voting/Voting.sol>` contract.

The invariant
^^^^^^^^^^^^^

   The sum of votes in favor and against is the total votes.

.. cvlinclude:: @lesson1/voting/Voting-advanced.spec
   :cvlobject: sumResultsEqualsTotalVotes
   :caption: :clink:`sumResultsEqualsTotalVotes<@lesson1/voting/Voting-advanced.spec>`

* Report: `sumResultsEqualsTotalVotes report`_.

Wrong translation to a rule
^^^^^^^^^^^^^^^^^^^^^^^^^^^
* Below is a *wrong* translation of the invariant into a rule since
  it lacks the both *pre-condition* and the function call.
* Report: `sumResultsEqualsTotalVotesWrong report`_.

.. cvlinclude:: @lesson1/voting/Voting-advanced.spec
   :cvlobject: sumResultsEqualsTotalVotesWrong
   :caption: :clink:`from Voting-advanced.spec <@lesson1/voting/Voting-advanced.spec>`

Correct translation to a rule
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
* Here is a correct translation of the *induction step* into a rule.
* Report: `sumResultsEqualsTotalVotesAsRule report`_.

.. important::

   This only translates the **induction step** to a rule. It does not verify the
   *induction base*, i.e. after the constructor.

.. cvlinclude:: @lesson1/voting/Voting-advanced.spec
   :cvlobject: sumResultsEqualsTotalVotesAsRule
   :caption: :clink:`from Voting-advanced.spec <@lesson1/voting/Voting-advanced.spec>`

----

Parametric rules can be wrong
-----------------------------
* Unlike invariants, parametric rules are *not checked after the constructor*.
* So a parametric rule can prove a property that is unreachable.

Example
^^^^^^^
This example uses the :clink:`ERC20 <@ERC20/contracts/ERC20.sol>` contract.
In the :ref:`lesson2_erc20_exercises` you will prove that the balance of
:solidity:`address(0)` is always zero using an invariant. However, here is a parametric
rule saying the balance is always greater than zero, *assuming it started that way*.

.. cvlinclude:: @ERC20/certora/specs/Parametric.spec
   :cvlobject: balanceOfZeroAlwaysPositive
   :caption: :clink:`balanceOfZeroAlwaysPositive <@ERC20/certora/specs/Parametric.spec>`

* Report: `balanceOfZeroAlwaysPositive report`_.


.. Links
   -----

.. _sumResultsEqualsTotalVotes report:
   https://prover.certora.com/output/98279/7a20cd96579942d4b101c3d48730ad86?anonymousKey=4e68eed79b8fbb8c2784d5d413c0d3e9b7eaa64d

.. _sumResultsEqualsTotalVotesWrong report:
   https://prover.certora.com/output/98279/344479de54b44a268efdb14041c31eb1?anonymousKey=261ee8437845bdaee90e3f2455c3acc809c361ee

.. _sumResultsEqualsTotalVotesAsRule report:
   https://prover.certora.com/output/98279/639f9b6f246143cd9b410b6db9ac864f?anonymousKey=036812f67ed7689dbfed727a8b46eb183f419409

.. _balanceOfZeroAlwaysPositive report:
   https://prover.certora.com/output/98279/1b1275c5e4ec4a2fba5b1b8c858a770f?anonymousKey=af005f9f840b1d746c6ed11ff4f0e053ec601c40
   
