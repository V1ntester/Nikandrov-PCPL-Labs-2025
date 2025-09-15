namespace CommonCollections;

using SimpleCollections;
public class Stack<T> : SimpleList<T>
{
    public void Push(T value)
    {
        Add(value);
    }

    public T Pop()
    {
        T value = this[Length];
        Remove(value);
        return value;
    }
}
