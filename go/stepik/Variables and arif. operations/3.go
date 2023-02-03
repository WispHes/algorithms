По данному целому числу, найдите его квадрат.

package main

import "fmt"

func main() {
	var x int
	fmt.Scan(&x)
	x *= x
	fmt.Print(x)
}
