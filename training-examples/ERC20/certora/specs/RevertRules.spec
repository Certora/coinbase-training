/*
 * Simple example rules for `ERC-20`
 */
methods {
    function balanceOf(address) external returns(uint) envfree;
    function allowance(address,address) external returns(uint) envfree;
    function totalSupply() external returns(uint) envfree;
}

// ---- Revert conditions ------------------------------------------------------

rule transferMathint(address sender, address recipient, uint256 amount) {
    env e;
    require e.msg.sender == sender;

    uint256 preBalance = balanceOf(sender);

    transfer(e, recipient, amount);

    assert(
        sender != recipient => (
            to_mathint(balanceOf(sender)) == preBalance - amount
        )
    );
    assert(
        sender == recipient => (balanceOf(sender) == preBalance)
    );
}


rule transferRequire(address sender, address recipient, uint256 amount) {
    env e;
    require e.msg.sender == sender;

    uint256 preBalance = balanceOf(sender);

    transfer(e, recipient, amount);

    assert(
        sender != recipient => (
            balanceOf(sender) == require_uint256(preBalance - amount)
        )
    );
    assert(
        sender == recipient => (balanceOf(sender) == preBalance)
    );
}


rule transferAssert(address sender, address recipient, uint256 amount) {
    env e;
    require e.msg.sender == sender;

    uint256 preBalance = balanceOf(sender);

    transfer(e, recipient, amount);

    assert(
        sender != recipient => (
            balanceOf(sender) == assert_uint256(preBalance - amount)
        )
    );
    assert(
        sender == recipient => (balanceOf(sender) == preBalance)
    );
}
