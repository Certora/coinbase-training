/* A basic ghost example for the `Voting` contract. */
methods {
    function totalVotes() external returns (uint256) envfree;
}

ghost bool someoneVoted;

hook Sstore _hasVoted[KEY address voter] bool newVal (bool oldVal) {
    someoneVoted = true;
}

/// @title If someone voted, then the vote function was called and total votes increased
rule someoneVotesUsingVote(method f) {
    // Like storage, ghost values are arbitrary at the start of a rule.
    require !someoneVoted;
    uint256 preTotal = totalVotes();

    env e;
    calldataarg args;
    f(e, args);

    uint256 postTotal = totalVotes();

    assert someoneVoted => (
        postTotal > preTotal &&
        f.selector == sig:vote(bool).selector
    );
}
