/* Examples of vacuous rules */
methods
{
    function totalVotes() external returns (uint256) envfree;
    function votesInFavor() external returns (uint256) envfree;
    function votesAgainst() external returns (uint256) envfree;
    function hasVoted(address voter) external returns (bool) envfree;
}

/// @title Obviously vacuous rule
rule obviouslyVacuous(bool isInFavor) {
    require isInFavor;
    require !isInFavor;

    uint256 inFavorBefore = votesInFavor();
    env e;
    vote(e, isInFavor);
    uint256 inFavorAfter = votesInFavor();

    assert false;
}

/// @title Require that will certainly revert
rule revertingRequire(bool isInFavor) {

    env e;
    require hasVoted(e.msg.sender);
    vote(e, isInFavor);

    satisfy true;
}
