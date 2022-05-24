// SPDX-License-Identifier: MIT

pragma solidity ^0.8.0;

import "./User.sol";
import "./Tribs.sol";

contract Tribbler {
    uint16 public constant MIN_LIST_USER = 20;
    mapping(address => User) public users;
    mapping(string => bool) public usernames; // this will be used to check if users already exist
    string[] usernameArray; // this will be used for listUsers

    function signUp(string memory username) public returns (bool) {
        require(!usernames[username], "User already exists");
        User user = new User(username);
        if (usernameArray.length < MIN_LIST_USER) usernameArray.push(username);
        users[msg.sender] = user;
        usernames[username] = true;
        return true;
    }

    function listUsers() public view returns (string[] memory) {
        return usernameArray;
    }

    function post(string memory username, string memory _post)
        public
        returns (bool)
    {
        //
    }

    function tribs(string memory username)
        public
        returns (Tribs.Trib[] memory)
    {}

    function home(string memory username)
        public
        view
        returns (string[] memory)
    {}

    // TODO: write functions that will call the user specific functions
}
