using Microsoft.VisualBasic;

namespace Shapes;

public abstract class Shape : IComparable
{
    public virtual double CalculateArea() => 0.0;

    public int CompareTo(object? obj)
    {
        if (obj is Shape shape) return CalculateArea().CompareTo(shape.CalculateArea());
        else throw new ArgumentException("Argument is incomparable.");
    }
}
