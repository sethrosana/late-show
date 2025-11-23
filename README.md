# Late Show API

A Flask-based REST API for managing late-night show episodes, guests, and their appearances. This application provides endpoints to retrieve episode information, manage guest details, and track guest ratings across different show appearances.

## Overview

Late Show API is a Python REST service built with Flask and SQLAlchemy that models the relationships between television episodes and celebrity guests. It allows you to query episodes, manage guest profiles, and record guest appearances with performance ratings.

## Features

- **Episode Management**: Create, read, and delete episode records with dates and episode numbers
- **Guest Database**: Maintain a comprehensive guest list with names and occupations
- **Appearance Tracking**: Record and rate guest appearances on specific episodes (1-5 scale)
- **RESTful API**: Clean, intuitive endpoints for all data operations
- **Data Validation**: Input validation for appearance ratings (must be between 1-5)
- **PostgreSQL Backend**: Persistent data storage with migration support

## Tech Stack

- **Framework**: Flask 2.3.0
- **ORM**: SQLAlchemy 2.0.44 with Flask-SQLAlchemy 3.0.3
- **Database**: PostgreSQL
- **API**: Flask-RESTful 0.3.10
- **Migrations**: Alembic via Flask-Migrate 4.0.4
- **Serialization**: SQLAlchemy-serializer 1.4.1
- **Testing**: pytest 7.3.1

## Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd late-show
   ```

2. **Activate virtual environment**
   ```bash
   source env/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure database**
   - Ensure PostgreSQL is running
   - Update the database URI in `server/app.py` if needed:
     ```python
     app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://late_show_user:sethmorara@localhost:5432/late_show_db"
     ```

5. **Run migrations**
   ```bash
   flask db upgrade
   ```

6. **Seed the database** (optional)
   ```bash
   python server/seed.py
   ```

## Usage

### Start the server
```bash
python server/app.py
```

The API will be available at `http://localhost:5555`

### API Endpoints

#### Episodes
- `GET /episodes` - Retrieve all episodes
- `GET /episodes/<id>` - Retrieve a specific episode with its appearances
- `DELETE /episodes/<id>` - Delete an episode

#### Guests
- `GET /guests` - Retrieve all guests
- `GET /guests/<id>` - Retrieve a specific guest

#### Appearances
- `POST /appearances` - Record a new guest appearance
  - Request body:
    ```json
    {
      "rating": 4,
      "episode_id": 1,
      "guest_id": 1
    }
    ```

### Example Requests

```bash
# Get all episodes
curl http://localhost:5555/episodes

# Get a specific episode
curl http://localhost:5555/episodes/1

# Create an appearance
curl -X POST http://localhost:5555/appearances \
  -H "Content-Type: application/json" \
  -d '{"rating": 5, "episode_id": 1, "guest_id": 2}'
```

## Project Structure

```
late-show/
├── server/
│   ├── app.py              # Flask application and API routes
│   ├── models.py           # SQLAlchemy models (Episode, Guest, Appearance)
│   ├── seed.py             # Database seeding script
│   └── testing/            # Unit tests
├── migrations/             # Alembic database migrations
├── requirements.txt        # Python dependencies
└── README.md              # This file
```

## Data Models

### Episode
- `id` (Integer, Primary Key)
- `date` (String)
- `number` (Integer)
- **Relationship**: One-to-many with Appearances

### Guest
- `id` (Integer, Primary Key)
- `name` (String)
- `occupation` (String)
- **Relationship**: One-to-many with Appearances

### Appearance
- `id` (Integer, Primary Key)
- `rating` (Integer, 1-5)
- `episode_id` (Foreign Key)
- `guest_id` (Foreign Key)
- **Relationships**: Many-to-one with Episode and Guest

## Testing

Run the test suite using pytest:
```bash
pytest server/testing/
```

## Development

To contribute to this project:
1. Create a feature branch
2. Make your changes
3. Write tests for new functionality
4. Run the test suite to ensure all tests pass
5. Submit a pull request

## License

This project is open source and available under the MIT License.