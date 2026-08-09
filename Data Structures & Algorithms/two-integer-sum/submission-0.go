func twoSum(nums []int, target int) []int {
	seen := map[int]int{}

	for idx, n := range nums {
		if oIdx, ok := seen[target-n]; ok {
			return []int{oIdx, idx}
		}

		seen[n] = idx
	}

	return []int{-1, -1}
}
