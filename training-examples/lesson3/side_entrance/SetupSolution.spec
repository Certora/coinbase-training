/* Setup and basic rules for `SideEntranceLenderPool` */

using ERC20 as _ERC20;

methods {
    // `ERC20`
    function ERC20.balanceOf(address) external returns (uint256) envfree;

    // `IFlashLoanReceiver`
    function _.execute(uint256) external => DISPATCHER(true);
}


/// @title Burrower cannot exploit the pool
/// @notice This rule should FAIL, due to a vulnerability in the pool
rule noExploit(uint256 amount) {

    env e;
    uint256 balancePre = _ERC20.balanceOf(e.msg.sender);
    uint256 depositsPre = currentContract.deposits[e.msg.sender];

    flashLoan(e, amount);
    withdraw(e);

    uint256 balancePost = _ERC20.balanceOf(e.msg.sender);
    uint256 depositsPost = currentContract.deposits[e.msg.sender];  // Should be zero

    assert balancePost + depositsPost <= balancePre + depositsPre, "No exploit possible";
}
