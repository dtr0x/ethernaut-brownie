pragma solidity ^0.6.0;

contract DoubleEntryPointAttack {

    function handleTransaction(address user, bytes calldata msgData) external {
        msg.sender.call(abi.encodeWithSignature('raiseAlert(address)', user)); 
    }

}
