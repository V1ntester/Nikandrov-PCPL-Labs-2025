class Program
{
    static void Main(string[] args)
    {
        string firstCoefficientBuffer;
        string secondCoefficientBuffer;
        string thirdCoefficientBuffer;

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
            PrintErrorMessage("Ошибка приведения значений ввода\n");
            ReadCoefficientsToBuffers(out firstCoefficientBuffer, out secondCoefficientBuffer, out thirdCoefficientBuffer);
        }

        if (firstCoefficient == 0)
        {
            PrintErrorMessage("Не является биквадратным уравнением");
            return;
        }

        double discriminant = secondCoefficient * secondCoefficient - 4 * firstCoefficient * thirdCoefficient;

        if (discriminant < 0.0)
        {
            PrintErrorMessage("Нет действительных решений уравнения");
            return;
        }

        List<double> roots = new List<double>();

        if (discriminant > 0.0)
        {
            double sqrtDiscriminant = Math.Sqrt(discriminant);
            double denominator = 2 * firstCoefficient;

            double firstReplacedRoot = (-secondCoefficient + sqrtDiscriminant) / denominator;
            roots.AddRange(CalculateRootsFromReplacedRoot(firstReplacedRoot));

            double secondReplacedRoot = (-secondCoefficient - sqrtDiscriminant) / denominator;
            roots.AddRange(CalculateRootsFromReplacedRoot(secondReplacedRoot));
        }
        else if (Math.Abs(discriminant) < double.Epsilon)
        {
            double replacedRoot = -secondCoefficient / (2 * firstCoefficient);
            roots.AddRange(CalculateRootsFromReplacedRoot(replacedRoot));
        }

        PrintRootsFromList(roots);
    }

    private static List<double> CalculateRootsFromReplacedRoot(double replacedRoot)
    {
        List<double> roots = new List<double>();

        if (replacedRoot > 0)
        {
            double firstRoot = Math.Sqrt(replacedRoot);
            double secondRoot = -firstRoot;

            roots.Add(firstRoot);
            roots.Add(secondRoot);
        }
        else if (Math.Abs(replacedRoot) < double.Epsilon)
        {
            roots.Add(0);
        }

        return roots;
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

    private static void PrintRootsFromList(List<double> roots)
    {
        Console.ForegroundColor = ConsoleColor.Green;
        foreach (double root in roots)
        {
            Console.Write("Корень: {0:F4}; ", root);
        }

        Console.Write('\n');
        Console.ResetColor();
    }

    private static void PrintErrorMessage(string message)
    {
        Console.ForegroundColor = ConsoleColor.Red;
        Console.WriteLine(message);
        Console.ResetColor();
    }
}
