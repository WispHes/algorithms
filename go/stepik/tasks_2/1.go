На вход подаются a и b - катеты прямоугольного треугольника. Нужно найти длину гипотенузы

package main

import (
	"fmt"
	"math"
)

func main() {
	var a, b int
	_, err := fmt.Scan(&a, &b)
	if err != nil {
		fmt.Println("Error")
	} else {
		fmt.Println(math.Sqrt(float64(a*a + b*b)))
	}
}
