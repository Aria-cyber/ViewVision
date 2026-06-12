# ViewVision

پلتفرم جامع معرفی فیلم و سریال با رابط کاربری فارسی و طراحی مدرن

A comprehensive movie and series discovery platform built with Django, featuring a fully Persian (RTL) interface and a dark neon-themed UI.

---

## ✨ Features

- **Movie & Series Catalog** — Browse, filter, and sort movies and series by genre, rating, and release date
- **Genre System** — 12 genres with unique icons (Action, Drama, Comedy, Sci-Fi, Horror, Thriller, Adventure, Animation, Documentary, Romance, Crime, Fantasy)
- **Search** — Full-text search across movie and series titles, descriptions, directors, and creators
- **User Authentication** — Register, login, logout, and profile management with avatar upload
- **Reviews & Ratings** — 1–5 star rating system with written comments
- **Personal Watchlist** — Add/remove movies and series to a personal watchlist
- **Pagination** — Paginated list pages (12 items per page) with elided page ranges
- **Dynamic Homepage** — Real-time database counts for movies, series, and genres
- **Admin Panel** — Jazzmin-powered dark admin interface for content management
- **Social Links** — Footer social media links loaded dynamically from `links.txt`
- **Responsive Design** — Fully responsive layout with mobile menu support
- **Persian Localization** — All UI text, notifications, and form labels in fluent Persian

---

## 🛠 Tech Stack

| Layer | Technology |
|-------|-----------|
| **Backend** | Django 6.0 |
| **Database** | SQLite (easily swappable to PostgreSQL) |
| **Frontend** | HTML5, CSS3 (Custom Properties), Vanilla JS |
| **Font** | Vazirmatn (Persian) |
| **Icons** | Font Awesome 6.5 |
| **Admin** | Jazzmin 3.0 |
| **Forms** | django-crispy-forms + Bootstrap 5 |
| **Static Files** | WhiteNoise |
| **Image Processing** | Pillow |

---

## 🚀 Getting Started

### Prerequisites

- Python 3.10+
- pip

### Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/your-username/ViewVision.git
   cd ViewVision
   ```

2. **Create and activate a virtual environment**

   ```bash
   python -m venv venv
   # Windows
   venv\Scripts\activate
   # macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Run database migrations**

   ```bash
   python manage.py migrate
   ```

5. **Create a superuser (admin account)**

   ```bash
   python manage.py createsuperuser
   ```

6. **(Optional) Populate sample data**

   ```bash
   python manage.py populate_sample_data
   ```

   This creates sample genres, movies, series, users, reviews, and watchlist items.

7. **Run the development server**

   ```bash
   python manage.py runserver
   ```

8. **Open in browser**

   - Main site: [http://localhost:8000](http://localhost:8000)
   - Admin panel: [http://localhost:8000/admin](http://localhost:8000/admin)

---

## 📁 Project Structure

```
ViewVision/
├── accounts/                  # User authentication app
│   ├── models.py              # CustomUser model (bio, avatar)
│   ├── views.py               # Register, profile views
│   ├── forms.py               # Registration, login, profile forms
│   └── urls.py                # Auth URL patterns
├── media_app/                 # Core media app
│   ├── models.py              # Genre, Movie, Series, Review, WatchlistItem
│   ├── views.py               # All media views (list, detail, search, watchlist)
│   ├── forms.py               # Review form
│   ├── templatetags/
│   │   └── genre_tags.py      # Genre icon template filter
│   └── management/commands/
│       ├── populate_sample_data.py  # Sample data generator
│       └── generate_posters.py      # Poster image generator
├── templates/                 # HTML templates (Persian/RTL)
│   ├── base.html              # Base layout with navbar & footer
│   ├── home.html              # Homepage with hero, stats, sections
│   ├── accounts/              # Auth templates
│   └── media_app/             # Media templates (lists, details, search)
├── static/
│   ├── css/style.css          # Main stylesheet (dark neon theme)
│   ├── css/admin_dark.css     # Admin panel dark theme
│   ├── js/main.js             # Client-side JavaScript
│   └── images/                # Static images (logo, etc.)
├── viewvision/                # Django project settings
│   ├── settings.py            # Configuration
│   ├── urls.py                # Root URL configuration
│   └── context_processors.py  # Social links context processor
├── links.txt                  # Social media URLs (editable)
├── manage.py
└── requirements.txt
```

---

## 🎨 Design

The UI features a **dark theme with neon blue accents** (`#00d4ff`) and a fully **right-to-left (RTL)** layout for Persian language support.

- **CSS Custom Properties** for consistent theming
- **Gradient accents** and **glow effects** on interactive elements
- **Smooth transitions** and hover animations
- **Responsive breakpoints** at 1024px, 768px, and 480px

---

## 🔧 Configuration

### Social Media Links

Edit `links.txt` in the project root to update footer social links:

```
instagram=https://instagram.com/your-handle
telegram=https://t.me/your-channel
linkedin=https://linkedin.com/in/your-profile
github=https://github.com/your-username
```

### Database

The project uses SQLite by default. To switch to PostgreSQL:

1. Install `psycopg2-binary` (already in requirements.txt)
2. Update `DATABASES` in `viewvision/settings.py`:

   ```python
   DATABASES = {
       'default': {
           'ENGINE': 'django.db.backends.postgresql',
           'NAME': 'your_db_name',
           'USER': 'your_db_user',
           'PASSWORD': 'your_db_password',
           'HOST': 'localhost',
           'PORT': '5432',
       }
   }
   ```

---

## 👥 Sample Users

When using `populate_sample_data`, the following users are created (password: `testpass123`):

| Username | Bio |
|----------|-----|
| ali | عاشق سینما و نقد فیلم |
| sara | منتقد فیلم و سریال |
| mohammad | طرفدار فیلم‌های علمی-تخیلی |
| fateme | علاقه‌مند به مستندسازی |
| reza | فیلم‌باز حرفه‌ای |

---

## 📄 License

This project is created for educational purposes.

---

**تولید شده توسط شایان فتاحی و محمد مهدی عبدیان**
