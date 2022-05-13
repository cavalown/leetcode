//? 2. Add Two Numbers
// You are given two non - empty linked lists representing two non - negative integers.The digits are stored in reverse order, and each of their nodes contains a single digit.Add the two numbers and return the sum as a linked list.
// You may assume the two numbers do not contain any leading zero, except the number 0 itself.

const addTwoNumbers = function (l1, l2) { 
    let sum = parseInt(l1.reverse().join('')) + parseInt(l2.reverse().join(''));
    let result = sum.toString().split('').reverse();
    console.log(result);
    return result
};

addTwoNumbers([2, 4, 3], [5, 6, 4])
addTwoNumbers([0], [0])
addTwoNumbers([9, 9, 9, 9, 9, 9, 9], [9, 9, 9, 9])

//! ex1:
// Input: l1 = [2, 4, 3], l2 = [5, 6, 4]
// Output: [7, 0, 8]
// Explanation: 342 + 465 = 807.

//! ex2:
// Input: l1 = [0], l2 = [0]
// Output: [0]

//! ex3:
// Input: l1 = [9, 9, 9, 9, 9, 9, 9], l2 = [9, 9, 9, 9]
// Output: [8, 9, 9, 9, 0, 0, 0, 1]