document.addEventListener('DOMContentLoaded', function () {
    document.querySelectorAll('.post').forEach(function(post ) {
        post.addEventListener('click', function () {
            window.location.href = post.getAttribute('data-url');
        });
    });
});