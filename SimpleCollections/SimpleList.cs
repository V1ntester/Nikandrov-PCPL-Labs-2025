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

        if (_head is null)
        {
            _head = newNode;
            _tail = newNode;
        }
        else
        {
            _tail!.Next = newNode;
            _tail = _tail.Next;
        }

        ++Length;
    }

    public bool Remove(T value)
    {
        if (Length == 0) throw new InvalidOperationException("List is empty");

        SimpleNode<T>? current = _head;
        SimpleNode<T>? previous = null;

        while (current is not null)
        {
            if (current.Value is not null && current.Value.Equals(value))
            {
                if (previous is null)
                {
                    _head = current.Next;

                    if (_head is null)
                    {
                        _tail = null;
                    }
                }
                else
                {
                    previous.Next = current.Next;

                    if (current.Next is null)
                    {
                        _tail = previous;
                    }
                }

                --Length;
                return true;
            }

            previous = current;
            current = current.Next;
        }

        return false;
    }

    public void RemoveAt(int index)
    {
        if (Length == 0) throw new InvalidOperationException("List is empty");
        else if (index < 0 || index >= Length) throw new IndexOutOfRangeException();

        SimpleNode<T>? current = _head;
        SimpleNode<T>? previous = null;

        for (int i = 0; i < index; i++)
        {
            previous = current;
            current = current!.Next;
        }

        if (previous is null)
        {
            _head = current!.Next;

            if (_head is null)
            {
                _tail = null;
            }
        }
        else
        {
            previous.Next = current!.Next;

            if (current.Next is null)
            {
                _tail = previous;
            }
        }

        --Length;
    }

    public T this[int index]
    {
        get
        {
            if (index < 0 || index >= Length) throw new IndexOutOfRangeException();

            SimpleNode<T>? current = _head;

            for (int i = 0; i < index; i++)
            {
                current = current!.Next;
            }

            return current!.Value;
        }

        set
        {
            if (index < 0 || index >= Length) throw new IndexOutOfRangeException();

            SimpleNode<T>? current = _head;

            for (int i = 0; i < index; i++)
            {
                current = current!.Next;
            }

            current!.Value = value;
        }
    }

    public bool Find(T value)
    {
        SimpleNode<T>? current = _head;

        while (current is not null && current.Value is not null)
        {
            if (current.Value.Equals(value)) return true;
            current = current.Next;
        }

        return false;
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
