func twoSum(A []int, target int) []int {
    m1 := make(map[int]int)
    for i, num := range A {
        value, exists := m1[target - num]
        if exists {
            return []int{value, i}
        } else {
            m1[num] = i
        }
    }
    return []int{}
}