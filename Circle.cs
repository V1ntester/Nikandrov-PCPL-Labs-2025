namespace Shapes;

public class Circle : Shape, IPrint
{
    public Circle(double radius)
    {
        Radius = Math.Abs(radius);
    }

    public double Radius { get; init; }

    public void Print() => Console.WriteLine(ToString());

    public override double CalculateArea() => Math.PI * Radius * Radius;

    public override string ToString() => $"Radius: {Radius:F4}; Area: {CalculateArea():F4}";
}
