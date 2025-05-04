methods {
    function totalSupply() external returns (uint256) envfree;
    function balanceOf(address) external returns (uint256) envfree;
}

/// @title An example of first minting
rule firstDepositIsPossible(address account, uint256 amount) {
    uint256 totalSupplyBefore = totalSupply();

    env e;
    mint(e, account, amount);

    uint256 totalSupplyAfter = totalSupply();
    satisfy totalSupplyBefore == 0 && totalSupplyAfter == amount;
}


/// @title Last withdraw is possible
rule lastWithdrawExample(uint256 amount) {
    require amount > 0;
    env e;
    withdraw(e, amount);

    satisfy totalSupply() == 0;
}


/// @title Total supply unaffected by transfer
rule totalSupplyUnaffected(address sender, address recipient, uint amount) {

    uint256 totalBefore = totalSupply();
    mathint sumBefore = balanceOf(sender) + balanceOf(recipient);

    env e;
    require e.msg.sender == sender;
    transfer(e, recipient, amount);
    
    uint256 totalAfter = totalSupply();
    mathint sumAfter = balanceOf(sender) + balanceOf(recipient);

    assert (
        totalBefore == totalAfter && sumBefore == sumAfter,
        "Sum unaffected by transfer"
    );
}
