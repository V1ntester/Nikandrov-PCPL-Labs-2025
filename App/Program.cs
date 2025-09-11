using System.Collections;

using Shapes;
using SparseMatrix;
using SimpleCollections;

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

        SparseMatrix3D<Shape> sparseMatrix3D = new(3, 3, 3);
        sparseMatrix3D[1, 1, 1] = new Circle(1);

        Console.WriteLine(sparseMatrix3D.ToString());

        Stack<Shape> stack = new();
        stack.Push(new Circle(1));

        Console.WriteLine(stack.Pop().ToString());
    }

    private static void PrintCollection(ArrayList arrayList)
    {
        foreach (var element in arrayList)
        {
            Console.WriteLine(element.ToString());
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
