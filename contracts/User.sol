// SPDX-License-Identifier: MIT

pragma solidity ^0.8.0;

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

        return true;
    }

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
        _tribs.push(trib);

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
        return true;
    }

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

        followUnfollowLog.push(logItem);
        return true;
    }

    function following() public view returns (FollowUnfollowLogItem[] memory) {
        return followUnfollowLog;
    }
}
