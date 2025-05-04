/*
 * Examples of invariants in ERC20
 */

methods {
    function balanceOf(address) external returns (uint) envfree;
    function allowance(address, address) external returns (uint) envfree;
    function totalSupply(address) external returns (uint) envfree;
}


/** @title Preserved block example - account balance <= `totalSupply`
 *  @notice The use of `require` statements makes this undound 
 */
invariant balanceAtMostTotalSupply(address account)
    balanceOf(account) <= totalSupply()
    {
        preserved with (env e1) {
            // This require statement is not sound!
            require (
                balanceOf(e1.msg.sender) + balanceOf(account) <= 
                to_mathint(totalSupply())
            );
        }
        preserved transferFrom(
            address sender, address recipient, uint256 amount
        ) with (env e2) {
            // This require statement is not sound!
            require (
                balanceOf(sender) + balanceOf(recipient) + balanceOf(account) <= 
                to_mathint(totalSupply())
            );
        }
    }
