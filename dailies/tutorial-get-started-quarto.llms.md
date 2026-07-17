# First data analysis with R in a Quarto document

This quick tutorial will show you how to use [Quarto documents](quarto.llms.md) within Positron. We will:

- Install Positron
- Create an R project
- Install the packages we need for our analysis
- Open a Quarto document
- Explore some data

## Install Positron

Positron is a free and source available code editor for data scientists. To install Positron on your computer, visit our [download page](download.llms.md) and click **Download**.

[![The Positron download page with the Download button.](images/download-button.png)](images/download-button.png "The Positron download page")

The Positron download page

Follow the instructions to install Positron.

## Make a folder for your analysis

It is good practice to give each analysis its own folder. A folder keeps your scripts, data, and outputs together in one tidy place. Positron makes it easy to create one.

Follow these steps:

1.  Open Positron
2.  Select **New \> New Folder from Template**

[![New Folder from Template option in the File menu.](images/new-folder-from-template.png)](images/new-folder-from-template.png "New Folder from Template in the File menu")

New Folder from Template in the File menu

3.  Select **R Project** from the template list

[![R Project template option in the New Folder from Template dialog.](images/r-project-template.png)](images/r-project-template.png "R Project template")

R Project template

4.  Select a location for your project folder and give it a name. Then click **Next**.

[![Create R Project dialog.](images/create-r-project.png)](images/create-r-project.png "Create R Project dialog")

Create R Project dialog

On the next screen, select a version of R to use from those available on your computer. Then click **Create**. Positron scaffolds the folder for you and launches an R console session automatically.

[![Create R Environment dialog.](images/create-r-environment.png)](images/create-r-environment.png "Create R Environment dialog")

Create R Environment dialog

## Install packages

Now that we have a project set up, we need to install the packages we will use for our analysis. For this tutorial, we will use the tidyverse package, which includes dplyr for data manipulation and ggplot2 for visualization.

tidyverse is a collection of R packages designed for data science. It includes packages that share a common design philosophy and cover the basic data science tasks: data import, tidying, transformation, visualization, and more.

To install tidyverse, navigate to the R Console in Positron (**View \> Console**) and run:

``` r
install.packages("tidyverse")
```

You only need to install a package once. After that, you load it with `library()` each time you start a new R session.

## Open a Quarto document

Now that we have our project set up and the packages we need installed, we can open a Quarto document to start our analysis.

To create a new Quarto document in Positron:

1.  Select **New \> New File**
2.  Select **Quarto Document** from the list of file types

[![New Quarto Document option in the New File dialog.](images/new-quarto-document.png)](images/new-quarto-document.png "New Quarto Document in the New File dialog")

New Quarto Document in the New File dialog

This opens a new `.qmd` file in your source editor. You can now start writing text and code.

A Quarto document is a plain text file that mixes markdown text with code cells. It is similar to an R Markdown document, but with more features and support for multiple languages. Learn more at the [Quarto documentation](https://quarto.org).

A Quarto document begins with a YAML header enclosed in `---` marks. This header contains metadata like the document’s title and output format. Below the header, you write markdown text and insert code cells to run R code.

To insert a new R code cell, use the keyboard shortcut . This inserts a fenced code block that looks like this:

```` markdown
```{r}

```
````

You can type your R code inside the cell and click **Run** at the top right of the cell to execute it. The output appears directly below the cell in the editor.

## Explore some data

Now that we have our Quarto document open, we can start exploring some data. For this tutorial, we will use the `starwars` dataset, which is a built-in dataset in the dplyr package. It contains information about Star Wars characters, including their name, height, mass, species, and more.

Insert a new code cell with and add the following code, then click **Run**:

``` r
library(tidyverse)
```

This loads the tidyverse packages into your R session. Next, insert another code cell and run:

``` r
starwars <- dplyr::starwars
```

Notice that the Variables pane to the right of the editor shows the `starwars` dataset. You can use the Variables pane to explore the columns in the dataset. Or you can click the grid-like icon to open the dataset in the Positron Data Explorer.

[![Variables pane showing the starwars dataset variable.](images/variables-pane-starwars.png)](images/variables-pane-starwars.png "The starwars dataset in the Variables pane")

The starwars dataset in the Variables pane

The Data Explorer allows you to sort and filter the data, as well as view summary statistics. If you would like to recreate a filter, click **Convert to Code** to copy the code for that filter to your clipboard. You can then paste that code into a cell in your Quarto document to run it.

Narrow the dataset down to human characters using the code generated by the Data Explorer:

``` r
starwars_humans <- starwars |>
  filter(species == "Human")
```

This video shows how to open a Quarto document and use the Data Explorer to generate the filtering code above.

Next we will visualize the relationship between height and mass for human Star Wars characters using ggplot2:

``` r
ggplot(starwars_humans, aes(x = height, y = mass)) +
  geom_point(aes(color = gender), size = 3, alpha = 0.7) +
  geom_smooth(method = "lm", se = FALSE) +
  labs(
    title = "Star Wars Humans: Height vs Mass",
    x = "Height (cm)",
    y = "Mass (kg)"
  )
```

And then make a quick summary table showing average height and mass by gender:

``` r
starwars_humans |>
  group_by(gender) |>
  summarize(
    avg_height = mean(height, na.rm = TRUE),
    avg_mass = mean(mass, na.rm = TRUE),
    n = n()
  ) |>
  arrange(desc(avg_height))
```

We can also write text in markdown between our code cells. For example, we can explain our work or add section headers. This is also a good time to change the title of your document, if you have not already.

Watch as we run the code above.

## Save your document

To save your document, click **Save** in the toolbar or use the keyboard shortcut . The `.qmd` file appears in the File Explorer on the left.

> **NOTE:**
>
> If your project is version-controlled with Git, you can commit and push straight from the Git pane in Positron. This is handy for sharing your analysis or keeping a backup on GitHub.
>
> Learn more about [using Git in Positron](git.llms.md).

## Render and preview your document

A major benefit of Quarto is that you can render your saved document into a polished report with a single shortcut. Press , or click **Preview** at the top of the editor.

Positron renders your `.qmd` file into an HTML document and displays a live preview in the Viewer pane alongside your source code. Every time you render, Quarto executes all of the code cells in order and produces a complete report with your text, code, and outputs.

The new HTML file is saved in the project folder beside your `.qmd` file. You can open this file in any web browser to view your report, or share it with others.

See this process unfold in the video.

Turn on **Render on Save** (in Settings, via the checkbox on the editor action bar, or by adding `editor: render-on-save: true` to the YAML header) and your report refreshes every time you save the file.

## Conclusion

Well done! You have set up an R project in Positron, installed packages, and built a small data analysis inside a Quarto document. To learn more about Quarto, see the [Quarto documentation](https://quarto.org).

> **NOTE:**
>
> To keep going, explore the [Guides](welcome.llms.md) for in-depth documentation on everything Positron can do.
