На вход подается строка. Нужно определить, является ли она палиндромом. 
Если строка является палиндромом - вывести Палиндром иначе - вывести Нет. 
Все входные строчки в нижнем регистре.

Палиндром — буквосочетание, слово или текст, одинаково читающееся в обоих направлениях (например, "топот", "око", "заказ").


package main

import "fmt"

func main() {
	var text, reversText string
	fmt.Scan(&text)
	for _, elem := range text {
		reversText = string(elem) + reversText
	}
	if text == reversText {
		fmt.Println("Палиндром")
	} else {
		fmt.Println("Нет")
	}
}
