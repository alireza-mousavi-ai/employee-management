# Developer Notes

Useful commands for developing and maintaining the project.

---

## Requirements

Generate `requirements.txt`:

```bash
pip freeze > requirements.txt
```

Install project dependencies:

```bash
pip install -r requirements.txt
```

---

## PyInstaller

Install PyInstaller:

```bash
pip install pyinstaller
```

Show version:

```bash
python -m PyInstaller --version
```

Build executable:

```bash
python -m PyInstaller --onefile --name EmployeeManagement main.py
```

Build executable with icon:

```bash
python -m PyInstaller --onefile --icon=icon.ico main.py
```

The executable will be generated in the `dist/` folder.

---

## Ruff

Install Ruff:

```bash
pip install ruff
```

Show version:

```bash
python -m ruff --version
```

Show package information:

```bash
python -m pip show ruff
```

Check code quality:

```bash
python -m ruff check .
```

Automatically fix problems:

```bash
python -m ruff check . --fix
```

Format the project:

```bash
python -m ruff format .
```

---

## Git

Check repository status:

```bash
git status
```

Stage all changes:

```bash
git add .
```

Commit changes:

```bash
git commit -m "Your commit message"
```

Push to GitHub:

```bash
git push
```