Preserved blocks and more
=========================

.. index::
   single: preserved

Preserved blocks
----------------
* A way to handle particular functions differently within invariants, or to relate to
  the :cvl:`env`.
* See `Preserved blocks (from Documentation)`_ and also
  `Preserved blocks (from Tutorials)`_.

Example
^^^^^^^
.. cvlinclude:: @ERC20/certora/specs/Invariants.spec
   :cvlobject: balanceAtMostTotalSupply
   :caption: :clink:`Preserved block example<@ERC20/certora/specs/Invariants.spec>`

.. warning::

   Using :cvl:`require` statements can be :term:`unsound`. In particular this example is
   **bad** since we're assuming *more* than what we're trying to prove.


.. index::
   single: requireInvariant

requireInvariant
----------------
* Requires the invariant (with the given parameters) holds.
* E.g. :cvl:`requireInvariant balanceAtMostTotalSupply(account);`.
* This is *sound* as long as we verify the invariant itself.
* It is also *sound* to use inside :cvl:`preserved` blocks, even of the invariant itself,
  see `Invariants and induction`_.
* Equivalent to a require statement using the invariant's condition.

In a nutshell, the reason :cvl:`requireInvariant` is sound inside :cvl:`preserved` is
that we assume the invariant in the *pre-state*. In other words, we make it part of
the induction assumption.


.. _funds-managers:

Funds managers example
----------------------

Description
^^^^^^^^^^^
The purpose of the :solidity:`IManager` is to keep track of funds' manager, and to
ensure each fund has a unique manager. Changing manager is a two step process:

#. The current manager must set their successor as the *pending* manager using
   :solidity:`setPendingManager`.
#. The pending manager must *claim* management using :solidity:`claimManagement`.

.. dropdown:: :solidity:`interface IManager`

   .. cvlinclude:: @lesson2/manager/IManager.sol
      :lines: 11-
      :caption:

Data structures
^^^^^^^^^^^^^^^
The main data structure is a mapping from fund-id to a struct describing the fund and
its management:

.. graphviz::
   :align: center
   :class: only-dark

   digraph {
       graph [
           bgcolor="#1a1a1a" color=gold fontcolor=bisque labelloc=t
           nodesep=0.25 rankdir=LR ranksep=0.5 margin=0
       ]
       node [shape=Mrecord color=gold fontcolor=bisque fontname="DejaVu Sans Mono"]
       edge [color=gold fontcolor=bisque fontname="DejaVu Sans Mono"]

       ID [label="uint256 fundid"]
       ST [
           label="struct ManagedFund | address currentManager\l |
           address pendingManager\l | uint256 amount\l"
       ]
       ID -> ST [label=mapping]
   }

.. graphviz::
   :align: center
   :class: only-light

   digraph {
       graph [
           bgcolor=gray90 color=goldenrod fontcolor=gray9 labelloc=t
           nodesep=0.25 rankdir=LR ranksep=0.5 margin=0
       ]
       node [shape=Mrecord color=goldenrod fontcolor=gray9 fontname="DejaVu Sans Mono"]
       edge [color=goldenrod fontcolor=gray9 fontname="DejaVu Sans Mono"]

       ID [label="uint256 fundid"]
       ST [
           label="struct ManagedFund | address currentManager\l |
           address pendingManager\l | uint256 amount\l"
       ]
       ID -> ST [label=mapping]
   }

----

Changing manager example
^^^^^^^^^^^^^^^^^^^^^^^^
.. graphviz::
   :align: center
   :class: only-dark

   digraph {
       graph [
           bgcolor="#1a1a1a" color=gold fontcolor=bisque labelloc=t
           nodesep=0.25 rankdir=LR ranksep=0.5 margin=0
       ]
       node [shape=Mrecord color=gold fontcolor=bisque fontname="DejaVu Sans Mono"]
       edge [color=cyan fontcolor=bisque fontname="DejaVu Sans Mono"]

       PRE [
           label="ManagedFund X | currentManager = Alice\l |
           pendingManager = 0\l | amount = Y\l"
       ]
       PEND [
           label="ManagedFund X | currentManager = Alice\l |
           pendingManager = Bob\l | amount = Y\l"
       ]
       CLA [
           label="ManagedFund X | currentManager = Bob\l |
           pendingManager = 0\l | amount = Y\l"
       ]
      
       PRE -> PEND [label="setPendingManager(X, Bob)"]
       PEND -> CLA [label="claimManagement(X)"]
   }

.. graphviz::
   :align: center
   :class: only-light

   digraph {
       graph [
           bgcolor=gray90 color=goldenrod fontcolor=gray9 labelloc=t
           nodesep=0.25 rankdir=LR ranksep=0.5 margin=0
       ]
       node [shape=Mrecord color=goldenrod fontcolor=gray9 fontname="DejaVu Sans Mono"]
       edge [color=blue fontcolor=gray9 fontname="DejaVu Sans Mono"]

       PRE [
           label="ManagedFund X | currentManager = Alice\l |
           pendingManager = 0\l | amount = Y\l"
       ]
       PEND [
           label="ManagedFund X | currentManager = Alice\l |
           pendingManager = Bob\l | amount = Y\l"
       ]
       CLA [
           label="ManagedFund X | currentManager = Bob\l |
           pendingManager = 0\l | amount = Y\l"
       ]
      
       PRE -> PEND [label="setPendingManager(X, Bob)"]
       PEND -> CLA [label="claimManagement(X)"]
   }

----

The goal
^^^^^^^^
The goal is to prove the following:

   The manager of a *created fund* is unique (i.e. does not manage another fund).

Where a *created fund* is a fund whose manager is not :solidity:`address(0)`.

----

Initial spec
^^^^^^^^^^^^
.. cvlinclude:: @lesson2/manager/Manager.spec
   :cvlobject: isCreated managerIsActive uniqueManager

* Report: `initial Manager spec report`_.
* We get spurious counter-examples:

  #. The invariant :cvl:`managerIsActive` fails on the :cvl:`claimManagement` function.
     The counter-example stems from the fact that two *different* funds have the
     *same* manager in the initial state (a non-unique manager contradicting
     :cvl:`uniqueManager` invariant).
  #. The invariant :cvl:`uniqueManager` fails on :cvl:`claimManagement`
     and :cvl:`createFund` functions.
     Both counter-examples stem from the initial state having a fund whose manager is
     not marked as an active manager of a fund, thereby contradicting the
     :cvl:`managerIsActive` invariant.

* The solution is for the invariants to require each other using preserved blocks and
  :cvl:`requireInvariant` statements.

----

Solution - using preserved blocks
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. dropdown:: Full solution -- do not peek!

  .. cvlinclude:: @lesson2/manager/Manager-solution.spec
     :cvlobject: isCreated managerIsActive uniqueManager

  * Report: `full solution report`_.


.. Links
   -----

.. _Preserved blocks (from Documentation):
   https://docs.certora.com/en/latest/docs/cvl/invariants.html#preserved-blocks

.. _Preserved blocks (from Tutorials):
   https://docs.certora.com/projects/tutorials/en/latest/lesson4_invariants/invariants/preserved.html

.. _Invariants and induction:
   https://docs.certora.com/en/latest/docs/cvl/invariants.html#invariants-and-induction

.. _initial Manager spec report:
   https://prover.certora.com/output/98279/824cf93ee5104cf6913a2d868d586a5e?anonymousKey=347080c41762a10fe41328cf53b4c5971ab4f63a

.. _full solution report:
   https://prover.certora.com/output/98279/ac7d4a6773a448ddbc20e4289993f848?anonymousKey=eac065452ab50c6563e23f0ae567f523e0474152
