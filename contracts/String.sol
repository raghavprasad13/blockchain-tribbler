// SPDX-License-Identifier: MIT

pragma solidity ^0.8.0;

library String {
    function compare(string memory s1, string memory s2)
        public
        pure
        returns (int256)
    {
        // this returns:
        // 1 if s1 < s2
        // -1 if s1 > s2
        // 0 if equal
        if (keccak256(abi.encodePacked(s1)) == keccak256(abi.encodePacked(s2)))
            return 0;

        bytes memory b1 = bytes(s1);
        bytes memory b2 = bytes(s2);

        uint256 l1 = b1.length;
        uint256 l2 = b2.length;

        uint256 traversalLength = l1 < l2 ? l1 : l2;

        for (uint256 i = 0; i < traversalLength; i++) {
            if (b1[i] < b2[i]) return 1;
            else if (b1[i] > b2[i]) return -1;
        }

        if (traversalLength == l1) return 1;
        return -1;
    }
}
