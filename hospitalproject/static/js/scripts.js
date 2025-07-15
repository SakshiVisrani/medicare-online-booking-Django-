

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


document.addEventListener('DOMContentLoaded', () => {
    const tabButtons = document.querySelectorAll('.tab-button');
    const tabPanes = document.querySelectorAll('.tab-pane');

    tabButtons.forEach(button => {
        button.addEventListener('click', () => {
            // Deactivate all buttons and hide all panes
            tabButtons.forEach(btn => btn.classList.remove('active'));
            tabPanes.forEach(pane => pane.classList.remove('active'));

            // Activate clicked button
            button.classList.add('active');

            // Show corresponding pane
            const targetTab = button.dataset.tab;
            document.getElementById(targetTab).classList.add('active');
        });
    });

    // Optional: Add logic for consultation option selection (like adding a class)
    const consultationOptions = document.querySelectorAll('.consultation-option-card input[type="radio"]');
    consultationOptions.forEach(radio => {
        radio.addEventListener('change', () => {
            consultationOptions.forEach(r => r.closest('.consultation-option-card').classList.remove('clinic-visit-selected'));
            if (radio.checked) {
                radio.closest('.consultation-option-card').classList.add('clinic-visit-selected');
            }
        });
    });
        });

document.addEventListener('DOMContentLoaded', () => {
    const tabButtons = document.querySelectorAll('.tab-button');
    const tabPanes = document.querySelectorAll('.tab-pane');

    tabButtons.forEach(button => {
        button.addEventListener('click', () => {
            // Deactivate all buttons and hide all panes
            tabButtons.forEach(btn => btn.classList.remove('active'));
            tabPanes.forEach(pane => pane.classList.remove('active'));

            // Activate clicked button
            button.classList.add('active');

            // Show corresponding pane
            const targetTab = button.dataset.tab;
            document.getElementById(targetTab).classList.add('active');

            // If switching to Availability tab, ensure first date is active and times are shown
            if (targetTab === 'availability') {
                const firstDateCard = document.querySelector('.date-selection-grid .date-option-card');
                const availableTimesSection = document.querySelector('.available-times-section');

                // Reset active state for all date cards
                document.querySelectorAll('.date-option-card').forEach(card => card.classList.remove('active'));
                // Set the first date card as active
                if (firstDateCard) {
                    firstDateCard.classList.add('active');
                }
                // Show the available times section
                if (availableTimesSection) {
                    availableTimesSection.classList.add('show');
                }
            }
        });
    });

    // Optional: Add logic for consultation option selection (like adding a class)
    const consultationOptions = document.querySelectorAll('.consultation-option-card input[type="radio"]');
    consultationOptions.forEach(radio => {
        radio.addEventListener('change', () => {
            consultationOptions.forEach(r => r.closest('.consultation-option-card').classList.remove('clinic-visit-selected'));
            if (radio.checked) {
                radio.closest('.consultation-option-card').classList.add('clinic-visit-selected');
            }
        });
    });

    // --- New JavaScript for Date and Time Slot Selection ---
    const dateOptionCards = document.querySelectorAll('.date-option-card');
    const availableTimesSection = document.querySelector('.available-times-section');
    const timeSlotTags = document.querySelectorAll('.time-slot-tag'); // Get all time slots

    // Handle Date Card Clicks
    dateOptionCards.forEach(card => {
        card.addEventListener('click', () => {
            // Remove 'active' class from all date cards
            dateOptionCards.forEach(c => c.classList.remove('active'));

            // Add 'active' class to the clicked card
            card.classList.add('active');

            // Show the available times section
            availableTimesSection.classList.add('show');

            // Optional: You could fetch/update time slots based on the selected date here
            // For this example, we're just showing the static list.
        });
    });

    // Handle Time Slot Tag Clicks (Optional: for selection feedback)
    timeSlotTags.forEach(slot => {
        slot.addEventListener('click', () => {
            // Remove 'selected' class from all time slots
            timeSlotTags.forEach(s => s.classList.remove('selected'));

            // Add 'selected' class to the clicked time slot
            slot.classList.add('selected');
        });
    });

    // Initial state: When page loads, if Availability is the default active tab,
    // ensure the "Today" date card is active and times are shown.
    const initialActiveTab = document.querySelector('.tab-button.active');
    if (initialActiveTab && initialActiveTab.dataset.tab === 'availability') {
        const firstDateCard = document.querySelector('.date-selection-grid .date-option-card');
        if (firstDateCard) {
            firstDateCard.classList.add('active');
        }
        if (availableTimesSection) {
            availableTimesSection.classList.add('show');
        }
    }
});
const dateCards = document.querySelectorAll('.date-option-card');
const slotSections = document.querySelectorAll('.slot-section');

dateCards.forEach(card => {
    card.addEventListener('click', () => {
        // Remove active class from all
        dateCards.forEach(c => c.classList.remove('active'));
        card.classList.add('active');

        const selectedDate = card.getAttribute('data-date');

        slotSections.forEach(section => {
            section.style.display = section.getAttribute('data-date') === selectedDate ? 'flex' : 'none';
        });
    });
});
   
    