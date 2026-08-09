func isAnagram(s string, t string) bool {
	letters := [26]int{}
	if len(s) != len(t) {
		return false
	}

	for _, c := range s {
		index := int(c - 'a')

		letters[index]++
	}

	for _, c := range t {
		index := int(c - 'a')

		letters[index]--
	}

	for _, l := range letters {
		if l > 0 {
			return false
		}
	}

	return true
}
