namespace Shapes;

public class Square : Rectangle
{
    public Square(double length) : base(length, length) { }
    
    public override string ToString() => $"Side length: {Width:F4}; Area: {CalculateArea():F4};";
}
