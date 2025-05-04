Exercises
=========

ERC-20 exercises
----------------
Exercises regarding the :clink:`ERC-20 contract<@ERC20/contracts/ERC20.sol>`.

Understanding violations
^^^^^^^^^^^^^^^^^^^^^^^^
The rule :cvl:`integrityOfTransferFrom` from :clink:`@ERC20/certora/specs/Integrity.spec`
has a type error and two mistakes.

#. Create a config file for running the spec.
#. Fix the type-error.
#. Run the spec, and using the reports fix the two mistakes.

.. dropdown:: ``integrityOfTransferFrom``

   .. cvlinclude:: @ERC20/certora/specs/Integrity.spec
      :cvlobject: integrityOfTransferFrom

Finding bugs
^^^^^^^^^^^^

#. Write a rule (or rules) for the integrity of the :solidity:`transfer` function,
   specifying how the balances of the message sender and recipient change.
#. Use this rule to find the bug in :clink:`@ERC20/contracts/broken/ERC20Bug1.sol`.


Voting contract exercises
-------------------------
Exercises regarding the :clink:`Voting contract<@lesson1/voting/Voting.sol>`.

Rule writing
^^^^^^^^^^^^

#. Write a rule showing the change in total votes caused by :cvl:`vote` equals
   the change in votes in favor plus the change in votes against.
#. Prove that no one voter can vote twice.
#. Show that a voter can vote once.
#. Run these rules on the fixed
   :clink:`Voting contract<@lesson1/voting/Voting.sol>`,
   and ensure they find no violations.

Finding bugs
^^^^^^^^^^^^
The folder :clink:`buggy_voting<@lesson1/buggy_voting>` holds several buggy
implementations of the :clink:`Voting contract<@lesson1/voting/Voting.sol>`.

#. Use the rules you wrote (or any other rules) to find the bugs in:

   * :clink:`VotingBug1.sol<@lesson1/buggy_voting/VotingBug1.sol>`
   * :clink:`VotingBug2.sol<@lesson1/buggy_voting/VotingBug2.sol>`
   * :clink:`VotingBug3.sol<@lesson1/buggy_voting/VotingBug3.sol>`

#. Create rules that find the bugs in:

   * :clink:`VotingBug4.sol<@lesson1/buggy_voting/VotingBug4.sol>`
   * :clink:`VotingBug5.sol<@lesson1/buggy_voting/VotingBug5.sol>`

