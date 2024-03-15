function setTheme() {
    const browserColor = window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light';
    $('html').attr('data-bs-theme', browserColor);
}

setTheme();

window.matchMedia('(prefers-color-scheme: dark)').addEventListener('change', e => {
    const newColorScheme = e.matches ? 'dark' : 'light';
    $('html').attr('data-bs-theme', newColorScheme);
});
