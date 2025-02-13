function printDiamondPattern(n) {
    // Top half of the diamond (including the middle row)
    for (let i = 0; i < n; i++) {
        // Print leading spaces
        let spaces = " ".repeat(2 * (n - i - 1));
        process.stdout.write(spaces);
        
        // Print stars
        let stars = "* ".repeat(2 * i + 1);
        process.stdout.write(stars);

        // Move to the next line
        console.log();
    }

    // Bottom half of the diamond (excluding the middle row)
    for (let i = 0; i < n - 1; i++) {
        // Print leading spaces
        let spaces = " ".repeat(2 * (i + 1));
        process.stdout.write(spaces);
        
        // Print stars
        let stars = "* ".repeat(2 * (n - i - 1) - 1);
        process.stdout.write(stars);

        // Move to the next line
        console.log();
    }
}

printDiamondPattern(n);
