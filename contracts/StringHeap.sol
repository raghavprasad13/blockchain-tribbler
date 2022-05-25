// SPDX-License-Identifier: MIT

pragma solidity ^0.8.0;

import "./String.sol";
import "./Utils.sol";

contract StringHeap {
    string[] stringHeap;

    constructor() {
        stringHeap[0] = "";
    }

    function push(string memory str) public {
        stringHeap.push(str);
        uint256 currIndex = stringHeap.length - 1;

        while (
            currIndex > 1 &&
            String.compare(stringHeap[currIndex / 2], stringHeap[currIndex]) ==
            1
        ) {
            stringHeap[currIndex] = stringHeap[currIndex / 2];
            stringHeap[currIndex / 2] = str;

            currIndex = currIndex / 2;
        }
    }

    function pop() public returns (string memory) {
        require(stringHeap.length > 1, "StringHeap is empty");

        string memory res = stringHeap[1];

        stringHeap[1] = stringHeap[stringHeap.length - 1];
        delete stringHeap[stringHeap.length - 1];

        uint256 currIndex = 1;

        while (currIndex * 2 < stringHeap.length - 1) {
            uint256 j = currIndex * 2;

            string memory leftChild = stringHeap[j];
            string memory rightChild = stringHeap[j + 1];

            if (String.compare(leftChild, rightChild) == 1) j++;

            if (String.compare(stringHeap[currIndex], stringHeap[j]) == -1)
                break;

            string memory temp = stringHeap[currIndex];
            stringHeap[currIndex] = stringHeap[j];
            stringHeap[j] = temp;

            currIndex = j;
        }

        return res;
    }

    function getStringHeap() public returns (string[] memory) {
        require(stringHeap.length > 1, "StringHeap is empty");

        string[] memory stringHeapOriginal = Utils.deepCopy(stringHeap);
        string[] memory stringHeapRes = Utils.deleteAtIndex(stringHeap, 0);
        stringHeap = Utils.deepCopy(stringHeapOriginal);

        return stringHeapRes;
    }

    function length() public view returns (uint256) {
        return stringHeap.length - 1;
    }

    function peek() public view returns (string memory) {
        require(stringHeap.length > 1, "StringHeap is empty");
        return stringHeap[1];
    }

    function popReverse() public returns (string memory) {
        require(stringHeap.length > 1, "StringHeap is empty");
        string memory res = stringHeap[stringHeap.length - 1];

        stringHeap.pop();

        return res;
    }
}
