// See https://aka.ms/new-console-template for more information
using System.ComponentModel.Design;

Console.WriteLine("press C to convert temperature from Fahrenheit to Celsius");
Console.WriteLine("or");
Console.WriteLine("press F to convert temperature from Celsius to Fahrenheit");
Console.Write("(C or F):  ");
string input=Console.ReadLine();
char User = Convert.ToChar(input);


if (User == 'c' || User == 'C') 
{
    Console.Write("your temperature in Fahrenheit: ");

    double Temp = Convert.ToDouble(Console.ReadLine());

    double Result= (Temp -32) / 1.8;
    Console.WriteLine("Temperature in Celsius: {0}",Result);

}

else if (User == 'f' || User == 'F')

{
    Console.Write("your temperature in Celsius: ");

    double Temp = Convert.ToDouble(Console.ReadLine());

    double Result = (Temp * 1.8)  +32;
   Console.WriteLine("Temperature in Fahrenheit: {0}",Result);
};