using System;

namespace C_
{
    class Program
    {
        static void Main(string[] args)
        {
            double Rosa(double a, double b){
                double c = Math.Pow(a, 2) + Math.Pow(b, 2);
                return c;
            }
            //double a2 = Math.Pow(3.00, 2.00);
            //double b2 = Math.Pow(5.00, 2.00);
            //double c = a2 + b2;
            
            double c = Rosa(815,871); //1422866, correct!
            Console.WriteLine(c);
        }
    }
}
