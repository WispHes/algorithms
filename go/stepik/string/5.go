Дается строка. Нужно удалить все символы, которые встречаются более одного раза и вывести получившуюся строку

package main

import (
	"fmt"
	"strings"
)

func main() {
	var item string
	fmt.Scan(&item)
	for i := 0; i < len(item); i++ {
		if strings.Count(item, string(item[i])) < 2 {
			fmt.Print(string(item[i]))
		}
	}
}
