// SPDX-License-Identifier: MIT
pragma solidity ^0.8.24;


import {IERC20} from '../../ERC20/contracts/IERC20.sol';


interface IFlashLoanReceiver {
    function execute(uint256 repayAmount) external;
}


/**
 * @title A liquidity pool with a vulnerability
 * Adapted from:
 * https://github.com/tinchoabbate/damn-vulnerable-defi/blob/v3.0.0/contracts/side-entrance/SideEntranceLenderPool.sol
 */
contract SideEntranceLenderPool {

    // The token used for deposits and loans
    IERC20 public token;

    // Fee for loans
    uint256 public immutable fee;

    // Deposits into the pool
    mapping (address => uint256) private deposits;

    function deposit(uint256 amount) external {
        bool success = token.transferFrom(msg.sender, address(this), amount);
        require(success, "Deposit failed");
        deposits[msg.sender] += amount;
    }

    function withdraw() external {
        uint256 amountToWithdraw = deposits[msg.sender];
        deposits[msg.sender] = 0;
        bool success = token.transfer(msg.sender, amountToWithdraw);
        require(success, "Wthdraw failed");
    }

    function flashLoan(uint256 amount) external {
        uint256 balanceBefore = token.balanceOf(address(this));
        require(balanceBefore >= amount, "Not enough ETH in balance to provide loan");

        bool success = token.transfer(msg.sender, amount);
        require(success, "Loan failed");
        IFlashLoanReceiver(msg.sender).execute(amount + fee);

        uint256 balanceAfter = token.balanceOf(address(this));
        require(balanceAfter >= balanceBefore + fee, "Flash loan hasn't been paid back");
    }
}
