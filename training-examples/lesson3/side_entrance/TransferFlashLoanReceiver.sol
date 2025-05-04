// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;


import {IFlashLoanReceiver} from "./SideEntranceLenderPool.sol";
import {IERC20} from '../../ERC20/contracts/IERC20.sol';


/// @title A simple IFlashLoanReceiver implementation that attempts to steal
/// from the pool
contract TransferFlashLoanReceiver is IFlashLoanReceiver {

    IERC20 public token;
    uint256 public amountToTake;

    function execute(uint256 repayAmount) external {
        // Try taking from the pool
        token.transferFrom(msg.sender, address(this), amountToTake);

        // Repay the loan
        token.transfer(msg.sender, repayAmount);
    }
}
