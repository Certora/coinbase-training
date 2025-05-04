.. index::
   single: reentrancy
   single: hook; opcode

Reentrancy vulnerability check
==============================
CVL has the ability to hook onto various EVM opcodes.
Here we provide an example using a hook onto the ``CALL`` opcode.
See `EVM opcode hooks`_ for other available opcode hooks.

Reentrancy check
----------------

Basic idea
^^^^^^^^^^

   The contract's storage *between* function calls satisfies the invariants of the spec,
   when assuming external calls do not re-enter the contract.
   
* Call the contract's expected storage state between calls a *"good"* state.
* The storage state during a function call might change to a *"bad"* state, i.e. a
  state which might not satisfy the invariants.
* An external call to a non-view function while the storage is in a *"bad"* state
  exposes the contract to exploits.
* Solution (partial): ensure such external calls are done only when the storage
  is in a good state. So for every function either:

  * all external calls are done before any storage access, or
  * external calls are executed only after all storage access.

Spec
^^^^
* The spec uses persistent ghosts, which are not affected by reverts or havocs.
* Using hooks, the spec sets these ghost flags if storage was accessed before or
  after an external call.
* The spec contains a single parametric rule, asserting there are no functions with
  storage access both before and after an external call.
* We use two special load and store hooks the hook onto *any* load and store operation.
  These are :cvl:`ALL_SLOAD` and :cvl:`ALL_SSTORE`.
  See `Hooking on all storage loads or stores`_.

.. cvlinclude:: @lesson5/pool/Reentrancy.spec
   :lines: 12-
   :caption:

Config notes
^^^^^^^^^^^^
* To use :cvl:`ALL_SLOAD` and :cvl:`ALL_SSTORE` we need to add the following line
  to the config:

  .. cvlinclude:: @lesson5/pool/Reentrancy.conf
     :start-at: prover_args
     :end-at: prover_args

* We can limit ``parametric_contracts`` to use only the current contract.


Unguarded pool example
----------------------

Pool code
^^^^^^^^^
* The :clink:`UnguardedPool<@lesson5/pool/UnguardedPool.sol>` is a liquidity pool
  contract over some underlying ERC-20 token called the *underlying asset*.
* The pool mints shares in return for depositing the underlying assets,
  and transfers an amount in the underlying asset when the user withdraws shares.
* For this example we disabled the :solidity:`nonReentrant` modifier.
* Note that apart from the reentrancy vulnerability, the pool has an additional
  vulnerability stemming from the way it calculates the conversion between amount and
  shares.

.. dropdown:: UnguardedPool code

   .. cvlinclude:: @lesson5/pool/UnguardedPool.sol
      :lines: 11-
      :emphasize-lines: 4-6
      :caption:

Config
^^^^^^
* The config used (see below) does not use any linking, as these are not needed for this
  check.
* Similarly, the config uses the :cvl:`UnguardedPool` as the only parametric contract.
* It requires additional ``prover_args``, see below.

.. cvlinclude:: @lesson5/pool/Reentrancy.conf
   :emphasize-lines: 7
   :caption: :clink:`Reentrancy config for UnguardedPool<@lesson5/pool/Reentrancy.conf>`

Report
^^^^^^
* `Reentrancy report for UnguardedPool`_.
* Only the :solidity:`deposit` function failed the report.
* The reason for the fail is that the pool mints shares *after* calling
  :solidity:`asset.transferFrom`, see below.
* A malicious asset can exploit this vulnerability (this scenario is unlikely).
 
.. cvlinclude:: @lesson5/pool/UnguardedPool.sol
   :lines: 30-42
   :emphasize-lines: 11-12
   :linenos:
   :lineno-start: 30
   :caption: :clink:`deposit<@lesson5/pool/UnguardedPool.sol>`

Exploiting the pool
^^^^^^^^^^^^^^^^^^^
* To show an exploit is possible, we write a malicious ERC-20 to serve as
  the underlying asset:
  :clink:`ExploitingAsset<@lesson5/pool/ExploitingAsset.sol>` (see below).
* The :solidity:`ExploitingAsset` front runs deposits to the pool, this is done
  in the :solidity:`tranferFrom` function.
* We write a spec instructing the Prover to find an example of a successful exploit:
  :clink:`ReentrancyExploit.spec<@lesson5/pool/ReentrancyExploit.spec>`.
* The config for this spec requires an additional parameter: ``contract_recursion_limit``,
  see :clink:`ReentrancyExploit.conf<@lesson5/pool/ReentrancyExploit.conf>`.
* The report shows an example of successfully exploiting the pool,
  see `Exploiting the pool report`_.

.. dropdown:: ExploitingAsset

   .. cvlinclude:: @lesson5/pool/ExploitingAsset.sol
      :lines: 17-
      :caption:

.. dropdown:: ReentrancyExploit.spec

   .. cvlinclude:: @lesson5/pool/ReentrancyExploit.spec
      :cvlobject: reentrancyExploitExample
      :caption:

.. dropdown:: ReentrancyExploit.spec

   .. cvlinclude:: @lesson5/pool/ReentrancyExploit.conf
      :emphasize-lines: 8-9, 13
      :caption:


.. Links
   -----

.. _EVM opcode hooks:
   https://docs.certora.com/en/latest/docs/cvl/hooks.html#evm-opcode-hooks

.. _Hooking on all storage loads or stores:
   https://docs.certora.com/en/latest/docs/cvl/hooks.html#hooking-on-all-storage-loads-or-stores

.. _Reentrancy report for UnguardedPool:
   https://prover.certora.com/output/98279/d78f79e0e296402bbcb2bdd8530c53dd?anonymousKey=a47abb4caea083949c1571fa0f64919b2fbd4100

.. _Exploiting the pool report:
   https://prover.certora.com/output/98279/cb73462ff79d44ea8c423cdb11249c11?anonymousKey=50a1321780b66d69da731c4bcd9d234b3d45dc37
