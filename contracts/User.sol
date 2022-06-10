// SPDX-License-Identifier: MIT

pragma solidity ^0.8.0;

import "./Utils.sol";

contract User {
    struct FollowUnfollowLogItem {
        bool isFollow;
        string whom;
        string txHash;
    }

    string username;
    Utils.Trib[] _tribs;
    FollowUnfollowLogItem[] followUnfollowLog;
    string[] _following;

    constructor(string memory _username) {
        username = _username;
    }

    function post(Utils.Trib memory trib) public returns (bool) {
        _tribs.push(trib);

        return true;
    }

    function tribs() public view returns (Utils.Trib[] memory) {
        return _tribs;
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
