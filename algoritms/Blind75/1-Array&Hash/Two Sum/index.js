/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function (nums, target) {
  const map = new Map();
  for (let i = 0; i < nums.length; i++) {
    const left = target - nums[i];
    if (map.has(left)) {
      return [i, map.get(left)];
    }
    map.set(nums[i], i);
  }
};

const testCase = [
  { input: [2, 7, 11, 15], target: 9 },
  { input: [3, 2, 4], target: 6 },
  { input: [3, 3], target: 6 },
];

for (const { input, target } of testCase) {
  const result = twoSum(input, target);
  console.log(`Input: ${JSON.stringify(input)}`);
  console.log(`Output: ${result} | Expected: ${target}\n`);
}
