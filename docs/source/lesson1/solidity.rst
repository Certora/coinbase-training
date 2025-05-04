.. index::
   single: solidity

Introduction to Solidity
========================

   A statically-typed curly-braces programming language designed for developing smart
   contracts that run on Ethereum.


Familiar elements
-----------------

.. index::
   single: contract
   single: constructor
   single: uint
   single: type; uint
   single: mapping
   single: public
   single: private

.. list-table:: Solidity elements
   :header-rows: 1

   * - Element
     - Description

   * - :solidity:`contract`
     - similar to a ``class`` in other languages

   * - :solidity:`constructor`
     - the constructor function of a contract

   * - :solidity:`uint`, :solidity:`uint256`
     - unsigned integer (256 bit)

   * - :solidity:`uint128`
     -
   
   * - :solidity:`mapping`
     - a mapping type, like ``dict`` in Python

   * - :solidity:`public`, :solidity:`private`
     - functions and state variables `Visibility modifiers`_

   * - :solidity:`function`
     - function definition (within a :solidity:`contract`)


Strange elements
----------------

.. index::
   single: msg.sender
   single: address
   single: block.timestamp
   single: view
   single: pure
   single: require

.. list-table:: Solidity elements
   :header-rows: 1

   * - Element
     - Description

   * - :solidity:`address`
     - a 20 byte value identifying an Ethereum address -- a user or a *deployed*
       contract (an "instance"), see `address`_

   * - :solidity:`view`
     - a view function can not change any state variables

   * - :solidity:`pure`
     - a pure function can not change *nor read* any state variables

   * - :solidity:`msg.sender`
     - the :solidity:`address` of the contract that called the current function,
       see `Block and transaction properties`_

   * - :solidity:`block.timestamp`
     - a :solidity:`uint`, the Unix timestamp of the current block

   * - :solidity:`pragma solidity`
     - declares the Solidity compiler version, see `Version pragma`_

   * - :solidity:`require`
     - *reverts* if the condition does not hold


.. _simple_voting_contract_example:

Simple voting contract example
------------------------------

.. cvlinclude:: @lesson1/voting/Voting.sol
   :caption:

Notes
^^^^^

* In :solidity:`vote` the voter is :solidity:`msg.sender`
* If the voter already voted, the function *reverts*


.. Links
   -----

.. _Visibility modifiers:
   https://docs.soliditylang.org/en/v0.8.24/contracts.html#visibility-and-getters

.. _Version pragma:
   https://docs.soliditylang.org/en/v0.8.24/layout-of-source-files.html#version-pragma

.. _address: https://docs.soliditylang.org/en/v0.8.24/types.html#address

.. _Block and transaction properties:
   https://docs.soliditylang.org/en/v0.8.24/cheatsheet.html#block-and-transaction-properties
