// SPDX-License-Identifier: MIT

pragma solidity ^0.8.0;

import "./Constants.sol";
import "./String.sol";
import "./Tribs.sol";

library Utils {
    /* Function to check if username parameters who and whom are same
     */
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
        require(size > 0, "EmptyArray");
        require(index < size && index >= 0, "ArrayIndexOutOfBounds");

        arr[index] = arr[size - 1]; // replace element at "index" with last element of array
        arr.pop(); // remove last element of array

        return arr;
    }

    function deleteAtIndexUnordered(Tribs.Trib[] storage arr, uint256 index)
        public
        returns (Tribs.Trib[] memory)
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

    function deleteAtIndex(Tribs.Trib[] storage arr, uint256 index)
        public
        returns (Tribs.Trib[] memory)
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

    function sort(
        string[] storage arr,
        uint256 startIndex,
        uint256 endIndex
    ) public {
        if (startIndex < endIndex) {
            uint256 mid = (startIndex + (endIndex - 1)) / 2;
            sort(arr, startIndex, mid);
            sort(arr, mid + 1, endIndex);
            merge(arr, startIndex, mid, endIndex);
        }
    }

    function merge(
        string[] storage arr,
        uint256 left,
        uint256 mid,
        uint256 right
    ) public {
        uint256 k;
        uint256 n1 = mid - left + 1;
        uint256 n2 = right - mid;

        string[] memory L = new string[](n1);
        string[] memory R = new string[](n2);

        for (uint256 i = 0; i < n1; i++) L[i] = arr[left + i];
        for (uint256 i = 0; i < n2; i++) R[i] = arr[mid + left + i];

        uint256 _i = 0;
        uint256 _j = 0;
        k = left;

        while (_i < n1 && _j < n2) {
            if (String.compare(L[_i], R[_j]) == 1) {
                arr[k] = L[_i];
                _i++;
            } else {
                arr[k] = R[_j];
                _j++;
            }
            k++;
        }

        while (_i < n1) {
            arr[k] = L[_i];
            _i++;
            k++;
        }

        while (_j < n2) {
            arr[k] = R[_j];
            _j++;
            k++;
        }
    }

    function sort(
        Tribs.Trib[] memory arr,
        uint256 startIndex,
        uint256 endIndex
    ) public {
        if (startIndex < endIndex) {
            uint256 mid = (startIndex + (endIndex - 1)) / 2;
            sort(arr, startIndex, mid);
            sort(arr, mid + 1, endIndex);
            merge(arr, startIndex, mid, endIndex);
        }
    }

    function merge(
        Tribs.Trib[] memory arr,
        uint256 left,
        uint256 mid,
        uint256 right
    ) public pure {
        uint256 k;
        uint256 n1 = mid - left + 1;
        uint256 n2 = right - mid;

        Tribs.Trib[] memory L = new Tribs.Trib[](n1);
        Tribs.Trib[] memory R = new Tribs.Trib[](n2);

        for (uint256 i = 0; i < n1; i++) L[i] = arr[left + i];
        for (uint256 i = 0; i < n2; i++) R[i] = arr[mid + left + i];

        uint256 _i = 0;
        uint256 _j = 0;
        k = left;

        while (_i < n1 && _j < n2) {
            if (Tribs.compare(L[_i], R[_j]) == 1) {
                arr[k] = L[_i];
                _i++;
            } else {
                arr[k] = R[_j];
                _j++;
            }
            k++;
        }

        while (_i < n1) {
            arr[k] = L[_i];
            _i++;
            k++;
        }

        while (_j < n2) {
            arr[k] = R[_j];
            _j++;
            k++;
        }
    }

    // Append one in-memory array to another
    function appendArray(Tribs.Trib[] memory arr1, Tribs.Trib[] memory arr2)
        public
        pure
        returns (Tribs.Trib[] memory)
    {
        Tribs.Trib[] memory res = new Tribs.Trib[](arr1.length + arr2.length);

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

    function bubbleSort(Tribs.Trib[] storage arr) public {
        uint256 i;
        uint256 j;
        uint256 n = arr.length;
        Tribs.Trib memory temp;
        for (i = 0; i < n; i++) {
            for (j = 0; j < n - i - 1; j++) {
                if (Tribs.compare(arr[j], arr[j + 1]) == -1) {
                    // arr[j+1] should appear above arr[j]
                    temp = arr[j];
                    arr[j] = arr[j + 1];
                    arr[j + 1] = temp;
                }
            }
        }
    }

    function bubbleSort_memTribs(Tribs.Trib[] memory arr)
        public
        pure
        returns (Tribs.Trib[] memory)
    {
        uint256 i;
        uint256 j;
        uint256 n = arr.length;
        Tribs.Trib memory temp;
        for (i = 0; i < n; i++) {
            for (j = 0; j < n - i - 1; j++) {
                if (Tribs.compare(arr[j], arr[j + 1]) == -1) {
                    // arr[j+1] should appear above arr[j]
                    temp = arr[j];
                    arr[j] = arr[j + 1];
                    arr[j + 1] = temp;
                }
            }
        }

        return arr;
    }
}
