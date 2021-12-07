# C Lang Supplement Knowledge (Review)

[C Lang](https://www.bilibili.com/video/BV1Q44y1x7Q4)



### printf and scanf

- `“%d”, x`: integer; `%f`: floating point number; `%lf`: double precision number; `%.2f`: fp with 2 decimal digits; `%g`: scientific; `%%`: `%` in output; `%s`: string.
- `\t`: tab; `\n`: enter
- In `scanf`: the input should add `&` before the var. name

### Pre-definitions

See ‘Pre-processor’ for more

- **Header fies**: `#include<>`

  - `stdio.h`: Standard input / output
  - `math.h`: Spec. math requires (`sqrt`)
  - `stdlib.h`: Dynamic allocation requires (`malloc()`)
  - `string.h`: String operations (`strcopy`, …)

- Use `#define MANY 5` and apply `i < MANY` and `printf("%d", MANY)`, etc. to pre-define and easy to modify 

  Better to use all UPPER-CASE

### Data Types

#### **int**

`sizeof(char) = 1` (byte = 8 bit (0 / 1))

`char <= short <= int (~4) <= long`

- `int`: -2^-31^, … , -1, 0, 1, … , 2^31^ - 1

- `unsigned(int)`: 0, 1, …, 2^32^ - 1 (int but no negative values)

  If need to use limit values, `<limits.h>`: `INT_MIN`, `INT_MAX`, `UINT_MAX`

#### **ASCII** 

(and Extended ASCII): 48(0) 49(1) … 65(A) … 97(a) … 127(DEL)

#### **float**

`float (~4; >=6 decimal number) <= double (~8; >=10) <= long double (>=10)`

Sign + Exp + matissa

#### Conversion / Promotion 

`char -> short -> int -> long -> float -> double`

### Expressions

- **Summing**: `sum += num` equiv to `sum = sum + num`

  `i = i+1` equiv to `i++` / `i += 1` (`++i`: Plus then use; `i++`: Use then plus)

- Unary: `++i`, `-x`
- Binary: `a*b`, `a == b`
- Ternary: `a<0 ? -a:b` (if a<0 => -a; no => b)

### Operations

- `%`: mod
- `0 < b < 8`: means `(return(0<b)) < 8` (for b = -1, `0<b` False => 0; `0<8` True => 1)

#### Priority

1. `()`
2. `++` / `--` / `+` / `-` (signs) / (types)
3. `*` / `/` / `%`
4. `+` / `-`
5. `<` / `<=` / `>` / `>=`
6. `==` / `!=`
7. `&&`
8. `||`
9. `?=`
10. `=` / `+=` / …

### if & Switch

- `if` - `else if` - `else`

  `if(0)`: won’t execute

- **Switch**

  ``` c
  switch (exp)	// must return an integer
  {
      case value_1: ....
          break;
      case value_2: ....
          break;
  
      ....
              
      default: ....	// optional            
  }
  ```

#### **Example**: Calculator

``` c
#include <stdio.h>

int main() 
{
    char op;
    int num1, num2, res;
    scanf("%d %c %d", &num1, &op, &num2);
    switch(op) {
        case '+': res = num1 + num2; break;
        case '-': res = num1 - num2; break;
        case '*': res = num1 * num2; break;
        case '/': res = num1 / num2; break;
        default: printf("Error: unknown operation.\n"); return 1;
    }
    printf(....);
    return 0;
}
```

### Bool

Use `#include<stdbool.h>` to apply bool type var. (logic)

Usually don’t mix with other types of data.

``` c
#include <stdbool.h>

int main(){
    int n;
	scanf("%d", &n);
    bool notZero = n;	// n not zero => true; n is zero => false (int->bool)
    if(notZero) {
        printf("n is non-zero!\n");
    }
}
```

`!5`: 0;	`!!5`: 1;	`5 && 0`: 0;	`5 && 'A'`: 1;	`5 || -5`: 1;	`5 || 0`: 1

### Loops

- **while**:

  ``` c
  while(exp)
      statement;
  ```

- **do while**: (at least 1 loop will be done)

  ``` c
  do
      statement;
  while(exp)
  ```

- **for**:

  ``` c
  for (exp1; exp2; exp3)	// usually only with `i`
      statement;
  ```

  Similar to while loop:

  ``` c
  exp1;	// `exp1` initializes the loop
  while (exp2) {	// `exp2` is the condition to check
      statement;
      exp3;	// `exp3` is the extra operation
  }
  ```

- **break**: jump out of the current {}

- **continue**: jump out of the current iteration (and jump to another new iteration) - Only in loops

#### **Example**: Factorial loop

``` c
#include<stdio.h>

int main() 
{
    int n;
    if (scanf("%d", &n) < 1)
        printf("Input error.\n")
        return 1;
    if (n > MAX4FACT)
        printf("Too big a number.\n")
        return 2;
    int i = 2;
    int factorial = 1; // at most `12!`
    
    /* while loop
    while (i <= n) {
        factorial *= 1;	 // or just `factorial *= i++`
        i++;	// or `++i`
    }  */
    
    // for loop
    for (; i <= n; i++) {
        factorial *= 1;
    }
    
    printf("%d! = %d", n, factorial);
    return 0;
}
```

#### **Example**: Greatest Common Divisor

``` c
#include <stdio.h>

int main() {
    int m, n;
    scan("%d%d", &m, &n);
    if(m == 0 && n == 0)	printf("Input error.\n");
    int m_orig = m, n_orig = n;
    if(m < 0)	m = -m;
    if(n < 0)	n = -n;
    while (n != 0) {
        int temp = m % n;
        m = n;
        n = temp;
    }
    printf("The gcd of %d and %d is %d", m_orig, n_orig, m);
    return 0;        
}
```

#### **Example**: Check prime

``` c
#include<stdio.h>
#include<math.h>

int main() 
{
    int n;
    scanf("%d", &n);
    int n_orig = n;
    if (n < 0)	n = -n;
    int is_prime = 1;
    if (n < 2 || n != 2 && n % 2 == 0)
        is_prime = 0;
    else {
        for (int i = 3; i < sqrt(n) + 0.5; i += 2) {
            if (n % i == 0) {
                is_prime = 0;
                break;                    
            }
        }
    }
    printf("%d is %sa prime\n", n_orig, is_prime ? "": "not ");
    // if is a prime => %s = ""; if not %s = "not " 
    return 0;
}
```

### Array

#### 1D Array

`int grades[800]`: Array with 800 elements: `grades[0]` ~ `grades[799]`

The length should be an integer, it can’t be a var.

##### **Initialization**

- ``` c
  for(i = 0; i < 800; i++) 
      scanf("%lf", &grades[i]);
  ```

- ``` c
  int grades[5] = {100, 97, 79, 0, 0};	// few elements
  ```

- ``` c
  int grades[5] = {100, 97, 79};	// defines the first 3 elem (last 2 as 0 defaultly)
  ```

- ``` c
  int grades[] = {100, 97, 79, 0, 0};		//equiv to the above 2
  ```

##### Example: Sieve

``` c
#include <stdio.h>
#include <math.h>

#define N 37	// output all prime numbers under 37

int main() {
    int sqrt_N = sqrt(N) + 0.5;
    bool prime[N+1] = {false, false};	// 0 and 1 are not prime
    for (int i = 2; i < N+1; ++i) {
         prime[i] = true;
    }
    for (int p = 2; p <= sqrt_N; ++p) {
        if (prime[p]) {
            for (int i = p; i*p <= N; ++i) {
                prime[i*p] = false;
            }
        }
    }
    printf("The prime numbers below %d are \n", N);
    for (int i = 2; i <= N; i++) {
        if (prime[i]) {
            printf("%d ", i);
        }
    }
}
```

#### 2D Array

##### Initialization

- `double matrix[2][3] = {{1, 2, 3}, {4, 5, 6}};`	(2 lines, 3 col)
- `double mat[2][3] = {{0}};`

##### Example: Blur a Picture

Pixel -> RGB Values

**Blur**: Average color with neighbors

``` c
#include <stdio.h>

#define N 10
#define M 10
#define FALSE 0
#define TRUE 1

int inBound(int i, int j);
int meanAroundPixel(int picture[N][M], int i, int j);
void copy2dArray(int to[N][M], int from[N][M]);			// in the declaration of high dim arrays
void bluePicture(int picture[N][M]);					// from the 2nd dim on, the size should be spec.

int main()
{
    ...
    int picture [N][M] = {...};
    blurPicture(picture);
    ...
}

int inBound(int i, int j) 
{	// in the allowed range
    return (	j >= 0 && j < N 
             && j >= 0 && j < M);
}

int meanAroundPixel(int picture[N][M], int ii, int jj)
{
    int di, dj, sum = 0, neighbours = 0;
    for (di = -1; di <= 1; ++di)
        for (dj = -1; dj <= 1; ++dj)
            if (inBound(ii+di, jj+dj)) {
                sum += picture[ii+di][jj+dj];
                neighbours++;
            }
    return (int)((double)sum / neighbours + 0.5);
}

void copy2dArray(int to[][M], int from[][M])
{
    int i, j;
    for (i = 0; i < N; ++i)
        for (j = 0; j < M; ++j)
            to[i][j] = from[i][j];
    return;
}

void blurPicture(int picture[][M])
{
    int ii, jj;
    int blurred[N][M];
    for (ii = 0; ii < N; ++ii)
        for (jj = 0; jj < M; ++jj)
            blurred[ii][jj] = meanAroundPixel(picture, ii, jj);
    copy2dArray(picture, blurred);
    return;
}
```

### Function

- `int` & `void`: return or not return a value

- if want to use a function, declare first: `void xxx();` before the main function

  `long power(int, int)` / `long power(int base, int exp)` 

``` c
return-type fcn-name(par-list)
{
    var. def.;
    statements;
    return sta;
}
```

Call by value (the var. in main and in function is not the same)

### Variable

- **Duration**: temp / fixed

- **Scope**: local / global 

  generally, in loops / functions will be local; define at first in the main func will be global

  In a smaller scope of `{}`, if a var (w/ the same name) has been re-defined, in this scope and in smaller scopes will be the re-defined value; if not re-defined, use the value in the larger scope.

#### Types

- **Global var.**: Global, defined until the program finishes

  Defines at the real beginning of a program (right after `#include<>` and other macros, before any function declaration)

  If re-defines in a function w/ a same name, it will be covered.

- **Static var.**: Global, defined until the program finishes

  `static data_type data` in some function, after this function, the static var. will still be valid.

  Useful when counting the function run account

#### Stack

Last in first out (LIFO) - Usually stores local var.

Attention that due to the existance of the stacks, the functions are called by value, the value cannot pass from the smaller scope to the larger scope.

### Pointer

#### Example: Swap

Use `*a` to point to the var. `a`'s position 

``` c
void swap(int* a, int* b) {	// actually swap the 2 addresses
    int temp = *a;			// temp now points to the position where stores a
    *a = *b;				// &a (address) -> a (var/value); &b -> b
    *b = temp;
    return;
}

int main()
{
    int a = 3, b = 5;
    swap(&a, &b);	// extract the address of a and b
    printf("a = %d, b = %d", a, b);
    return 0;
}
```

#### Definition

`type *`: pointer to the type

(`*p`: **p is a pointer** pointing to sth; `&a`: **a is a variable** and this is its address; `p = &a`:OK; `y = *p`: y is now the value of a; `*p = 7`: OK, a = 7)

```c
char c;
char *cp1, *cp2 = &c;
```

#### Return Multiple

Void cannot return value, but if use pointers, it can be used to “return” multiple values

#### Generic Pointer: void*

- Point to nothing: `int *p = NULL;`
- Temporally need a pointer but cannot define yet: `void *p2;`

``` c
int a = 5, b, *p1;
char c = 'x';
void *p2, *p3 = &c;		// generic, can be used as a pointer of any type of data 
p1 = &a; 
p2 = p1;
b = *p1 + *(int*)p2;	// to use an undefined pointer, still need to add the type

// sizeof(*p1) = sizeof(int)
// sizeof(*p2) not defined
```

#### Operations

- Constant movement: `+/- n`: Move `n*sizeof()` bytes
- `++`, `--`, `+=`, `-=`: OK
- `-`: Ok if same “entity” (e.g. array): continuous
- `+`, `*`, `/`: Cannot!

``` c
int *p, *q;
p = 300; q = 400;
// p + 1 == p++ == 304; p + 2 == 308 (sizeof(int) = 4); q - p == 25;
// (char*)p + 2 == 302; (char*)q - (char*)p == 100;
// q - (char*)p: invalid
```

#### Array with Pointer

Actually the name of the array is the pointer itself

For an array `double s[3];`

- `&s[0]` => `s`
- `&s[1]` => `s+1`
- `&s[i]` => `s+i`
- `s[i]` => `*(s+i)`

Arrays occupy memory at definition, pointers don’t (unless they are actually def. to point to sth).

So a pointer cannot be given a value (or given a value as an array elem)

### Dynamic Allocation

- Requires `stdlib.h` header file
- `malloc(): void *`

``` c
double *p;	// still not know what is the size of p
int n;
...
p = (double*)malloc(n * sizeof(double));	// p points to double, so `(double*)` (same type) & `sizeof(double)` here
// the memory here is [n x sizeof(double)]
if (p == NULL)
    return 1;
...
for (i = 0; i < n; i++)
    scanf("%lf", &p[i]);
...
free (p);	// Release memory
```

### String

chars + `\0` (ASCII: 0)

#### Definition

- `char s[] = {'H', 'e', 'l', 'l', 'o', '!', '\0'};`
- `char s[] = "Hello!";` (No need `\0`)

The string length: No need to count `\0`; if as an array: Need to count `\0`

Use in **checking**:

- `while (s[i])` & `while (*p)`: can check if a char is `\0` or not (if is, will be false => break the loop)

#### Operations

Requires `string.h`

- `strlen(s)`: Find the length of `s`
- `strcpy(d, s)`: Copy string `s` to `d`
- `strcat(d, s)`: Concatenate (add) `s` after `d`
- `strcmp(s1, s2)`: Compare if `s1` and `s2` equal => yes: 0; no: which is bigger (alphabetical)
  
  ``` c
  strcmp("lion", "zebra");		// < 0: "l" smaller than "z" (smaller)
  strcmp("tiger", "tiger");		// 0
  strcmp("koala", "Koala");		// > 0: "k" after "K" in ASCII
  strcmp("rat", "rat snake");		// < 0
  strcmp("jaguar?", "jaguar!");	// > 0: "?" 
  ```

#### Complex Application: Sorting

##### Max-Sort

``` c
// Find the index of the maximal elem
int index_of_max(int a[], int n)
{
    int i, i_max = 0;
    for (i = 1; i < n; ++i)
        if (a[i] > a[i_max])
            i_max = i;
    return i_max;
}

void max_sort(int a[], int n)
{
    int length;
    for (length = n; length > 1; --length){
        int i_max = index_of_max(a, length);
        swap(&a[length - 1], &a[i_max]);
    }
    return;
}
```

##### Bubble Sort

``` c
int bubble(int a[], int n)
{
    int i, swapped = 0;
    for (i = 1; i < n; ++i)
        if (a[i-1] > a[i]){
            swap(&a[i], &a[i-1]);
            swapped = 1;
        }
    return swapped;
}

void bubble_sort(int a[], int n)
{
    int not_sorted = 1;
    while ((n > 1) && not_sorted)
        not_sorted = bubble(a, n--);
}
```

##### Merge

$\mathcal{O}(na + nb)$ 

``` c
void merge(int a[], int na, int b[], int nb, int c[])
{
    int ia, ib, ic;
    for (ia = ib = ic = 0; (ia < na) && (ib < nb); ic++) {
        if (a[ia] < b[ib]) {
            c[ic] = a[ia];
            ia++;
        }
        else {
            c[ic] = b[ib];
            ib++;
        }
    }
    for (; ia < na; ia++, ic++) c[ic] = a[ia];
    for (; ib < nb; ib++, ic++) c[ic] = b[ib];
}
```

### Complexitiy

Worst case

- $\sum_i^{n} i \sim \mathcal{O}(n^2)$ 
- $\sum_i^{n} \frac{1}{i} \sim \mathcal{O}(\log n)$
- $\sum_i^{n} i^2 \sim \mathcal{O}(n^3)$
- $\sum_i^{n} i^k \sim \mathcal{O}(n^{k+1})$ 

### Recursion

“n” <- “n-1”

Call the function in itself. Easier to use when do some reversely printing work

- Time complexity: recur = iter
- Space complexity: recur > iter

#### Example: Factorial

``` c
int factorial (int n)
{
    if (n == 0) return 1;	// halting (stop) condition (0! == 1) Here return and have jumped out of the `if`
    return n * factorial(n-1); 	// recursive step
}
```

``` c
int factorial (int n)	// wrapper fcn
{
    if (n < 0 || n > MAX)	return 0;
    return rec_fac(n);
}
int rec_fac (int n)
{
    if (n <= 1)	return 1;
    return n * rec_fac(n-1);
}
```

#### Example: Binary Search

``` c
int binSearch(int a[], int n, int val)
{
    if (n == 1)	return a[0] == val? 0: NOT_FOUND;	// hauting cond
    int mid = n / 2;
    if (a[mid] < val) {
        int result = binSearch (a+mid+1, n-mid-1, val);
        return result == NOT_FOUND? NOT_FOUND: result + mid + 1;
    }
    return binSearch(a, mid+1, val);
}
```

 #### Example: Fibonacci

0 1 1 2 3 5 8 13 21 34 55

``` c
int Fibo(int n)
{
    static int f[N] = {0, 1};	// use static to avoid wrong additions
    if (n < 0 || n >= N)	return -1;
    return recFibo(n, f);
}

int recFibo (int n, int f[])
{
    if (n > 2)	return n;
    if (f[n] != 0)	return f[n];
    return f[n] = recFibo(n-1, f) + recFibo(n-2, f);
}
```

### Enumerated Types (enum) (C99)

Available in C99

Defines a new type and a set of named values

The names are more important than its given value since the values should only be integers.

``` c
// def
enum Gender {MALE, FEMALE};	// MALE -> 0; FEMALE -> 1
enum Month {JAN, FEB, MAR, /* ... */, DEC, MONTH_NUM};	// DEC -> 11; MONTH_NUM -> 12 (Useful trick to count)
enum Season {SUMMER = 1, FALL, WINTER = 8, SPRING};	// FALL -> 2; SPRING -> 9

// usage
enum Gender gender = MALE;
enum Season seasons[MONTH_NUM];	// number of elem in the array = 12
seasons[JAN] = WINTER;

enum Month next_month(enum Month current) {
    if (current == DEC)
        return JAN;
    return (enum Month) (current + 1);
}
```

#### Bool

Actually bool can be regarded as an enum type: `enum bool {FALSE, TRUE};`

### Const Keyword (C99)

``` c
const type identifier = expression;	// cannot change after init.
```

``` c
const double PI = 3.141592654;
const double EPSILON = 1e-6;	// usually def as UPPERCASE -> divide from var.
double rad;

if (PI * rad * rad < EPSILON) {
    printf("circle is too small \n")
}
```

- `const` vs `enum`
  - can represent non-integer values
  - use const when the value of the constant matters (physical const, etc.)
  - `const` more about the value, `enum` only distinguishes the different objects rather than some values
- `const` vs `#define`
  - a const variable gets its value at runtime
  - a const variable is scoped (like all C var.)
  - the priority of `#define` is higher 

### Inline Functions (C99)

A normal function call has a small overhead (managing stack, copying parameters values, etc.). It can become large if function is critical

To reduce the overhead, usually write the called function inside the loop other than call one outside. (not that clean)

-> **Inline functions**: Ask the compiler to replace each call to this function with **efficient equivalent code** that does not perform the call

``` c
inline int max(int a, int b){	// use `inline` before the type to indicate 
    return a > b ? a : b;		// return the larger
}

int a, b, c, d;
...					// when `max()` is inlined, the complier will compile the code as:
int x = max(a, b);	// int x = a > b ? a : b;
int y = max(c, d);	// int x = c > d ? c : d;
int z = max(3, 4);	// int z = 4; (for const, just compute intermediately)
```

**Properties**:

- **Larger** compiled files
  - codes will be **relicated** in every call
  - use only with **short** and **critical** functions only
- Just a **recommendation**: 
  - The compiler may not choose to inline a too long function or may choose to inline for optimization automatically
- Hard to **predict** improve efficiency or not
  - Use a **profiler** before

### Pre-processor

<img src="C:/Users/TR/Desktop/C_Preprocessor.svg" alt="C_Preprocessor" style="zoom:80%;" />

#### Pre-process Usage

- **File Inclusion**

  ``` c
  #include <file-name>	// mainly use standard lib headers
  #include "file-name"	// for user def headers
  ```

- **Marco Definitions**

  ``` c
  #define identifier value
  #define identifier(variables) value 	// function-like
  #undef identifier		// undo definition
  ```

- **Conditional Compilation**

  ``` c
  #if condition
  #ifdef identifier	// usually test if have been defined
  #ifndef identifier
  
  #else
  #endif
  ```

#### User Headers

If there are some very complex functions needed to be defined. create a new header file to contain them.

``` c
// `functions.h` (only declarations, no details)
int function1(int n);
int function2(int n);
```

``` c
// `functions.c` (details of the functions)
int function1(int n) {
    ...
}

int function2(int n) {
    ...
}
```

``` c
// `main.c`
#include "functions.h"	// ok to just include the .h file, the .c file will automatically add (implicitly)

int main(){
    printf("%d\n", function1(5));
    return 0;
}
```

Use `gcc -E main.c` (only preprocess the code) => The code that actually generate for compiling will be (`.c` file will not show up but linked to be used)

``` c
int function1(int n);	// only show up the declarations
int function2(int n);

int main(){
    printf("%d\n", function1(5));
    return 0;
}
```

#### Macros

Exactly, macros are replacements

The preprocessor doesn’t know c codes. The job is replacing the texts exactly as it is directed

For example: if `#define return :)`, for `return 0;` the result will be `:) 0;` [NOT compile]

##### **Problems**

- **Operator precedence errors**

  - Internal

    ``` c
    #define SQR(x) x*x
    
    double res1 = SQR(5);	// = 5*5 (OK)
    double res2 = SQR(5+3);	// = 5+3*5+3 (compute wrong thing)
    ```

  - External

    ``` c
    (int)SQR(a);	// (int)a * a	(casts the left operand only)
    ```

  - Solution: Use parentheses: `#define SQR(x) ((x)*(x))`

- **Side effect errors** (no solution)

  ``` c
  SQR(++i)	// ((++i)*(++i))	=> undefined
  ```

- **Unncessary function calls** (no solution) 

  ``` c
  SQR(some_func(a, z, t)) 	// will compute the function twice
  ```

If cannot be solved in macros, try inline functions (such as `sqr(++i)` called by value => OK) 

For complex ones try to use inline functions, for type not important value macro is sufficient.

##### **Advanced Techniques**

- Argument can turn to **string literal** containing the par.: `#define PRINT_INT(a) printf("%s = %d", #a, a)`
- **Helper functions**: (Add an underline before the function name) `#define PRINT_INT(a) _print_int(a, #a)`

##### **Conditionals**

Often be used in the macro part

- Demo with `#if` & `#endif`

  ``` c
  #define LOW 1
  #define MEDIUM 2
  #define HIGH 3
  
  #define LOGGING_LVL HIGH	// macros can use other previously defined macros
  
  void load_conf(){
      
      //...
      
  #if LOGGING_LEVEL > MEDIUM
      printf("Conf loaded\n");
  #endif
      
  }
  ```

  The preprocessed result:

  ```c
  void load_conf(){
      
      //...
      printf("Conf loaded\n");
      
  }
  ```

- Another demo with `#ifdef`, `#else` & `endif`:

  ``` c
  #ifdef _WIN32
  printf("Running on Windows");
  #else
  printf("Running on Unix");
  #endif
  ```

- `defined(indentifier)`:

  `#ifdef MY_MACRO` == `#if defined(MY_MACRO)`

  `#ifndef MY_MACRO` == `#if !defined(MY_MACRO)`

  ``` c
  #ifdef DEBUG_ON
  #define DEBUG_PRINT(MSG) fprintf(stderr, "%s", MSG)
  #else
  #define DEBUG_PRINT(MSG) ((void)0)
  #endif
  ```

- Add extra checks while debugging (without affecting the performance of the final product)

  ``` c
  int safe_get(struct array arr, int i) {
  #ifndef NDEBUG	
      if (arr.a == NULL) {
          fprintf(stderr, "Null array\n");
          exit(1);
      }
      if (i < 0 || i >= arr.n) {
          fprintf(stderr, "Out of bounds\n");
          exit(1);
      }
  #endif
      return arr.a[i];
  }
  ```

  ``` c
  struct array{
      int* a;	// array name (pointer)
      int n;	// array length
  }
  ```

  ``` c
  int sum = 0;
  for (int i = 0; i < n; i++) {
      sum += safe_get(arr, i);	// Adding #define NDEBUG removes all checks from compiled code
  }
  ```

  (Or use `gcc -DNDEBUG`)

##### Predefined Macros

- Some special macros are predefined:	(Useful in debug)
  - `__LINE__`: expands to the line num in the file being processed
  - `__FILE__`: expands to the name of the file being processed
- Some macros are defined by the compiler
  - Allows code to compile under different environment

##### Assert Macro

- Def in `<assert.h>`, used to helpfind errors as early as possible

``` c
#ifdef NDEBUG
#define assert(x) ((void)0)		// call the assert function, if no debug nothing will be done
#else /* debugging enabled */
void _assert (const char* condition, const char* filenamem, int line);	// helper func
#define assert(e) ((e) ? (void)0 : _assert(#e, __FILE__, __LINE__))		// error @ which file and which line
	// `_assert` just prints an error msg and calls abort()
#endif	/* NDEBUG */
```

Possible Result: `Assertion failed: arr.a != NULL, file main.c, line 23`

#### File Inclusions

Most declarations must not appear more than once (must protect against including a file more than once)

**DEMO**

- Declare at `utility.h` (this is use to avoid including more than once)

  ``` c
  // conditional inclusion of this file
  #ifndef UTILITY_H
  #define UTILITY_H
  
  // the contents of utility.h comes here
  ...
  #endif /* UTILITY_H */
  ```

- Implement at `utility.c`

  ``` c
  #include "utility.h"
  ...	//details
  ```

- Another declation of `testing.h`

  ``` c
  #ifndef TESTING_H
  #define TESTING_H
  #include "utility.h"
  
  // ...
  
  #endif /* TESTING_H */
  ```

- Details… at `testing.c`

  ``` c
  #include "utility.h"	// another inclusion of `utility.h`
  #include "testing.h"	// will not include `utility.h` again
  ...
  ```

- Main program: `main.c`

  ``` c
  #include "utility.h"	// recommend to write this part again
  #include "testing.h"	// will not include `utility.h` again
  ...
  ```

### Type Definition

Declares a new type name. Commonly appear in a header file to share across code files. (if too many new types, a `types.h` could be useful)

`typedef typename name-def` (actually add a nickname of a type)

- Defining a **type** that may **need to be changed** in the future

  `typedef double Real`: represents real numbers in a physics sim; if run into memory problems, change to float

- Improve code **readability**: e.g. defined as `Length` (or other physics properties)

- **Hide** implementation details

  ```c
  // stdio.h def a FILE type for reading/writing files
  #include <stdio.h>
  
  FILE* in_file = fopen("params.dat");	
  // implementation of the FILE type is irrelavent (only used through dedicated functions)
  ```

- **Abbreviate** long type names

  ``` c
  typedef enum Gender Gender;	// now `Gender` instead of `enum Gender`
  ```

### Structures (struct)

Basis for defining new types in C that can represent **complicated objects**

Each field has a **type** and a **name**

```c
struct name { field-list };
```

**Demo**: Complex num

- `complex.h`

  ```c
  struct complex {
      double re, im;	// real / imaginary parts
  };
  typedef struct complex Complex;	// the name is "struct complex" originally, -> "Complex"
  
  Complex complexAdd(Complex x, Complex y);	// given complex num x and y, return complex num (z in the following .c file)
  // Usually we write the definition with its related functions in the same .h file
  ```

- `complex.c`

  ```c
  #include "complex.h"
  
  Complex complexAdd (Complex x, Complex y) {
      Complex z;
      z.re = x.re + y.re;
      z.im = x.im + y.im;
      return z;
  }
  ```
  
- Structures may be init. 

  - In order -> NOT RECOMMENDED in most cases (break when change field order)

    ``` c
    Complex z = {2.3, -.4};
    ```

  - **Creation Function** -> Safer approach

    ``` c
    Complex complexCreate(double re, double im) {	
        Complex z;
        z.re = re;
        z.im = im;
        return z;
    }	
    ```

    ``` c
    Complex z = complexCreate(2.3, -.4)	// still work when we change the field order in the struct
    ```


**Usage**:

- Return from functions

  ``` c
  double x = complexAdd(z1, z2).re;
  ```

- Assigning a structure copies its fields

  ``` c
  z2 = z1;	// copy both re and im
  ```

- Pass and return from function by copying by value

  ``` c
  void f(Complex c) {
      c.re += 3;	// will not change the struct outside the function
      //...
  }
  ```

- Pointer in struct

  - `(*pointer).value` equiv to `pointer->v`
  - `*(ptr + k)` equiv to `ptr[k]`
  
  A pointer can have an integer **added** / **substracted** -> moves the address according to the size (mostly in arrays)
  
  <img src="https://cdn.jsdelivr.net/gh/Nikucyan/MD_IMG//img/image-20211108115709289.png" alt="image-20211108115709289" style="zoom:67%;" />

### Pointers (Advanced)

#### void* Pointers

`void*` is used as a **generic** pointer type. (we don’t know its exact type but want a pointer)

It cannot be dereferenced (i.e. with `*` or `[]`) and cannot be used with pointer arithmetic, unless it is cast to its true type.

**DEMO**

``` c
int i = 1;
double d = 1.0;

void* ptr0 = &i;	// i and d's address (i's is int and d's is double)
void* ptr1 = &d;	// these two pointers are valid but without types

double e = *ptr0 + *ptr1;	// invalid (compilation error), cannot fetch result with *
e = *(int*)ptr0 + *(double*)ptr1;	// valid, because have spec. the types
```

`void*` pointer can be used for generic **low-level memory operations** (avoid such code whenever possible)

(Type `char` is guaranteed to occupy exactly 1 byte) -> casting a `void*` to `char*` allows accessing individual bytes in the memory

``` c
void swap (void* p, void* q, size_t nbytes) {	/* size_t is typedef from <stdlib.h> => counting bytes usually (unsigned) int */
    for (int i = 0; i < nbytes; i++) {
        char tmp = ((char*)p)[i];
        ((char*)p)[i] = ((char*)q)[i];
        ((char*)q)[i] = tmp;            
    }
}
```

``` c
double d1, d2;
int a[5], b[10];
//...
swap(&d1, &d2, sizeof(double));	// swap the storage address of d1 and d2
swap(a, b, 5*sizeof(int));		// swap the first 5 elems
```

#### Const and Pointers

- A **const pointer** cannot change where it points to 

  ``` c
  int x = 5;
  int* const ptr = &x;	// ptr will always points to x
  *ptr = 7;				// actually only change x
  ptr++;					// NOT compile (ptr is const)
  ```

- A **pointer to a const** cannot change to what it points to 

  ``` C
  int x = 5;
  const int* ptr = &x;	// ptr is pointer points to a constant integer (ptr will never change the value of x (const int))
  *ptr = 7;				// NOT compile (x is const)
  ptr++;					// OK, ptr points to another location
  *ptr = 10;				// NOT compile
  const int* const ptr2 = &x;	// can combine both const types
  ```

- Taking a **pointer to const** => not modify the contents of the pointer (useful for strings because we won’t modify them)

  ``` c
  char* strcpy(char* str1, const char* str2);		// copy str2 to str1 (str1 should not be const)
  int strcmp(const char* str1, const char* str2);	// compare str1 and 2 (don't want to change both)
  int strlen(const char* str);					// len to str
  ```

- A function taking a pointer not intending to modify => Using const

  To distinguish in/outputs. Without it, pointers to const data cannot be passed to the func

#### Pointers to Functions

The type of a function => function’s signature

``` c
double sin(double);
double cos(double);
double fabs(double);	// in <math.h>, all these func have the same type
```

``` c
double (*fptr)(double);
// fptr can point to any func that takes one double and returns a double (in / output types)
fptr = cos;		// point fptr to the code of func `cos()`
fptr = printf;	// NOT compile => wrong type
```

**DEMO**

``` c
double derivative(double (*func)(double), double x) {	// deriv at x point
    const double h = 1e-6;
    double diff = func(x+h) - func(x-h);
    return diff/(2*h);	// at small h -> tends to be the derivative
}
```

``` c
double square(double x) {	// also double (*func)(double)	(same type)
    return x*x;
}

void compute() {	
    printf("%lf\n", derivative(square, 1));		// 2.000	x^2 derivative at 1.0 
    printf("%lf\n", derivative(sin, 0));		// 1.000
    printf("%lf\n", derivative(cos, PI/2));		// -1.000
}
```

### Dynamic Memory Allocation (Advanced)

Predifined std func: (`<stdlib.h>`)

``` c
void* malloc (size_t num_bytes);
void* calloc (size_t num_elem, size_t elem_size);	// Contiguous allocation. Only function that zeros the allocated bytes
void* realloc (void* old_ptr, size_t new_size);		// Reallocations

void free (void* ptr);
```

#### **Memory Management**

- **Stack**: Stores **local** var. and calls to func.
- **Heap**: Stores data **dynamically** allocated by the program (need to free)
- **Data**: Stores **global var. and static func. var.**. Marked as read-only and stores string const
- **Code**: Stores the machine code (read-only)

<img src="https://cdn.jsdelivr.net/gh/Nikucyan/MD_IMG//img/image-20211108172732061.png" alt="image-20211108172732061" style="zoom:50%;" />

C99 added variable-length arrays. However not good: (not intro to C++)

Stack size - Small; Heap - Larger  => **Stack overflow** can occur, which is unrecoverable error



