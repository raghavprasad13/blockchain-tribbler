// SPDX-License-Identifier: MIT

pragma solidity ^0.8.0;

// import "../Seriality/src/Seriality.sol";
import "./Utils.sol";
import "./String.sol";
import "./Tribs.sol";

contract User {
    struct FollowUnfollowLogItem {
        bool isValid;
        bool isFollow;
        string whom;
        string txHash;
    }

    string username;
    Tribs.Trib[] _tribs;
    FollowUnfollowLogItem[] followUnfollowLog;
    string[] _following;

    constructor(string memory _username) {
        username = _username;
    }

    function getUserName() public view returns (string memory) {
        return username;
    }

    function post(Tribs.Trib memory trib) public returns (bool) {
        _tribs.push(trib);
        return true;
    }

    function tribs() public view returns (Tribs.Trib[] memory) {
        // uint256 numberOfTribs = _tribs.length;
        // Utils.bubbleSort(_tribs);
        // if (numberOfTribs > Constants.MAX_TRIB_FETCH) {
        //     uint256 numTribsToDelete = numberOfTribs - Constants.MAX_TRIB_FETCH;
        //     for (uint256 i = 0; i < numTribsToDelete; i++) {
        //         _tribs.pop();
        //     }
        // }

        return _tribs;
        // Tribs.Trib[] memory mem_tribs = _tribs;
        // return mem_tribs;
    }

    function appendToFollowUnfollowLog(
        bool isFollow,
        string memory whom,
        string memory txHash
    ) public returns (bool) {
        FollowUnfollowLogItem memory logItem = FollowUnfollowLogItem({
            isValid: true,
            isFollow: isFollow,
            whom: whom,
            txHash: txHash
        });

        followUnfollowLog.push(logItem);

        delete _following;

        for (uint256 i = 0; i < followUnfollowLog.length; i++) {
            FollowUnfollowLogItem storage _logItem = followUnfollowLog[i];

            if (_logItem.isFollow) {
                if (Utils.getIndex(_following, _logItem.whom) != -1) {
                    _logItem.isValid = false;
                } else {
                    _following.push(_logItem.whom);
                }
            } else {
                int256 idx = Utils.getIndex(_following, _logItem.whom);
                if (idx != -1) {
                    _following = Utils.deleteAtIndexUnordered(
                        _following,
                        uint256(idx)
                    );
                } else {
                    _logItem.isValid = false;
                }
            }
        }

        uint256 followingCount = _following.length;
        require(
            followingCount <= Constants.MAX_FOLLOWING,
            "Following too many people"
        );

        bool followResult;
        bool foundLogEntry;

        for (uint256 i = 0; i < followUnfollowLog.length; i++) {
            FollowUnfollowLogItem storage _logItem = followUnfollowLog[i];
            if (
                String.compare(_logItem.whom, whom) == 0 &&
                String.compare(_logItem.txHash, txHash) == 0
            ) {
                followResult = _logItem.isValid;
                foundLogEntry = true;
            }
        }

        if (!(foundLogEntry && followResult)) {
            return false; // already following
        }

        return true;
    }

    // function isFollowing(string memory otherUser) public returns (bool) {
    //     string[] memory followingList = following();
    //     return Utils.exists(followingList, otherUser);
    // }

    function following() public view returns (FollowUnfollowLogItem[] memory) {
        // delete _following;

        // for (uint256 i = 0; i < followUnfollowLog.length; i++) {
        //     FollowUnfollowLogItem storage logItem = followUnfollowLog[i];

        //     if (logItem.isFollow) {
        //         if (Utils.getIndex(_following, logItem.whom) != -1) {
        //             logItem.isValid = false;
        //         } else {
        //             _following.push(logItem.whom);
        //         }
        //     } else {
        //         int256 idx = Utils.getIndex(_following, logItem.whom);
        //         if (idx != -1) {
        //             _following = Utils.deleteAtIndexUnordered(
        //                 _following,
        //                 uint256(idx)
        //             );
        //         } else {
        //             logItem.isValid = false;
        //         }
        //     }
        // }

        // return _following; // maybe have a Util function to convert storage to memory?

        return followUnfollowLog;
    }
}
