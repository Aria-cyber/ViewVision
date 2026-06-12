"""
Management command to generate stylish poster images locally using Pillow.
Creates gradient backgrounds with movie/series titles for a polished look.
"""
import sys
import os
import math
from io import BytesIO
from django.core.management.base import BaseCommand
from django.core.files.base import ContentFile
from media_app.models import Movie, Series

try:
    from PIL import Image, ImageDraw, ImageFont
except ImportError:
    print("Pillow is required. Install with: pip install Pillow")
    sys.exit(1)

POSTER_WIDTH = 500
POSTER_HEIGHT = 750
BACKDROP_WIDTH = 1280
BACKDROP_HEIGHT = 720

# Color palettes for different genres (dark, cinematic feel)
COLOR_PALETTES = [
    ((10, 10, 30), (0, 80, 150)),       # Deep blue
    ((20, 10, 30), (100, 0, 150)),       # Purple
    ((30, 10, 10), (150, 20, 20)),       # Dark red
    ((10, 20, 10), (0, 100, 50)),        # Forest green
    ((20, 20, 10), (120, 100, 0)),       # Gold/amber
    ((10, 15, 25), (0, 120, 180)),       # Teal
    ((25, 10, 20), (140, 0, 80)),        # Magenta
    ((15, 15, 25), (50, 50, 140)),       # Navy
]


def create_gradient(width, height, color1, color2):
    """Create a vertical gradient image."""
    img = Image.new('RGB', (width, height))
    draw = ImageDraw.Draw(img)
    for y in range(height):
        ratio = y / height
        r = int(color1[0] + (color2[0] - color1[0]) * ratio)
        g = int(color1[1] + (color2[1] - color1[1]) * ratio)
        b = int(color1[2] + (color2[2] - color1[2]) * ratio)
        draw.line([(0, y), (width, y)], fill=(r, g, b))
    return img


def get_font(size):
    """Try to get a nice font, fall back to default."""
    font_paths = [
        'C:/Windows/Fonts/segoeui.ttf',
        'C:/Windows/Fonts/arial.ttf',
        'C:/Windows/Fonts/tahoma.ttf',
        '/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf',
        '/usr/share/fonts/TTF/DejaVuSans.ttf',
    ]
    for path in font_paths:
        try:
            return ImageFont.truetype(path, size)
        except (OSError, IOError):
            continue
    try:
        return ImageFont.truetype("arial.ttf", size)
    except (OSError, IOError):
        return ImageFont.load_default()


