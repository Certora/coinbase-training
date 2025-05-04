/* Loop iteration example */
methods {
    function loop(uint) external returns (uint) envfree;
}


/// @title An example of loop iteration
/// @notice Vacuous if n<3 and optimistic loop
rule loopExample(uint n) {
    uint result = loop(n);
    satisfy true;
}


/// @title Loop formula
rule loopValue(uint n) {
    assert to_mathint(loop(n)) == n + 3;
}
