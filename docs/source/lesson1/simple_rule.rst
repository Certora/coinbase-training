A simple rule
=============

The structure of a spec
-----------------------

We create a spec for the :clink:`Voting<@lesson1/voting/Voting.sol>` contract
verifying that whenever someone voted, :cvl:`totalVotes` increase in
:clink:`SimpleRule.spec<@lesson1/voting/SimpleRule.spec>`. The spec is written
in the :term:`CVL` language.

The rule
^^^^^^^^
.. cvlinclude:: @lesson1/voting/SimpleRule.spec
   :cvlobject: voteIntegrity
   :caption:

.. index::
   single: env
   single: type; env

The :cvl:`env` type
^^^^^^^^^^^^^^^^^^^
* The type :cvl:`env` holds the environment, e.g.:

  * :cvl:`e.msg.sender`
  * :cvl:`e.block.timestamp`

* So the voter is :cvl:`e.msg.sender`
* What if the voter has already voted?

.. index::
   single: envfree
   single: methods block

The methods block
^^^^^^^^^^^^^^^^^
Here we declare that :cvl:`env` is not needed for the :cvl:`totalVotes` getter.
The Prover will also check this.

.. cvlinclude:: @lesson1/voting/SimpleRule.spec
   :cvlobject: methods
   :caption: :clink:`The methods block of SimpleRule.spec<@lesson1/voting/SimpleRule.spec>`


Running the Prover
------------------

.. index::
   single: command-line

From command line
^^^^^^^^^^^^^^^^^
From the :file:`training-examples@lesson1/voting/` folder, run:

.. code-block:: bash

   certoraRun Voting.sol:Voting --verify Voting:SimpleRule.spec --solc solc8.0


.. index::
   single: conf
   single: config

Use a config file
^^^^^^^^^^^^^^^^^
* The config file :clink:`SimpleRule.conf<@lesson1/voting/SimpleRule.conf>` holds the
  configuration for the run.
* Uses `JSON5`_ format, so it supports comments.

.. cvlinclude:: @lesson1/voting/SimpleRule.conf
   :caption:

Config file fields
^^^^^^^^^^^^^^^^^^

``files``
   The relevant files to compile (determines the files in the *scene*).
   A list of ``"<solidity_file>:<contract>"`` strings.

``verify``
   Syntax ``"<contract_to_verify>:<spec_file_path>"``.

``solc``
   Path to the relevant Solidity compiler.

.. seealso::

   See `CLI options`_ for more information and additional options.


Reports
-------
Voting report
^^^^^^^^^^^^^
* The results of running the Prover using
  :clink:`SimpleRule.conf<@lesson1/voting/SimpleRule.conf>` are shown in the
  `job report`_.
* The report shows the rule is verified.

Injected bug report
^^^^^^^^^^^^^^^^^^^
* The :clink:`BuggyVoting<@lesson1/voting/BuggyVoting.sol>` contract has a bug
  injected, see below.
* The config file :clink:`BuggyVoting.conf<@lesson1/voting/BuggyVoting.conf>`
  runs the :clink:`SimpleRule.spec<@lesson1/voting/SimpleRule.spec>` on
  the :clink:`BuggyVoting<@lesson1/voting/BuggyVoting.sol>` contract.
* The report: `BuggyVoting job report`_ shows a violation, i.e. a counter example to
  the rule.
* Understand the counter example.

.. dropdown:: BuggyVoting contract

   .. cvlinclude:: @lesson1/voting/BuggyVoting.sol
      :lines: 5-
      :emphasize-lines: 15
      :caption:

.. Links
   -----

.. _JSON5: https://json5.org/

.. _CLI options: https://docs.certora.com/en/latest/docs/prover/cli/options.html

.. _job report:
   https://prover.certora.com/output/98279/b4b9de21976343188c894729aea01f58?anonymousKey=1864eb01c1607e998d3398574b3bba79511b5c3f

.. _BuggyVoting job report:
   https://prover.certora.com/output/98279/150925787a2b44d2a5d1ea08feb7dafe?anonymousKey=a46d8c5506eb6b6b944ab4bfadfb2889745d19bc
