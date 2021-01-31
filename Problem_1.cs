using System;

namespace euler 
{
    class Problem1 
    {
        static void Main(string[] args)
        {
            int result = 0;
            for (int i=1; i<1000; i++)
            {
                if (((i%3) == 0) || (i%5) == 0)
                {
                    result += i;
                }
            }

            Console.WriteLine("The sum on numbers div. by 3 and 5 is {0}", result);
        }       
    }
}   