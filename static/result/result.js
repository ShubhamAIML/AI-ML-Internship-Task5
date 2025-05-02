// Animate the probability bar on page load
document.addEventListener('DOMContentLoaded', function() {
    setTimeout(function() {
        document.querySelector('.probability-fill').style.width = '{{ result.probability }}%';
    }, 300);
});

// Clear session storage for animation state on unload
window.addEventListener('unload', function() {
    sessionStorage.removeItem('predictClicked');
    sessionStorage.removeItem('sessionId');
});