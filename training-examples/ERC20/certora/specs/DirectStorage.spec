/* Direct storage example rule for `ERC-20` */
methods {
    function balanceOf(address) external returns(uint) envfree;
    function allowance(address,address) external returns(uint) envfree;
    function totalSupply() external returns(uint) envfree;
}

// ---- Revert conditions ------------------------------------------------------

/// @title `transfer` reverts on insufficient funds
rule transferReverts(address sender, address recipient, uint256 amount) {
    env e;
    require e.msg.sender == sender;

    uint256 preBalance = balanceOf(sender);

    transfer@withrevert(e, recipient, amount);
    bool isReverted = lastReverted;  // Save result in a variable

    assert (
        preBalance < amount => isReverted,
        "transfer must revert if funds are insufficient"
    );
}
