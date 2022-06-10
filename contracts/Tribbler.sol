// SPDX-License-Identifier: MIT

pragma solidity ^0.8.0;

import "./User.sol";

// import "./Utils.sol";

contract Tribbler {
    uint16 public constant MIN_LIST_USER = 20;

    // mapping(string => User) public usernameUserMapping;
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
        // require(Utils.isValidUsername(username), "Username is invalid"); - checked in frontend in python
        // require(!usernames[username], "User already exists");

        // User user = new User(username);
        usernameUserContractAddr[username] = userContractAddr;

        // if (usernameArray.length < Utils.MIN_LIST_USER)
        if (usernameArray.length < MIN_LIST_USER) usernameArray.push(username);
        // usernameUserMapping[username] = user;
        usernames[username] = true;
        return true;
    }

    // Sorting in python frontend scripts for now
    function listUsers() public view returns (string[] memory) {
        require(usernameArray.length > 0, "No users exist");
        return usernameArray;
    }

    // function post(string memory username, string memory _post)
    //     public
    //     returns (bool)
    // {
    //     // this function must remain `non-pure`

    //     return true;
    // }

    // function addTrib(
    //     string memory username,
    //     string memory message,
    //     uint256 timestamp,
    //     uint256 blockNum,
    //     uint256 txIndex
    // ) public returns (bool) {
    //     Utils.Trib memory trib = Utils.Trib(
    //         username,
    //         message,
    //         timestamp,
    //         blockNum,
    //         txIndex
    //     );

    //     User user = usernameUserMapping[username];
    //     return user.post(trib);
    // }

    // function tribs(string memory username)
    //     public
    //     view
    //     returns (Utils.Trib[] memory)
    // {
    //     require(usernames[username], "User does not exist");

    //     User user = usernameUserMapping[username];
    //     return user.tribs();
    // }

    // function followOrUnfollow(string memory who, string memory whom)
    //     public
    //     returns (bool)
    // {
    //     // this function must remain `non-pure`
    //     // require(
    //     //     !Utils.whoWhomSame(who, whom),
    //     //     "Both the usernames are the same"
    //     // );
    //     // require(
    //     //     Utils.isValidUsername(who) && Utils.isValidUsername(whom),
    //     //     "Username is invalid"
    //     // );
    //     require(usernames[who] && usernames[whom], "User does not exist");

    //     return true;
    // }

    // function appendToFollowUnfollowLog(
    //     bool isFollow,
    //     string memory who,
    //     string memory whom,
    //     string memory txHash
    // ) public returns (bool) {
    //     User user = usernameUserMapping[who];
    //     return user.appendToFollowUnfollowLog(isFollow, whom, txHash);
    // }

    // function following(string memory username)
    //     public
    //     view
    //     returns (User.FollowUnfollowLogItem[] memory)
    // {
    //     // require(Utils.isValidUsername(username), "Username is invalid");
    //     require(usernames[username], "User does not exist");

    //     // User user = users[msg.sender];
    //     User user = usernameUserMapping[username];
    //     return user.following();
    // }
}
