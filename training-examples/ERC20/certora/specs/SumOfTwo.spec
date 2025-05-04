/* Sum of two balances spec */
methods {
    function totalSupply() external returns(uint) envfree;
    function balanceOf(address) external returns(uint) envfree;
}

// ---- Sum of balances ghost --------------------------------------------------

/// @title Sum of balances ghost
persistent ghost mathint sumOfBalances {
    // `init_state` determines the state after the constructor
    init_state axiom sumOfBalances == 0;
}


hook Sstore _balances[KEY address addr] uint256 newValue (uint256 oldValue) {
    // Update the sum whenever a balance changes
    sumOfBalances = sumOfBalances - oldValue + newValue;
}


/// @title `totalSupply` is the sum of all balances
invariant totalSupplyIsSumOfBalances()
    to_mathint(totalSupply()) == sumOfBalances;

// ---- Sum of two balances ----------------------------------------------------

/// @title Sum of two balances is at most total supply
invariant sumOfTwo(address user1, address user2)
    user1 != user2 => balanceOf(user1) + balanceOf(user2) <= sumOfBalances
    {
        preserved {
            requireInvariant totalSupplyIsSumOfBalances();
        }
    }
    

/// @title Sum of two balances is at most total supply - using preserved blocks
invariant sumOfTwoPreserveds(address user1, address user2)
    user1 != user2 => balanceOf(user1) + balanceOf(user2) <= sumOfBalances
    {
        preserved {
            requireInvariant totalSupplyIsSumOfBalances();
        }
        preserved burn(address user3, uint256 amount) with (env e) {
            requireInvariant totalSupplyIsSumOfBalances();
            requireInvariant sumOfTwoPreserveds(user1, user3);
            requireInvariant sumOfTwoPreserveds(user2, user3);
        }
        preserved withdraw(uint256 amount) with (env e) {
            requireInvariant totalSupplyIsSumOfBalances();
            requireInvariant sumOfTwoPreserveds(user1, e.msg.sender);
            requireInvariant sumOfTwoPreserveds(user2, e.msg.sender);
        }
        preserved transfer(address recipient, uint256 amount) with (env e) {
            requireInvariant totalSupplyIsSumOfBalances();
            requireInvariant sumOfTwoPreserveds(user1, recipient);
            requireInvariant sumOfTwoPreserveds(user2, recipient);
            requireInvariant sumOfTwoPreserveds(user1, e.msg.sender);
            requireInvariant sumOfTwoPreserveds(user2, e.msg.sender);
        }
        preserved transferFrom(
            address sender,
            address recipient,
            uint256 amount
        ) with (env e) {
            requireInvariant totalSupplyIsSumOfBalances();
            requireInvariant sumOfTwoPreserveds(user1, recipient);
            requireInvariant sumOfTwoPreserveds(user2, recipient);
            requireInvariant sumOfTwoPreserveds(user1, sender);
            requireInvariant sumOfTwoPreserveds(user2, sender);
        }
    }
