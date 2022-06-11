// SPDX-License-Identifier: MIT

pragma solidity ^0.8.0;

// Library of utility functions

library Utils {
    uint16 public constant MAX_USERNAME_LEN = 15;
    uint16 public constant MAX_FOLLOWING = 2000;
    uint16 public constant MAX_TRIB_FETCH = 100;
    uint16 public constant MIN_LIST_USER = 20;
    uint16 public constant MAX_TRIB_LEN = 140;

    /* Function to compare two strings
     * this returns:
     * 1 if s1 < s2 i.e. s1 comes first lexicographically
     * -1 if s1 > s2 i.e. s2 comes first lexicographically
     * 0 if equal

     * keywords 
     * public: visible externally and internally (creates a getter function for storage/state variables)
     * pure: Disallows modification or access of state.
     */
    function string_compare(string memory s1, string memory s2)
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

    struct Trib {
        string who;
        string message;
        uint256 timestamp;
        uint256 blockNum;
        uint256 txIndex; // because we cannot get txIndex. Update: we can get txIndex, but then the operation will have to be broken up into 2 transactions
    }

    function trib_compare(Trib memory t1, Trib memory t2)
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
                    if (string_compare(t1.who, t2.who) == 1) return 1;
                    else if (string_compare(t1.who, t2.who) == -1) return -1;

                    // compare messages
                    return string_compare(t1.message, t2.message);
                }
            }
        }
    }

    function getIndex(string[] memory arr, string memory elem)
        public
        pure
        returns (int256)
    {
        for (uint256 i = 0; i < arr.length; i++) {
            if (
                keccak256(abi.encodePacked(arr[i])) ==
                keccak256(abi.encodePacked(elem))
            ) return int256(i);
        }
        return -1;
    }

    // NOTE: All of the delete functions delete data inplace and therefore perform array resizing

    // Use this function if you want to delete the element at the specified
    // index but you don't care about the order of the elements in the array
    // This is more efficient than deleteAtIndex and should be used to save gas
    function deleteAtIndexUnordered(string[] storage arr, uint256 index)
        public
        returns (string[] memory)
    {
        uint256 size = arr.length;
        require(size > 0, "EmptyArray");
        require(index < size && index >= 0, "ArrayIndexOutOfBounds");

        arr[index] = arr[size - 1]; // replace element at "index" with last element of array
        arr.pop(); // remove last element of array

        return arr;
    }

    function deleteAtIndexUnordered(Trib[] storage arr, uint256 index)
        public
        returns (Trib[] memory)
    {
        uint256 size = arr.length;
        require(size > 0, "EmptyArray");
        require(index < size && index >= 0, "ArrayIndexOutOfBounds");

        arr[index] = arr[size - 1];
        arr.pop();

        return arr;
    }

    // delete element at given index and shift all the other elements in the same order
    function deleteAtIndex(string[] storage arr, uint256 index)
        public
        returns (string[] memory)
    {
        uint256 size = arr.length;
        require(size > 0, "EmptyArray");
        require(index < size && index >= 0, "ArrayIndexOutOfBounds");

        for (uint256 i = index; i < size - 1; i++) {
            // i goes till size-2 so that i+1 goes till size-1
            arr[i] = arr[i + 1];
        }
        arr.pop();

        return arr;
    }

    function deleteAtIndex(Trib[] storage arr, uint256 index)
        public
        returns (Trib[] memory)
    {
        uint256 size = arr.length;
        require(size > 0, "EmptyArray");
        require(index < size && index >= 0, "ArrayIndexOutOfBounds");

        for (uint256 i = index; i < size - 1; i++) {
            // i goes till size-2 so that i+1 goes till size-1
            arr[i] = arr[i + 1];
        }
        arr.pop();

        return arr;
    }

    // Append one in-memory array to another
    function appendArray(Trib[] memory arr1, Trib[] memory arr2)
        public
        pure
        returns (Trib[] memory)
    {
        Trib[] memory res = new Trib[](arr1.length + arr2.length);

        uint256 i;
        for (i = 0; i < arr1.length; i++) {
            res[i] = arr1[i];
            if (i < arr2.length) res[i + arr1.length] = arr2[i];
        }

        while (i < arr2.length) {
            res[i + arr1.length] = arr2[i];
            i++;
        }

        return res;
    }
}
