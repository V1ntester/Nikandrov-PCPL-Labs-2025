namespace Shapes;

public class Rectangle : Shape, IPrint
{
    public Rectangle(double width, double height)
    {
        Width = Math.Abs(width);
        Height = Math.Abs(height);
    }

    public double Width { get; init; }
    public double Height { get; init; }

    public void Print() => Console.WriteLine(ToString());

    public override double CalculateArea() => Width * Height;

    public override string ToString() => $"Width: {Width:F4}; Height: {Height:F4}; Area: {CalculateArea():F4};";
}
