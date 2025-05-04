pragma solidity ^0.8.0;

import {ERC20} from "./ERC20.sol";

/// @notice ERC20 implementation using loops for multi-transfer
contract LoopyERC20 is ERC20 {

    /// @dev Transfer the given amount to each of the recipients
    function multiTransfer(
        address[] memory recipients,
        uint256 amount
    ) public {
        for(uint256 i ; i < recipients.length ; i++ ){
            // Prevent transfer to self
            require(msg.sender != recipients[i]);

            _balances[msg.sender] -= amount;
            _balances[recipients[i]] += amount;
        }
    }

    /// @dev Transfer the given amount to each of the recipients - with a bug
    function multiTransferWithBug(
        address[] memory recipients,
        uint256 amount
    ) public {
        // require (recipients.length > 2);
        uint256 totalToReduce = 0;
        for(uint256 i ; i < recipients.length ; i++ ){
            // Prevent transfer to self
            require(msg.sender != recipients[i]);

            totalToReduce = amount;
            _balances[recipients[i]] += amount;
        }
        _balances[msg.sender] -= totalToReduce;
    }

    // The following functions are just to provide examples for loop unrolling

    function loop(uint n) public pure returns (uint) {
        uint j = 0;
        for (uint i; i < n; i++) {
            j++;
        }
        return j;
    }
    
    function unrolled(uint n) public pure returns (uint) {
        require(n <= 3);  // 3 unrolls will be enough
        uint j = 0;

        // Start unrolling
        uint i; // i=0
        if (i < n) {
            j++;

            // Next unroll
            i ++; // i=1
            if (i < n) {
                j++;

                // Next unroll
                i++; // i=2
                if (i < n) {
                    j++;

                    i++; // i=3
                }
            }
        }
        // Require that the exit condition holds
        require(i >= n);
        // Or assert that it holds (in CVL)
        // assert i>=n;
        return j;
    }
}
