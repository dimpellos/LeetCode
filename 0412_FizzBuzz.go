func fizzBuzz(n int) []string {
    var mySlice []string
    for i := 1; i <= n;i++ {
        s := ""
        if i%3 == 0 {
            s += "Fizz"
        }
        if i%5 == 0 {
            s += "Buzz"
        }
        if s != "" {
            mySlice = append(mySlice, s)
        } else
        {
            mySlice = append(mySlice, strconv.Itoa(i))
        }
    }
    return mySlice
}