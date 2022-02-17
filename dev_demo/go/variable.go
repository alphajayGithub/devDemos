package main

import "fmt"

var swapA, swapB int

func main() {
	//var identifier1, identifier2 type
	var a string = "Runoob"
	var b, c int = 1, 2
	fmt.Println(a)
	fmt.Println(b, c)

	// 没有初始化就为零值
	var d int
	fmt.Println(d)

	// bool 零值为 false
	var e bool
	fmt.Println(e)

	var i int
	var f float64
	var check bool
	var s string
	fmt.Printf("uninit %v %v %v %q\n", i, f, check, s)

	var dd = true
	fmt.Println(dd)

	initVal := 1
	// :=是声明 等同于 var intVal int； intVal=1
	initVal1, initVal2, initVal3 := 1, "test", &initVal

	fmt.Println(initVal, initVal1, initVal2, initVal3)

	swapA = 111
	swapB = 222
	fmt.Print(swapA, swapB)

	swapA, swapB = swapB, swapA
	fmt.Print("\nswap\n")

	fmt.Print(swapA, swapB)
	/*
		var a1 *int
		var a2 []int
		var a3 map[string]int
		var a4 chan int
		var a5 func(string) int
		var a6 error
	*/

}
