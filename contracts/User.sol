// SPDX-License-Identifier: MIT

pragma solidity ^0.8.0;

// Code to manage user specific oprations

contract User {
    struct FollowUnfollowLogItem {
        // bool isValid;
        bool isFollow;
        string whom;
        string txHash;
    }

    struct Trib {
        string who;
        string message;
        uint256 timestamp;
        uint256 blockNum;
        uint256 txIndex; // because we cannot get txIndex. Update: we can get txIndex, but then the operation will have to be broken up into 2 transactions
    }

    string username;
    Trib[] _tribs;
    FollowUnfollowLogItem[] followUnfollowLog;
    string[] _following;

    constructor(string memory _username) {
        username = _username;
    }

    function getUsername() public view returns (string memory) {
        return username;
    }

    function post(string memory post) public returns (bool) {
        // this function must remain `non-pure`
        // hash of this transaction will be used in the actual trib data structure
        return true;
    }

    // Function to actually add a trib in blockchain
    function addTrib(
        string memory message,
        uint256 timestamp,
        uint256 blockNum,
        uint256 txIndex
    ) public returns (bool) {
        Trib memory trib = Trib(
            username,
            message,
            timestamp,
            blockNum,
            txIndex
        );
        _tribs.push(trib); // add trib

        return true;
    }

    function tribs() public view returns (Trib[] memory) {
        return _tribs;
    }

    function followOrUnfollow(string memory who, string memory whom)
        public
        returns (bool)
    {
        // this function must remain `non-pure`
        // hash of this transaction will be used in the actual trib data structure
        return true;
    }

    // Function to actually add a follow or unfollow log in blockchain
    function appendToFollowUnfollowLog(
        bool isFollow,
        string memory whom,
        string memory txHash
    ) public returns (bool) {
        FollowUnfollowLogItem memory logItem = FollowUnfollowLogItem({
            isFollow: isFollow,
            whom: whom,
            txHash: txHash
        });

        followUnfollowLog.push(logItem); // append log
        return true;
    }

    function following() public view returns (FollowUnfollowLogItem[] memory) {
        return followUnfollowLog; // return log and process in frontend
    }
}
