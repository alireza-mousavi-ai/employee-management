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

==========================================
Git & GitHub Cheat Sheet
==========================================

------------------------------------------
1. Go to the project folder
------------------------------------------

cd path/to/project

Example:

cd C:\Users\lenovo\Desktop\employee-management


------------------------------------------
2. Initialize a Git repository
(Only once per project)
------------------------------------------

git init


------------------------------------------
3. Check repository status
------------------------------------------

git status


------------------------------------------
4. Add files to the staging area
------------------------------------------

Add all files:

git add .

Add a specific file:

git add README.md


------------------------------------------
5. Create a commit
------------------------------------------

First commit:

git commit -m "Initial commit"

Examples:

git commit -m "Update README"

git commit -m "Fix validation bug"

git commit -m "Add Excel export"


------------------------------------------
6. Connect local repository to GitHub
(Only once)
------------------------------------------

git remote add origin https://github.com/USERNAME/REPOSITORY.git


------------------------------------------
7. Rename the default branch
(Only once)
------------------------------------------

git branch -M main


------------------------------------------
8. Push the project to GitHub
(First time only)
------------------------------------------

git push -u origin main


------------------------------------------
9. Daily workflow
------------------------------------------

git status

git add .

git commit -m "Describe your changes"

git push


------------------------------------------
10. Download latest changes
------------------------------------------

git pull


------------------------------------------
11. View commit history
------------------------------------------

git log

Short version:

git log --oneline


------------------------------------------
12. Show remote repositories
------------------------------------------

git remote -v


------------------------------------------
13. Remove a file from staging
------------------------------------------

git restore --staged filename


------------------------------------------
14. Delete the local Git repository
------------------------------------------

Delete the hidden ".git" folder.

This removes Git tracking but keeps all project files.


==========================================
Complete Workflow
==========================================

Create Project
      │
      ▼
git init
      │
      ▼
git status
      │
      ▼
git add .
      │
      ▼
git commit -m "Initial commit"
      │
      ▼
Create Repository on GitHub
      │
      ▼
git remote add origin ...
      │
      ▼
git branch -M main
      │
      ▼
git push -u origin main
      │
      ▼
------------------------------------------
Daily Development
------------------------------------------
      │
      ▼
Edit Code
      │
      ▼
git status
      │
      ▼
git add .
      │
      ▼
git commit -m "Describe your changes"
      │
      ▼
git push

==========================================
Most Used Commands
==========================================

git status

git add .

git commit -m "Message"

git push

git pull

git log --oneline

==========================================