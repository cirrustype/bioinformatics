using System;

namespace variables_arithmetic
{
    class Program
    {
        static void Main(string[] args)
        {
            double a = 3; // have to include 'int' c# does not know type automatically 
            double b = 5;
                        //needed to be 'double' because of the powers
            double a2 = Math.Pow(3.00, 2.00);
            double b2 = Math.Pow(5.00, 2.00);

            double c = a2 + b2;

        
            Console.WriteLine(value: c);
        }
    }
}
