

        // Add some interactive functionality
    document.querySelector('.search-input').addEventListener('focus', function() {
        this.style.boxShadow = '0 0 0 2px rgba(255, 255, 255, 0.3)';
        });

    document.querySelector('.search-input').addEventListener('blur', function() {
        this.style.boxShadow = 'none';
        });

    document.querySelector('.location-input').addEventListener('focus', function() {
        this.style.boxShadow = '0 0 0 2px rgba(255, 255, 255, 0.3)';
        });

    document.querySelector('.location-input').addEventListener('blur', function() {
        this.style.boxShadow = 'none';
        });

        // Add click functionality to service items
        document.querySelectorAll('.service-item').forEach(item => {
        item.addEventListener('click', function (e) {
            e.preventDefault();
            this.style.transform = 'translateY(-5px) scale(0.98)';
            setTimeout(() => {
                this.style.transform = 'translateY(-5px)';
            }, 150);
        });
        });

    // Make doctor popup closeable
    document.querySelector('.doctor-popup').addEventListener('click', function() {
        this.style.display = 'none';
        });
