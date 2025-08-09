# RemedyAI Backend

## Quick Start

Apabila sudah melakukan instalasi, cukup jalankan

```bash
.venv/Scripts/activate
uvicorn main:app
```

Namun, apabila belum pernah menjalankan aplikasi ini sebelumnya, lakukan langkah-langkah berikut

### 1. Install Dependencies

```bash
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
uv venv -p 3.13
.venv/Scripts/activate
uv pip install -e .
```

### 2. Setup Environment

```bash
cp .env.example .env
```

### 3. Setup Database

Initialize the SQLite database:
```bash
python ./scripts/init_db.py
```

### 4. Jalankan server

```bash
uvicorn main:app
```

API bisa diakses pada `http://localhost:8000`

## Cara pengetesan API

Untuk membuat pesan, coba *paste* perintah ini ke terminal

```bash
Invoke-WebRequest -Uri http://localhost:8000/messages/create -Method POST -ContentType "application/json" -Body '{"text": "Hello world"}'
```

Periksa pesan yang tersimpan dengan perintah berikut

```bash
# Pengaksesan semua pesan
Invoke-WebRequest -Method GET -Uri http://localhost:8000/messages

# Pengaksesan pesan tertentu
Invoke-WebRequest -Method GET -Uri http://localhost:8000/messages/{id}
```

Pesan yang sudah disimpan dapat dihapus dengan perintah berikut

```bash
Invoke-WebRequest -Method DELETE -Uri http://localhost:8000/messages/{id}
```
