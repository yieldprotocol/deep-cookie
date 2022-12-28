pragma solidity ^0.8.0;
contract CryptoAuctionUser {

    // The instance of the CryptoAuction contract
    CryptoAuction public cryptoAuction;

    // The address of the highest bidder
    address public highestBidder;

    // The amount of the highest bid
    uint256 public highestBid;

    // Constructor to initialize the auction
    constructor(address _token, uint256 _startingPrice, uint256 _expirationTime) public {
        cryptoAuction = new CryptoAuction(_token, _startingPrice, _expirationTime);
    }

    // Function to make a bid
    function bid(uint256 _bid) public {
        // Call the bid() function of the CryptoAuction contract
        cryptoAuction.bid(_bid);

        // Set the highest bidder and highest bid
        highestBidder = cryptoAuction.highestBidder();
        highestBid = cryptoAuction.highestBid();
    }

    // Function to end the auction
    function endAuction() public {
        // Call the endAuction() function of the CryptoAuction contract
        cryptoAuction.endAuction();
    }

    // Function to use the CryptoAuction contract through a full lifecycle
    function use() public {
        // Make a bid
        bid(10);

        // End the auction
        endAuction();
    }
}

