Даются две строки X и S. Нужно найти и вывести первое вхождение подстроки S в строке X. 
Если подстроки S нет в строке X - вывести -1


package main

import (
	"fmt"
	"strings"
)

func main() {
	var text, subString string
	fmt.Scan(&text, &subString)
	fmt.Println(strings.Index(text, subString))
}
