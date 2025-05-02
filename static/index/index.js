// Function to show toast notification
function showToast(message) {
    const toast = document.getElementById("toast");
    toast.textContent = message;
    toast.className = "show";
    setTimeout(() => { toast.className = toast.className.replace("show", ""); }, 3000);
}

// Reset animation state (without clearing form)
function resetAnimationState() {
    const loadingOverlay = document.getElementById('loadingOverlay');
    const contentWrapper = document.getElementById('contentWrapper');
    const submissionIntent = document.getElementById('submissionIntent');
    const body = document.body;
    
    submissionIntent.value = '';
    sessionStorage.removeItem('predictClicked');
    sessionStorage.removeItem('sessionId');
    loadingOverlay.classList.remove('show');
    contentWrapper.classList.remove('loading');
    body.classList.remove('loading-active');
}

// Save form data to sessionStorage
function saveFormData() {
    const form = document.getElementById('predictionForm');
    const inputs = form.querySelectorAll('input, select');
    const formData = {};
    inputs.forEach(input => {
        if (input.name && input.name !== 'submission_intent') {
            formData[input.name] = input.value;
        }
    });
    sessionStorage.setItem('formData', JSON.stringify(formData));
}

// Restore form data from sessionStorage
function restoreFormData() {
    const savedFormData = sessionStorage.getItem('formData');
    if (savedFormData) {
        const formData = JSON.parse(savedFormData);
        const form = document.getElementById('predictionForm');
        Object.keys(formData).forEach(key => {
            const input = form.querySelector(`[name="${key}"]`);
            if (input) {
                input.value = formData[key];
            }
        });
    }
}

// Clear form and sessionStorage
function resetForm() {
    const form = document.getElementById('predictionForm');
    form.reset();
    sessionStorage.removeItem('formData');
}

// Handle page show (including BFCache)
window.addEventListener('pageshow', function(event) {
    const navigationType = performance.getEntriesByType('navigation')[0]?.type;
    if (event.persisted || navigationType === 'back_forward') {
        resetAnimationState();
        restoreFormData(); // Restore form data for back navigation
    } else {
        resetForm(); // Clear form for non-back navigation
    }
});

// Handle page load
document.addEventListener('DOMContentLoaded', function() {
    resetAnimationState();
    resetForm(); // Clear form on initial load or reload
    // Restore form data only if coming from /predict (back navigation)
    if (document.referrer.endsWith('/predict')) {
        restoreFormData();
    }
});

// Clear session storage on unload (except formData for back navigation)
window.addEventListener('unload', function() {
    sessionStorage.removeItem('predictClicked');
    sessionStorage.removeItem('sessionId');
});

// Handle Predict button click
document.getElementById('predictButton').addEventListener('click', function(e) {
    e.preventDefault();
    
    const form = document.getElementById('predictionForm');
    const inputs = form.querySelectorAll('input[required], select[required]');
    const submissionIntent = document.getElementById('submissionIntent');
    const body = document.body;
    let isValid = true;
    
    // Validate all required fields
    inputs.forEach(input => {
        if (!input.value) {
            isValid = false;
            input.style.borderColor = 'var(--secondary)';
        } else {
            input.style.borderColor = '';
        }
    });
    
    if (!isValid) {
        showToast('Please fill all required fields');
        return;
    }
    
    // Set submission intent and timestamp
    submissionIntent.value = 'predict';
    const sessionId = Date.now().toString();
    sessionStorage.setItem('predictClicked', sessionId);
    sessionStorage.setItem('sessionId', sessionId);
    
    // Save form data
    saveFormData();
    
    // Show loading animation
    const loadingOverlay = document.getElementById('loadingOverlay');
    const contentWrapper = document.getElementById('contentWrapper');
    contentWrapper.classList.add('loading');
    loadingOverlay.classList.add('show');
    body.classList.add('loading-active');
    
    // Generate random delay between 1-4 seconds (1000-4000 ms)
    const randomDelay = Math.floor(Math.random() * 3000) + 1000;
    
    // Submit form after delay
    setTimeout(() => {
        form.submit();
    }, randomDelay);
});

// Handle Reset button click
document.getElementById('resetButton').addEventListener('click', function() {
    resetForm();
    // Clear server-side session
    fetch('/clear-session', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' }
    });
    showToast('Form reset');
});

// Prevent form submission unless explicitly triggered
document.getElementById('predictionForm').addEventListener('submit', function(e) {
    const sessionId = sessionStorage.getItem('sessionId');
    const predictClicked = sessionStorage.getItem('predictClicked');
    if (!predictClicked || 
        document.getElementById('submissionIntent').value !== 'predict' || 
        predictClicked !== sessionId) {
        e.preventDefault();
        resetAnimationState();
        window.location.assign('/reset');
    }
});