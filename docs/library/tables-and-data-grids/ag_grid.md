---
components:
  - ag_grid
---

```python exec
from pcweb.pages.docs import library
from pcweb.pages.docs import vars
```

# AG Grid

Reflex AG Grid is a high-performance and highly customizable grid that wraps AG Grid.

```bash
pip install reflex-ag-grid
```

## Your First Reflex AG Grid

A basic Reflex AG Grid contains column definitions `column_defs`, which define the columns to be displayed in the grid, and `row_data`, which contains the data to be displayed in the grid.

Each grid also requires a unique `id`, which is needed to uniquely identify the Ag-Grid instance on the page. If you have multiple grids on the same page, each grid must have a unique `id` so that it can be correctly rendered and managed.

```md alert info
# Grid for Layout

If you are looking for a grid for layout purposes, i.e. to layout Reflex components, consider using the [Grid component]({library.layout.grid.path}).
```

```python demo exec
import reflex as rx
from reflex_ag_grid import ag_grid
import pandas as pd


df = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/wind_dataset.csv")

column_defs = [
    ag_grid.column_def(field="direction"),
    ag_grid.column_def(field="strength"),
    ag_grid.column_def(field="frequency"),

]

def ag_grid_simple():
    return ag_grid(
        id="ag_grid_basic_1",
        row_data=df.to_dict("records"),
        column_defs=column_defs,
        width="100%",
    )
```

The format of the data passed to the `row_data` prop is a list of dictionaries. Each dictionary represents a row in the grid as seen below.

```python
[
   \{direction: "N", strength: "0-1", frequency: 0.5},
   \{direction: "NNE", strength: "0-1", frequency: 0.6},
   \{direction: "NE", strength: "0-1", frequency: 0.5},
]
```

The previous example showed the `column_defs` written out in full. You can also extract the required information from the dataframe's column names:

```python demo exec
import reflex as rx
from reflex_ag_grid import ag_grid
import pandas as pd


df = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/wind_dataset.csv")


def ag_grid_simple_2():
    return ag_grid(
        id="ag_grid_basic_2",
        row_data=df.to_dict("records"),
        column_defs=[{"field": i} for i in df.columns],
        width="100%",
        height="40vh",
    )
```

## Headers

In the above example, the first letter of the field names provided are capitalized when displaying the header name. You can customize the header names by providing a `header_name` key in the column definition. In this example, the `header_name` is customized for the second and third columns.

```python demo exec
import reflex as rx
from reflex_ag_grid import ag_grid
import pandas as pd


df = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/gapminder2007.csv")

column_defs = [
    ag_grid.column_def(field="country"),
    ag_grid.column_def(field="pop", header_name="Population"),
    ag_grid.column_def(field="lifeExp", header_name="Life Expectancy"),
]

def ag_grid_simple_headers():
    return ag_grid(
            id="ag_grid_basic_headers",
            row_data=df.to_dict("records"),
            column_defs=column_defs,
            width="100%",
            height="40vh",
        )
```

## Column Filtering

Allow a user to filter a column by setting the `filter` key to `True` in the column definition. In this example we enable filtering for the first and last columns.

```python demo exec
import reflex as rx
from reflex_ag_grid import ag_grid
import pandas as pd


df = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/gapminder2007.csv")

column_defs =  [
    ag_grid.column_def(field="country", header_name="Country", filter=True),
    ag_grid.column_def(field="pop", header_name="Population"),
    ag_grid.column_def(field="lifeExp", header_name="Life Expectancy", filter=True),
]

def ag_grid_simple_column_filtering():
    return ag_grid(
        id="ag_grid_basic_column_filtering",
        row_data=df.to_dict("records"),
        column_defs=column_defs,
        width="100%",
        height="40vh",
    )
```

### Filter Types

You can set `filter=True` to enable the default filter for a column.

You can also set the filter type using the `filter` key. The following filter types are available: `ag_grid.filters.date`, `ag_grid.filters.number` and `ag_grid.filters.text`. These ensure that the input you enter to the filter is of the correct type.

(`ag_grid.filters.set` and `ag_grid.filters.multi` are available with AG Grid Enterprise)

