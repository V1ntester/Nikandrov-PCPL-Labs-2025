using System.Collections;

namespace SimpleCollections;

public class SimpleList<T> : IEnumerable<T>
{
    private SimpleNode<T>? _head;
    private SimpleNode<T>? _tail;
    public int Length { get; private set; }

    public void Add(T value)
    {
        SimpleNode<T> newNode = new(value);

        if (_head is null) _head = newNode;
        else _head.Next = newNode;

        ++Length;
    }

    public bool Remove(T value)
    {
        SimpleNode<T>? current = _head;
        SimpleNode<T>? previous = null;

        while (current is not null && current.Value is not null)
        {
            if (current.Value.Equals(value))
            {
                
            }
        }
    }

    IEnumerator<T> IEnumerable<T>.GetEnumerator()
    {
        SimpleNode<T>? current = _head;

        while (current is not null)
        {
            yield return current.Value;
            current = current.Next;
        }
    }

    IEnumerator IEnumerable.GetEnumerator()
    {
        return ((IEnumerable<T>)this).GetEnumerator();
    }

}   
