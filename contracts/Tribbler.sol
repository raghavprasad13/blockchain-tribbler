// SPDX-License-Identifier: MIT

pragma solidity ^0.8.0;

import "./User.sol";

contract Tribbler {
    uint16 public constant MIN_LIST_USER = 20;

    mapping(string => string) public usernameUserContractAddr;
    mapping(string => bool) public usernames; // this will be used to check if users already exist
    string[] usernameArray; // this will be used for listUsers

    function isUserExists(string memory username) public view returns (bool) {
        return usernames[username];
    }

    function getUserContractAddr(string memory username)
        public
        view
        returns (string memory)
    {
        return usernameUserContractAddr[username];
    }

    function signup(string memory username, string memory userContractAddr)
        public
        returns (bool)
    {
        usernameUserContractAddr[username] = userContractAddr;

        if (usernameArray.length < MIN_LIST_USER) usernameArray.push(username);
        usernames[username] = true;
        return true;
    }

    // Sorting in python frontend scripts for now
    function listUsers() public view returns (string[] memory) {
        require(usernameArray.length > 0, "No users exist");
        return usernameArray;
    }
}
