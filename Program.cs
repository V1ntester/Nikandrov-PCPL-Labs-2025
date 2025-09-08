using System;

class Program
{
    public static void Main(string[] args)
    {
        string firstCoefficientBuffer = string.Empty;
        string secondCoefficientBuffer = string.Empty;
        string thirdCoefficientBuffer = string.Empty;

        if (args.Length == 3)
        {
            firstCoefficientBuffer = args[0];
            secondCoefficientBuffer = args[1];
            thirdCoefficientBuffer = args[2];
        }
        else
        {
            ReadCoefficientsToBuffers(out firstCoefficientBuffer, out secondCoefficientBuffer, out thirdCoefficientBuffer);
        }

        double firstCoefficient;
        double secondCoefficient;
        double thirdCoefficient;

        while (!(double.TryParse(firstCoefficientBuffer, out firstCoefficient) &&
                 double.TryParse(secondCoefficientBuffer, out secondCoefficient) &&
                 double.TryParse(thirdCoefficientBuffer, out thirdCoefficient)))
        {
            Console.WriteLine("Ошибка приведения значенийй ввода\n");
            ReadCoefficientsToBuffers(out firstCoefficientBuffer, out secondCoefficientBuffer, out thirdCoefficientBuffer);
        }

        if (firstCoefficient == 0 && secondCoefficient == 0)
        {
            Console.ForegroundColor = ConsoleColor.Red;

            if (thirdCoefficient == 0)
            {
                Console.WriteLine("Бесконечное количество решений уравнения");
            }
            else
            {
                Console.WriteLine("Нет решений уравнения");
            }

            return;
        }

        double discriminant = secondCoefficient * secondCoefficient - 4 * firstCoefficient * thirdCoefficient;

        if (discriminant > 0)
        {
            double firstRoot = (-secondCoefficient + Math.Sqrt(discriminant)) / (2 * firstCoefficient);
            double secondRoot = (-secondCoefficient - Math.Sqrt(discriminant)) / (2 * firstCoefficient);

            Console.ForegroundColor = ConsoleColor.Green;
            Console.WriteLine("Первый корень уравнения: {0}; Второй корень уравнения: {1}", firstRoot, secondRoot);
        }
        else if (discriminant == 0)
        {
            double root = -secondCoefficient / (2 * firstCoefficient);

            Console.ForegroundColor = ConsoleColor.Green;
            Console.WriteLine("Корень уравнения: {0}", root);
        }
        else
        {
            Console.ForegroundColor = ConsoleColor.Red;
            Console.WriteLine("Нет действительных решений уравнения");
        }
    }

    private static void ReadCoefficientsToBuffers(out string firstCoefficientBuffer, out string secondCoefficientBuffer, out string thirdCoefficientBuffer)
    {
        Console.Write("Введите коэффициент A: ");
        firstCoefficientBuffer = Console.ReadLine() ?? "0";

        Console.Write("Введите коэффициент B: ");
        secondCoefficientBuffer = Console.ReadLine() ?? "0";

        Console.Write("Введите коэффициент C: ");
        thirdCoefficientBuffer = Console.ReadLine() ?? "0";
    }
}