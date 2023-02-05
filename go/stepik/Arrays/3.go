На ввод подаются пять целых чисел, которые записываются в массив.
Вам нужно написать фрагмент кода, с помощью которого можно найти и вывести максимальное число в этом массиве.


package main
import "fmt"

func main()  {
	array := [5]int{}
	var a int
	for i:=0; i < 5; i++{
		fmt.Scan(&a)
		array[i] = a
	}
    var item int = array[0]
    for index := range array{
        if array[index] > item{
            item = array[index]
        }
    }
    fmt.Println(item)
}
