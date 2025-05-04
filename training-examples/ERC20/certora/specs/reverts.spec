methods {
    function balanceOf(address) external returns (uint256) envfree;
}


rule tranferRevertCondition(address sender, address recipient, uint256 amount) {
    env e;
    require e.msg.sender == sender;
    require sender != recipient;
    require amount > 0;
    uint256 preRecipBalance = balanceOf(recipient);

    transfer@withrevert(e, recipient, amount);
    bool hasReverted = lastReverted;

    assert(
        balanceOf(recipient) == preRecipBalance => hasReverted
    );
}


rule transferRevertsOn(address sender, address recipient, uint256 amount) {
    env e;
    require e.msg.sender == sender;
    require sender != 0;
    require recipient != 0;
    require e.msg.value == 0;

    uint256 balanceBefore = balanceOf(sender);

    transfer@withrevert(e, recipient, amount);
    bool hasReverted = lastReverted;

    assert (
        balanceBefore >= amount => !hasReverted
    );
}
