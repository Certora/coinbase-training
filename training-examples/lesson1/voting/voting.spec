methods {
    function totalVotes() external returns (uint256) envfree;
    function hasVoted(address) external returns (bool) envfree;
}

/// @title Calling vot increases total votes
rule votingIncreasesNumberVotes(bool isInFavor) {
    uint256 totalBefore = totalVotes();

    env e;
    vote(e, isInFavor);

    uint256 totalAfter = totalVotes();
    assert totalAfter > totalBefore, "total votes increased";
}

/// @title Can vote
rule someoneCanVote(bool isInFavor) {
    env e;
    vote(e, isInFavor);
    satisfy true;
}

/// @title Revert conditions
rule canVoteHowILike(bool isInFavor) {
    
    env e;
    vote@withrevert(e, isInFavor);
    bool isReverted = lastReverted;

    bool messageValueCond = e.msg.value > 0;
    bool alreadyVoted = hasVoted(e.msg.sender);

    assert (
        isReverted <=> (alreadyVoted || messageValueCond),
        "revert conditions"
    );
}

/// @title Example of voting against
rule canVoteAgainst() {
    env e;
    vote(e, false);
    satisfy true;
}

/// @title No double voting!
rule voteOnlyOnce(
    address voter, bool isInFavor1, bool isInFavor2
) {

    env e1;
    require e1.msg.sender == voter;
    vote(e1, isInFavor1);

    env e2;
    require e2.msg.sender == voter;
    vote@withrevert(e2, isInFavor2);

    assert lastReverted;
}
