# C++ Symbols
* [Common Code](#common-code)
* [Variables](#variables)
* [Brackets](#brackets)
* [Comparison Operators](#comparison-operators)
* [Logic Operators](#logic-operators)
* [key Words](#key-words)
    * [Protected States](#protected-states)
    * [Functional](#functional)

## Common Code

Function:
```csharp
//void can be swapped for any type
//setup is just a name.
//Parameters can be added inside the () to customize functions
void setup()
{

}
```

Variable:
```csharp
// = 0; is not needed, by default all values start at 0 / false / null
// float can be replaced with any type
float x = 0;
```

Array:
```csharp
// [] indicates it's an array with a size of 10.
// Can be any type.
int [] highScores = new int[10];
```

Loop:
```csharp
//(i = 0;) Starting at 0 
//(i < highScores.length) While i is smaller than the number of highScores (10)
//(++i) Increase i by 1
for(int i = 0; i < highScores.length; ++i)
{
    //Effectively counts: 0,1,2,3,4,5,6,7,8,9
}
```


## Variables 

| Name                       | (C#) Bytes Used           | Purpose                              |
|----------------------------|---------------------------|--------------------------------------|
| const char * (String)      | Number of characters + 1  | Words / Text                         |
| long                       | 8                         | Huge numbers (bigger than 4 billion) |
| double                     | 8                         | Huge Nubmers with Decimals           |
| Object Reference (pointer) | 4                         | Using objects                        |
| int                        | 4                         | Number                               |
| float                      | 4                         | Number with Decimals                 |
| short                      | 2                         | Small Number (Smaller than 65000)    |
| char                       | 1 (depending on encoding) | 1 Letter                             |
| byte                       | 1                         | Numbers smaller than 255             |
| bool                       | 1                         | True or False                        |

## Brackets

| Symbol | Alternative Name                                     | Purpose / Meaning | Example                                | Example English                                                                            |
|--------|------------------------------------------------------|-------------------|----------------------------------------|--------------------------------------------------------------------------------------------|
| ()     | Parenthesis, Circle Brackets, Parameters / Arguments | Define a function | void setup() {  size(800,800); }       | Make a function named setup, and call the size function with args 800 width and 800 height |
| {}     | Brackets, Squiggle Brackets                          | Do Something      | void setup() {   size(800,800); }      | When setup happens, change the size to 800 width and 800 height                            |
| []     | Square Brackets                                      | Array / Index of  | int [] nums = new int[5];              | Create an array of 5 integers                                                              |
| <>     | Triangle Brackets, Angle Brackets                    | Type of           | vector<int> nums = new vector<int>(5); | Create a list of integers with a default size of 5.                                        | 

## Comparison Operators
| Symbol | Alternative Name | Example                    | Example English                    |
|--------|------------------|----------------------------|------------------------------------|
| ==     | is               | int x = 0; if(x == 5){}    | if x is 5                          |
| !=     | is not           | int x = 0; if(x != 5){}    | if x is not 5                      |
| \>     | Greater Than     | int x = 0; if(x > 5){}     | if x is greater than 5             |
| <      | Smaller Than     | int x = 0; if(x < 5){}     | if x is smaller than 5             |
| \>=    | Greater or Equal | int x = 0; if(x >= 5){}    | if x is greater than or equal to 5 |
| <=     | Smaller or Equal | int x = 0; if(x <= 5){}    | if x is smaller than or equal to 5 |


## Logic Operators

| Symbol 	| Alternative Name      	| Example                            	| Example English                                               	|
|--------	|-----------------------	|---------------------------------	|---------------------------------------------------------------	|
| &&     	| AND                   	| int x = 0; if(x > -1 && x < 1){}   	| if x is greater than -1 AND smaller than 1                    	|
| \|\|   	| OR                    	| int x = 0; if(x > -1 \|\| x < 1){} 	| if x is greater than -1 OR smaller than 1                     	|
| &      	| Bitwise AND (bitmask) 	| int x = 0; if(x & 1 == 0){}        	| if the binary version of x's first bit is not active          	|
| \|     	| Bitwise OR            	| int x = 0; if(x \| 12 == 0){}      	| if the binary version of x or 12 has the first bit active     	|
| ^      	| XOR                   	| int x = 0; if(x > -1 ^ x < -1){}   	| if x is either bigger than -1 or smaller than -1 BUT NOT BOTH 	|
| !      	| NOT                   	| bool x = true; if(!x){}         	| if x is not true                                              	|


## Key Words


### Protected States
| Term      	| Meaning                                                      	|
|-----------	|--------------------------------------------------------------	|
| private   	| The term is only visible in this file                        	|
| protected 	| The term is only visible to this file and it's children      	|
| public    	| The term is visible anywhere                                 	|
| internal  	| The term is only visible to scripts within the same assembly 	|

### Functional
| Term     	| Meaning                                                                                                      	|
|----------	|--------------------------------------------------------------------------------------------------------------	|
| return   	| Cancel the function and give back some value. NOTE: you can use return in void functions to end the function 	|
| continue 	| Skip the current iteration in the loop                                                                       	|
| break    	| Exit the current loop                                                                                        	|








