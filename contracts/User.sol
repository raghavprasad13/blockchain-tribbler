// SPDX-License-Identifier: MIT

pragma solidity ^0.8.0;

// import "../Seriality/src/Seriality.sol";
import "./Utils.sol";

contract User {
    uint16 public constant MAX_FOLLOWING = 2000;
    uint16 public constant MAX_USERNAME_LEN = 15;
    uint16 public constant MAX_TRIB_LEN = 140;
    uint16 public constant MAX_TRIB_FETCH = 100;

    struct FollowUnfollowLogItem {
        bool isValid;
        bool isFollow;
        string whom;
        // TODO: add unique identifier: tx hash
    }

    struct Trib {
        string username;
    }

    string username;
    string[] posts;
    FollowUnfollowLogItem[] followUnfollowLog;

    // mapping(string => bool) _followingMapping; // to be used in following function

    constructor(string memory _username) {
        username = _username;
    }

    function getUserName() public view returns (string memory) {
        return username;
    }

    function post(string memory _post) public returns (bool) {
        // TODO: error checking here, or in Python
        posts.push(_post);
        return true;
    }

    function tribs() public view returns (string[] memory) {
        return posts;
    }

    function follow(string memory userToFollow) public returns (bool) {
        // TODO: error checking, here or in Python
        // TODO: add transaction hash as unique identifier
        followUnfollowLog.push(FollowUnfollowLogItem(true, true, userToFollow));
        // isFollowing[userToFollow] = true;
        return true;
    }

    function unfollow(string memory userToUnfollow) public returns (bool) {
        // TODO: error checking, here or in Python
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
        string[] memory _following = new string[](MAX_FOLLOWING);
        uint16 _followingSize = 0;

        for (uint256 i = 0; i < followUnfollowLog.length; i++) {
            FollowUnfollowLogItem storage logItem = followUnfollowLog[i];

            if (logItem.isFollow) {
                if (Utils.getIndex(_following, logItem.whom) != -1) {
                    logItem.isValid = false;
                } else {
                    _following[_followingSize] = logItem.whom;
                    _followingSize++;
                }
            } else {
                int256 idx = Utils.getIndex(_following, logItem.whom);
                if (idx != -1) {
                    Utils.deleteAtIndexUnordered(
                        _following,
                        uint256(idx),
                        _followingSize
                    );
                    _followingSize--;
                } else {
                    logItem.isValid = false;
                }
            }
        }

        return _following;
    }

    // function
}
