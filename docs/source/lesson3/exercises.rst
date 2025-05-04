Exercises
=========

Side entrance pool
------------------
* In this exercise we will setup a liquidity pool and discover its vulnerability.
* This is based on `Damn Vulnerable DeFi Challenge #4 - Side Entrance`_.

.. _side_entrance_setup:

Setup
^^^^^
* The pool is
  :clink:`SideEntranceLenderPool<@lesson3/side_entrance/SideEntranceLenderPool.sol>`
  (shown below).
* To burrow from the pool, a contract must implement the :solidity:`IFlashLoanReceiver`
  interface. Two implementations are:

  #. :clink:`TrivialFlashLoanReceiver<@lesson3/side_entrance/TrivialFlashLoanReceiver.sol>`
  #. :clink:`TransferFlashLoanReceiver<@lesson3/side_entrance/TransferFlashLoanReceiver.sol>`

Exercises
"""""""""
#. Prepare a setup for the pool using
   :clink:`@ERC20/contracts/ERC20.sol` as the token and
   :clink:`TrivialFlashLoanReceiver<@lesson3/side_entrance/TrivialFlashLoanReceiver.sol>`
   and
   :clink:`TransferFlashLoanReceiver<@lesson3/side_entrance/TransferFlashLoanReceiver.sol>`
   as potential :solidity:`IFlashLoanReceiver` implementations.
#. Write a rule showing that using :cvl:`flashLoan` followed by :cvl:`withdraw` cannot
   increase the user's ERC20 balance plus pool deposit.
   *(We'll next see that this is in fact wrong).*
   
.. dropdown:: SideEntranceLenderPool

   .. cvlinclude:: @lesson3/side_entrance/SideEntranceLenderPool.sol
      :lines: 18-
      :caption:

.. dropdown:: Solution - do not peek!

   .. cvlinclude:: @lesson3/side_entrance/SetupSolution.spec
      :caption:

   .. cvlinclude:: @lesson3/side_entrance/SetupSolution.conf
      :caption:

   Report: `setup solution report`_.

Find the exploit
^^^^^^^^^^^^^^^^
* The
  :clink:`ComplexFlashLoanReceiver<@lesson3/side_entrance/ComplexFlashLoanReceiver.sol>`
  (see below) uses the Prover's :term:`over-approximation` of storage states in order to
  "randomly" perform many actions.
* This will enable the Prover to consider many actions when looking for an exploit
  example.

.. dropdown:: ComplexFlashLoanReceiver

   .. cvlinclude:: @lesson3/side_entrance/ComplexFlashLoanReceiver.sol
      :lines: 14-
      :caption:

Exercises
"""""""""
#. Update the setup :ref:`side_entrance_setup` to include the
   :clink:`ComplexFlashLoanReceiver<@lesson3/side_entrance/ComplexFlashLoanReceiver.sol>`
   among the possible flash loan receivers.
#. Run the config and discover the exploit. If needed, use a :cvl:`satisfy` rule to
   better understand the counter example.

.. tip::

   You will need to use the following config options:
   
   * ``"optimistic_contract_recursion": true"``,
   * ``contract_recursion_limit`` (use a small number), see `contract_recursion_limit`_,
   * ``"optimistic_summary_recursion": true"``,
   * ``summary_recursion_limit`` (use a small number), see `Options regarding summarization`_.

.. dropdown:: Solution - do not peek!

   .. cvlinclude:: @lesson3/side_entrance/SideSolution.conf
      :emphasize-lines: 14-15, 21-24
      :caption: :clink:`Solution config<@lesson3/side_entrance/SideSolution.conf>`

   Report: `exploit solution report`_.


.. Links
   -----

.. _Damn Vulnerable DeFi Challenge #4 - Side Entrance:
   https://www.damnvulnerabledefi.xyz/challenges/side-entrance/

.. _contract_recursion_limit:
   https://docs.certora.com/en/latest/docs/prover/cli/options.html#contract-recursion-limit

.. _setup solution report:
   https://prover.certora.com/output/98279/d117c7da0c5c4606b72c6f5070d2091b?anonymousKey=d119d5e851559783b6b704af28cb8c4227693b62

.. _exploit solution report:
   https://prover.certora.com/output/98279/4dea4bd56e884c7f85aef766b1d90861?anonymousKey=a8a0ed3df6d20a2af0fe53f318d3765bf5c991ee

.. _Options regarding summarization:
   https://docs.certora.com/en/latest/docs/prover/cli/options.html#options-regarding-summarization
