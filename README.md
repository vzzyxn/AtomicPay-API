# AtomicPay API 💳

A high-performance, thread-safe financial ledger API built with **FastAPI**, **SQLAlchemy**, and **PostgreSQL**.

This project demonstrates how to build a production-grade payment system that handles **concurrency**, **race conditions**, and **idempotency** to ensure financial data integrity.

## 🚀 Key Features

* **Idempotency:** Implements idempotency keys to ensure that retrying a request (e.g., due to network failure) never results in a duplicate charge.
* **Concurrency Control:** Uses database row-locking (`SELECT FOR UPDATE`) to prevent **Double Spend** attacks when multiple transactions occur simultaneously.
* **Graceful Retries:** Detects duplicate requests and returns the original receipt instead of an error, ensuring a seamless user experience.
* **Atomic Transactions:** All database operations (balance updates + transaction logging) happen within a single atomic commit.

## 🛠️ Tech Stack

* **Language:** Python 3.8+
* **Framework:** FastAPI
* **Database:** PostgreSQL
* **ORM:** SQLAlchemy
* **Validation:** Pydantic

## ⚙️ Setup & Installation

**1. Clone the repository**
```bash
git clone [https://github.com/yourusername/atomic-pay-api.git](https://github.com/yourusername/atomic-pay-api.git)
cd atomic-pay-api
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
