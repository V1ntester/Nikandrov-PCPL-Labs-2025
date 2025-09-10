using Shapes;
using System.Collections;

class Program
{
    static void Main(string[] args)
    {
        ArrayList arrayList = new();
        arrayList.Add(new Rectangle(2, 3));
        arrayList.Add(new Square(2));
        arrayList.Add(new Circle(1));

        Console.WriteLine("ArrayList: ");
        PrintCollection(arrayList);

        arrayList.Sort();

        Console.Write('\n');
        PrintCollection(arrayList);

        List<Shape> list = new();
        list.Add(new Rectangle(2, 3));
        list.Add(new Square(2));
        list.Add(new Circle(1));

        Console.WriteLine("\nList:");
        PrintCollection(list);

        list.Sort();

        Console.Write('\n');
        PrintCollection(list);
    }

    private static void PrintCollection(ArrayList arrayList)
    {
        foreach (object obj in arrayList)
        {
            Console.WriteLine(obj.ToString());
        }
    }

    private static void PrintCollection(List<Shape> list)
    {
        foreach (Shape shape in list)
        {
            Console.WriteLine(shape.ToString());
        }
    }
}
