// SPDX-License-Identifier: MIT

pragma solidity ^0.8.0;

// import "../Seriality/src/Seriality.sol";
import "./Utils.sol";
import "./TribHeap.sol";

contract User {
    struct FollowUnfollowLogItem {
        bool isValid;
        bool isFollow;
        string whom;
        // TODO: add unique identifier: txHash. It seems like txHash is not accessibl, maybe block.timestamp may come handy (unlikely though)
    }

    address _address;
    string username;
    TribHeap _tribs;
    FollowUnfollowLogItem[] followUnfollowLog;
    string[] _following;

    constructor(string memory _username) {
        username = _username;
        _tribs = new TribHeap();
        _address = msg.sender;
    }

    function getUserName() public view returns (string memory) {
        return username;
    }

    function post(Tribs.Trib memory trib) public returns (bool) {
        _tribs.push(trib);
        return true;
    }

    function tribs() public returns (Tribs.Trib[] memory) {
        uint256 numberOfTribs = _tribs.length();
        if (numberOfTribs > Constants.MAX_TRIB_FETCH) {
            uint256 numTribsToDelete = numberOfTribs - Constants.MAX_TRIB_FETCH;
            for (uint256 i = 0; i < numTribsToDelete; i++) {
                _tribs.popReverse();
            }
        }

        return _tribs.getTribHeap();
    }

    function follow(string memory userToFollow) public returns (bool) {
        // TODO
        // TODO: add transaction hash as unique identifier
        followUnfollowLog.push(FollowUnfollowLogItem(true, true, userToFollow));
        // isFollowing[userToFollow] = true;
        // this may have to be done in Python because the txHash to uniquely identify the log entry isn't available until the transaction is complete.
        // In python, the follow/unfollow operation could be one transaction, then the txHash of that transaction can be used to store into the FollowUnfollowlog
        return true;
    }

    function unfollow(string memory userToUnfollow) public returns (bool) {
        // TODO
        followUnfollowLog.push(
            FollowUnfollowLogItem(true, false, userToUnfollow)
        );
        // isFollowing[userToUnfollow] = false;
        return true;
    }

    function isFollowing(string memory otherUser) public returns (bool) {
        string[] memory followingList = following();
        return Utils.exists(followingList, otherUser);
    }

    function following() public returns (string[] memory) {
        delete _following;

        for (uint256 i = 0; i < followUnfollowLog.length; i++) {
            FollowUnfollowLogItem storage logItem = followUnfollowLog[i];

            if (logItem.isFollow) {
                if (Utils.getIndex(_following, logItem.whom) != -1) {
                    logItem.isValid = false;
                } else {
                    _following.push(logItem.whom);
                }
            } else {
                int256 idx = Utils.getIndex(_following, logItem.whom);
                if (idx != -1) {
                    _following = Utils.deleteAtIndexUnordered(
                        _following,
                        uint256(idx)
                    );
                } else {
                    logItem.isValid = false;
                }
            }
        }

        return _following;
    }

    function home() public returns (Tribs.Trib[] memory) {
        // TODO
    }
}
