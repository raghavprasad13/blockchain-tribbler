// SPDX-License-Identifier: MIT

pragma solidity ^0.8.0;

import "./Constants.sol";
import "./Tribs.sol";

library Utils {
    function whoWhomSame(string memory who, string memory whom)
        public
        pure
        returns (bool)
    {
        return
            keccak256(abi.encodePacked(who)) ==
            keccak256(abi.encodePacked(whom));
    }

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
        // This returns a "memory" copy of a string[] variable

        string[] memory res = new string[](arr.length);
        for (uint256 i = 0; i < arr.length; i++) res[i] = arr[i];

        return res;
    }

    function deepCopy(string[] memory arr, string[] storage copy) public {
        // This copies from "memory" string[] variable to "storage" string[] variable
        // Take care that copy is empty before passing it in here

        for (uint256 i = 0; i < arr.length; i++) copy.push(arr[i]);
    }

    function deepCopy(Tribs.Trib[] memory arr)
        public
        pure
        returns (Tribs.Trib[] memory)
    {
        // This returns a "memory" copy of a Tribs.Trib[] variable

        Tribs.Trib[] memory res = new Tribs.Trib[](arr.length);
        for (uint256 i = 0; i < arr.length; i++) res[i] = arr[i];

        return res;
    }

    function deepCopy(Tribs.Trib[] memory arr, Tribs.Trib[] storage copy)
        public
    {
        // This copies from "memory" Tribs.Trib[] variable to "storage" Tribs.Trib[] variable
        // Take care that copy is empty before passing it in here

        for (uint256 i = 0; i < arr.length; i++) copy.push(arr[i]);
    }

    function mergeSortedArrays(
        Tribs.Trib[] memory arr1,
        Tribs.Trib[] memory arr2
    ) public pure returns (Tribs.Trib[] memory) {
        uint256 n1 = arr1.length;
        uint256 n2 = arr2.length;

        Tribs.Trib[] memory resArr = new Tribs.Trib[](n1 + n2);

        uint256 i;
        uint256 j;
        uint256 k;

        while (i < n1 && j < n2) {
            if (Tribs.compare(arr1[i], arr2[j]) == 1) {
                resArr[k] = arr1[i];
                k++;
                i++;
            } else {
                resArr[k] = arr2[j];
                k++;
                j++;
            }
        }

        while (i < n1) {
            resArr[k] = arr1[i];
            k++;
            i++;
        }

        while (j < n2) {
            resArr[k] = arr2[j];
            k++;
            j++;
        }

        return resArr;
    }
}
