/*
 * @lc app=leetcode.cn id=1 lang=golang
 *
 * [1] 两数之和
 */

// @lc code=start

/*
package main

import (
	"fmt"
)

func main() {
	nums := []int{2,7,11,15}
	target := 9
	res := twoSum(nums, target)
	fmt.Println(res)
}

*/
func twoSum(nums []int, target int) []int {
    hashTable := map[int]int{}
    for i, x := range nums {
        if p, ok := hashTable[target-x]; ok {
            return []int{p, i}
        }
        hashTable[x] = i
    }
    return nil
}

// @lc code=end

