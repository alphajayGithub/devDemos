package main

import "fmt"

func main() { //error when single line with "{" -> syntax error: unexpected semicolon or newline before {
	/* multiple comments:
	 * 当标识符（包括常量、变量、类型、函数名、结构字段等等）以一个大写字母开头，
	 * 如：Group1，那么使用这种形式的标识符的对象就可以被外部包的代码所使用（客户端程序需要先导入这个包），
	 * 这被称为导出（像面向对象语言中的 public）；标识符如果以小写字母开头，则对包外是不可见的，
	 * 但是他们在整个包的内部是可见并且可用的（像面向对象语言中的 protected)
	 */

	fmt.Println("Hello, World!")
	fmt.Println("Google" + "Runoob")

	// %d 表示整型数字，%s 表示字符串
	var stockcode = 123
	var enddate = "2020-12-31"
	var url = "Code=%d & endDate=%s"
	var target_url = fmt.Sprintf(url, stockcode, enddate)
	fmt.Println(target_url)

}