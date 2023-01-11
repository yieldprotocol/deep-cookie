pragma solidity ^0.8.9;
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
contract Contract {
    address payable public highestBidder;
    uint public highestBid;
    ERC20 public token;

    constructor() public {
        token = ERC20(0x50cE419A46190C23093232f66F1f3012F5A70949);
    }

    function bid(uint256 _bid) public payable {
        require(msg.value > highestBid);
        highestBidder = payable(msg.sender);
        highestBid = _bid;
    }

    function finishAuction() public {
        require(msg.sender == highestBidder);
        token.transfer(msg.sender, highestBid);
    }
}
