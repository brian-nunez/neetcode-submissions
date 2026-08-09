func isAnagram(s string, t string) bool {
	letters := [26]int{}
	if len(s) != len(t) {
		return false
	}

	for i := range s {
		sIndex := int(s[i] - 'a')
		tIndex := int(t[i] - 'a')

		letters[sIndex]++
		letters[tIndex]--
	}

	for _, l := range letters {
		if l > 0 {
			return false
		}
	}

	return true
}
