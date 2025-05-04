.. index::
   single: ERC20
   single: token; ERC20
   single: contract; ERC20

ERC-20 Token contract
=====================
This *optional* section presents an ERC-20 token.

* The contract we will use is :clink:`ERC20.sol<@ERC20/contracts/ERC20.sol>`.
* The interfaces are
   * :clink:`IERC20.sol<@ERC20/contracts/IERC20.sol>`
   * :clink:`IERC20Metadata.sol<@ERC20/contracts/IERC20Metadata.sol>`


ERC-20 Glossary
---------------

.. glossary::

   EIP
      Ethereum Improvement Proposal (like PEP in Python).

   ERC
      Ethereum Request for Comment (an :term:`EIP` for standards).

   ERC-20
      The standard for a :term:`token` (currencies or coins) on the Ethereum blockchain.
      See `ERC-20`_ for an explanation, see `EIP-20`_ for the details of the standard.

   token
      A coin, currency or any sort of score on the Ethereum blockchain.


Inheritance diagram
-------------------

.. graphviz::
   :align: center
   :class: only-dark

   digraph {
       graph [
           label="ERC-20 inheritance diagram"
           bgcolor="#1a1a1a" color=gold fontcolor=bisque labelloc=t layout=dot margin=0
           nodesep=0.25 rankdir=BT ranksep=0.5
       ]

       ERC20 [
           label="{ERC20 | ~onlyOwner\l | increaseAllowance\l | decreaseAllowance\l | 
           _transfer\l | _approve\l | deposit\l | withdraw\l }"
           color=gold fillcolor=gray10 fontcolor=bisque fontname="DejaVu Sans Mono" 
           fontsize=8 shape=Mrecord style="" tooltip="ERC20.sol"
       ]
       IERC20 [
           label="{IERC20 | totalSupply\l | balanceOf\l | transfer\l | allowance\l |
           approve\l | transferFrom\l | mint\l | burn\l}"
           color=greenyellow fillcolor=gray10 fontcolor=bisque
           fontname="DejaVu Sans Mono" fontsize=8 shape=Mrecord style=""
           tooltip="IERC20.sol"
       ]
       IERC20Metadata [
           label="{IERC20Metadata | name\l | symbol\l | decimals\l}"
           color=greenyellow fillcolor=gray10 fontcolor=bisque
           fontname="DejaVu Sans Mono" fontsize=8 shape=Mrecord style=""
           tooltip="IERC20Metadata.sol"
       ]

       IERC20Metadata -> IERC20 [
           arrowhead=normal color=gold fontcolor=bisque fontname="DejaVu Sans Mono"
           fontsize=8 style=solid
       ]
       ERC20 -> IERC20Metadata [
           arrowhead=normal color=gold fontcolor=bisque fontname="DejaVu Sans Mono"
           fontsize=8 style=solid
       ]

       subgraph cluster_legend {
           graph [color=gray fontsize=10 label=Legend labelloc=b margin=8]
           Contract [label="{Contract | ~ modifier}"
               color=gold fillcolor=gray10 fontcolor=bisque fontname="DejaVu Sans Mono"
               fontsize=8 shape=Mrecord style=""
           ]
           Interface [
               color=greenyellow fillcolor=gray10 fontcolor=bisque
               fontname="DejaVu Sans Mono" fontsize=8 shape=Mrecord style=""
           ]
           A [style=invis]
           B [style=invis]
           A -> B [
               label=inheritance arrowhead=normal color=gold fontcolor=bisque
               fontname="DejaVu Sans Mono" fontsize=8 style=solid
           ]
       { rank=source; Contract; Interface; A;}
       }
   }

