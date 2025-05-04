// Defines the compiler version, here any 0.8.x
pragma solidity ^0.8.0;


contract Voting {

  // An internal mapping, which is a state variable.
  // `_hasVoted[user]` is true if the user voted.
  mapping(address => bool) internal _hasVoted;

  // Public state variables automatically have external getters
  uint256 public votesInFavor;  // How many in favor
  uint256 public votesAgainst;  // How many opposed
  uint256 public totalVotes;  // Total number voted

  // Public functions have external access
  function vote(bool isInFavor) public {
    // `msg.sender` is the address of the caller
    require(!_hasVoted[msg.sender]);
    _hasVoted[msg.sender] = true;

    totalVotes += 1;
    if (isInFavor) {
      votesInFavor += 1;
    } else {
      votesAgainst += 1;
    }
  }

  // View functions may not modify state variables.
  // This function provides a public getter to `_hasVoted`.
  function hasVoted(address voter) public view returns (bool) {
    return _hasVoted[voter];
  }
}
