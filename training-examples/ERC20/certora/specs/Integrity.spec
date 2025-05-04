methods {
    function balanceOf(address) external returns(uint) envfree;
    function allowance(address,address) external returns(uint) envfree;
}


/// @title Integrity of `transferFrom`
rule integrityOfTransferFrom(address sender, address recipient, uint256 amount) {
    env e;
    uint256 allowanceBefore = allowance(sender, e.msg.sender);
    uint256 senderBalanceBefore = balanceOf(sender);
    uint256 recipBalanceBefore = balanceOf(recipient);

    transferFrom(e, sender, recipient, amount);

    uint256 allowanceAfter = allowance(sender, e.msg.sender);
    uint256 senderBalanceAfter = balanceOf(sender);
    uint256 recipBalanceAfter = balanceOf(recipient);

    assert (
        allowanceBefore > allowanceAfter,
        "Allowance must decrease after using it to pay on behalf of someone else"
    );
    assert (
        senderBalanceBefore == senderBalanceAfter + amount,
        "Sender's balance decreases by amount"
    );
    assert (
        recipBalanceBefore + amount == recipBalanceAfter,
        "Recipient's balance increases by amount"
    );

}