def create_poster(title, is_series=False, palette_index=None):
    """Create a stylish poster image with title text."""
    if palette_index is None:
        palette_index = hash(title) % len(COLOR_PALETTES)
    palette = COLOR_PALETTES[palette_index]
    color1, color2 = palette

    img = create_gradient(POSTER_WIDTH, POSTER_HEIGHT, color1, color2)
    draw = ImageDraw.Draw(img)

    # Draw decorative elements
    # Corner accent lines
    accent_color = (0, 212, 255)  # Neon blue
    line_len = 60
    margin = 30
    # Top-right corner
    draw.line([(POSTER_WIDTH - margin - line_len, margin), (POSTER_WIDTH - margin, margin)], fill=accent_color, width=2)
    draw.line([(POSTER_WIDTH - margin, margin), (POSTER_WIDTH - margin, margin + line_len)], fill=accent_color, width=2)
    # Bottom-left corner
    draw.line([(margin, POSTER_HEIGHT - margin - line_len), (margin, POSTER_HEIGHT - margin)], fill=accent_color, width=2)
    draw.line([(margin, POSTER_HEIGHT - margin), (margin + line_len, POSTER_HEIGHT - margin)], fill=accent_color, width=2)

    # Draw subtle horizontal lines for texture
    for i in range(0, POSTER_HEIGHT, 40):
        opacity = 8 + int(5 * math.sin(i * 0.05))
        draw.line([(0, i), (POSTER_WIDTH, i)], fill=(255, 255, 255), width=1)

    # Large icon in center-top area
    icon_font = get_font(80)
    icon = "🎬" if not is_series else "📺"
    # Use a simple film/TV symbol instead of emoji
    icon_text = "▶" if not is_series else "◈"
    bbox = draw.textbbox((0, 0), icon_text, font=icon_font)
    icon_w = bbox[2] - bbox[0]
    icon_x = (POSTER_WIDTH - icon_w) // 2
    icon_y = 180
    draw.text((icon_x, icon_y), icon_text, fill=(60, 60, 80), font=icon_font)

    # Title text - wrap if needed
    title_font = get_font(36)
    small_font = get_font(18)

    # Word wrap the title
    words = title.split()
    lines = []
    current_line = ""
    max_width = POSTER_WIDTH - 80
    for word in words:
        test_line = f"{current_line} {word}".strip()
        bbox = draw.textbbox((0, 0), test_line, font=title_font)
        if bbox[2] - bbox[0] <= max_width:
            current_line = test_line
        else:
            if current_line:
                lines.append(current_line)
            current_line = word
    if current_line:
        lines.append(current_line)

    # Draw title centered
    line_height = 45
    total_height = len(lines) * line_height
    start_y = 380
    for i, line in enumerate(lines):
        bbox = draw.textbbox((0, 0), line, font=title_font)
        tw = bbox[2] - bbox[0]
        x = (POSTER_WIDTH - tw) // 2
        y = start_y + i * line_height
        # Text shadow
        draw.text((x + 2, y + 2), line, fill=(0, 0, 0), font=title_font)
        draw.text((x, y), line, fill=(255, 255, 255), font=title_font)

    # "ViewVision" branding at bottom
    brand_font = get_font(16)
    brand_text = "ViewVision"
    bbox = draw.textbbox((0, 0), brand_text, font=brand_font)
    bw = bbox[2] - bbox[0]
    draw.text(((POSTER_WIDTH - bw) // 2, POSTER_HEIGHT - 60), brand_text, fill=(0, 212, 255), font=brand_font)

    # Accent line under title
    line_y = start_y + total_height + 20
    line_w = 80
    draw.line(
        [(POSTER_WIDTH // 2 - line_w, line_y), (POSTER_WIDTH // 2 + line_w, line_y)],
        fill=accent_color, width=2
    )

    # Type label
    type_text = "MOVIE" if not is_series else "SERIES"
    type_font = get_font(14)
    bbox = draw.textbbox((0, 0), type_text, font=type_font)
    tw = bbox[2] - bbox[0]
    draw.text(((POSTER_WIDTH - tw) // 2, line_y + 15), type_text, fill=(150, 150, 170), font=type_font)

    return img


def create_backdrop(title, palette_index=None):
    """Create a widescreen backdrop image."""
    if palette_index is None:
        palette_index = hash(title) % len(COLOR_PALETTES)
    palette = COLOR_PALETTES[palette_index]
    color1, color2 = palette

    img = create_gradient(BACKDROP_WIDTH, BACKDROP_HEIGHT, color1, color2)
    draw = ImageDraw.Draw(img)

    # Subtle horizontal scan lines
    for i in range(0, BACKDROP_HEIGHT, 3):
        draw.line([(0, i), (BACKDROP_WIDTH, i)], fill=(255, 255, 255), width=1)

    # Title in center
    title_font = get_font(48)
    bbox = draw.textbbox((0, 0), title, font=title_font)
    tw = bbox[2] - bbox[0]
    x = (BACKDROP_WIDTH - tw) // 2
    y = (BACKDROP_HEIGHT - 48) // 2
    draw.text((x + 2, y + 2), title, fill=(0, 0, 0), font=title_font)
    draw.text((x, y), title, fill=(255, 255, 255), font=title_font)

    # Accent line
    accent_color = (0, 212, 255)
    draw.line(
        [(BACKDROP_WIDTH // 2 - 60, y + 60), (BACKDROP_WIDTH // 2 + 60, y + 60)],
        fill=accent_color, width=2
    )

    return img


def image_to_bytes(img, fmt='JPEG', quality=85):
    """Convert PIL Image to bytes."""
    buf = BytesIO()
    img.save(buf, format=fmt, quality=quality)
    return buf.getvalue()


class Command(BaseCommand):
    help = 'Generate stylish poster and backdrop images locally using Pillow'

    def handle(self, *args, **kwargs):
        if sys.stdout.encoding != 'utf-8':
            sys.stdout.reconfigure(encoding='utf-8')

        self.stdout.write('Generating poster images...')

        generated = 0

        # Generate movie posters
        for movie in Movie.objects.all():
            if movie.poster and hasattr(movie.poster, 'path'):
                try:
                    if movie.poster.path and os.path.exists(movie.poster.path):
                        self.stdout.write(f'  Skipping (exists): {movie.title}')
                        continue
                except (ValueError, OSError):
                    pass

            self.stdout.write(f'  Generating poster for: {movie.title}')
            palette_idx = hash(movie.slug) % len(COLOR_PALETTES)

            # Generate poster
            poster_img = create_poster(movie.title, is_series=False, palette_index=palette_idx)
            poster_bytes = image_to_bytes(poster_img)
            movie.poster.save(f'{movie.slug}.jpg', ContentFile(poster_bytes), save=False)

            # Generate backdrop
            backdrop_img = create_backdrop(movie.title, palette_index=palette_idx)
            backdrop_bytes = image_to_bytes(backdrop_img)
            movie.backdrop.save(f'{movie.slug}-backdrop.jpg', ContentFile(backdrop_bytes), save=False)

            movie.save()
            generated += 1

        # Generate series posters
        for ser in Series.objects.all():
            if ser.poster and hasattr(ser.poster, 'path'):
                try:
                    if ser.poster.path and os.path.exists(ser.poster.path):
                        self.stdout.write(f'  Skipping (exists): {ser.title}')
                        continue
                except (ValueError, OSError):
                    pass

            self.stdout.write(f'  Generating poster for: {ser.title}')
            palette_idx = hash(ser.slug) % len(COLOR_PALETTES)

            # Generate poster
            poster_img = create_poster(ser.title, is_series=True, palette_index=palette_idx)
            poster_bytes = image_to_bytes(poster_img)
            ser.poster.save(f'{ser.slug}.jpg', ContentFile(poster_bytes), save=False)

            # Generate backdrop
            backdrop_img = create_backdrop(ser.title, palette_index=palette_idx)
            backdrop_bytes = image_to_bytes(backdrop_img)
            ser.backdrop.save(f'{ser.slug}-backdrop.jpg', ContentFile(backdrop_bytes), save=False)

            ser.save()
            generated += 1

        self.stdout.write(self.style.SUCCESS(
            f'\nDone! Generated posters for {generated} items.'
        ))
        self.stdout.write(self.style.SUCCESS(
            'Images saved to media/posters/ directory.'
        ))
