 На вход дается строка, из нее нужно сделать другую строку, оставив только нечетные символы (считая с нуля)

package main
import "fmt"

func main() {
	var item string
    fmt.Scan(&item)
	for i := 1; i < len(item); i += 2 {
		fmt.Print(string(item[i]))
	}
}
