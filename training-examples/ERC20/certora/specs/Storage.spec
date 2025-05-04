/* Storage examples for `ERC-20` */


/// @title Direct storage access example - only holder can increase allowance
rule directStorageAccess(address holder, address spender, method f) {

    uint256 allowanceBefore = currentContract._allowances[holder][spender];

    env e;
    calldataarg args;
    f(e, args);

    uint256 allowanceAfter = currentContract._allowances[holder][spender];

    assert (
        allowanceAfter > allowanceBefore => e.msg.sender == holder,
        "Only holder can increase allowance"
    );
}


/// @title Last storage example - transfer via intermediary
rule lastStorageUse(
    address sender,
    address recipient,
    address intermediary,
    uint256 amount
) {
    // Saving initial storage state
    storage init = lastStorage;

    // Transfer via intermediary
    env e1;
    require e1.msg.sender == sender;
    transfer(e1, intermediary, amount);

    env e2;
    require e2.msg.sender == intermediary;
    transfer(e2, recipient, amount);

    // Save current state
    storage viaIntermediary = lastStorage;

    // Transfer directly, using initial storage
    env e3;
    require e3.msg.sender == sender;
    transfer(e3, recipient, amount) at init;

    storage directTransfer = lastStorage;

    assert (
        viaIntermediary == directTransfer,
        "Transfer via intermediary is the same as direct transfer"
    );
}
