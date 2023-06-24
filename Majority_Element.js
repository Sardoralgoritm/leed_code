/**
 * @param {number[]} nums
 * @return {number}
 */
var majorityElement = function(nums) {
    let count = 0
    let max = 0
    let element;
    for(let i=0; i<nums.length; i++)
    {
        for(let j=i; j<nums.length; j++)
        {
            if(nums[i] == nums[j])
            {
                count += 1
            }
            if(count > max)
            {
                max = count
                element = nums[i]
            }
        }
        count = 0
    }
    return element
};
