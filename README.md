# Event Management System

A Flask-based web application for managing events, user registrations, and event bookings with admin dashboard functionality.

## Features

- **User Authentication**: Register and login
- **Event Management**: Create, read, update, and delete events
- **Event Booking**: Users can book events
- **Admin Dashboard**: View all events and users
- **File Upload**: Support for event images
- **Role-based Access**: Admin and user roles

## Technology Stack

- **Backend**: Flask (Python)
- **Database**: SQLite
- **Frontend**: HTML/CSS/JavaScript with Jinja2 templating
- **Server**: Gunicorn
- **Deployment**: Heroku-ready

## Installation

### Prerequisites

- Python 3.11+
- pip (Python package manager)

### Local Setup

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd Event_Management
   ```

2. **Create and activate virtual environment**
   ```bash
   # Windows
   python -m venv venv
   venv\Scripts\activate

   # macOS/Linux
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   ```bash
   # Copy example file
   cp .env.example .env
   
   # Edit .env and update SECRET_KEY with a strong random string
   ```

5. **Run the application**
   ```bash
   cd Event_Manage
   python app.py
   ```

   The application will be available at `http://localhost:5000`

## Database

The application uses SQLite with three main tables:

- **users**: User accounts with username, password, and role
- **events**: Event information (name, date, location, description, image)
- **bookings**: User event bookings

Database is automatically initialized on first run.

## Default Admin Setup

To create an admin account, use the provided script:

```bash
cd Event_Manage
python create_admin.py
```

## Deployment

### Heroku Deployment

1. **Install Heroku CLI** and login
   ```bash
   heroku login
   ```

2. **Create Heroku app**
   ```bash
   heroku create your-app-name
   ```

3. **Set environment variables**
   ```bash
   heroku config:set SECRET_KEY="your-secret-key-here"
   heroku config:set FLASK_ENV="production"
   ```

4. **Deploy**
   ```bash
   git push heroku main
   ```

5. **View logs**
   ```bash
   heroku logs --tail
   ```

## Project Structure

```
Event_Management/
├── Event_Manage/
│   ├── app.py                 # Main Flask application
│   ├── create_admin.py        # Admin user creation script
│   ├── static/
│   │   └── uploads/           # Uploaded event images
│   └── templates/
│       ├── base.html          # Base template
│       ├── index.html         # Home page
│       ├── login.html         # Login page
│       ├── register.html      # Registration page
│       ├── add_event.html     # Add event page
│       ├── edit_event.html    # Edit event page
│       ├── bookings.html      # Bookings page
│       └── admin_dashboard.html # Admin dashboard
├── requirements.txt           # Python dependencies
├── .env.example              # Environment variables template
├── Procfile                  # Heroku deployment config
└── README.md                 # This file
```

## Security Notes

⚠️ **Important**: Never commit `.env` file to version control. Always use `.env.example` as a template.

### Before Production:

- Change the `SECRET_KEY` to a strong random string
- Ensure `FLASK_DEBUG` is set to `0`
- Consider using password hashing instead of plain text
- Implement HTTPS/SSL
- Use a production database (PostgreSQL recommended)
- Add CSRF protection
- Implement rate limiting

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Push to the branch
5. Create a Pull Request

## License

This project is open source and available under the MIT License.

## Support

For issues or questions, please create an issue in the repository.