```python demo exec
import reflex as rx
from reflex_ag_grid import ag_grid
import pandas as pd


df = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/GanttChart-updated.csv")

column_defs =  [
    ag_grid.column_def(field="Task", filter=True),
    ag_grid.column_def(field="Start", filter=ag_grid.filters.date),
    ag_grid.column_def(field="Duration", filter=ag_grid.filters.number),
    ag_grid.column_def(field="Resource", filter=ag_grid.filters.text),
]

def ag_grid_simple_column_filtering():
    return ag_grid(
        id="ag_grid_basic_column_filtering",
        row_data=df.to_dict("records"),
        column_defs=column_defs,
        width="100%",
        height="40vh",
    )
```

## Row Sorting

By default, the rows can be sorted by any column by clicking on the column header. You can disable sorting of the rows for a column by setting the `sortable` key to `False` in the column definition.

In this example, we disable sorting for the first column.

```python demo exec
import reflex as rx
from reflex_ag_grid import ag_grid
import pandas as pd


df = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/gapminder2007.csv")

column_defs =  [
    ag_grid.column_def(field="country", sortable=False),
    ag_grid.column_def(field="pop", header_name="Population"),
    ag_grid.column_def(field="lifeExp", header_name="Life Expectancy"),
]

def ag_grid_simple_row_sorting():
    return ag_grid(
        id="ag_grid_basic_row_sorting",
        row_data=df.to_dict("records"),
        column_defs=column_defs,
        width="100%",
        height="40vh",
    )
```

## Row Selection

Row Selection is enabled using the `row_selection` attribute. Setting it to `multiple` allows users to select multiple rows at a time. You can use the `checkbox_selection` column definition attribute to render checkboxes for selection.

```python demo exec
import reflex as rx
from reflex_ag_grid import ag_grid
import pandas as pd


df = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/gapminder2007.csv")

column_defs = [
    ag_grid.column_def(field="country", checkbox_selection=True),
    ag_grid.column_def(field="pop", header_name="Population"),
    ag_grid.column_def(field="continent"),
]

def ag_grid_simple_row_selection():
    return ag_grid(
        id="ag_grid_basic_row_selection",
        row_data=df.to_dict("records"),
        column_defs=column_defs,
        row_selection="multiple",
        width="100%",
        height="40vh",
    )
```

## Editing

Enable Editing by setting the `editable` attribute to `True`. The cell editor is inferred from the cell data type. Set the cell editor type using the `cell_editor` attribute.

There are 7 provided cell editors in AG Grid:

1. `ag_grid.editors.text`
2. `ag_grid.editors.large_text`
3. `ag_grid.editors.select`
4. `ag_grid.editors.rich_select`
5. `ag_grid.editors.number`
6. `ag_grid.editors.date`
7. `ag_grid.editors.checkbox`

In this example, we enable editing for the second and third columns. The second column uses the `number` cell editor, and the third column uses the `select` cell editor.

The `on_cell_value_changed` event trigger is linked to the `cell_value_changed` event handler in the state. This event handler is called whenever a cell value is changed and changes the value of the backend var `_data_df` and the state var `data`.

```python demo exec
import reflex as rx
from reflex_ag_grid import ag_grid
import pandas as pd

class AGGridEditingState(rx.State):
    _data_df = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/gapminder2007.csv")
    data: list[dict] = _data_df.to_dict("records")

    @rx.event
    def cell_value_changed(self, row, col_field, new_value):
        self._data_df.at[row, col_field] = new_value
        self.data = self._data_df.to_dict("records")
        yield rx.toast(f"Cell value changed, Row: {row}, Column: {col_field}, New Value: {new_value}")


column_defs = [
    ag_grid.column_def(field="country"),
    ag_grid.column_def(field="pop", header_name="Population", editable=True, cell_editor=ag_grid.editors.number),
    ag_grid.column_def(field="continent", editable=True, cell_editor=ag_grid.editors.select, cell_editor_params={
        "values": ['Asia', 'Europe', 'Africa', 'Americas', 'Oceania']
        }
    ),
]

def ag_grid_simple_editing():
    return ag_grid(
        id="ag_grid_basic_editing",
        row_data=AGGridEditingState.data,
        column_defs=column_defs,
        on_cell_value_changed=AGGridEditingState.cell_value_changed,
        width="100%",
        height="40vh",
    )
```

## Pagination

By default, the grid uses a vertical scroll. You can reduce the amount of scrolling required by adding pagination. To add pagination, set `pagination=True`. You can set the `pagination_page_size` to the number of rows per page and `pagination_page_size_selector` to a list of options for the user to select from.

