/* Sum pattern example for `ERC-20` */
methods {
    function totalSupply() external returns(uint) envfree;
}

/// @title Sum of balances ghost
/// @notice It is better to use `mathint` - doesn't overflow or underflow
persistent ghost mathint sumOfBalances {
    // `init_state` determines the state after the constructor
    init_state axiom sumOfBalances == 0;
}


// Update the sum of balances
hook Sstore _balances[KEY address addr] uint256 newValue (uint256 oldValue) {
    // Update the sum whenever a balance changes
    sumOfBalances = sumOfBalances - oldValue + newValue;
}


/// @title `totalSupply` is the sum of all balances
invariant totalSupplyIsSumOfBalances()
    to_mathint(totalSupply()) == sumOfBalances;
