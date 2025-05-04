/* Voting contract - invariants and parametric rules */
methods
{
    function totalVotes() external returns (uint256) envfree;
    function votesInFavor() external returns (uint256) envfree;
    function votesAgainst() external returns (uint256) envfree;
    function hasVoted(address voter) external returns (bool) envfree;
}


/// @title Sum results is total votes
invariant sumResultsEqualsTotalVotes()
    votesInFavor() + votesAgainst() == to_mathint(totalVotes());


// Correct translation of the invariant to a rule (only the induction step)
rule sumResultsEqualsTotalVotesAsRule(method f) {
    // Precondition
    require votesInFavor() + votesAgainst() == to_mathint(totalVotes());

    env e;
    calldataarg args;
    f(e, args);
    
    assert (
        votesInFavor() + votesAgainst() == to_mathint(totalVotes()),
        "Sum of votes should equal total votes"
    );
}


// Wrong translation of the invariant into a rule
rule sumResultsEqualsTotalVotesWrong() {
    assert (
        votesInFavor() + votesAgainst() == to_mathint(totalVotes()),
        "Sum of votes should equal total votes"
    );
}
