Glossary
========

.. glossary::

   CVL
      Certora Verification Language -- used for writing specs.

   loop unrolling
      Writing explicitely several iterations of a loop. See :ref:`loop_unrolling_example`
      and also `Loop unrolling`_ in the Documentation.

   over-approximation
      Assuming more *states* and *computation paths* than may occur in reality.
      See `overapproximation`_ in the Documentation.

   quantifier grounding
      *Quantifier grounding* is an optimization that seeks to reduce the overhead
      of using quantifiers such as :cvl:`forall`. See `Quantifier Grounding`_.

   scene
      The *scene* is the set of contract instances that the Certora Prover knows about.

   unsound
   unsoundness
      Means that rules may be verified despite a counter example existing. Usually due to
      wrong assumptions. See also `unsound in Certora Documentation`_.

   vacuous
   vacuity
      A rule is *vacuous* if it has no example nor a counter-example, see
      :doc:`lesson1/vacuity`. Loop iterations can be a source of vacuity, see
      :ref:`loop_iterations_sec`.

.. Links:
   ------

.. _unsound in Certora Documentation:
   https://docs.certora.com/en/latest/docs/user-guide/glossary.html#term-unsound

.. _Loop unrolling: https://docs.certora.com/en/latest/docs/prover/approx/loops.html

.. _Quantifier Grounding:
   https://docs.certora.com/en/latest/docs/prover/approx/grounding.html

.. _overapproximation:
   https://docs.certora.com/en/latest/docs/user-guide/glossary.html#term-overapproximation
