// SPDX-License-Identifier: MIT

pragma solidity ^0.8.0;

// library to mange string operations

library String {
    /* Function to compare two strings
     * this returns:
     * 1 if s1 < s2 i.e. s1 comes first lexicographically
     * -1 if s1 > s2 i.e. s2 comes first lexicographically
     * 0 if equal

     * keywords 
     * public: visible externally and internally (creates a getter function for storage/state variables)
     * pure: Disallows modification or access of state.
     */
    function compare(string memory s1, string memory s2)
        public
        pure
        returns (int256)
    {
        if (keccak256(abi.encodePacked(s1)) == keccak256(abi.encodePacked(s2)))
            return 0;

        // convert strings to bytes
        bytes memory b1 = bytes(s1);
        bytes memory b2 = bytes(s2);

        uint256 l1 = b1.length;
        uint256 l2 = b2.length;

        uint256 traversalLength = l1 < l2 ? l1 : l2; // take minimum of two lengths to iterate on

        for (uint256 i = 0; i < traversalLength; i++) {
            if (b1[i] < b2[i]) return 1;
            else if (b1[i] > b2[i]) return -1;
        }

        if (traversalLength == l1) return 1;
        return -1;
    }
}
