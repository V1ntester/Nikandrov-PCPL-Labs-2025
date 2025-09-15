namespace SparseMatrix;

public class SparseMatrix3D<T>
{
    private Dictionary<(int, int, int), T?> _values = new();
    private int _rowsCount;
    private int _columnsCount;
    private int _layersCount;

    public SparseMatrix3D(int rowsCount, int columnsCount, int layersCount)
    {
        if (rowsCount < 0 || columnsCount < 0 || layersCount < 0) {
            throw new ArgumentOutOfRangeException("Argument out of range");
        }

        _rowsCount = rowsCount;
        _columnsCount = columnsCount;
        _layersCount = layersCount;
    }

    public T? this[int row, int column, int layer]
    {
        get
        {
            if (!ValidateCoords(row, column, layer))
            {
                throw new IndexOutOfRangeException("Index out of range");
            }

            if (_values.ContainsKey((row, column, layer)))
            {
                return _values[(row, column, layer)];
            }
            else
            {
                return default;
            }
        }

        set
        {
            if (!ValidateCoords(row, column, layer))
            {
                throw new IndexOutOfRangeException("Index out of range");
            }

            if (value is null)
            {
                _values.Remove((row, column, layer));
            }
            else
            {
                _values[(row, column, layer)] = value;                
            }
        }
    }

    public override string ToString()
    {
        string result = "\n";

        foreach (var element in _values)
        {   
            result += $"Coords: {element.Key.Item1} {element.Key.Item2} {element.Key.Item3}; Value: {element.Value?.ToString() ?? "Null"}\n";
        }

        return result;
    }

    private bool ValidateCoords(int row, int column, int layer)
    {
        return row >= 0 && row < _rowsCount && 
            column >= 0 && column < _columnsCount && 
            layer >= 0 && layer < _layersCount;
    }
}
