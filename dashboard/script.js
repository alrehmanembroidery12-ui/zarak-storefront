document.addEventListener('DOMContentLoaded', () => {
    // Tab Navigation
    const menuItems = document.querySelectorAll('.menu-item');
    const tabContents = document.querySelectorAll('.tab-content');

    menuItems.forEach(item => {
        item.addEventListener('click', () => {
            // Remove active class from all
            menuItems.forEach(mi => mi.classList.remove('active'));
            tabContents.forEach(tc => tc.classList.remove('active'));

            // Add active class to clicked
            item.classList.add('active');
            const targetId = item.getAttribute('data-target');
            document.getElementById(targetId).classList.add('active');
        });
    });

    // Helper: Show Toast
    function showToast(message, isError = false) {
        const toast = document.getElementById('toast');
        toast.textContent = message;
        toast.style.backgroundColor = isError ? 'var(--danger)' : 'var(--success)';
        toast.classList.add('show');
        setTimeout(() => toast.classList.remove('show'), 3000);
    }

    // Helper: Handle File Input to Base64
    function handleFileInput(fileInputId, previewContainerId) {
        const input = document.getElementById(fileInputId);
        const previewOpts = document.getElementById(previewContainerId);

        input.addEventListener('change', function () {
            const file = this.files[0];
            if (file) {
                const reader = new FileReader();
                reader.onload = function (e) {
                    previewOpts.innerHTML = `<img src="${e.target.result}" alt="Preview">`;
                    // Store the base64 temporarily on the form element for submission
                    input.dataset.base64 = e.target.result;
                }
                reader.readAsDataURL(file);
            } else {
                previewOpts.innerHTML = '<span class="preview-placeholder">Image Preview</span>';
                input.dataset.base64 = '';
            }
        });
    }

    handleFileInput('upload-file', 'upload-preview');
    handleFileInput('change-file', 'change-preview');

    // 1. Upload Picture (Generic)
    document.getElementById('upload-form').addEventListener('submit', (e) => {
        e.preventDefault();
        const targetId = document.getElementById('upload-image-id').value.trim();
        const fileInput = document.getElementById('upload-file');
        const base64Data = fileInput.dataset.base64;

        if (targetId && base64Data) {
            localStorage.setItem('zarak-img-' + targetId, base64Data);
            showToast(`Image uploaded for ID: ${targetId}`);
            e.target.reset();
            document.getElementById('upload-preview').innerHTML = '<span class="preview-placeholder">Image Preview</span>';
        } else {
            showToast('Please provide an ID and select an image', true);
        }
    });

    // 2. Change Picture (Pre-defined Dropdown)
    document.getElementById('change-form').addEventListener('submit', (e) => {
        e.preventDefault();
        const targetId = document.getElementById('change-image-select').value;
        const fileInput = document.getElementById('change-file');
        const base64Data = fileInput.dataset.base64;

        if (targetId && base64Data) {
            localStorage.setItem('zarak-img-' + targetId, base64Data);
            showToast(`Image changed for: ${targetId}`);
            e.target.reset();
            document.getElementById('change-preview').innerHTML = '<span class="preview-placeholder">Image Preview</span>';
        } else {
            showToast('Please select an image target and file', true);
        }
    });

    // 3. Delete Picture
    document.getElementById('delete-form').addEventListener('submit', (e) => {
        e.preventDefault();
        const targetId = document.getElementById('delete-image-select').value;
        if (targetId) {
            localStorage.removeItem('zarak-img-' + targetId);
            showToast(`Custom image removed for: ${targetId}`);
            e.target.reset();
        } else {
            showToast('Please select an image to delete', true);
        }
    });

    // 4. Privacy Policy
    const privacyText = document.getElementById('privacy-text');
    // Load existing
    const existingPolicy = localStorage.getItem('zarak-privacy-policy');
    if (existingPolicy) {
        privacyText.value = existingPolicy;
    }

    document.getElementById('privacy-form').addEventListener('submit', (e) => {
        e.preventDefault();
        const content = privacyText.value;
        localStorage.setItem('zarak-privacy-policy', content);
        showToast('Privacy Policy updated successfully');
    });
});
