methods {
    function balanceOf(address) external returns (uint256) envfree;
}


/// @title Address zero always has balance zero
invariant zeroHasBalanceZero()
    balanceOf(0) == 0;


/// @title Zero has positive balance
rule zeroHasPositiveBalance(method f) {
    require balanceOf(0) > 0;

    env e;
    calldataarg args;
    f(e, args);

    assert balanceOf(0) > 0;
}
