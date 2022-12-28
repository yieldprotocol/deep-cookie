
pragma solidity ^0.8.0;

contract CryptoAuction {

    // The ERC-20 token to be auctioned
    address public token;

    // The address of the highest bidder
    address public highestBidder;

    // The amount of the highest bid
    uint256 public highestBid;

    // The starting price of the auction
    uint256 public startingPrice;

    // The expiration time of the auction
    uint256 public expirationTime;

    // Event that is triggered when a bid is made
    event BidMade(address bidder, uint256 bid);

    // Event that is triggered when the auction ends
    event AuctionEnded(address winner, uint256 finalBid);

    // Constructor to initialize the auction
    constructor(address _token, uint256 _startingPrice, uint256 _expirationTime) public {
        token = _token;
        startingPrice = _startingPrice;
        expirationTime = _expirationTime;
    }

    // Function to make a bid
    function bid(uint256 _bid) public {
        // Ensure that the bid is greater than the starting price
        require(_bid > startingPrice, "Bid must be greater than starting price");

        // Ensure that the bid is greater than the current highest bid
        require(_bid > highestBid, "Bid must be greater than current highest bid");

        // Set the highest bidder and highest bid
        highestBidder =msg.sender;
        highestBid = _bid;

        // Trigger the BidMade event
        emit BidMade(msg.sender, _bid);
    }

    // Function to end the auction
    function endAuction() public {
        // Ensure that the auction has expired
        require(block.timestamp > expirationTime, "Auction has not expired yet");

        // Transfer the token to the highest bidder
//        token.transfer(highestBidder, highestBid);

        // Trigger the AuctionEnded event
        emit AuctionEnded(highestBidder, highestBid);
    }
}

