/* Sum pattern example for ERC-20 */
methods {
    function totalSupply() external returns (uint256) envfree;
    function balanceOf(address) external returns (uint256) envfree;
}


/// @title Sum of balances ghost
persistent ghost mathint sumBalances {
    init_state axiom sumBalances == 0;
}


/// @title Update to sum of balances
hook Sstore _balances[KEY address account] uint256 newBalance (uint256 oldBalance) {
    sumBalances = sumBalances - oldBalance + newBalance;
}


invariant totalSupplyIsSumOfBalances()
    sumBalances == to_mathint(totalSupply());


invariant balanceIsBalance(address account)
    currentContract._balances[account] == balanceOf(account);


invariant balanceIsLessThanSum(address account)
    to_mathint(balanceOf(account)) <= sumBalances
    {
        preserved transfer(address recipient, uint256 amount) with (env e) {
            require sumBalances >= balanceOf(account) + balanceOf(e.msg.sender);
        }
    }


invariant balanceIsLessThanTotalSupply(address account)
    balanceOf(account) <= totalSupply();
