Bug injection
=============

Malicious contract
------------------

.. cvlinclude:: @lesson1/voting/MaliciousVoting.sol
   :lines: 7-8, 19-31
   :emphasize-lines: 7
   :caption:


Third party protection rule
---------------------------

First formulation
^^^^^^^^^^^^^^^^^
A rule verifying that unrelated party should not be affected by the actions of
:solidity:`msg.sender`.

.. cvlinclude:: @lesson1/voting/Voting.spec
   :cvlobject: votePreservesThirdParty

.. index::
   single: require

* Note the use of the :cvl:`require` statement

  * It is different from :solidity:`require` in solidity
  * It limits the possible computation paths that are checked by :cvl:`assert`.
  * Be careful -- :cvl:`require` statements can be the source of *unsoundness*!

----

Second formulation -- using implication
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. cvlinclude:: @lesson1/voting/Voting.spec
   :cvlobject: votePreservesThirdPartyImplication
   :caption: Using implication

----

Generalized version of the rule
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
We can generalize the implication version, to account for both cases, i.e. whether
:cvl:`thirdParty` is the message sender or not:

.. cvlinclude:: @lesson1/voting/Voting.spec
   :cvlobject: voteConsequences
   :caption: General version

----

Report and config
^^^^^^^^^^^^^^^^^
* Here is the `Full Report`_.

.. dropdown:: Config file

   .. cvlinclude:: @lesson1/voting/MaliciousVoting.conf
      :language: json
      :caption:


.. Links
   -----

.. _Full Report:
   https://prover.certora.com/output/98279/87b1aa6b569d441ab325bb1129fd5ae7?anonymousKey=4303e84f35bb8affb936e66e978f5a74d16783f8
