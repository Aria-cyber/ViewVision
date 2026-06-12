/* ============================================
   ViewVision - Main JavaScript
   ============================================ */

document.addEventListener('DOMContentLoaded', function () {

    // --- Navbar Scroll Effect ---
    const navbar = document.querySelector('.navbar');
    if (navbar) {
        window.addEventListener('scroll', function () {
            if (window.scrollY > 20) {
                navbar.classList.add('scrolled');
            } else {
                navbar.classList.remove('scrolled');
            }
        });
    }

    // --- Mobile Menu Toggle ---
    window.toggleMobileMenu = function () {
        const menu = document.getElementById('mobileMenu');
        if (menu) {
            menu.classList.toggle('show');
        }
    };

    // --- User Dropdown Toggle ---
    window.toggleUserMenu = function () {
        const dropdown = document.getElementById('userDropdown');
        if (dropdown) {
            dropdown.classList.toggle('show');
        }
    };

    // Close dropdown when clicking outside
    document.addEventListener('click', function (e) {
        const userMenu = document.querySelector('.user-menu');
        const dropdown = document.getElementById('userDropdown');
        if (userMenu && dropdown && !userMenu.contains(e.target)) {
            dropdown.classList.remove('show');
        }
    });

    // --- Auto-dismiss Alerts ---
    const alerts = document.querySelectorAll('.alert');
    alerts.forEach(function (alert) {
        setTimeout(function () {
            alert.style.transition = 'opacity 0.3s ease, transform 0.3s ease';
            alert.style.opacity = '0';
            alert.style.transform = 'translateX(100%)';
            setTimeout(function () {
                alert.remove();
            }, 300);
        }, 5000);
    });

    // --- Star Rating Input ---
    const starContainers = document.querySelectorAll('.star-rating-input');
    starContainers.forEach(function (container) {
        const stars = container.querySelectorAll('.star');
        const input = container.parentElement.querySelector('select[name="rating"]');

        stars.forEach(function (star, index) {
            star.addEventListener('click', function () {
                if (input) {
                    input.value = index + 1;
                }
                stars.forEach(function (s, i) {
                    if (i <= index) {
                        s.classList.add('active');
                        s.classList.remove('empty');
                    } else {
                        s.classList.remove('active');
                        s.classList.add('empty');
                    }
                });
            });

            star.addEventListener('mouseenter', function () {
                stars.forEach(function (s, i) {
                    if (i <= index) {
                        s.style.color = '#ffab00';
                    } else {
                        s.style.color = '';
                    }
                });
            });
        });

        container.addEventListener('mouseleave', function () {
            const currentVal = input ? parseInt(input.value) || 0 : 0;
            stars.forEach(function (s, i) {
                if (i < currentVal) {
                    s.style.color = '#ffab00';
                } else {
                    s.style.color = '';
                }
            });
        });
    });

    // --- Smooth Scroll for Anchor Links ---
    document.querySelectorAll('a[href^="#"]').forEach(function (anchor) {
        anchor.addEventListener('click', function (e) {
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                e.preventDefault();
                target.scrollIntoView({ behavior: 'smooth', block: 'start' });
            }
        });
    });

    // --- Intersection Observer for Fade-in Animation ---
    const observerOptions = {
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px'
    };

    const observer = new IntersectionObserver(function (entries) {
        entries.forEach(function (entry) {
            if (entry.isIntersecting) {
                entry.target.classList.add('fade-in');
                observer.unobserve(entry.target);
            }
        });
    }, observerOptions);

    document.querySelectorAll('.media-card, .genre-card, .review-card').forEach(function (el) {
        el.style.opacity = '0';
        observer.observe(el);
    });

    // --- Search Input Focus Effect ---
    const searchInput = document.querySelector('.search-input');
    if (searchInput) {
        searchInput.addEventListener('focus', function () {
            this.parentElement.style.borderColor = 'var(--accent)';
        });
        searchInput.addEventListener('blur', function () {
            this.parentElement.style.borderColor = '';
        });
    }

});
