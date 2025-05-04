.. index::
   single: invariant

Invariants
==========

Introduction
------------
* Use invariants for properties about the state (storage).
* See `Invariants`_ documentation, in particular `Invariants and induction`_ section.


Ball game example
-----------------

Rules
^^^^^
* Four players: A, B, C, D.
* Players A and C pass to each other.
* Players B and D pass to each other.
* The game begins with player A holding the ball.

Code modeling the game
^^^^^^^^^^^^^^^^^^^^^^

.. literalinclude:: ../../../training-examples/lesson2/ballgame/BallGame.sol
   :language: solidity


Invariants
^^^^^^^^^^

Bad invariant
"""""""""""""
.. cvlinclude:: ../../../training-examples/lesson2/ballgame/BallGame.spec
   :cvlobject: neverWillDGetTheBall

Fixed invariant
"""""""""""""""
.. cvlinclude:: ../../../training-examples/lesson2/ballgame/BallGame.spec
   :cvlobject: neverWillDGetTheBall_fixed

* `Ball game report`_

.. Links
   -----

.. _Invariants: https://docs.certora.com/en/latest/docs/cvl/invariants.html

.. _Invariants and induction:
   https://docs.certora.com/en/latest/docs/cvl/invariants.html#invariants-and-induction

.. _Ball game report:
   https://prover.certora.com/output/98279/4b722520a7274cc4afa80c65ecc9c512?anonymousKey=3a829cb6793541f71202292e55bdabde4ddc1847
