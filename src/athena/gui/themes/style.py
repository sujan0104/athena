from athena.gui.themes.colors import Colors


APP_STYLE = f"""
QMainWindow {{
    background-color: {Colors.BACKGROUND};
}}

QWidget {{
    background-color: {Colors.BACKGROUND};
    color: {Colors.TEXT};
    font-family: Segoe UI;
    font-size: 14px;
}}

QPushButton {{
    background-color: transparent;
    color: {Colors.TEXT_SECONDARY};
    border: none;
    border-radius: 12px;
    padding: 14px;
    text-align: left;
    font-size: 14px;
}}

QPushButton:hover {{
    background-color: {Colors.SURFACE};
    color: {Colors.TEXT};
}}

QPushButton[active="true"] {{
    background-color: {Colors.PRIMARY};
    color: white;
    font-weight: bold;
}}

QLabel {{
    color: {Colors.TEXT};
}}

QFrame {{
    border: none;
}}

QListWidget {{
    border: none;
}}
"""