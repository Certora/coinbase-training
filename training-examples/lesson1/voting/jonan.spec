/* First example spec for Voting contract */
methods {
    function totalVotes() external returns (uint256) envfree;
    function votesAgainst() external returns (uint256) envfree;
    function votesInFavor() external returns (uint256) envfree;
    function hasVoted(address) external returns (bool) envfree;
}

/// @title Basic check for `vote` function
rule voteIntegrity(bool isInFavor) {
    uint256 votesBefore = totalVotes();

    env e;
    vote(e, isInFavor);

    uint256 votesAfter = totalVotes();
    assert (votesAfter > votesBefore, "total votes should increase");
}


rule votesIncreased(bool isInFavor) {
    mathint sumBefore = votesInFavor() + votesAgainst();

    env e;
    vote(e, isInFavor);

    mathint sumAfter = votesInFavor() + votesAgainst();
    assert (sumBefore + 1 == sumAfter, "votes increased by 1");
}


rule example(bool isInFavor) {

    env e;
    vote(e, isInFavor);

    satisfy isInFavor;
}


rule revertConditions(bool isInFavor) {

    env e;
    bool hasUserVoted = hasVoted(e.msg.sender);
    require (totalVotes() < 10 && votesInFavor() < 10 && votesAgainst() < 10);
    require (e.msg.value == 0);

    vote@withrevert(e, isInFavor);

    bool hasReverted = lastReverted;

    assert (hasUserVoted <=> hasReverted, "can't vote twice");
}
