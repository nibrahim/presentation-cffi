libleftpad.so: leftpad.c
	gcc -fPIC -shared -std=gnu11 -Wall -Wextra -Wunused -o $@ $^

leftpad: leftpad.c
	gcc -Wall -fprofile-arcs -ftest-coverage -o $@ $^
