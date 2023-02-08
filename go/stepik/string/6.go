Ваша задача сделать проверку подходит ли пароль вводимый пользователем под заданные требования. 
Длина пароля должна быть не менее 5 символов, он должен содержать только арабские цифры и буквы латинского алфавита. 
На вход подается строка-пароль. 
Если пароль соответствует требованиям - вывести "Ok", иначе вывести "Wrong password"


package main

import (
	"fmt"
	"unicode"
)

func body(item string) string {
	if len(item) >= 5 {
		for i := 0; i < len(item); i++ {
			if unicode.IsDigit(rune(item[i])) || unicode.Is(unicode.Latin, rune(item[i])) {
				continue
			} else {
				return "Wrong password"
			}
		}
		return "Ok"
	} else {
		return "Wrong password"
	}
}

func main() {
	var item string
	fmt.Scan(&item)
	fmt.Println(body(item))
}
