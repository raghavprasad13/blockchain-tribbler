// SPDX-License-Identifier: MIT

pragma solidity ^0.8.0;

import "./Utils.sol";

contract User {
    struct FollowUnfollowLogItem {
        // bool isValid;
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

        // need to cleanup old tribs - DELAY for now

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
            // isValid: true,
            isFollow: isFollow,
            whom: whom,
            txHash: txHash
        });

        followUnfollowLog.push(logItem);

        // delete _following;

        // for (uint256 i = 0; i < followUnfollowLog.length; i++) {
        //     FollowUnfollowLogItem storage _logItem = followUnfollowLog[i];

        //     if (_logItem.isFollow) {
        //         if (Utils.getIndex(_following, _logItem.whom) != -1) {
        //             _logItem.isValid = false;
        //         } else {
        //             _following.push(_logItem.whom);
        //         }
        //     } else {
        //         int256 idx = Utils.getIndex(_following, _logItem.whom);
        //         if (idx != -1) {
        //             _following = Utils.deleteAtIndexUnordered(
        //                 _following,
        //                 uint256(idx)
        //             );
        //         } else {
        //             _logItem.isValid = false;
        //         }
        //     }
        // }

        // uint256 followingCount = _following.length;
        // require(
        //     followingCount <= Utils.MAX_FOLLOWING,
        //     "Following too many people"
        // );

        // bool followResult;
        // bool foundLogEntry;

        // for (uint256 i = 0; i < followUnfollowLog.length; i++) {
        //     FollowUnfollowLogItem storage _logItem = followUnfollowLog[i];
        //     if (
        //         Utils.string_compare(_logItem.whom, whom) == 0 &&
        //         Utils.string_compare(_logItem.txHash, txHash) == 0
        //     ) {
        //         followResult = _logItem.isValid;
        //         foundLogEntry = true;
        //     }
        // }

        // if (!(foundLogEntry && followResult)) {
        //     return false; // already following
        // }

        return true;
    }

    function following() public view returns (FollowUnfollowLogItem[] memory) {
        return followUnfollowLog;
    }
}
