### 2. Set up a Virtual Environment
Create an isolated environment for the project to manage dependencies cleanly.

```bash
# Create the virtual environment
python3 -m venv venv

# Activate the virtual environment
# On Linux/macOS:
source venv/bin/activate

# On Windows:
# .\venv\Scripts\activate

### 3. Install Dependencies
```bash
pip install fastapi uvicorn sqlalchemy psycopg2-binary requests

### 4. Run the server
```bash
uvicorn main:app --reload
