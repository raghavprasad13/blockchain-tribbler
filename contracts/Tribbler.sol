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

    // why sort in place? sorting in place also makes a transaction
    // function listUsers() public returns (string[] memory) {
    //     require(usernameArray.length > 0, "No users exist");
    //     Utils.sort(usernameArray, 0, usernameArray.length - 1);
    //     return usernameArray;
    // }

    // Using below function instead of above one. Sorting in python scripts for now
    function listUsers() public returns (string[] memory) {
        require(usernameArray.length > 0, "No users exist");
        usernameArray = bubbleSort(usernameArray);
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
        // string memory who,
        string memory whom,
        string memory txHash
    ) public returns (bool) {
        User user = users[msg.sender];
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

        // get own tribs first
        Tribs.Trib[] memory homeList = user.tribs();

        // TODO?: cleanup logs; maybe in following?

        string[] memory followList = user.following();

        for (uint256 i = 0; i < followList.length; i++) {
            string memory followedUsername = followList[i];
            if (!usernames[followedUsername]) continue;

            User followedUser = usernameUserMapping[followedUsername];
            Tribs.Trib[] memory followedUserTribs = followedUser.tribs();
            homeList = Utils.appendArray(homeList, followedUserTribs);
        }

        homeList = Utils.bubbleSort_memTribs(homeList);

        return homeList;
    }

    // function sort(
    //     string[] memory arr,
    //     uint256 startIndex,
    //     uint256 endIndex
    // ) public returns (string[] memory) {
    //     if (startIndex < endIndex) {
    //         uint256 mid = (startIndex + (endIndex - 1)) / 2;
    //         arr = sort(arr, startIndex, mid);
    //         arr = sort(arr, mid + 1, endIndex);
    //         arr = merge(arr, startIndex, mid, endIndex);
    //     }

    //     return arr;
    // }

    // function merge(
    //     string[] memory arr,
    //     uint256 left,
    //     uint256 mid,
    //     uint256 right
    // ) public pure returns (string[] memory) {
    //     uint256 k;
    //     uint256 n1 = mid - left + 1;
    //     uint256 n2 = right - mid;

    //     string[] memory L = new string[](n1);
    //     string[] memory R = new string[](n2);

    //     for (uint256 i = 0; i < n1; i++) L[i] = arr[left + i];
    //     for (uint256 i = 0; i < n2; i++) {
    //         // console.log("i = ", i);
    //         R[i] = arr[mid + left + i];
    //     }

    //     uint256 _i = 0;
    //     uint256 _j = 0;
    //     k = left;

    //     while (_i < n1 && _j < n2) {
    //         if (String.compare(L[_i], R[_j]) == 1) {
    //             arr[k] = L[_i];
    //             _i++;
    //         } else {
    //             arr[k] = R[_j];
    //             _j++;
    //         }
    //         k++;
    //     }

    //     while (_i < n1) {
    //         arr[k] = L[_i];
    //         _i++;
    //         k++;
    //     }

    //     while (_j < n2) {
    //         arr[k] = R[_j];
    //         _j++;
    //         k++;
    //     }

    //     return arr;
    // }

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

    // function bubbleSort(Tribs.Trib[] memory arr)
    //     public
    //     pure
    //     returns (Tribs.Trib[] memory)
    // {
    //     uint256 i;
    //     uint256 j;
    //     uint256 n = arr.length;
    //     Tribs.Trib memory temp;
    //     for (i = 0; i < n; i++) {
    //         for (j = 0; j < n - i - 1; j++) {
    //             if (Tribs.compare(arr[j], arr[j + 1]) == -1) {
    //                 // arr[j+1] should appear above arr[j]
    //                 temp = arr[j];
    //                 arr[j] = arr[j + 1];
    //                 arr[j + 1] = temp;
    //             }
    //         }
    //     }

    //     return arr;
    // }
}
