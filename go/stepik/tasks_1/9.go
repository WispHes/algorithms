Цифровой корень
Цифровой корень натурального числа — это цифра,полученная в результате итеративного процесса суммирования цифр,
на каждой итерации которого для подсчета суммы цифр берут результат, полученный на предыдущей итерации. 
Этот процесс повторяется до тех пор, пока не будет получена одна цифра.

Например цифровой корень 65536 это 7 , потому что 6+5+5+3+6=25 и 2+5=7 . 
По данному числу определите его цифровой корень.

Входные данные
Вводится одно натуральное число n, не превышающее 10^7

Выходные данные
Вывести цифровой корень числа n.


package main

import "fmt"

func main() {
	var item, res int
	fmt.Scan(&item)
	for i := item; i != 0; i /= 10 {
		res += item % 10
		item /= 10
	}
	fmt.Print(res/10 + res%10)
}
