На вход подается строка. Нужно определить, является ли она правильной или нет. 
Правильная строка начинается с заглавной буквы и заканчивается точкой. 
Если строка правильная - вывести Right иначе - вывести Wrong


package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
	"unicode"
)

func main() {
	text, _ := bufio.NewReader(os.Stdin).ReadString('\n')
	rs := []rune(text)
	if unicode.IsUpper(rs[0]) && strings.HasSuffix(text, ".") {
		fmt.Print("Right")
	} else {
		fmt.Print("Wrong")
	}
}
