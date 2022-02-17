package main

import (
	"fmt"
	"unsafe"
)

const (
	a = "global"
	b = len(a)
	c = unsafe.Sizeof(a)
)

const (
	Unknown = 0
	Female  = 1
	Male    = 2
)

func main() {
	const LENGTH int = 10
	const WIDTH int = 5
	var area int
	println(a, b, c)
	const a, b, c = 1, false, "str" //多重赋值
	println(a, b, c)

	// LENGTH = 20 -> cannot assign to LENGTH (declared const)
	area = LENGTH * WIDTH
	fmt.Printf("面积为 : %d", area)

}
