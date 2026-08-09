type Node struct {
	Value int
	Next  *Node
}

type LinkedList struct {
	Head *Node
	Tail *Node
	Size int
}

func NewLinkedList() *LinkedList {
	return &LinkedList{}
}

func (ll *LinkedList) Get(index int) int {
	if index < 0 || index >= ll.Size {
		return -1
	}

	curr := ll.Head

	for range index {
		curr = curr.Next
	}

	return curr.Value
}

func (ll *LinkedList) InsertHead(val int) {
	node := &Node{Value: val, Next: ll.Head}

	if ll.Head == nil {
		ll.Tail = node
	}

	ll.Head = node
	ll.Size++
}

func (ll *LinkedList) InsertTail(val int) {
	node := &Node{Value: val}

	if ll.Tail == nil {
		ll.Head = node
		ll.Tail = node
		ll.Size++

		return
	}

	ll.Tail.Next = node
	ll.Tail = node
	ll.Size++
}

func (ll *LinkedList) Remove(index int) bool {
	if index < 0 || index >= ll.Size {
		return false
	}

	if index == 0 {
		ll.Head = ll.Head.Next
		ll.Size--

		if ll.Size == 0 {
			ll.Tail = nil
		}

        return true
	}

	curr := ll.Head

	for range index - 1 {
		curr = curr.Next
	}

	curr.Next = curr.Next.Next

	if index == ll.Size-1 {
		ll.Tail = curr
	}

	ll.Size--

	return true
}

func (ll *LinkedList) GetValues() []int {
	arr := []int{}

	curr := ll.Head

	for curr != nil {
		arr = append(arr, curr.Value)
		curr = curr.Next
	}

	return arr
}
