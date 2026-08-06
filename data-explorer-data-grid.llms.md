# Data Grid

View millions of rows and columns in Positron’s efficient Data Explorer, with real-time updates and support for Pandas, Polars, tibbles, and database connections.

The data grid is the primary display, with a spreadsheet-like cell-by-cell view. It’s intended to scale efficiently to relatively large in-memory datasets, up to millions of rows or columns.

[![Data grid displaying flight data for January 1, 2013, with columns for year, month, day, dep_time, sched_dep_tim, and dep_delay.](images/data-explorer-grid-example.png)](images/data-explorer-grid-example.png "Data Explorer Grid Example")

Data Explorer Grid Example

Each Data Explorer instance watches the underlying data for changes, so if you edit a data file or modify an in-memory dataframe, the changes will be reflected in the Data Explorer.

### Supported data frame libraries

Pandas and Polars dataframe objects are supported in Python, and `data.frame`, `tibble`, and `data.table` are supported in R. Previews of database connections managed by the [**Connections** pane](connections-pane.llms.md) are also supported, for both Python and R.

Based on [user feedback](feedback.llms.md#feedback-and-issues), we may add support for other libraries that expose a tabular data interface.

### Column overview

Each column header has the column name above the data type, which is dependent on the backend type (language runtime or DuckDB).

At the top right of each column, there is a context menu for column specific actions.

[![Data explorer column dropdown menu open, showing options: Copy Column, Select Column, Pin Column, Sort Ascending, Sort Descending, Clear Sorting, and Add Filter.](images/data-explorer-column-menu.png)](images/data-explorer-column-menu.png "Data Explorer Column Menu")

Data Explorer Column Menu

Columns can be resized by selecting and dragging the border on either side of a column.

### Row overview

Row labels default to the observed row index, with a zero-based index in Python and a one-based index in R. Alternatively, `pandas` and R users may also have rows with modified indices or string-based labels.

Right-clicking on a row header will bring up a context menu for row specific actions.

[![Data explorer row right-click menu open, showing options: Copy Row, Select Row, and Pin Row.](images/data-explorer-row-menu.png)](images/data-explorer-row-menu.png "Data Explorer Row Menu")

Data Explorer Row Menu

### Cell overview

For long strings or other data values that do not fully fit in a grid cell, you can see a tooltip containing the complete value by hovering over the cell:

[![Data explorer cell showing '2013-01-01 0...'. A highlighted row with an expanded view displays '2013-01-01 05:00:00.'](images/data-explorer-cell-value-tooltip.png)](images/data-explorer-cell-value-tooltip.png "Data Explorer Cell Value Tooltip")

Data Explorer Cell Value Tooltip

Right-clicking or pressing on a cell will bring up a context menu for cell specific actions.

[![Data explorer row right-click menu open, showing options: Copy, Select Column, Select Row, Pin Column, Pin Row, Sort Ascending, Sort Descending, Clear Sorting, and Add Filter.](images/data-explorer-cell-menu.png)](images/data-explorer-cell-menu.png "Data Explorer Cell Menu")

Data Explorer Cell Menu

When focused on a cell you can bring up the row header menu by pressing . You can bring up the column header menu by pressing

## Sorting

To sort the values in a column, open a column context menu from the top of the grid and select either **Sort Ascending** or **Sort Descending**.

[![Data explorer column dropdown menu open, showing options: Copy Column, Select Column, Pin Column, Sort Ascending, Sort Descending, Clear Sorting, and Add Filter.](images/data-explorer-column-menu.png)](images/data-explorer-column-menu.png "Data Explorer Column Menu")

Data Explorer Column Menu

To clear an individual column sort, select the column header and choose **Clear Sorting** from the context menu.

When a column is sorted, the column header displays an arrow pointing up or down to indicate the sort direction. You can sort by multiple columns by opening the context menu for a second column and sorting it as well. The number next to the sort direction indicates the sort order of the column.

[![Data Explorer displaying two columns, 'dep_time' with 1.00 values and 'sched_dep_time' showing 2359. Arrows next to column name indicate sorting ascending or descending. Numbers next to arrows indicate order of sort.](images/data-explorer-sort-multiple-columns.png)](images/data-explorer-sort-multiple-columns.png "Sorting Data by Multiple Columns")

Sorting Data by Multiple Columns

To clear all sorting, select the **Clear Column Sorting** button in the top action bar.

## Pinning columns and rows

You can pin columns and rows to keep them visible while scrolling through large datasets. Pinned columns appear on the left side of the grid, and pinned rows appear at the top.

### Pin columns

To pin a column, right-click the column header and select **Pin Column** from the context menu. The column moves to the left side of the grid and remains visible when you scroll horizontally.

To unpin a column, right-click the pinned column header and select **Unpin Column** from the context menu.

### Pin rows

To pin a row, right-click the row header and select **Pin Row** from the context menu. The row moves to the top of the grid and remains visible when you scroll vertically.

To unpin a row, right-click the pinned row header and select **Unpin Row** from the context menu.

### Pin multiple items

You can pin multiple columns and rows. Pinned columns appear in the order you pin them, starting from the leftmost position. Pinned rows appear in the order you pin them, starting from the top.

## Selection, copy, and paste

The data grid provides copy-and-paste capabilities similar to a spreadsheet. You can select:

- A single cell
- A rectangular range of cells
- One or more rows
- One or more columns

To copy a single value, select a cell and press . You can also copy the value using the right-click context menu.

To copy a rectangular range of cells, select a cell, then hold ShiftShift and select another cell to define the range. Press or use the context menu to copy the values.

[![Data grid showing a rectangular selection of cells highlighted in blue, spanning multiple rows and columns of numeric data.](images/data-explorer-copy-rectangular-range.png)](images/data-explorer-copy-rectangular-range.png "Copying a Rectangular Range of Cells")

Copying a Rectangular Range of Cells

When you copy a rectangular range of cells, the system copies the values with column names in tab-separated format. This format makes pasting into Excel or Google Sheets easier.

To copy entire rows or columns, select the first row label or column label. Then either hold ShiftShift and select another row or column label to define a range, or hold and select additional labels to choose individual rows or columns.

[![Data grid showing multiple entire rows selected and highlighted in blue, with row numbers visible on the left.](images/data-explorer-copy-whole-rows.png)](images/data-explorer-copy-whole-rows.png "Copying Multiple Data Rows")

Copying Multiple Data Rows

[![Data grid showing multiple entire columns selected and highlighted in blue, with column headers visible at the top.](images/data-explorer-copy-whole-columns.png)](images/data-explorer-copy-whole-columns.png "Copying Multiple Data Columns")

Copying Multiple Data Columns

When you copy entire rows or columns, the system includes column names in the tab-separated output, similar to copying a rectangular range of cells.