```python demo exec
import reflex as rx
from reflex_ag_grid import ag_grid
import pandas as pd

df = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/gapminder2007.csv")

column_defs = [
    ag_grid.column_def(field="country"),
    ag_grid.column_def(field="pop", header_name="Population"),
    ag_grid.column_def(field="lifeExp", header_name="Life Expectancy"),
]

def ag_grid_simple_pagination():
    return ag_grid(
        id="ag_grid_basic_pagination",
        row_data=df.to_dict("records"),
        column_defs=column_defs,
        pagination=True,
        pagination_page_size=10,
        pagination_page_size_selector=[10, 40, 100],
        width="100%",
        height="40vh",
    )
```

## Themes

You can style your grid with a theme. AG Grid includes the following themes:

1. `quartz`
2. `alpine`
3. `balham`
4. `material`

The grid uses `quartz` by default. To use any other theme, set it using the `theme` prop, i.e. `theme="alpine"`.

```python demo exec
import reflex as rx
from reflex_ag_grid import ag_grid
import pandas as pd

class AGGridThemeState(rx.State):
    """The app state."""

    theme: str = "quartz"
    themes: list[str] = ["quartz", "balham", "alpine", "material"]

df = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/gapminder2007.csv")

column_defs = [
    ag_grid.column_def(field="country"),
    ag_grid.column_def(field="pop", header_name="Population"),
    ag_grid.column_def(field="lifeExp", header_name="Life Expectancy"),
]

def ag_grid_simple_themes():
    return rx.vstack(
        rx.hstack(
            rx.text("Theme:"),
            rx.select(AGGridThemeState.themes, value=AGGridThemeState.theme, on_change=AGGridThemeState.set_theme),
        ),
        ag_grid(
            id="ag_grid_basic_themes",
            row_data=df.to_dict("records"),
            column_defs=column_defs,
            theme=AGGridThemeState.theme,
            width="100%",
            height="40vh",
        ),
        width="100%",
    )
```

## AG Grid with State

### Putting Data in State

Assuming you want to make any edit to your data, you can put the data in State. This allows you to update the grid based on user input. Whenever the `data` var is updated, the grid will be re-rendered with the new data.

```python demo exec
from typing import Any
import reflex as rx
from reflex_ag_grid import ag_grid
import pandas as pd

class AGGridState2(rx.State):
    _data_df = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/gapminder2007.csv")
    data: list[dict] = _data_df.to_dict("records")

column_defs = [
    ag_grid.column_def(field="country"),
    ag_grid.column_def(field="pop", header_name="Population"),
    ag_grid.column_def(field="continent"),
]

def ag_grid_state_2():
    return ag_grid(
        id="ag_grid_state_2",
        row_data=AGGridState2.data,
        column_defs=column_defs,
        width="100%",
        height="40vh",
    )
```

### Updating the Grid with State

You can use State to update the grid based on a users input. In this example, we update the `column_defs` of the grid when a user clicks a button.

```python demo exec
import reflex as rx
from reflex_ag_grid import ag_grid
import pandas as pd

class AgGridState(rx.State):
    """The app state."""
    all_columns = [
        ag_grid.column_def(field="country"),
        ag_grid.column_def(field="pop"),
        ag_grid.column_def(field="continent"),
        ag_grid.column_def(field="lifeExp"),
        ag_grid.column_def(field="gdpPercap"),
    ]

    two_columns = [
        ag_grid.column_def(field="country"),
        ag_grid.column_def(field="pop"),
    ]
    column_defs = all_columns
    n_clicks = 0

    @rx.event
    def update_columns(self):
        self.n_clicks += 1
        if self.n_clicks % 2 != 0:
            self.column_defs = self.two_columns
        else:
            self.column_defs = self.all_columns


df = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/gapminder2007.csv")


def ag_grid_simple_with_state():
    return rx.box(
        rx.button("Toggle Columns", on_click=AgGridState.update_columns),
        ag_grid(
            id="ag_grid_basic_with_state",
            row_data=df.to_dict("records"),
            column_defs=AgGridState.column_defs,
            width="100%",
            height="40vh",
        ),
        width="100%",
    )
```

## AG Grid with Data from a Database

In this example, we will use a database to store the data. The data is loaded from a csv file and inserted into the database when the page is loaded using the `insert_dataframe_to_db` event handler.

