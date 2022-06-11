// SPDX-License-Identifier: MIT

pragma solidity ^0.8.0;

// main tribbler contract

import "./User.sol";
import "./Utils.sol";

contract Tribbler {
    mapping(string => User) public usernameUserMapping;
    mapping(string => bool) public usernames; // this will be used to check if users already exist
    string[] usernameArray; // this will be used for listUsers

    function signup(string memory username) public returns (bool) {
        require(!usernames[username], "User already exists");

        User user = new User(username);
        if (usernameArray.length < Utils.MIN_LIST_USER)
            usernameArray.push(username);
        usernameUserMapping[username] = user;
        usernames[username] = true;
        return true;
    }

    // Sorting in python frontend scripts for now
    function listUsers() public view returns (string[] memory) {
        require(usernameArray.length > 0, "No users exist");
        return usernameArray;
    }

    function post(string memory username, string memory _post)
        public
        returns (bool)
    {
        // this function must remain `non-pure`
        // hash of this transaction will be used in the actual trib data structure
        return true;
    }

    // Function to actually add a trib in blockchain
    function addTrib(
        string memory username,
        string memory message,
        uint256 timestamp,
        uint256 blockNum,
        uint256 txIndex
    ) public returns (bool) {
        Utils.Trib memory trib = Utils.Trib(
            username,
            message,
            timestamp,
            blockNum,
            txIndex
        );

        User user = usernameUserMapping[username];
        return user.post(trib);
    }

    function tribs(string memory username)
        public
        view
        returns (Utils.Trib[] memory)
    {
        require(usernames[username], "User does not exist");

        User user = usernameUserMapping[username];
        return user.tribs();
    }

    function followOrUnfollow(string memory who, string memory whom)
        public
        returns (bool)
    {
        // this function must remain `non-pure`
        // hash of this transaction will be used in the actual trib data structure
        require(usernames[who] && usernames[whom], "User does not exist");

        return true;
    }

    // Function to actually add a follow or unfollow log in blockchain
    function appendToFollowUnfollowLog(
        bool isFollow,
        string memory who,
        string memory whom,
        string memory txHash
    ) public returns (bool) {
        User user = usernameUserMapping[who];
        return user.appendToFollowUnfollowLog(isFollow, whom, txHash);
    }

    function following(string memory username)
        public
        view
        returns (User.FollowUnfollowLogItem[] memory)
    {
        require(usernames[username], "User does not exist");

        User user = usernameUserMapping[username];
        return user.following();
    }
}
