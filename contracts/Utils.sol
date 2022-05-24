// SPDX-License-Identifier: MIT

pragma solidity ^0.8.0;

library Utils {
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

    // Use this function if you want to delete the element at the specified
    // index but you don't care about the order of the elements in the array
    // This is more efficient than deleteAtIndex and should be used to save gas
    function deleteAtIndexUnordered(
        string[] memory arr,
        uint256 index,
        uint256 size
    ) public pure {
        require(index < size && size > 0, "ArrayIndexOutOfBounds");

        arr[index] = arr[size - 1];
        delete arr[size - 1];
    }

    function deleteAtIndex(
        string[] memory arr,
        uint256 index,
        uint256 size
    ) public pure {
        require(index < size && size > 0, "ArrayIndexOutOfBounds");

        for (uint256 i = index; i < size - 1; i++) {
            arr[i] = arr[i + 1];
        }
        delete arr[size - 1];
    }
}
