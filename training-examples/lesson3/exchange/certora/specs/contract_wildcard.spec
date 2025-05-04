/* Example that wildcard contract takes precedence over wildcard function */

using ERC20DummyA as _ERC20DummyA;
using ERC20DummyB as _ERC20DummyB;

methods {
    function tokenA() external returns (address) envfree;
    function tokenB() external returns (address) envfree;

    // Using a dispatcher with wildcard contract
    function _.balanceOf(address) external => DISPATCHER(true);
    function _.transfer(address, uint256) external => DISPATCHER(true);
    function _.transferFrom(address, address, uint256) external => DISPATCHER(true);

    // A wildcard function
    function ERC20DummyA._ external => NONDET;
}


/// @title Wildcard contract overrides wildcard function
rule wildcardContract(uint256 amount) {
    require tokenA() == _ERC20DummyA;
    require tokenB() == _ERC20DummyB;

    env e;
    uint256 preA = _ERC20DummyA.balanceOf(e, e.msg.sender);

    transferAtoB(e, amount);

    uint256 postA = _ERC20DummyA.balanceOf(e, e.msg.sender);

    // We'll see in the report that the storage changes
    //satisfy to_mathint(postA) == preA + amount;
    satisfy true;
}
