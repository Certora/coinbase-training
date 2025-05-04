// Testing the `multiTransferWithBug` function of `LoopyERC20`

methods {
    function balanceOf(address) external returns(uint) envfree;
}


/// @title Verify the integrity of `multiTransferWithBug`
rule multiTransferIntegrity(address sender, address[] recipients, uint256 amount) {

    uint256 balanceBefore = balanceOf(sender);

    env e;
    require e.msg.sender == sender;
    multiTransferWithBug(e, recipients, amount);

    uint256 balanceAfter = balanceOf(sender);

    assert balanceBefore - balanceAfter == amount * recipients.length;
}
