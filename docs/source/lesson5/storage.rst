.. index::
   single: storage

Storage in CVL
==============

.. index::
   single: storage; direct access

Direct storage access
---------------------

* CVL allows to directly access storage elements from the spec, including internal ones.
* This should be used prudently, as storage structure is usually an implementation
  detail and it is better for the spec not rely on implementation details.

Syntax
^^^^^^
* :cvl:`currentContract._storageVaribale`
* Direct storage access is also available to contracts declared with a :cvl:`using`
  statement. For example:

  .. code-block:: cvl

     using ERC20 as _ERC20;
     ...
     require _ERC20._balances[user] == 0;

Example
^^^^^^^
* Report: `Storage spec report`_.

.. cvlinclude:: @ERC20/certora/specs/Storage.spec
   :cvlobject: directStorageAccess
   :emphasize-lines: 4, 10
   :caption: :clink:`directStorageAccess<@ERC20/certora/specs/Storage.spec>`


.. index::
   single: lastStorage
   single: storage; lastStorage

Last storage
------------
* CVL allows saving storage states, reusing them and comparing them.
* In particular, it is possible to call solidity functions using a specified
  storage state.
* This is handy for comparing different operations that should result in the same
  outcome.

Syntax
^^^^^^
* The type is :cvl:`storage`.
* CVL has a :cvl:`storage` variable which holds the last storage state called
  :cvl:`lastStorage`.
* To run a function at a given storage state use :cvl:`f(e, args) at someStorage;`.

Example
^^^^^^^
* Using :cvl:`lastStorage` we check that in an ERC-20 contract, transferring an amount
  via an intermediary is the same as transferring directly to the final recipient.
  See the rule :cvl:`lastStorageUse` from
  :clink:`Storage.spec<@ERC20/certora/specs/Storage.spec>` (shown below).
* Report: `Storage spec report`_.

.. cvlinclude:: @ERC20/certora/specs/Storage.spec
   :cvlobject: lastStorageUse
   :emphasize-lines: 9, 21, 26
   :caption: :clink:`Storage.spec<@ERC20/certora/specs/Storage.spec>`


.. Links
   -----

.. _Storage spec report:
   https://prover.certora.com/output/98279/06d756fbabf94afba8c90dc150225ab5?anonymousKey=b57431e490f88cc7e06b48080ac0a93ded54c9a3
