// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;


import {IFlashLoanReceiver} from "./SideEntranceLenderPool.sol";
import {IERC20} from '../../ERC20/contracts/IERC20.sol';


/// @title A simple IFlashLoanReceiver implementation that does nothing
contract TrivialFlashLoanReceiver is IFlashLoanReceiver {

    IERC20 public token;

    function execute(uint256 repayAmount) external {
        // Just repay the loan
        token.transfer(msg.sender, repayAmount);
    }
}
