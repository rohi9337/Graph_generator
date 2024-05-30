````markdown
# Django Graph Generation App

![Project Logo](https://via.placeholder.com/150) 

## Overview

This project is a **Graph Generation App** built with Django and Matplotlib. It allows users to create various types of graphs (line, scatter, bar, histogram) based on user input and display them dynamically in the web interface.

## Features

- **Graph Creation**: Users can create line, scatter, bar, and histogram graphs.
- **Customization**: Titles, labels, colors, and grid options for the graphs.
- **Dynamic Rendering**: Graphs are rendered dynamically based on user input.
- **Image Export**: Users can save generated graphs as PNG files.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Abelleul23/graph-generator.git
   ```
````

2. Navigate to the project directory:
   ```bash
   cd graph-generator
   ```
3. Create a virtual environment:
   ```bash
   python -m venv env
   ```
4. Activate the virtual environment:
   - On Windows:
     ```bash
     .\env\Scripts\activate
     ```
   - On macOS and Linux:
     ```bash
     source env/bin/activate
     ```
5. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
6. Apply migrations:
   ```bash
   python manage.py migrate
   ```
7. Run the development server:
   ```bash
   python manage.py runserver
   ```

## Usage

1. Navigate to `http://127.0.0.1:8000/` in your web browser.
2. Use the graph form to input data and preferences.
3. View the dynamically generated graph on the results page.
4. Optionally, save the generated graph as a PNG file.

## Screenshots

![Graph Form](https://github.com/Abelleul23/graph-generator/Screenshots/graph_form.png) 
_Graph Form_

![Generated Graph](https://github.com/Abelleul23/graph-generator/Screenshots/generated_graph.png)
_Generated Graph_



## Technologies Used

- **Django**: The web framework used for developing the application.
- **Matplotlib**: For generating dynamic graphs.
- **Bootstrap**: For responsive design and UI components.
- **JavaScript**: For interactivity and dynamic content.

## Contributing

Contributions are welcome! Please create an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

- **Abel Leul**: abelteamr@gmail.com
- **Project Link**: [https://github.com/Abelleul23/graph-generator.git](https://github.com/Abelleul23/graph-generator.git)

```

```
