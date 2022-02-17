package main
import "fmt"
func main(){
    str := "[[\"[2,7,11,15]\",\"9\"]]"
    arr := parseStringArrArr(str)
    for i:=0;i<len(arr);i++ {
        unitArgs:=arr[i]
        arg0 := parseIntegerArr(unitArgs[0]);
        arg1 := parseInteger(unitArgs[1]);
        result := twoSum(arg0,arg1);
        resultabc :=serializeInterface(result);
        fmt.Printf("resultabc%d:%sresultend", i,resultabc)
    }
}