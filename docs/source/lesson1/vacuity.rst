.. index::
   single: vacuity

Vacuity
=======

   All persons over 10 meters tall have 3 arms.

* Formally, a rule is *vacuous* if it has no valid computation paths.
* Such a rule has no counter-examples, and is therefore considered as verified
  (non-violated).


Examples
--------
* The examples here are from :clink:`Vacuity.spec<@lesson1/voting/Vacuity.spec>`, and
  the rules are for the :clink:`Voting.sol<@lesson1/voting/Voting.sol>` contract.
* See `Vacuous rules report`_ for their report.

Obviously vacuous
^^^^^^^^^^^^^^^^^
* Below is an obviously vacuous rule: :cvl:`obviouslyVacuous`.
* We can identify a vacuous rule by seeing if :cvl:`assert false;` is verified.
* Equivalently, we can check if :cvl:`satisfy true;` is violated.

.. cvlinclude:: @lesson1/voting/Vacuity.spec
   :cvlobject: obviouslyVacuous
   :caption: :clink:`obviouslyVacuous rule<@lesson1/voting/Vacuity.spec>`


Requirement causing revert
^^^^^^^^^^^^^^^^^^^^^^^^^^^
* Here is a less obvious example, where the :cvl:`require` statement causes the revert.

.. cvlinclude:: @lesson1/voting/Vacuity.spec
   :cvlobject: revertingRequire
   :emphasize-lines: 5
   :caption: :clink:`revertingRequire rule<@lesson1/voting/Vacuity.spec>`


.. index::
   single: rule_sanity
   single: sanity

Rule sanity
-----------

* The Prover can be made to look for vacuous rules.
* This is done using the ``rule_sanity`` config option (equivalently ``--rule_sanity``
  CLI option).
* Use ``"rule_sanity": "basic"``.
* See `Rule sanity`_ from the Documentation for more information.
* See `Report with sanity`_ for a report using rule sanity.

.. important::

   Always use at least ``"rule_sanity": "basic"`` when running jobs.


.. Links
   -----

.. _Vacuous rules report:
   https://prover.certora.com/output/98279/fbbd8f46cf6a4c1e9c9f7781afd59910?anonymousKey=1588c2b79378c8391d99c7098a4bafda51924c74

.. _Rule sanity:
   https://docs.certora.com/en/latest/docs/prover/cli/options.html#rule-sanity

.. _Report with sanity:
   https://prover.certora.com/output/98279/4bf4d2fa8f2948d79b3e103869972fda?anonymousKey=1c28fd1f4b99cb7fe8d374e189c7a7f791f7c9fb