The data is then fetched from the database and displayed in the grid using the `data` [computed var]({vars.computed_vars.path}).

When a cell value is changed, the data is updated in the database using the `cell_value_changed` event handler.

```python
import reflex as rx
from reflex_ag_grid import ag_grid
import pandas as pd
from sqlmodel import select

class Country(rx.Model, table=True):
    country: str
    population: int
    continent: str


class AGGridDatabaseState(rx.State):

    countries: list[Country]

    # Insert data from a csv loaded dataframe to the database (Do this on the page load)
    @rx.event
    def insert_dataframe_to_db(self):
        data = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/gapminder2007.csv")
        with rx.session() as session:
            for _, row in data.iterrows():
                db_record = Country(
                    country=row['country'],
                    population=row['pop'],
                    continent=row['continent'],
                )
                session.add(db_record)
            session.commit()

    # Fetch data from the database using a computed variable
    @rx.var
    def data(self) -> list[dict]:
        with rx.session() as session:
            results = session.exec(select(Country)).all()
            self.countries = [result.dict() for result in results]
        return self.countries

    # Update the database when a cell value is changed
    @rx.event
    def cell_value_changed(self, row, col_field, new_value):
        self.countries[row][col_field] = new_value
        with rx.session() as session:
            country = Country(**self.countries[row])
            session.merge(country)
            session.commit()
        yield rx.toast(f"Cell value changed, Row: \{row}, Column: \{col_field}, New Value: \{new_value}")


column_defs = [
    ag_grid.column_def(field="country"),
    ag_grid.column_def(field="population", header_name="Population", editable=True, cell_editor=ag_grid.editors.number),
    ag_grid.column_def(field="continent", editable=True, cell_editor=ag_grid.editors.select, cell_editor_params={
        "values": ['Asia', 'Europe', 'Africa', 'Americas', 'Oceania']
        }
    ),
]

def index():
    return ag_grid(
        id="ag_grid_basic_editing",
        row_data=AGGridDatabaseState.data,
        column_defs=column_defs,
        on_cell_value_changed=AGGridDatabaseState.cell_value_changed,
        width="100%",
        height="40vh",
    )

# Add state and page to the app.
app = rx.App()
app.add_page(index, on_load=AGGridDatabaseState.insert_dataframe_to_db)
```

## Using AG Grid Enterprise

AG Grid offers both community and enterprise versions. See the [AG Grid docs](https://www.ag-grid.com/archive/31.2.0/react-data-grid/licensing/) for details on purchasing a license key.

To use an AG Grid Enterprise license key with Reflex AG Grid set the environment variable `AG_GRID_LICENSE_KEY`:

```bash
export AG_GRID_LICENSE_KEY="your_license_key"
```

## column_def props

The following props are available for `column_defs` as well as many others that can be found here: [AG Grid Column Def Docs](https://www.ag-grid.com/react-data-grid/column-properties/). (it is necessary to use snake_case for the keys in Reflex, unlike in the AG Grid docs where camelCase is used)

- `field`: `str`: The field of the row object to get the cell's data from.
- `col_id`: `str | None`: The unique ID to give the column. This is optional. If missing, the ID will default to the field.
- `type`: `str | None`: The type of the column.
- `cell_data_type`: `bool | str | None`: The data type of the cell values for this column. Can either infer the data type from the row data (true - the default behaviour), define a specific data type (string), or have no data type (false).
- `hide`: `bool`: Set to true for this column to be hidden.
- `editable`: `bool | None`: Set to true if this column is editable, otherwise false.
- `filter`: `AGFilters | str | None`: Filter component to use for this column. Set to true to use the default filter. Set to the name of a provided filter to use that filter. (Check out the Filter Types section of this page for more information)
- `floating_filter`: `bool`: Whether to display a floating filter for this column.
- `header_name`: `str | None`: The name to render in the column header. If not specified and field is specified, the field name will be used as the header name.
- `header_tooltip`: `str | None`: Tooltip for the column header.
- `checkbox_selection`: `bool | None`: Set to true to render a checkbox for row selection.
- `cell_editor`: `AGEditors | str | None`: Provide your own cell editor component for this column's cells. (Check out the Editing section of this page for more information)
- `cell_editor_params`: `dict[str, list[Any]] | None`: Params to be passed to the cellEditor component.
