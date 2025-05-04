/*
 * Simple example rules for `ERC-20`
 */
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


/// @title An example of a bad use of `lastReverted`
rule transferRevertsWrong(address sender, address recipient, uint256 amount) {
    env e;
    require e.msg.sender == sender;

    uint256 preRecipBalance = balanceOf(recipient);

    transfer@withrevert(e, recipient, amount);

    // Calling `balanceOf` will change the value of `lastReverted`
    assert (
        balanceOf(recipient) == preRecipBalance  => lastReverted,
        "transfer must succeed if funds are sufficient"
    );
}


/// @title `transfer` must succeed if there are sufficient funds
rule transferSucceeds(address sender, address recipient, uint256 amount) {
    env e;
    require e.msg.sender == sender;

    // Avoid reverting for other reasons:
    require e.msg.value == 0;  // Understand why this is needed
    require balanceOf(recipient) + amount < max_uint; // Why is this needed
    require e.msg.sender != 0;
    require recipient != 0;

    bool success = transfer@withrevert(e, recipient, amount);
    bool isReverted = lastReverted;  // Save result in a variable

    // Calling `balanceOf` will change the value of `lastReverted`
    assert (
        balanceOf(sender) >= amount => (!isReverted && success),
        "transfer must succeed revert if funds are sufficient"
    );
}


/// @title A revert rule missing a revert condition
rule transferSucceedsMissing(address sender, address recipient, uint256 amount) {
    env e;
    require e.msg.sender == sender;

    // Avoid reverting for other reasons:
    require e.msg.sender != 0;
    require recipient != 0;

    bool success = transfer@withrevert(e, recipient, amount);
    bool isReverted = lastReverted;  // Save result in a variable

    // Calling `balanceOf` will change the value of `lastReverted`
    assert (
        balanceOf(sender) >= amount => (!isReverted && success),
        "transfer must succeed revert if funds are sufficient"
    );
}

// ---- Satisfy rules ----------------------------------------------------------

/// @title First deposit example
rule satisfyFirstDepositSucceeds(address account, uint256 amount) {
    require totalSupply() == 0;
    require amount > 0;

    env e;
    mint(e, account, amount);

    satisfy totalSupply() == amount;
}


/// @title Completely withdraw token example
rule satisfyLastWithdrawSucceeds(uint256 amount) {
    env e;

    require totalSupply() == balanceOf(e.msg.sender);
    require amount > 0;
    withdraw(e, amount);

    satisfy totalSupply() == 0;
}

// ---- Relational properties --------------------------------------------------

/// @title Sum of balances unaffected by transfer
rule sumBalancesConstant(address sender, address recipient, uint256 amount) {

    // Note we use the type `mathint` here
    mathint sumBefore = balanceOf(sender) + balanceOf(recipient);

    env e;
    require e.msg.sender == sender;
    transfer(e, recipient, amount);

    mathint sumAfter = balanceOf(sender) + balanceOf(recipient);
    assert (
        sumBefore == sumAfter,
        "Sum balances remains constant under transfer"
    );
}
