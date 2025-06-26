# NetAuto: A Network Automation Web Platform

[![Project Status](https://img.shields.io/badge/status-in%20development-orange)](https://github.com/your-username/netauto)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python Version](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![Django Version](https://img.shields.io/badge/django-4.x-green.svg)](https://www.djangoproject.com/)

NetAuto is a web-based platform designed to centralize the management and automation of network devices like routers, switches, and firewalls. It provides a simple, clean interface for maintaining a device inventory and executing commands, with a modular architecture for future expansion.

## ✨ Features

-   **Centralized Device Inventory**: A single source of truth for all your network devices.
-   **CRUD Operations**: Easily create, read, update, and delete devices through a web UI and the Django admin panel.
-   **SSH-Based Automation**: (Planned) Leverage Nornir and Netmiko/Napalm to run commands and push configurations to multiple devices simultaneously.
-   **Modular & Extensible**: Designed with Django apps to easily add new functionality like user roles, job scheduling, monitoring, and a REST API.
-   **Minimalist UI**: Simple and effective frontend using Django Templates, focusing on functionality over complexity.

---

## 🚦 Project Roadmap & Status

| Phase | Feature                             | Status            |
| :---: | ----------------------------------- | ----------------- |
|   1   | Device model + Django Admin UI      | ✅ **Completed**   |
|   2   | Device List/Create/Update/Delete UI | ▶️ **In Progress** |
|   3   | CLI Runner (Nornir Task Execution)  | ⏳ **Planned**     |
|   4   | User Authentication & Roles         | ⏳ **Planned**     |
|   5   | Job History & Output Logging        | ⏳ **Planned**     |
|   6   | REST API (DRF)                      | 🌟 **Future**      |
|   7   | Device Monitoring & Alerting        | 🌟 **Future**      |

---

## 🛠️ Tech Stack

| Layer          | Tool                                | Description                                      |
| :------------- | :---------------------------------- | :----------------------------------------------- |
| **Backend**    | Django (Python)                     | Core web framework for rapid development.        |
| **Automation** | Nornir + Netmiko/Napalm             | Engine for network device automation (SSH).      |
| **Frontend**   | Django Templates + (Minimal CSS/JS) | Server-side rendered, functional web UI.         |
| **Database**   | SQLite (dev), PostgreSQL (prod)     | Flexible data persistence.                       |
| **Auth**       | Django Auth                         | Built-in user authentication.                    |
| **Task Queue** | Celery (Future)                     | For running long automation jobs asynchronously. |
| **API Layer**  | Django Rest Framework (Future)      | For building a comprehensive REST API.           |
| **Deployment** | Localhost / Docker                  | Simple and flexible deployment options.          |

---

## 🚀 Getting Started

Follow these instructions to get a local development environment running.

### Prerequisites

-   [Python](https://www.python.org/downloads/) (3.9 or higher)
-   [Git](https://git-scm.com/)

### Installation

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/your-username/netauto.git
    cd netauto
    ```

2.  **Create and activate a virtual environment:**
    ```bash
    # For macOS/Linux
    python3 -m venv venv
    source venv/bin/activate

    # For Windows
    python -m venv venv
    .\venv\Scripts\activate
    ```

3.  **Install project dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
    *(Note: You will need to create a `requirements.txt` file containing `Django`, `nornir`, etc.)*

4.  **Set up environment variables:**
    Create a `.env` file in the project root directory by copying the example file:
    ```bash
    cp .env.example .env
    ```
    Now, open the `.env` file and set a `SECRET_KEY`. You can generate one easily.
    ```ini
    # .env
    SECRET_KEY='your-super-secret-key-here'
    DEBUG=True
    ```

5.  **Apply database migrations:**
    This will create the database schema, including the `NetworkDevice` table.
    ```bash
    python manage.py migrate
    ```

6.  **Create a superuser:**
    This account will be used to access the Django admin interface.
    ```bash
    python manage.py createsuperuser
    ```
    Follow the prompts to set a username, email, and password.

7.  **Run the development server:**
    ```bash
    python manage.py runserver
    ```

8.  **Access the application:**
    -   **Web App**: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
    -   **Admin Panel**: [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)

---

## 📁 Project Structure

```
netauto/
├── config/         # Django settings & root URL configuration
├── devices/        # Core app for device inventory management (Models, Views, Forms)
├── users/          # (Planned) User authentication, profiles, and roles
├── jobs/           # (Planned) App for running and logging automation tasks
├── api/            # (Optional) Houses the Django Rest Framework API
├── templates/      # Global HTML templates shared across apps
├── static/         # Global static files (CSS, JavaScript, images)
├── manage.py       # Django's command-line utility
└── db.sqlite3      # Development database file
```

---

## 🔐 Security Considerations

-   **Secrets Management**: Never commit your `.env` file or any other files containing sensitive credentials to version control. Use environment variables or a secrets management tool in production.
-   **Password Storage**: The `NetworkDevice` model stores passwords in plaintext for automation. In a production environment, this is highly discouraged. Use a secure vault (e.g., HashiCorp Vault, Ansible Vault) and integrate it with the application.
-   **Role-Based Access Control (RBAC)**: The `users` app is planned to implement RBAC, restricting device access and job execution capabilities based on user roles (e.g., Admin vs. Operator).
-   **Debug Mode**: Ensure `DEBUG` is set to `False` in production environments.

---

## 🤝 Contributing

Contributions are welcome! If you have suggestions or want to add a feature, please follow these steps:

1.  Fork the Project.
2.  Create your Feature Branch (`git checkout -b feature/AmazingFeature`).
3.  Commit your Changes (`git commit -m 'Add some AmazingFeature'`).
4.  Push to the Branch (`git push origin feature/AmazingFeature`).
5.  Open a Pull Request.

---

## 📄 License

This project is open-source and distributed under the **MIT License**. See the [`LICENSE`](/LICENSE) file for more information.
