methods {
    function balanceA() external returns (uint256) envfree;
    function balanceB() external returns (uint256) envfree;

    // Dummy tokens
    function _.balanceOf(address) external => DISPATCHER(true);
    function _.transferFrom(
        address, address, uint256
    ) external => DISPATCHER(true);
    function _.transfer(
        address, uint256
    ) external => DISPATCHER(true);
}

/// @title Integrity of transfer from A to B
rule transferIntegrity(address sender, uint256 amount) {
    uint256 preA = balanceA();
    uint256 preB = balanceB();

    env e;
    require e.msg.sender == sender;
    require sender != currentContract;
    transferAtoB(e, amount);

    uint256 postA = balanceA();
    uint256 postB = balanceB();
    
    assert postA - preA == to_mathint(amount);
    assert preB - postB == to_mathint(amount);
}
