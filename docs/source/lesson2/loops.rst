.. index::
   single: loop
   single: optimistic_loop
   single: loop_iter
   :name: loop_handling

Loops
=====

Unrolling
---------

* For a complete explanation see `Loop unrolling`_ from the Documentation.
* Loops and recursion are *undecidable* (see `Undecidable problem`_),
  so the Prover must *unroll* loops.
* The number of loop unrolls is determined by the ``loop_iter`` parameter
  (either in config or in CLI).
* At the end of the unrolled loop, we either

  * :cvl:`require` that the stop condition is met, or 
  * :cvl:`assert` that it is met.

* The :cvl:`require` is used if the ``optimistic_loop`` flag is set,
  otherwise the Prover applies the :cvl:`assert`.

.. _loop_unrolling_example:

Unrolling example
^^^^^^^^^^^^^^^^^
In this example we unroll a loop three times.

.. cvlinclude:: @lesson2/loops/Loopy.sol
   :caption: :clink:`A loop unrolled<@lesson2/loops/Loopy.sol>`

----

.. _loop_iterations_sec:

Loop iterations
---------------
* The number of ``loop_iter`` determines the number of loop unrolling.
* This can have a critical effect of verification of rules.
* A too low number (with ``optimistic_loop``) can result in a :term:`vacuous` rule.
* A too high number might result in a timeout.

----

Basic examples
--------------
* These example use the contract :clink:`Loopy<@lesson2/loops/Loopy.sol>`.
* The :solidity:`loop` function needs at least 3 iterations to unroll correctly.
* The rule :cvl:`loopExample` below simply asks for any example of a run, while
  the rule :cvl:`loopValue` asserts the formula for summing numbers up to 
  and including :math:`n + 2`.

.. cvlinclude:: @lesson2/loops/Loopy.sol
   :start-at: function loop
   :end-before: Unroll of the loop above
   :caption: :clink:`loop function<@lesson2/loops/Loopy.sol>`

.. cvlinclude:: @lesson2/loops/Loopy.spec
   :cvlobject: loopExample loopValue
   :caption:

We ran the following three configs using the same spec:

.. tab-set::

   .. tab-item:: Loopy-pessim.conf

      .. cvlinclude:: @lesson2/loops/Loopy-pessim.conf
         :emphasize-lines: 6
         :caption:

   .. tab-item:: Loopy-vacuous.conf

      .. cvlinclude:: @lesson2/loops/Loopy-vacuous.conf
         :emphasize-lines: 6-7
         :caption:

   .. tab-item:: Loopy.conf

      .. cvlinclude:: @lesson2/loops/Loopy.conf
         :emphasize-lines: 6-7
         :caption:

#. The config :clink:`Loopy-pessim.conf<@lesson2/loops/Loopy-pessim.conf>`:

   * Does not use ``optimistic_loop``.
   * Hence the rule :cvl:`loopValue` is violated -- due to the stop condition being
     violated.
   * Report: `Loopy pessimistic report`_.

#. :clink:`Loopy-vacuous.conf<@lesson2/loops/Loopy-vacuous.conf>`:

   * Uses ``optimistic_loop`` but only 2 loop iterations.
   * The Prover fails to find an example (*is vacuous*) for :cvl:`loopExample`
     and :cvl:`loopValue` is marked as vacuous.
   * Report: `Loopy vacuity report`_.

#. :clink:`Loopy.conf<@lesson2/loops/Loopy.conf>`:

   * Uses ``optimistic_loop`` and 4 iterations.
   * The rule :cvl:`loopValue` is verified (this would also work with 3 iterations).
   * Report: `Loopy example four iterations optimistic`_.

.. warning::

   Note how critical the ``loop_iter`` is. Be aware that ``optimistic_loop``
   adds a :cvl:`require` statement that might be :term:`unsound`.

----

ERC-20 examples
---------------
* The contract :clink:`LoopyERC20<@ERC20/contracts/LoopyERC20.sol>` inherits from
  the :clink:`ERC20<@ERC20/contracts/ERC20.sol>` and adds some functions to it.
* The function we shall verify is :solidity:`multiTransferWithBug`, which transfers
  the same amount to each address in an array of recipients.

Here is the function :solidity:`multiTransferWithBug` and a version of the
function without the bug named :solidity:`multiTransfer`.

.. cvlinclude:: @ERC20/contracts/LoopyERC20.sol
   :lines: 6-38
   :caption:

* The following is a rule checking the integrity of :solidity:`multiTransferWithBug`.
* When the rule is run with ``loop_iter`` of 1, the rule is verified.
  See `Single loop iteration report`_.
* But when using ``loop_iter`` of 3, a violation is found.
  See `Three loop iterations report`_.

.. cvlinclude:: @ERC20/certora/specs/Loopy.spec
   :cvlobject: multiTransferIntegrity
   :caption: :clink:`multiTransferIntegrity <@ERC20/certora/specs/Loopy.spec>`

Here are the two config files used.

.. grid:: 2

    .. grid-item-card:: One iteration

       .. cvlinclude:: @ERC20/certora/confs/Loopy.conf
          :caption:

    .. grid-item-card:: Three iterations

       .. cvlinclude:: @ERC20/certora/confs/LoopyFixed.conf
          :caption:


.. Links
   -----

.. _Loop unrolling: https://docs.certora.com/en/latest/docs/prover/approx/loops.html

.. _Undecidable problem: https://en.wikipedia.org/wiki/Undecidable_problem

.. _Loopy pessimistic report:
   https://prover.certora.com/output/98279/b9985ac9ef42405c813a75f200af0e74?anonymousKey=4c4367c5a8e0c1c6457e438e3b76bdc1a967374c

.. _Loopy vacuity report:
   https://prover.certora.com/output/98279/7ce3c6399afd4fd2a0634694fe757a61?anonymousKey=01c944c551d13bc1eece81e74f4ecce6c097422f

.. _Loopy example four iterations optimistic:
   https://prover.certora.com/output/98279/b3480fe1af4d4791bb8f5168736242d2?anonymousKey=87d8ef48859f69fd133e54eee00c20551fbc534b

.. _Single loop iteration report:
   https://prover.certora.com/output/98279/394e141ecf4e4541b71e7da0516b4b91?anonymousKey=78440ecb2b175434b7b9f2d1a82d76c8dcf6f8e9

.. _Three loop iterations report:
   https://prover.certora.com/output/98279/be8cdc0ab8234d96bd5fde11b8af2ec1?anonymousKey=9abe0e39592513cb9c9bb57b40aa9d6365b0f069
