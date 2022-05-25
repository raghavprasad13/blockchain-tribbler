// SPDX-License-Identifier: MIT

pragma solidity ^0.8.0;

import "./Tribs.sol";
import "./Utils.sol";

contract TribHeap {
    Tribs.Trib[] tribHeap;

    constructor() {
        tribHeap[0] = Tribs.Trib("", "", 0, 0, 0); // the top of the heap will be a dummy element
    }

    function push(Tribs.Trib memory trib) public {
        tribHeap.push(trib);
        uint256 currIndex = tribHeap.length - 1;

        while (
            currIndex > 1 &&
            Tribs.compare(tribHeap[currIndex / 2], tribHeap[currIndex]) == 1
        ) {
            tribHeap[currIndex] = tribHeap[currIndex / 2];
            tribHeap[currIndex / 2] = trib;

            currIndex = currIndex / 2;
        }
    }

    function pop() public returns (Tribs.Trib memory) {
        require(tribHeap.length > 1, "TribHeap is empty");

        Tribs.Trib memory res = tribHeap[1];

        tribHeap[1] = tribHeap[tribHeap.length - 1];
        delete tribHeap[tribHeap.length - 1];

        uint256 currIndex = 1;

        while (currIndex * 2 < tribHeap.length - 1) {
            uint256 j = currIndex * 2;

            Tribs.Trib memory leftChild = tribHeap[j];
            Tribs.Trib memory rightChild = tribHeap[j + 1];

            if (Tribs.compare(leftChild, rightChild) == 1) j++;

            if (Tribs.compare(tribHeap[currIndex], tribHeap[j]) == -1) break;

            Tribs.Trib memory temp = tribHeap[currIndex];
            tribHeap[currIndex] = tribHeap[j];
            tribHeap[j] = temp;

            currIndex = j;
        }

        return res;
    }

    function getTribHeap() public returns (Tribs.Trib[] memory) {
        require(tribHeap.length > 1, "TribHeap is empty");

        Tribs.Trib[] memory tribHeapOriginal = Utils.deepCopy(tribHeap);
        Tribs.Trib[] memory tribHeapRes = Utils.deleteAtIndex(tribHeap, 0);
        tribHeap = Utils.deepCopy(tribHeapOriginal);

        return tribHeapRes;
    }

    function length() public view returns (uint256) {
        return tribHeap.length - 1;
    }

    function peek() public view returns (Tribs.Trib memory) {
        require(tribHeap.length > 1, "TribHeap is empty");

        return tribHeap[1];
    }

    function popReverse() public returns (Tribs.Trib memory) {
        require(tribHeap.length > 1, "TribHeap is empty");

        Tribs.Trib memory res = tribHeap[tribHeap.length - 1];

        tribHeap.pop();

        return res;
    }
}
