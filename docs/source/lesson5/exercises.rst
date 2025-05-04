Exercises
=========

Ghosts and hooks
----------------

Voting contract
^^^^^^^^^^^^^^^
#. Use a :ref:`sum_pattern_example` to show that in the
   :clink:`Voting<@lesson1/voting/Voting.sol>` contract :solidity:`totalVotes` equals
   the number of addresses :solidity:`a` such :solidity:`_hasVoted[a]` is true.
#. Write a parametric rule asserting that in any function :cvl:`_hasVoted` is changed
   at most once. Use this rule to find the bug in
   :clink:`VotingBug7.sol<@lesson1/buggy_voting/VotingBug7.sol>`.


----

Storage
-------
#. Show for the :clink:`ERC20<@ERC20/contracts/ERC20.sol>` contract
   from :clink:`@ERC20/contracts/` that transferring
   from :solidity:`address a` to :solidity:`address b` amount :math:`x` followed by
   amount :math:`y` is the same as transferring :math:`x + y`.
#. This exercises is for the :clink:`UnguardedPool<@lesson5/pool/UnguardedPool.sol>`
   using the :clink:`ERC20<@lesson5/pool/UnguardedPool.sol>` from the same folder
   as its underlying asset. Write a :cvl:`satisfy` rule providing an example that
   depositing :math:`x` followed by depositing :math:`y` yields a different number
   of shares than depositing :math:`x + y`.

----

String and hooks
----------------
One possible revert cause is an incorrectly encoded string in storage. This section guides
you through identifying this revert cause and checking for it.

The contract
^^^^^^^^^^^^
* The contract :clink:`StrIssue<@lesson5/string/StrIssue.sol>` has an array of structs
  and functions that manipulate them.

.. dropdown:: StrIssue

   .. cvlinclude:: @lesson5/string/StrIssue.sol
      :lines: 10-
      :caption:

Revert example exercise
^^^^^^^^^^^^^^^^^^^^^^^
Write a spec containing two rule:

#. A rule asserting that :cvl:`push` reverts only when :cvl:`e.msg.value` is non-zero,
#. A rule asserting that :cvl:`getData` reverts only when :cvl:`e.msg.value` is non-zero
   or when the index is out of bounds.

Running the spec you will discover that both rules are violated.

.. dropdown:: Solution

   A solution is found at
   :clink:`StrIssueExample.spec<@lesson5/string/StrIssueExample.spec>`.

Revert cause
^^^^^^^^^^^^
In general, storage variables are stored in particular slots, where each slot
has 32 bytes, see `Layout of State Variables in Storage`_.
Strings have a particular encoding in storage, meant to avoid wasting storage,
detailed in `Bytes and String Layout in Storage`_. In short:

* If the length of the string, denoted :math:`l`, is 31 bytes or less, 
  the entire string will be
  stored in the relevant slot, and the lowest-order byte will hold
  :math:`2 \cdot l` (twice the length of the string).
* If the length of the string :math:`l` is 32 bytes or more, the value of the slot
  will be :math:`2 \cdot l + 1`.

So values like 3, or 100 cannot be stored in the slot of a string. When reading
a string, Solidity reverts if the value in the slot is invalid. Note that solidity
also reads the existing value *before writing* a new string. So a write could also
potentially result in a revert.

Identifying the cause exercise
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#. Use a :cvl:`persistent ghost` and a hook to identify when an illegal string is read.
#. Add this cause to the two revert rules, and ensure they are verified.

**Notes.**

* To hook into loads from the slot of the :cvl:`y` field use:

  .. code-block:: cvl
   
     hook Sload bytes32 slotValue structArray[INDEX uint256 index].(offset 32)

* To convert :cvl:`bytes32` to :cvl:`uint256` use:

  .. code-block:: cvl

     uint256 encoded;
     require to_bytes32(encoded) == slotValue;

.. dropdown:: Solution

   A solution is found at
   :clink:`StrIssuePersistent.spec<@lesson5/string/StrIssuePersistent.spec>`.

Verifying all strings are legally encoded exercise
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#. Using a ghost and an :cvl:`Sstore` hook, write an invariant verifying that the
   strings in the field :cvl:`y` of the struct are legally encoded.
#. Run the invariant, it should provide a counter example for the :cvl:`dirty` function.

.. dropdown:: Solution

   A solution is found at
   :clink:`StrIssueInvariant.spec<@lesson5/string/StrIssueInvariant.spec>`.


.. Links
   -----

.. _Layout of State Variables in Storage:
   https://docs.soliditylang.org/en/stable/internals/layout_in_storage.html

.. _Bytes and String Layout in Storage:
   https://docs.soliditylang.org/en/stable/internals/layout_in_storage.html#bytes-and-string
