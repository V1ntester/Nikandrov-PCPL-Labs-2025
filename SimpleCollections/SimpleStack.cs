namespace SimpleCollections;

public class SimpleStack<T> : SimpleList<T>
{
    public void Push(T value)
    {
        Add(value);
    }

    public T Pop()
    {
        if (Length == 0) throw new InvalidOperationException("Stack is empty");
        
        T value = this[Length - 1];
        RemoveAt(Length - 1);
        return value;
    }
}
