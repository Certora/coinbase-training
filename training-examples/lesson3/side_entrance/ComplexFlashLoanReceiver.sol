// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;


import {IFlashLoanReceiver, SideEntranceLenderPool} from "./SideEntranceLenderPool.sol";
import {IERC20} from '../../ERC20/contracts/IERC20.sol';

/**
 * @title A complex flash loan reciever
 * This contract may do arbitrary actions during a flash loan.
 * By using the Prover's over-approximation of storage for enabling
 * any possible action.
 */
contract ComplexFlashLoanReceiver is IFlashLoanReceiver {

    IERC20 public token;

    SideEntranceLenderPool public pool;

    // Which function to call
    enum Func {
        Deposit,
        Withdraw,
        FlashLoan,
        Transfer
    }
    mapping(uint8 => Func) public toCalls;

    // The amounts to use in the function calls
    mapping(uint8 => uint256) public amounts;

    // The iteration number
    uint8 public i;

    function execute(uint256) external {
        require(msg.sender == address(pool));

        i += 1;  // Increase iteration

        if (toCalls[i] == Func.Deposit) {
            pool.deposit(amounts[i]);
        } else if (toCalls[i] == Func.Withdraw) {
            pool.withdraw();
        } else if (toCalls[i] == Func.FlashLoan) {
            pool.flashLoan(amounts[i]);
        } else {
            // Repay some money
            i += 1;
            bool success = token.transfer(address(pool), amounts[i]);
            require(success, "Transfer to pool failed");
        }
    }
}
