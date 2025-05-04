/*
 * Examples of parametric rules in ERC20
 */

methods {
    function balanceOf(address) external returns(uint) envfree;
    function allowance(address, address) external returns(uint) envfree;
}


/// @title Only account holder can increase allowance
rule allowanceIncreaseAlwaysCalledByHolder(
    method f, address holder, address spender
) {
    uint256 preAllowance = allowance(holder, spender);

    env e;
    calldataarg args;
    f(e, args);

    uint256 postAllowance = allowance(holder, spender);

    assert (
        postAllowance > preAllowance => e.msg.sender == holder,
        "Only account holder may increase allowance"
    );
}


/// @title Conditions for increasing allowance
rule allowanceIncreaseConditions(
    method f, address holder, address spender
) {
    uint256 preAllowance = allowance(holder, spender);

    env e;
    calldataarg args;
    f(e, args);

    uint256 postAllowance = allowance(holder, spender);

    assert (
        postAllowance > preAllowance => (
            e.msg.sender == holder &&
            (
                f.selector == sig:approve(address, uint256).selector ||
                f.selector == sig:increaseAllowance(address, uint256).selector
            )
        ),
        "Only account holder may increase allowance using approve or increaseAllowance"
    );
}


/// @title Bad parametric rule - would have failed as an invariant
rule balanceOfZeroAlwaysPositive(method f) {
    require balanceOf(0) > 0;

    env e;
    calldataarg args;
    f(e, args);

    assert balanceOf(0) > 0;
}
