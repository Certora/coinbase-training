methods {
    function allowance(address, address) external returns(uint) envfree;
    function balanceOf(address) external returns(uint) envfree;
    function totalSupply() external returns(uint) envfree;
}

/// @title The balance of any account is at most total supply
invariant balanceAtMostTotalSupply(address anyone)
    balancEOf(anyone) <= totalSupply();
