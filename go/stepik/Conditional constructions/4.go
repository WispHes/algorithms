Определите является ли билет счастливым. Счастливым считается билет, в шестизначном номере которого сумма первых трёх цифр совпадает с суммой трёх последних.

Формат входных данных

На вход подается номер билета - одно шестизначное  число.

Формат выходных данных
Выведите "YES", если билет счастливый, в противном случае - "NO".


package main

import "fmt"

func main() {
	var item int
	fmt.Scan(&item)
	var (
		a_1 = item / 100000
		a_2 = (item / 10000) % 10
		a_3 = (item / 1000) % 10
		b_1 = (item / 100) % 10
		b_2 = (item / 10) % 10
		b_3 = item % 10
	)
	var (
		first_sum  = a_1 + a_2 + a_3
		second_sum = b_1 + b_2 + b_3
	)
	switch {
	case first_sum == second_sum:
		fmt.Println("YES")
	default:
		fmt.Println("NO")
	}
}
