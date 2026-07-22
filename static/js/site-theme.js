/**
 * Automated Hardware Theme Manager
 * Syncs the website styling seamlessly with the device's system color scheme.
 */
document.addEventListener("DOMContentLoaded", () => {
  const applySystemTheme = () => {
    // Detect if device is in dark mode
    const isDark = window.matchMedia("(prefers-color-scheme: dark)").matches;
    const theme = isDark ? "dark" : "light";

    // Apply globally to Bootstrap 5
    document.documentElement.setAttribute("data-bs-theme", theme);
  };

  // Run on page load
  applySystemTheme();

  // Watch for system mode changes instantly
  window
    .matchMedia("(prefers-color-scheme: dark)")
    .addEventListener("change", applySystemTheme);
});
