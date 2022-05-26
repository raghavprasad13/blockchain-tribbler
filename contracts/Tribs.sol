// SPDX-License-Identifier: MIT

pragma solidity ^0.8.0;

import "./String.sol";

library Tribs {
    struct Trib {
        string who;
        string message;
        uint256 timestamp;
        uint256 blockNum;
        uint256 txIndex; // because we cannot get txIndex. Update: we can get txIndex, but then the operation will have to be broken up into 2 transactions
    }

    function compare(Trib memory t1, Trib memory t2)
        public
        pure
        returns (int256)
    {
        // this returns:
        // 1 if t1 > t2; i.e. t1 appears above t2
        // -1 if t1 < t2; i.e. t2 appears above t1
        // 0 if t1 == t2

        // Tribble order is:
        // Trib with higher block number appears on top; if equal
        // Trib with higher tx index number appears on top; if equal
        // Trib with higher timestamp appears on top; if equal
        // Trib with lexicographically first username appears on top; if equal
        // Trib with lexicographically first message appears on top; if equal
        // order it any way

        // In our implementation, we have chosen to stop at the comparison of timestamps because
        // comparing strings lexicographically is unnecessarily expensive and will consume gas

        // compare blockNum
        if (t1.blockNum > t2.blockNum) return 1;
        else if (t1.blockNum < t2.blockNum) return -1;
        else {
            // compare txIndex
            if (t1.txIndex > t2.txIndex) return 1;
            else if (t1.txIndex < t2.txIndex) return -1;
            else {
                // compare timestamp
                if (t1.timestamp > t2.timestamp) return 1;
                else if (t1.timestamp < t2.timestamp) return -1;
                else {
                    // compare usernames
                    if (String.compare(t1.who, t2.who) == 1) return 1;
                    else if (String.compare(t1.who, t2.who) == -1) return -1;

                    // compare messages
                    return String.compare(t1.message, t2.message);
                }
            }
        }
    }
}
