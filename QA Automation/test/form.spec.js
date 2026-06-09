const { test, expect } = require('@playwright/test');

test('successful form submission', async ({ page }) => {

    // Open local HTML file
    await page.goto('file:///YOUR_PROJECT_PATH/index.html');

    // Fill form
    await page.fill('#name', 'Rahul');

    await page.fill('#email', 'rahul@test.com');

    // Click submit
    await page.click('button');

    // Verify success message
    await expect(page.locator('#message'))
        .toHaveText('Form Submitted Successfully');
});


test('empty form validation', async ({ page }) => {

    await page.goto('file:///YOUR_PROJECT_PATH/index.html');

    // Submit without filling
    await page.click('button');

    // Verify validation message
    await expect(page.locator('#message'))
        .toHaveText('All fields are required');
});