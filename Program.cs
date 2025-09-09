using Shapes;

class Program
{
    static void Main(string[] args)
    {
        Rectangle rectangle = new(2.0, 3.0);
        Square square = new(2);
        Circle circle = new(3);

        rectangle.Print();
        square.Print();
        circle.Print();
    }
}
