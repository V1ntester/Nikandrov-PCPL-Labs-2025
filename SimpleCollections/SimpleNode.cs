namespace SimpleCollections;

public class SimpleNode<T>
{
    public SimpleNode(T value)
    {
        Value = value;
    }

    public T Value { get; set; }
    public SimpleNode<T>? Next { get; set; } 
} 