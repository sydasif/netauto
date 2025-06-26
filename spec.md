# Network Automation Web Application — Specification

## 📌 Project Overview

A web-based platform to manage and automate network devices such as routers, switches, and firewalls. The application will provide:
- Centralized device inventory
- SSH-based configuration/command execution
- Modular architecture (extensible to users, jobs, monitoring, and REST API)

---

## 📁 Project Structure

```
netauto/
├── config/               # Django settings & root URL conf
├── devices/              # Device inventory management
├── users/                # (planned) User authentication & roles
├── jobs/                 # (planned) CLI command runs, config push
├── api/                  # (optional) REST API layer
├── templates/            # Shared HTML templates
├── static/               # Static files (CSS, JS)
├── manage.py
└── db.sqlite3            # Development database
```

---

## 🧱 Tech Stack

| Layer            | Tool                    | Description                            |
|------------------|------------------------ |----------------------------------------|
| Backend          | Django (Python)         | Core framework                         |
| Automation       | Nornir + Netmiko/Napalm | Network device automation (SSH)        |
| Frontend         | Django templates        | Minimalist web UI                      |
| Database         | SQLite (dev), PostgreSQL (prod) | Data persistence               |
| Authentication   | Django Auth             | User login (with optional extension)   |
| Task Queue       | (Future: Celery)        | For async CLI execution                |
| API Layer        | (Future: DRF)           | REST endpoints for external use        |
| Deployment       | Localhost or Docker     | Flexible, simple development setup     |

---

## ✅ Phase 1: Device Inventory

### 🎯 Goals
- CRUD operations for network devices
- Admin UI via Django
- Forms/UI for adding/viewing devices

### 🔢 Model: `NetworkDevice`
```python
class NetworkDevice(models.Model):
    name        = models.CharField(max_length=100)
    ip_address  = models.GenericIPAddressField()
    device_type = models.CharField(max_length=20, choices=[...])
    vendor      = models.CharField(max_length=50, blank=True)
    platform    = models.CharField(max_length=50)  # e.g., cisco_ios
    username    = models.CharField(max_length=50)
    password    = models.CharField(max_length=50)
```

### 🧰 Admin Panel
- View devices
- Search by name/IP/vendor
- Add/edit/delete entries

---

## ⏳ Future Apps

### 🔐 Users App
- User signup, login, logout
- Optional roles: Admin, Operator
- Access control for devices/jobs

### ⚙️ Jobs App
- Select devices, run CLI commands via Nornir
- Show per-device results
- Store output history

### 🔄 Monitoring App
- Periodic health checks (ping/SSH/API)
- Status view (up/down)
- Alerts/logging

### 🌐 API App
- REST API for CRUD, jobs, auth
- Token or session-based auth

---

## 🚦 Milestones

| Phase | Feature                      | Status  |
|-------|------------------------------|---------|
| 1     | Device model + admin UI      | ⏳      |
| 2     | Device list/create UI        | ⏳ Next |
| 3     | CLI runner (Nornir task)     | ⏳ Planned |
| 4     | User login + roles           | ⏳ Planned |
| 5     | Logs & job history           | ⏳ Planned |
| 6     | REST API                     | ⏳ Future |
| 7     | Monitoring + alerting        | ⏳ Future |

---

## 🔐 Security Notes

- Passwords will be stored encrypted or via environment variables in production
- Role-based access control to be added in `users` app
- Use `.env` file or Django secrets management for sensitive data

---

## 📄 License

This project is open-source and licensed under the [MIT License](LICENSE).
