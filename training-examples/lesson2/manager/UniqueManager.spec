// #contract Manager.sol
// Prove that two distinct funds have two different managers
methods {
    function getCurrentManager(uint256) external returns (address) envfree;
    function isActiveManager(address) external returns (bool) envfree;
}

function isCreated(uint256 fund) returns bool {
    return getCurrentManager(fund) != 0;
}

/// @title Address zero cannot become manager of a created fund
rule zeroNeverManages(uint256 fund, method f) {
    bool isBefore = isCreated(fund);

    env e;
    calldataarg args;
    f(e, args);

    bool isAfter = isCreated(fund);
    assert isBefore => isAfter, "Zero cannot manage created fund";
}

/// @title Managers of different funds are different
invariant managersAreUnique(uint256 fund1, uint256 fund2)
    (isCreated(fund1) && isCreated(fund2) && fund1 != fund2) => (
        getCurrentManager(fund1) != getCurrentManager(fund2)
    )
    {
        preserved {
            requireInvariant currentManagerIsActive(fund1);
            requireInvariant currentManagerIsActive(fund2);
        }
    }


/// @title The current manager of a fund is an active manager
invariant currentManagerIsActive(uint256 fund)
    isCreated(fund) <=> isActiveManager(getCurrentManager(fund))
    {
        preserved claimManagement(uint256 fundId) with (env e) {
            requireInvariant managersAreUnique(fund, fundId);
        }
    }