.. graphviz::
   :align: center
   :class: only-light

   digraph {
       graph [
           label="ERC-20 inheritance diagram"
           bgcolor=gray90 color=goldenrod fontcolor=gray9 labelloc=t layout=dot margin=0
           nodesep=0.25 rankdir=BT ranksep=0.5
       ]

       ERC20 [
           label="{ERC20 | ~onlyOwner\l | increaseAllowance\l | decreaseAllowance\l | 
           _transfer\l | _approve\l | deposit\l | withdraw\l }"
           color=goldenrod fontcolor=gray9 fontname="DejaVu Sans Mono" 
           fontsize=8 shape=Mrecord style="" tooltip="ERC20.sol"
       ]
       IERC20 [
           label="{IERC20 | totalSupply\l | balanceOf\l | transfer\l | allowance\l |
           approve\l | transferFrom\l | mint\l | burn\l}"
           color=olivedrab fontcolor=gray9
           fontname="DejaVu Sans Mono" fontsize=8 shape=Mrecord style=""
           tooltip="IERC20.sol"
       ]
       IERC20Metadata [
           label="{IERC20Metadata | name\l | symbol\l | decimals\l}"
           color=olivedrab fontcolor=gray9
           fontname="DejaVu Sans Mono" fontsize=8 shape=Mrecord style=""
           tooltip="IERC20Metadata.sol"
       ]

       IERC20Metadata -> IERC20 [
           arrowhead=normal color=orange fontcolor=gray9 fontname="DejaVu Sans Mono"
           fontsize=8 style=solid
       ]
       ERC20 -> IERC20Metadata [
           arrowhead=normal color=orange fontcolor=gray9 fontname="DejaVu Sans Mono"
           fontsize=8 style=solid
       ]

       subgraph cluster_legend {
           graph [color=gray fontsize=10 label=Legend labelloc=b margin=8]
           Contract [
               label="{Contract | ~ modifier}"
               color=goldenrod fontcolor=gray9 fontname="DejaVu Sans Mono" 
               fontsize=8 shape=Mrecord style=""
           ]
           Interface [
               color=olivedrab fontcolor=gray9
               fontname="DejaVu Sans Mono" fontsize=8 shape=Mrecord style=""
           ]
           A [style=invis]
           B [style=invis]
           A -> B [
               label=inheritance
               arrowhead=normal color=orange fontcolor=gray9 fontname="DejaVu Sans Mono"
               fontname="DejaVu Sans Mono" fontsize=8 style=solid
           ]
       { rank=source; Contract; Interface; A;}
       }
   }

Data structures
---------------

.. cvlinclude:: @ERC20/contracts/ERC20.sol
   :lines: 36-42

``_balances``
   The balance of each account.

``_allowances``
  :solidity:`_allowances[holder][spender]` -- how much of *holder's* balance is the
  *spender* allowed to spend.

``_totalSuplly``
   The sum total of all balances.

``_owner``
   The *owner's* address -- has certain privileges when calling functions.

Functions
---------

Getters
^^^^^^^

.. cvlinclude:: @ERC20/contracts/ERC20.sol
   :lines: 89

.. cvlinclude:: @ERC20/contracts/ERC20.sol
   :lines: 94-99

.. cvlinclude:: @ERC20/contracts/ERC20.sol
   :lines: 123-128

Transfer
^^^^^^^^

.. cvlinclude:: @ERC20/contracts/ERC20.sol
   :lines: 112-116

.. cvlinclude:: @ERC20/contracts/ERC20.sol
   :lines: 163-167

Allowance
^^^^^^^^^

.. cvlinclude:: @ERC20/contracts/ERC20.sol
   :lines: 140-144

.. cvlinclude:: @ERC20/contracts/ERC20.sol
   :lines: 194-197

.. cvlinclude:: @ERC20/contracts/ERC20.sol
   :lines: 221-224

Only owner
^^^^^^^^^^

.. cvlinclude:: @ERC20/contracts/ERC20.sol
   :lines: 282, 301


.. Links
   -----

.. _ERC-20: https://ethereum.org/en/developers/docs/standards/tokens/erc-20/
.. _EIP-20: https://eips.ethereum.org/EIPS/eip-20
.. _NatSpec Format: https://solidity-fr.readthedocs.io/fr/latest/natspec-format.html
