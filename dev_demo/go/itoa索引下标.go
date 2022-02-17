package main

import "fmt"

const (
	i = 1 << iota // 1<<0
	j = 3 << iota // 11 -> 110=6
	k             // k = 3 << iota
	l             // l = 3 << iota
)

func main() {
	const (
		a = iota //0
		b        //1
		c        //2
		d = "ha" //独立值，iota += 1
		e        //"ha"   iota += 1
		f = 100  //iota +=1
		g        //100  iota +=1
		h = iota //7,恢复计数
	)

	println(a, b, c, d, e, f, g, h)

	fmt.Println("i=", i)
	fmt.Println("j=", j)
	fmt.Println("k=", k)
	fmt.Println("l=", l)
}
