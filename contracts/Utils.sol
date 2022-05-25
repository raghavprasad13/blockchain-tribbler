// SPDX-License-Identifier: MIT

pragma solidity ^0.8.0;

import "./Constants.sol";
import "./Tribs.sol";

library Utils {
    function isValidUsername(string memory username)
        public
        pure
        returns (bool)
    {
        if (
            bytes(username).length == 0 ||
            bytes(username).length > Constants.MAX_USERNAME_LEN
        ) return false;

        bytes memory chars = bytes(username);

        // check if the first character is a lowercase alphabet
        if (
            !(chars[0] >= 0x61 && chars[0] <= 0x7A) //a-z
        ) return false;

        // check the rest of the characters
        for (uint256 i = 0; i < chars.length; i++) {
            bytes1 char = chars[i];
            if (
                !(char >= 0x30 && char <= 0x39) && //9-0
                !(char >= 0x61 && char <= 0x7A) //a-z
            ) return false;
        }

        return true;
    }

    function exists(string[] memory arr, string memory elem)
        public
        pure
        returns (bool)
    {
        return getIndex(arr, elem) != -1;
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
        require(index < size && size > 0, "ArrayIndexOutOfBounds");

        arr[index] = arr[size - 1];
        arr.pop();

        return arr;
    }

    function deleteAtIndexUnordered(Tribs.Trib[] storage arr, uint256 index)
        public
        returns (Tribs.Trib[] memory)
    {
        uint256 size = arr.length;
        require(index < size && size > 0, "ArrayIndexOutOfBounds");

        arr[index] = arr[size - 1];
        arr.pop();

        return arr;
    }

    function deleteAtIndex(string[] storage arr, uint256 index)
        public
        returns (string[] memory)
    {
        // overloaded function that deletes element
        // at index in a string array inplace

        uint256 size = arr.length;
        require(index < size && size > 0, "ArrayIndexOutOfBounds");

        for (uint256 i = index; i < size - 1; i++) {
            arr[i] = arr[i + 1];
        }
        arr.pop();

        return arr;
    }

    function deleteAtIndex(Tribs.Trib[] storage arr, uint256 index)
        public
        returns (Tribs.Trib[] memory)
    {
        // overloaded function that deletes element
        // at index in a string array inplace

        uint256 size = arr.length;
        require(index < size && size > 0, "ArrayIndexOutOfBounds");

        for (uint256 i = index; i < size - 1; i++) {
            arr[i] = arr[i + 1];
        }
        arr.pop();

        return arr;
    }

    function deepCopy(string[] memory arr)
        public
        pure
        returns (string[] memory)
    {
        string[] memory res = new string[](arr.length);
        for (uint256 i = 0; i < arr.length; i++) res[i] = arr[i];

        return res;
    }

    function deepCopy(Tribs.Trib[] memory arr)
        public
        pure
        returns (Tribs.Trib[] memory)
    {
        Tribs.Trib[] memory res = new Tribs.Trib[](arr.length);
        for (uint256 i = 0; i < arr.length; i++) res[i] = arr[i];

        return res;
    }
}
