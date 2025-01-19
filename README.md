# Numerics

http://persson.berkeley.edu/Programming_for_Mathematical_Applications/index.html

https://github.com/popersson/math124files/blob/main/projects/project5_neural_network_character_recognition.ipynb

## Table of Contents
1. [Requirements](#requirements)
    - [Software Installation](#software-installation)
    - [VSCode Extensions](#vscode-extensions)
    - [Dependencies](#dependencies)
2. [Accessing the Julia REPL](#accessing-the-julia-repl)
    - [Windows](#on-windows)
    - [Mac](#on-mac)
3. [Running the Project](#running-the-project)
    - [Setting Up and Using Tasks](#setting-up-and-using-tasks)
    - [Predefined Tasks](#predefined-tasks)
    - [Assigning Custom Shortcuts to Tasks](#assigning-custom-shortcuts-to-tasks)

## Requirements

Make sure the following software is installed:

### Software Installation
- **Python** (version 3.12.3 or compatible)  
  Install via [Python's official website](https://www.python.org/downloads/).

- **Julia** (version 1.11.2 or compatible)  
  Install via [Julia's official website](https://julialang.org/downloads/).

- **VSCode** (recommended editor for both Python and Julia)  
  Install via [VSCode's official website](https://code.visualstudio.com/).

You can check that Python and Julia are installed correctly with
```bash
julia --version
```
and 
```bash
python --version
```

### VSCode Extensions:
- **Python** extension (for Python code execution and debugging).
- **Julia** extension (for Julia code execution and debugging).

### Dependencies

#### Python dependencies:
You can install the necessary dependencies using `pip`. These include `NumPy` and `Matplotlib`:

```bash
pip install numpy matplotlib
```

#### Julia dependencies:
For Julia, install the necessary packages by running the following in the Julia REPL:

```julia
using Pkg  
Pkg.add("Plots")  
Pkg.add("Optim")
```

## Accessing the Julia REPL

### On Windows:
1. **Open Julia**:
   - Press the `Windows` key on your keyboard and type "Julia".
   - Click on the "Julia" application to open it.
   
   Alternatively, if you have Julia installed in a specific directory, you can open a command prompt (`cmd`) and navigate to that directory, then run:
   julia
2. This will launch the Julia REPL, where you can start entering Julia commands.

### On Mac:
1. **Open Julia**:
   - Open `Finder`, go to `Applications`, and find the Julia app.
   - Double-click on the Julia icon to launch the Julia REPL.

   Alternatively, if you have Julia installed via Homebrew, you can open the Terminal and type:
   ```bash
   julia
   ```
2. This will open the Julia REPL, where you can begin executing Julia commands.

## Running the Project

This project uses VSCode tasks to run Julia and Python scripts with the press of a button or a custom shortcut.

### Setting Up and Using Tasks

1. **Ensure `tasks.json` is in place**:
   The `tasks.json` file is pre-configured to run specific Julia and Python scripts. Ensure that it is located under the `.vscode` directory in the root of the repository.

2. **Running Tasks Using Shortcuts**:
   After opening your project in VSCode, you can run predefined tasks with the following shortcut:

   - Press `Ctrl + Shift + B` (Windows/Linux) or `Cmd + Shift + B` (Mac).
   - A prompt will appear asking you to select a task. Choose the one you want to run from the available list.

3. **Predefined Tasks**:
   The tasks configured in `tasks.json` include:
   - **Run Julia GradientOptimization**: Runs the `GradientOptimization.jl` script.
   - **Run Julia gradientTest**: Runs the `gradientTest.jl` script.
   - **Run Python GradientOptimization**: Runs the `GradientOptimization.py` script.
   - **Run Python gradientTest**: Runs the `gradientTest.py` script.

4. **Assigning Custom Shortcuts to Tasks (Optional)**:
   You can assign custom keybindings to specific tasks to make them even more accessible:
   - Open the **Command Palette** (`Ctrl + Shift + P` / `Cmd + Shift + P`).
   - Search for `Preferences: Open Keyboard Shortcuts (JSON)`.
   - Add custom shortcuts for tasks in the `keybindings.json` file. Here’s an example:
   ```json
     [
         {
             "key": "ctrl+alt+g",  // Your custom keybinding
             "command": "workbench.action.tasks.runTask",
             "args": "Run Julia GradientOptimization"
         },
         {
             "key": "ctrl+alt+t",  // Your custom keybinding
             "command": "workbench.action.tasks.runTask",
             "args": "Run Python GradientOptimization"
         }
     ]
    ```
   Replace `"ctrl+alt+g"` and `"ctrl+alt+t"` with your preferred key combinations.
