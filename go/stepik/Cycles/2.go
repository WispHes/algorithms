Требуется написать программу, при выполнении которой с клавиатуры считываются два натуральных числа A и B (каждое не более 100, A < B).
Вывести сумму всех чисел от A до B  включительно.


package main

import "fmt"

func main() {
	var (
		a   int
		b   int
		sum int
	)
	fmt.Scan(&a, &b)
	for i := a; i <= b; i++ {
		sum += i
	}
	fmt.Print(sum)
}
