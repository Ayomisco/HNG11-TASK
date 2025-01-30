
# Public API for HNG12 Stage 0 Task

## Project Overview

This is a simple public API developed for the HNG12 Stage 0 Backend task. It provides basic information, including the developer's registered email, the current UTC datetime, and the GitHub repository URL.

## Technologies Used

* **Framework:** Django Rest Framework (DRF)
* **Programming Language:** Python
* **Deployment:** Hosted on a publicly accessible endpoint
* **Version Control:** GitHub

## API Documentation

### Endpoint

```
GET /api/info/
```

### Response Format (200 OK)

```
{
  "email": "your-email@example.com",
  "current_datetime": "2025-01-30T09:30:00Z",
  "github_url": "https://github.com/yourusername/your-repo"
}
```

### Response Fields

* **email**: The email address registered with HNG12 Slack workspace.
* **current_datetime**: The current date and time in ISO 8601 format (UTC).
* **github_url**: Link to the GitHub repository of this project.

## Setup Instructions

### Prerequisites

* Python 3.x installed
* Django and Django Rest Framework installed

### Installation Steps

1. Clone the repository:
   ```
   git clone https://github.com/Ayomisco/HNG11-TASK.git
   cd your-repo
   ```
2. Create a virtual environment and activate it:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```
3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
4. Run migrations:
   ```
   python manage.py migrate
   ```
5. Start the development server:
   ```
   python manage.py runserver
   ```
6. Test the API:
   ```
   curl http://127.0.0.1:8000/api/info/
   ```

## Deployment

This API is deployed on a publicly accessible endpoint.

## Related Resources

* Learn more about Django: [https://hng.tech/hire/python-developers](https://hng.tech/hire/python-developers)

## License

This project is open-source and available under the MIT License.
