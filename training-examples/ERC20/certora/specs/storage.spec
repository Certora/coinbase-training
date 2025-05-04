


rule transitivityOfTransfer(
    address sender,
    address intermediary,
    address recipient,
    uint256 amount
) {
    // Initial storage state
    storage init = lastStorage;

    require currentContract._balances[sender] >= amount;

    // Transfer via intermediary
    env e1;
    require e1.msg.sender == sender;
    transfer(e1, intermediary, amount);

    env e2;
    require e2.msg.sender == intermediary;
    transfer(e2, recipient, amount);

    storage viaIntermediary = lastStorage;

    // Transfer directly
    env e3;
    require e3.msg.sender == sender;
    transfer(e3, recipient, amount) at init;

    storage directly = lastStorage;

    satisfy directly == viaIntermediary, "Transfer transitivity";
}
