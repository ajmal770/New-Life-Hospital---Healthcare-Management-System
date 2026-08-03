document.addEventListener('DOMContentLoaded', () => {
    // Auto-hide flash messages after 5 seconds
    const alerts = document.querySelectorAll('.alert');
    alerts.forEach(alert => {
        setTimeout(() => {
            const bsAlert = new bootstrap.Alert(alert);
            bsAlert.close();
        }, 5000);
    });

    // Initialize tooltips
    const tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'));
    tooltipTriggerList.map(function (tooltipTriggerEl) {
        return new bootstrap.Tooltip(tooltipTriggerEl);
    });
});

/**
 * Copy 24/7 Helpline Hotline Number to Clipboard
 */
function copyHelplineNumber(number = '1800-233-4567') {
    if (navigator.clipboard && window.isSecureContext) {
        navigator.clipboard.writeText(number).then(() => {
            showHelplineToast('Hotline Copied!', `Helpline number <strong>${number}</strong> copied to clipboard.`);
        }).catch(() => {
            fallbackCopyHelpline(number);
        });
    } else {
        fallbackCopyHelpline(number);
    }
}

function fallbackCopyHelpline(text) {
    const textArea = document.createElement("textarea");
    textArea.value = text;
    textArea.style.position = "fixed";
    textArea.style.left = "-999999px";
    document.body.appendChild(textArea);
    textArea.focus();
    textArea.select();
    try {
        document.execCommand('copy');
        showHelplineToast('Hotline Copied!', `Helpline number <strong>${text}</strong> copied to clipboard.`);
    } catch (err) {
        alert(`Helpline Hotline: ${text}`);
    }
    document.body.removeChild(textArea);
}

/**
 * Custom Toast Trigger for Helpline Actions
 */
function showHelplineToast(title, message) {
    const toastContainer = document.querySelector('.toast-container') || createToastContainer();
    const toastEl = document.createElement('div');
    toastEl.className = 'toast show align-items-center bg-white border-0 shadow-lg mb-3 rounded-4 toast-border-success';
    toastEl.setAttribute('role', 'alert');
    toastEl.style.minWidth = '300px';
    toastEl.style.animation = 'slideInRight 0.35s ease';

    toastEl.innerHTML = `
        <div class="d-flex p-3">
            <div class="toast-icon me-3 d-flex align-items-center justify-content-center text-success">
                <i class="bi bi-telephone-check-fill" style="font-size: 1.6rem;"></i>
            </div>
            <div class="toast-body p-0 d-flex flex-column justify-content-center flex-grow-1">
                <h6 class="mb-1 fw-bold text-dark">${title}</h6>
                <div class="text-secondary small fw-medium">${message}</div>
            </div>
            <button type="button" class="btn-close me-1 m-auto" onclick="this.closest('.toast').remove();" aria-label="Close"></button>
        </div>
    `;

    toastContainer.appendChild(toastEl);
    setTimeout(() => {
        if (toastEl.parentNode) {
            toastEl.style.opacity = '0';
            toastEl.style.transform = 'translateX(100%)';
            toastEl.style.transition = 'all 0.4s ease';
            setTimeout(() => toastEl.remove(), 400);
        }
    }, 4000);
}

function createToastContainer() {
    const container = document.createElement('div');
    container.className = 'toast-container position-fixed top-0 end-0 p-4';
    container.style.marginTop = '80px';
    container.style.zIndex = '1060';
    document.body.appendChild(container);
    return container;
}

