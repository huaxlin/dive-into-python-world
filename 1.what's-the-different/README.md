prepare docker image

```shell
$ docker build -t ubuntu:22.04-cn -f ubuntu.Dockerfile .
$
$ docker build -t ubuntu-devel:22.04-cn -f devel.ubuntu.Dockerfile .
```


first, clean docker image

```shell
$ docker run -ti --rm -v `pwd`/code:/code ubuntu:22.04-cn bash
root@5adc36593e6d:/code# cat > hello.py <<-EOF
#!/usr/bin/env python

print("Hello Python!")
EOF
root@5adc36593e6d:/code# cat hello.py
#!/usr/bin/env python

print("Hello Python!")
root@5adc36593e6d:/code# 
root@5adc36593e6d:/code# chmod +x hello.py
root@5adc36593e6d:/code# ./hello.py
/usr/bin/env: 'python': No such file or directory
root@5adc36593e6d:/code# 
root@5adc36593e6d:/code# cat > main.go <<-EOF
package main

import ("fmt")
func main(){
    fmt.Println("Hello Golang!")
}
EOF
root@5adc36593e6d:/code# cat main.go
...
root@5adc36593e6d:/code# chmod +x main.go
root@5adc36593e6d:/code# ./main.go
./main.go: line 1: package: command not found
./main.go: line 3: syntax error near unexpected token `"fmt"'
./main.go: line 3: `import ("fmt")'
root@5adc36593e6d:/code#
```

second, in development environment:

```shell
$ docker run -ti --rm -v `pwd`/code:/code ubuntu-devel:22.04-cn bash
root@2a3eab37bffd:/code# whereis python
python: /usr/bin/python
root@2a3eab37bffd:/code# ls 
hello.py  main.go
root@2a3eab37bffd:/code# ./hello.py 
Hello Python!
root@2a3eab37bffd:/code#
root@2a3eab37bffd:/code# ./main.go 
./main.go: line 1: package: command not found
./main.go: line 3: syntax error near unexpected token `"fmt"'
./main.go: line 3: `import ("fmt")'
root@2a3eab37bffd:/code#
root@2a3eab37bffd:/code# whereis go
go: /usr/bin/go /usr/lib/go /usr/share/go
root@2a3eab37bffd:/code# go run main.go 
Hello Golang!
root@2a3eab37bffd:/code# ### Quiz: Is Golang an interpreter?
```

did you know the word "compile"?

```shell
root@2a3eab37bffd:/code#
root@2a3eab37bffd:/code# go --help 2>&1 |grep compile
	build       compile packages and dependencies
	install     compile and install packages and dependencies
	run         compile and run Go program
root@2a3eab37bffd:/code# go build main.go
root@2a3eab37bffd:/code# ./main
Hello Golang!
root@2a3eab37bffd:/code#
```

now, back into clean ubuntu:

```shell
$ docker run -ti --rm -v `pwd`/code:/code ubuntu:22.04-cn bash
root@0c4643bab591:/code# ./main
Hello Golang!
root@0c4643bab591:/code# whereis go
go:
root@0c4643bab591:/code# go run main.go
bash: go: command not found
root@0c4643bab591:/code#
```
