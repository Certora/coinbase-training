/*  A spec for funds manager `IManager.sol` exemplifying preserved blocks */
methods {
    function getCurrentManager(uint256) external returns (address) envfree;
    function getPendingManager(uint256) external returns (address) envfree;
    function isActiveManager(address) external returns (bool) envfree;
}


/// @return whether the fund exists
function isCreated(uint256 fundId) returns bool {
    return getCurrentManager(fundId) != 0;
}


/// @title A fund's manager is active
invariant managerIsActive(uint256 fundId)
    isCreated(fundId) <=> isActiveManager(getCurrentManager(fundId))
    {
        preserved claimManagement(uint256 fundId2) with (env e) {
            requireInvariant uniqueManager(fundId, fundId2);
        }
    }


/// @title A fund has a unique manager
invariant uniqueManager(uint256 fundId1, uint256 fundId2)
	((fundId1 != fundId2) && isCreated(fundId1)) => (
        getCurrentManager(fundId1) != getCurrentManager(fundId2)
    ) {
        preserved {
            requireInvariant managerIsActive(fundId1);
            requireInvariant managerIsActive(fundId2);
        }
    }
