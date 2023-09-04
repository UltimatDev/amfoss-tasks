package main

import (
	"fmt"
)

func isPrime(n int) bool {

	for i := 2; i < ((n)/2)+1; i++ {
		if n%i == 0 && n != i {
			return false
		}

	}
	return true

}

func main() {

	var i int
	fmt.Println("Hello World!")
	fmt.Scanf("%v", &i)
	for x := 2; x <= i; x++ {
		var check bool = isPrime(x)
		if check {
			fmt.Println(x)
		}

	}
}
