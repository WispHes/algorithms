Напишите программу, которая считывает целые числа с консоли по одному числу в строке.

Для каждого введённого числа проверить:

если число меньше 10, то пропускаем это число;
если число больше 100, то прекращаем считывать числа;
в остальных случаях вывести это число обратно на консоль в отдельной строке.


package main

import "fmt"

func main() {
	var item int
	for fmt.Scan(&item); item <= 100; fmt.Scan(&item) {
		if item >= 10 {
			fmt.Println(item)
		}
	}
}