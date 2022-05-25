// SPDX-License-Identifier: MIT

pragma solidity ^0.8.0;

import "./User.sol";
import "./Constants.sol";
import "./Tribs.sol";
import "./Utils.sol";
import "./StringHeap.sol";

contract Tribbler {
    mapping(address => User) public users;
    mapping(string => bool) public usernames; // this will be used to check if users already exist
    StringHeap usernameArray; // this will be used for listUsers

    constructor() {
        usernameArray = new StringHeap();
    }

    function signUp(string memory username) public returns (bool) {
        require(Utils.isValidUsername(username), "Username is invalid");
        require(!usernames[username], "User already exists");

        User user = new User(username);
        if (usernameArray.length() < Constants.MIN_LIST_USER)
            usernameArray.push(username);
        users[msg.sender] = user;
        usernames[username] = true;
        return true;
    }

    function listUsers() public returns (string[] memory) {
        return usernameArray.getStringHeap();
    }

    function post(string memory username, string memory _post)
        public
        returns (bool)
    {
        require(
            bytes(_post).length < Constants.MAX_TRIB_LEN,
            "Post is too long"
        );
        require(Utils.isValidUsername(username), "Username is invalid");

        Tribs.Trib memory trib = Tribs.Trib(
            username,
            _post,
            block.timestamp,
            block.number,
            tx.gasprice
        );

        User user = users[msg.sender];
        return user.post(trib);
    }

    function tribs(string memory username)
        public
        returns (Tribs.Trib[] memory)
    {
        require(Utils.isValidUsername(username), "Username is invalid");
        require(usernames[username], "User does not exist");

        User user = users[msg.sender];
        return user.tribs();
    }

    function follow(string memory who, string memory whom)
        public
        returns (bool)
    {
        require(
            !Utils.whoWhomSame(who, whom),
            "Both the usernames are the same"
        );
        require(
            Utils.isValidUsername(who) && Utils.isValidUsername(whom),
            "Username is invalid"
        );
        require(usernames[who] && usernames[whom], "User does not exist");

        User user = users[msg.sender];
        return user.follow(whom);
    }

    function unfollow(string memory who, string memory whom)
        public
        returns (bool)
    {
        require(
            !Utils.whoWhomSame(who, whom),
            "Both the usernames are the same"
        );
        require(
            Utils.isValidUsername(who) && Utils.isValidUsername(whom),
            "Username is invalid"
        );
        require(usernames[who] && usernames[whom], "User does not exist");

        User user = users[msg.sender];
        return user.unfollow(whom);
    }

    function isFollowing(string memory who, string memory whom)
        public
        returns (bool)
    {
        require(
            !Utils.whoWhomSame(who, whom),
            "Both the usernames are the same"
        );
        require(
            Utils.isValidUsername(who) && Utils.isValidUsername(whom),
            "Username is invalid"
        );
        require(usernames[who] && usernames[whom], "User does not exist");

        User user = users[msg.sender];
        return user.isFollowing(whom);
    }

    function following(string memory username)
        public
        returns (string[] memory)
    {
        require(Utils.isValidUsername(username), "Username is invalid");
        require(usernames[username], "User does not exist");

        User user = users[msg.sender];
        return user.following();
    }

    function home(string memory username) public returns (Tribs.Trib[] memory) {
        require(Utils.isValidUsername(username), "Username is invalid");
        require(usernames[username], "User does not exist");

        User user = users[msg.sender];
        return user.home();
    }
}
