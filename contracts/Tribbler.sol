// SPDX-License-Identifier: MIT

pragma solidity ^0.8.0;

import "./User.sol";
import "./Constants.sol";
import "./Tribs.sol";
import "./Utils.sol";

contract Tribbler {
    mapping(address => User) public users;
    mapping(string => User) public usernameUserMapping;
    mapping(string => bool) public usernames; // this will be used to check if users already exist
    string[] usernameArray; // this will be used for listUsers

    function signup(string memory username) public returns (bool) {
        require(Utils.isValidUsername(username), "Username is invalid");
        require(!usernames[username], "User already exists");

        User user = new User(username);
        if (usernameArray.length < Constants.MIN_LIST_USER)
            usernameArray.push(username);
        users[msg.sender] = user;
        usernameUserMapping[username] = user;
        usernames[username] = true;
        return true;
    }

    // Using below function instead of above one. Sorting in python scripts for now
    function listUsers() public view returns (string[] memory) {
        require(usernameArray.length > 0, "No users exist");
        return usernameArray;
    }

    function post(string memory username, string memory _post)
        public
        returns (bool)
    {
        // this function must remain `non-pure`
        require(
            bytes(_post).length < Constants.MAX_TRIB_LEN,
            "Post is too long"
        );
        require(Utils.isValidUsername(username), "Username is invalid");

        return true;
    }

    function addTrib(
        string memory username,
        string memory message,
        uint256 timestamp,
        uint256 blockNum,
        uint256 txIndex
    ) public returns (bool) {
        Tribs.Trib memory trib = Tribs.Trib(
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
        returns (Tribs.Trib[] memory)
    {
        require(Utils.isValidUsername(username), "Username is invalid");
        require(usernames[username], "User does not exist");

        User user = usernameUserMapping[username];
        return user.tribs();
    }

    function followOrUnfollow(string memory who, string memory whom)
        public
        returns (bool)
    {
        // this function must remain `non-pure`
        require(
            !Utils.whoWhomSame(who, whom),
            "Both the usernames are the same"
        );
        require(
            Utils.isValidUsername(who) && Utils.isValidUsername(whom),
            "Username is invalid"
        );
        require(usernames[who] && usernames[whom], "User does not exist");

        return true;
    }

    function appendToFollowUnfollowLog(
        bool isFollow,
        string memory who,
        string memory whom,
        string memory txHash
    ) public returns (bool) {
        User user = usernameUserMapping[who];
        return user.appendToFollowUnfollowLog(isFollow, whom, txHash);
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

        User user = usernameUserMapping[who];
        return user.isFollowing(whom);
    }

    function following(string memory username)
        public
        returns (string[] memory)
    {
        require(Utils.isValidUsername(username), "Username is invalid");
        require(usernames[username], "User does not exist");

        User user = usernameUserMapping[username];
        return user.following();
    }

    function home(string memory username) public returns (Tribs.Trib[] memory) {
        require(Utils.isValidUsername(username), "Username is invalid");
        require(usernames[username], "User does not exist");

        User user = usernameUserMapping[username];

        // get own tribs first
        Tribs.Trib[] memory homeList = user.tribs();

        string[] memory followList = user.following();

        for (uint256 i = 0; i < followList.length; i++) {
            string memory followedUsername = followList[i];
            if (!usernames[followedUsername]) continue;

            User followedUser = usernameUserMapping[followedUsername];
            Tribs.Trib[] memory followedUserTribs = followedUser.tribs();
            homeList = Utils.appendArray(homeList, followedUserTribs);
        }

        homeList = Utils.bubbleSort_memTribs(homeList);

        // return only top MAX_TRIB_FETCH tribs
        Tribs.Trib[] memory returnHomeList = new Tribs.Trib[](
            Constants.MAX_TRIB_FETCH
        );
        uint256 numTribs = homeList.length < Constants.MAX_TRIB_FETCH
            ? homeList.length
            : Constants.MAX_TRIB_FETCH;
        for (uint256 i = 0; i < numTribs; i++) {
            returnHomeList[i] = homeList[i];
        }

        return returnHomeList;
    }

    function bubbleSort(string[] memory arr)
        public
        pure
        returns (string[] memory)
    {
        uint256 i;
        uint256 j;
        uint256 n = arr.length;
        string memory temp;
        for (i = 0; i < n; i++) {
            for (j = 0; j < n - i - 1; j++) {
                if (String.compare(arr[j], arr[j + 1]) == -1) {
                    // arr[j+1] comes first lexicographically
                    temp = arr[j];
                    arr[j] = arr[j + 1];
                    arr[j + 1] = temp;
                }
            }
        }

        return arr;
    }
}
