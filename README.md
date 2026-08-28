# DevOps Python Practice

A small Flask API designed for practicing:

- Git and GitHub
- Python virtual environments
- Unit testing with pytest
- Docker
- GitHub Actions CI
- Branches and pull requests
- Basic Linux/server-style environment variables

## 1. Run locally

### Windows PowerShell

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
pytest -q
python app.py
```

Open:

- http://localhost:5000/
- http://localhost:5000/health
- http://localhost:5000/info

### Linux/macOS

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pytest -q
python app.py
```

## 2. Docker

Build:

```bash
docker build -t devops-python-practice .
```

Run:

```bash
docker run --rm -p 5000:5000 -e APP_ENV=docker devops-python-practice
```

Then open http://localhost:5000/health

## 3. Git practice

After extracting this project:

```bash
git init
git add .
git commit -m "Initial DevOps Python practice project"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPOSITORY.git
git push -u origin main
```

Replace `YOUR_USERNAME/YOUR_REPOSITORY` with your GitHub repository.

## 4. Branch and Pull Request practice

```bash
git checkout -b feature/add-version-endpoint
```

Make a change, then:

```bash
git add .
git commit -m "Add version endpoint"
git push -u origin feature/add-version-endpoint
```

Open GitHub and create a Pull Request.

## 5. Suggested practice tasks

1. Add a `/version` endpoint.
2. Add an environment variable called `APP_VERSION`.
3. Add tests for your new endpoint.
4. Create a feature branch.
5. Push the branch.
6. Open a Pull Request.
7. Merge it.
8. Delete the branch.
9. Build the Docker image.
10. Break a test intentionally and watch GitHub Actions fail.
11. Fix the test and push again.
12. Add a simple deployment script.

This gives you hands-on practice with the basic DevOps workflow: code -> Git -> PR -> CI -> Docker.
