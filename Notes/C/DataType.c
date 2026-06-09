#include<stdio.h>
int main (){
    char ch = 'A';
    printf("%c", ch);
    
    char c = 65, d = 66, e = 67;
    printf("\n %c %c %c", c, d, e);
    
    // char h = 'Hello'; // through error because char only store 1 bit space so it can only store the single character.
    // printf("%s", h);
    
    double myNum = 19.99;
    printf("%lf", myNum);
    
    float num = 3e2;
    printf("\n %f", num);
    
    float num2 = 3.44444;
    printf("\n%.3f", num2);
    
    // memory size: 
    int myInt;
    float myFloat;
    double myDouble;
    char myChar;
    
    printf("\n%zu\n", sizeof(myInt));
    printf("%zu\n", sizeof(myFloat));
    printf("%zu\n", sizeof(myDouble));
    printf("%zu\n", sizeof(myChar));
    
    
    int normalInt = 1000;                       // standard int 
    double normalDouble = 3.14;                 // standard double
    
    short int small = -100;                     // smaller int
    unsigned int count = 25;                    // only positive int
    long int big = 1234567890;                  // larger int
    long long int veryBig = 9223372036854775807; // very large int
    unsigned long long int huge = 18446744073709551615U; 
    // very large, only positive
    long double precise = 3.141592653589793238L; 
    // extended precision
    
    printf("Normal int: %d\n", normalInt);
    printf("Normal double: %lf\n", normalDouble);
    printf("Small: %hd\n", small);
    printf("Count: %u\n", count);
    printf("Big: %ld\n", big);
    printf("Very Big: %lld\n", veryBig);
    printf("Huge: %llu\n", huge);
    printf("Precise: %Lf\n", precise);
	
	
	// Inmplicit type data conversion
	float myFloat = 9;
	printf("%f", myFloat); // 9.000000
	
	int myInt = 9.99;
	printf("%d", myInt); // 9 here need careful because .99 is lost, it may create any runtime error or unfavourable result can be comes.
	
	// Explicit type conversion
	
		float sum = (float) 5 / 2;
	printf("%f", sum); // 2.500000

    
    return 0;
}